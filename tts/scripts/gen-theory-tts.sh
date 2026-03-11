#!/bin/bash
# Generate TTS MP3s for all theory files in a module
# Usage: gen-theory-tts.sh <module-dir>
set -e

MODULE_DIR="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TTS_DIR="$(dirname "$SCRIPT_DIR")"
REPO_ROOT="$(dirname "$TTS_DIR")"
WORK_DIR=$(mktemp -d)

if [ -z "$MODULE_DIR" ]; then
    echo "Usage: $0 <module-dir>"
    exit 1
fi

echo "=== Theory TTS Generation: $MODULE_DIR ==="

# Find all theory markdown files
for theory_file in "$REPO_ROOT/$MODULE_DIR"/*-theory.md; do
    [ -f "$theory_file" ] || continue
    
    basename=$(basename "$theory_file" .md)
    output_mp3="$REPO_ROOT/$MODULE_DIR/${basename}.mp3"
    
    # Skip if MP3 already exists
    if [ -f "$output_mp3" ]; then
        echo "SKIP: $basename (MP3 exists)"
        continue
    fi
    
    echo ""
    echo "--- Processing: $basename ---"
    
    # Step 1: Convert to spoken text
    echo "  [1/4] Extracting spoken text..."
    python3 "$SCRIPT_DIR/theory-to-tts.py" "$theory_file" > "$WORK_DIR/spoken.txt"
    CHARS=$(wc -c < "$WORK_DIR/spoken.txt")
    echo "  Extracted $CHARS chars"
    
    # Step 2: Apply pronunciation dictionary
    echo "  [2/4] Applying pronunciation..."
    python3 "$SCRIPT_DIR/apply-pronunciation.py" "$WORK_DIR/spoken.txt" "$TTS_DIR/pronunciation.txt" > "$WORK_DIR/pronounced.txt"
    
    # Step 3: Chunk text
    echo "  [3/4] Chunking..."
    rm -f "$WORK_DIR"/chunk_*.txt
    python3 "$SCRIPT_DIR/chunk-text.py" "$WORK_DIR/pronounced.txt" --max-chars 2000 --output-dir "$WORK_DIR" --prefix chunk
    CHUNK_COUNT=$(ls "$WORK_DIR"/chunk_*.txt 2>/dev/null | wc -l)
    echo "  Split into $CHUNK_COUNT chunks"
    
    # Step 4: Generate audio per chunk
    echo "  [4/4] Generating audio..."
    for chunk in "$WORK_DIR"/chunk_*.txt; do
        cbase=$(basename "$chunk" .txt)
        echo "    $cbase..."
        python3 ~/.openclaw/skills/voice/scripts/tts-kokoro \
            "$(cat "$chunk")" \
            --voice will --format mp3 \
            --output "$WORK_DIR/${cbase}.mp3" > /dev/null
    done
    
    # Step 5: Concatenate
    ls "$WORK_DIR"/chunk_*.mp3 | sort | sed "s|.*|file '&'|" > "$WORK_DIR/concat.txt"
    ffmpeg -y -f concat -safe 0 -i "$WORK_DIR/concat.txt" \
        -c:a libmp3lame -b:a 128k "$output_mp3" 2>/dev/null
    
    # Report
    DURATION=$(ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$output_mp3")
    SIZE=$(ls -lh "$output_mp3" | awk '{print $5}')
    DMINS=$(python3 -c "d=$DURATION; print(f'{int(d//60)}m {int(d%60)}s')")
    echo "  ✅ $basename.mp3 — $DMINS, $SIZE"
    
    # Clean chunk files for next iteration
    rm -f "$WORK_DIR"/chunk_*.txt "$WORK_DIR"/chunk_*.mp3 "$WORK_DIR/concat.txt"
done

rm -rf "$WORK_DIR"
echo ""
echo "=== Module theory TTS complete ==="
