# GEMINI.md

This file provides guidance to Gemini Agents when working with code in this repository.

## Project Overview

This is a demo environment for showcasing Gemini capabilities to product managers. The repository contains example data, custom agents, slash commands, and workflows demonstrating end-to-end product management tasks from research synthesis to BRD creation and implementation prototyping.

## Repository Architecture

### Directory Structure
```
.gemini/
├── agents/              # Custom Gemini agents
│   ├── planning-brd-agent.md        # BRD generation agent
│   ├── research-synthesizer.md      # Research & pain point synthesis
│   ├── frontend-developer.md        # Frontend implementation
│   ├── ui-designer.md               # UI/UX design agent
│   └── *-review-agent.md            # Review agents (designer, engineer, executive)
└── commands/            # Slash commands for quick workflows
    ├── brd.md                       # /brd - Generate BRD
    ├── customer-summary.md          # /customer-summary - Synthesize interviews
    ├── meeting-notes.md             # /meeting-notes - Process transcripts
    └── release-announcement.md      # /release-announcement

docs/
├── business-info.md                 # StreamlineAI company context
├── writing-styles/                  # Style guides (technical, user-friendly, internal)
└── example-brds/                    # Sample BRD templates

data/
├── customer-interviews/             # Interview transcripts for synthesis
└── meeting-transcripts/             # Meeting notes for processing

transcript_summarizer_code/          # YouTube transcript summarizer tool
smartphone-specs-2026/               # Example research data
```

### Key Context Files
- **Business Context**: `docs/business-info.md` - StreamlineAI B2B SaaS company (150 employees, $12M ARR)
- **Writing Styles**: `docs/writing-styles/` - Technical, user-friendly, and internal-audience style guides
- **Example BRDs**: `docs/example-brds/` - Reference BRD structure and formatting

## Common Workflows

### Available Slash Commands
- `/brd` - Generate comprehensive Business Requirements Document
- `/customer-summary` - Synthesize customer interview insights
- `/meeting-notes` - Process and summarize meeting transcripts
- `/release-announcement` - Create product release communications
- `/get-time` - Get current timestamp

### Available Agents
Use `gemini dev` to launch agents or reference them in prompts:

**Planning & Documentation:**
- `planning-brd-agent` - Creates comprehensive BRDs with technical specifications, user stories, and task breakdowns

**Research & Analysis:**
- `research-synthesizer` - Synthesizes pain points from Reddit/community data using Perplexity and Reddit MCP

**Development:**
- `frontend-developer` - Frontend implementation tasks
- `ui-designer` - UI/UX design and mockup creation

**Review & Feedback:**
- `designer-review-agent` - Design critique and feedback
- `engineer-review-agent` - Technical code review
- `executive-review-agent` - Business-focused review

### Typical PM Workflow
1. **Research Phase**: Use `research-synthesizer` agent to identify pain points
2. **Planning Phase**: Use `/brd` command or `planning-brd-agent` to create specifications
3. **Implementation Phase**: Use `frontend-developer` or appropriate dev agent
4. **Review Phase**: Use review agents for feedback

## 3-Agent Workflow Architecture

### Research Agent
- **Tools**: Perplexity MCP, Reddit MCP, Read, Edit
- **Purpose**: Search and analyze topics, synthesize pain points
- **Output**: 400-500 word pain points document with TL;DR, key issues, quotes, market signals

### Requirements & Documentation Agent  
- **Tools**: CCPM MCP, Google Drive MCP, Slack MCP, Read, Edit
- **Purpose**: Convert research into formal requirements and documentation
- **Output**: Structured BRD, stored documentation, team communications

### Implementation Agent
- **Tools**: Read, Edit, Bash, Grep, Glob, Git
- **Purpose**: Build working prototypes from requirements
- **Output**: Minimal viable implementation demonstrating core functionality

## Demo Personas and Writing Styles

### Demo Personas
- **Mentor**: Supportive, encouraging tone for guidance scenarios
- **Support Pro**: Direct, solution-focused responses for troubleshooting  
- **Skeptical Engineer**: Critical, detail-oriented questions for review scenarios

### Writing Styles (see `docs/writing-styles.md`)
- **Technical**: Precise language, specifications, implementation details
- **User-Friendly**: Conversational, benefit-focused, minimal jargon
- **Internal-Audience**: Strategic context, business rationale, cross-functional language

## Demo Best Practices

### File Operations
- Always use existing demo data files for synthesis exercises
- Reference business context from `docs/business-info.md` for realistic scenarios
- Use customer interview data for pain point analysis

### MCP Demonstrations
- Test Perplexity connection first with simple search
- Use Reddit MCP for community insight gathering
- Show combined MCP workflows for end-to-end automation

### Agent Workflows
- Always run agents in sequence: Research → Requirements → Implementation
- Use realistic business scenarios from provided data
- Keep implementations surgical and demo-focused

## Troubleshooting and Contingencies

### MCP Issues
- If Drive or Slack MCP fails, paste text manually and continue
- Reddit MCP can substitute for some Perplexity functionality
- Always have manual fallback options prepared

### Implementation Issues
- For TypeScript/build failures: "diagnose and apply minimal fix"
- Keep changes surgical and focused on working demo
- Prioritize demonstration over perfect code

### Timing Issues
- Skip slide generation if running short
- Focus on core 3-agent workflow over peripheral features
- Have backup prompts ready in `DEMO-PROMPTS.md`

## Success Metrics for Demo

- **Time Savings**: Demonstrate 12+ hours → 20 minutes workflow compression
- **Quality**: Professional outputs following best practices
- **Integration**: Connected tool ecosystem functionality
- **Accessibility**: Show PM capabilities without coding requirements

## Best Practices for Version Control

- Never commit anything unless confirming first