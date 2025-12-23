---
name: pdf-generation
description: Generate PDF documents from markdown content, BRDs, research reports, and other documents. Convert text and formatted content into professional PDFs using pandoc or reportlab. Use when you need to create PDF files from documents, export reports to PDF, or generate PDF versions of BRDs and research materials.
allowed-tools: Read, Bash, Edit, Write
---

# PDF Generation Skill

## Requirements

Install required packages:
```bash
# Install pandoc (recommended for markdown conversion)
brew install pandoc

# Install Python packages for advanced PDF operations
pip install reportlab pdfplumber pypdf
```

## Quick Start

### Convert Markdown to PDF using Pandoc

```bash
pandoc input.md -o output.pdf
```

### Convert with Professional Formatting

```bash
pandoc input.md \
  -o output.pdf \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  --pdf-engine=pdflatex
```

### Generate PDF with reportlab (Python)

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("document.pdf", pagesize=letter)
story = []
styles = getSampleStyleSheet()

# Add title
story.append(Paragraph("Document Title", styles['Title']))
story.append(Spacer(1, 12))

# Add content
story.append(Paragraph("Content goes here", styles['BodyText']))

doc.build(story)
```

### Extract Text from PDFs

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

## Usage Examples for PM Demo Environment

### Generate BRD as PDF

```bash
# Simple conversion
pandoc docs/brds/voice-workflow-builder.md -o docs/brds/voice-workflow-builder.pdf

# With professional formatting
pandoc docs/brds/voice-workflow-builder.md \
  -o docs/brds/voice-workflow-builder.pdf \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V documentclass=report
```

### Create Research Report PDF

```bash
pandoc data/research-report.md -o outputs/research-report.pdf
```

### Export Customer Interview Summary

```bash
pandoc data/customer-interviews/summary.md \
  -o outputs/customer-insights.pdf \
  -V geometry:margin=1in
```

## Helper Script

Use the included `generate_pdf.py` script for easy conversions:

```bash
python .claude/skills/pdf-generation/scripts/generate_pdf.py input.md [output.pdf]
```

## Best Practices

- **Use pandoc** for simple markdown-to-PDF conversion (fastest, cleanest)
- **Use reportlab** for complex layouts and custom styling
- **Use pypdf** for merging multiple PDFs
- **Test output** on target readers for accessibility and formatting
- **Version control** the markdown source, not the PDF outputs (add PDFs to .gitignore)

## Common Workflows

1. **BRD Export**: Read BRD markdown → Convert with pandoc → Save to outputs/
2. **Research Report**: Synthesize data → Generate markdown → Convert to PDF
3. **Release Notes**: Draft announcement → Format as PDF → Ready for distribution
4. **Meeting Notes**: Process transcript → Export as PDF for stakeholders

## Troubleshooting

- **pandoc not found**: Run `brew install pandoc` (macOS) or check installation
- **PDF engine errors**: Install BasicTeX or use `--pdf-engine=pdflatex`
- **Formatting issues**: Adjust geometry and font settings in pandoc command
- **Python errors**: Ensure packages installed with `pip install reportlab pdfplumber pypdf`
