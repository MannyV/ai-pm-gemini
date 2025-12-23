#!/usr/bin/env python3
"""
Helper script to generate PDFs from markdown or text files
Usage: python generate_pdf.py <input.md> [output.pdf]
"""
import sys
import subprocess
from pathlib import Path


def convert_markdown_to_pdf(input_file, output_file=None, custom_options=None):
    """
    Convert markdown file to PDF using pandoc

    Args:
        input_file: Path to input markdown file
        output_file: Path to output PDF file (optional)
        custom_options: List of additional pandoc options (optional)

    Returns:
        Path to generated PDF file or None if failed
    """
    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Error: Input file '{input_file}' not found")
        return None

    if output_file is None:
        output_file = input_path.stem + ".pdf"

    # Default pandoc options for professional formatting
    pandoc_cmd = [
        "pandoc",
        str(input_file),
        "-o",
        str(output_file),
        "-V", "geometry:margin=1in",
        "-V", "fontsize=11pt",
        "-V", "linestretch=1.15",
    ]

    # Add custom options if provided
    if custom_options:
        pandoc_cmd.extend(custom_options)

    try:
        result = subprocess.run(
            pandoc_cmd,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✓ Successfully created: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"✗ Error converting {input_file}:")
        print(f"  {e.stderr}")
        return None
    except FileNotFoundError:
        print("✗ Error: pandoc not found. Please install it:")
        print("  macOS: brew install pandoc")
        print("  Linux: sudo apt-get install pandoc")
        print("  Windows: choco install pandoc")
        return None


def print_usage():
    """Print usage information"""
    print("PDF Generation Helper Script")
    print()
    print("Usage:")
    print("  python generate_pdf.py <input.md> [output.pdf]")
    print()
    print("Examples:")
    print("  python generate_pdf.py docs/brds/my-brd.md")
    print("  python generate_pdf.py research.md outputs/research-report.pdf")
    print()
    print("Options:")
    print("  input.md    : Input markdown file (required)")
    print("  output.pdf  : Output PDF file (optional, defaults to input name)")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help", "help"]:
        print_usage()
        sys.exit(0 if len(sys.argv) >= 2 else 1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = convert_markdown_to_pdf(input_file, output_file)

    if result is None:
        sys.exit(1)
    else:
        sys.exit(0)
