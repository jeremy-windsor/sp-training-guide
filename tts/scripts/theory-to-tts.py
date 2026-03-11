#!/usr/bin/env python3
"""Convert theory markdown files to spoken text for TTS.

Strips code blocks, tables, packet diagrams, and markdown formatting.
Converts headers to natural speech transitions.
Keeps prose and list content for narration.
"""
import re
import sys


def strip_code_blocks(text):
    """Remove fenced code blocks entirely."""
    return re.sub(r'```[\s\S]*?```', '', text)


def strip_tables(text):
    """Remove markdown tables (pipe-delimited rows and separator lines)."""
    text = re.sub(r'^\|[^\n]+\|$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[-|:\s]+$', '', text, flags=re.MULTILINE)
    return text


def strip_ascii_diagrams(text):
    """Remove ASCII art diagrams (lines with box-drawing chars or heavy formatting)."""
    diagram_chars = set('┌┐└┘├┤┬┴─│┼▶►▷→←↑↓↕')
    lines = text.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append(line)
            continue
        # Count diagram characters
        diag_count = sum(1 for c in stripped if c in diagram_chars)
        # If more than 30% of non-space chars are diagram chars, skip
        non_space = len(stripped.replace(' ', ''))
        if non_space > 0 and diag_count / non_space > 0.3:
            continue
        result.append(line)
    return '\n'.join(result)


def convert_headers(text):
    """Convert markdown headers to spoken transitions."""
    def header_to_speech(match):
        level = len(match.group(1))
        title = match.group(2).strip()
        # Remove numbering like "1." or "3a." from beginning
        title = re.sub(r'^\d+[a-z]?\.\s*', '', title)
        if level <= 2:
            return f'\n{title}.\n'
        else:
            return f'\n{title}.\n'
    
    return re.sub(r'^(#{1,6})\s+(.+)$', header_to_speech, text, flags=re.MULTILINE)


def clean_inline_markdown(text):
    """Remove inline markdown formatting."""
    # Inline backticks — keep content
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Bold
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    # Italic
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    # Links — keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Blockquote markers
    text = re.sub(r'^>\s?', '', text, flags=re.MULTILINE)
    # Horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)
    # List markers — remove but keep content
    text = re.sub(r'^(\s*)[-*]\s+', r'\1', text, flags=re.MULTILINE)
    text = re.sub(r'^(\s*)\d+\.\s+', r'\1', text, flags=re.MULTILINE)
    return text


def strip_footer(text):
    """Remove the footer (sources, companion references)."""
    # Strip everything after "---" near the end (companion notice, sources)
    text = re.sub(r'\n---\n\*This is the theory companion.*$', '', text, flags=re.DOTALL)
    text = re.sub(r'\n---\n\*Sources:.*$', '', text, flags=re.DOTALL)
    # Strip "Further Reading" section — it's just book titles
    text = re.sub(r'\nFurther Reading\.?\n[\s\S]*?(?=\n[A-Z]|\Z)', '', text)
    return text


def clean_whitespace(text):
    """Normalize whitespace for TTS."""
    # Collapse multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove lines that are just whitespace
    text = re.sub(r'^\s+$', '', text, flags=re.MULTILINE)
    # Collapse multiple spaces
    text = re.sub(r'  +', ' ', text)
    return text.strip()


def convert_to_speech(md_text):
    """Full pipeline: markdown theory -> spoken text."""
    text = md_text
    
    # Strip non-spoken elements
    text = strip_code_blocks(text)
    text = strip_tables(text)
    text = strip_ascii_diagrams(text)
    
    # Convert structure to speech
    text = convert_headers(text)
    text = strip_footer(text)
    text = clean_inline_markdown(text)
    text = clean_whitespace(text)
    
    return text


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: theory-to-tts.py <theory-file.md>", file=sys.stderr)
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        md = f.read()
    
    spoken = convert_to_speech(md)
    print(spoken)
