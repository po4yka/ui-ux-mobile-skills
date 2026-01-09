# uipro-mobile CLI

CLI tool for installing UI/UX Mobile skill for Claude Code and OpenAI Codex.

## Installation

```bash
npm install -g uipro-mobile
```

Or use directly with npx:

```bash
npx uipro-mobile init
```

## Usage

### Install Skill

Install the UI/UX Mobile skill in your project:

```bash
# Interactive mode (prompts for AI type)
uipro-mobile init

# Install for specific AI
uipro-mobile init --ai claude
uipro-mobile init --ai codex
uipro-mobile init --ai all

# Force overwrite existing installation
uipro-mobile init --ai claude --force
```

### Update Skill

Update to the latest version:

```bash
# Update detected installation
uipro-mobile update

# Update specific AI
uipro-mobile update --ai claude
uipro-mobile update --ai all
```

### List Versions

```bash
uipro-mobile versions
```

## Supported AI Assistants

| AI | Folder | Skill Path |
|----|--------|------------|
| Claude Code | `.claude/` | `.claude/skills/ui-ux-mobile/` |
| OpenAI Codex | `.codex/` | `.codex/skills/ui-ux-mobile/` |

## What Gets Installed

- `SKILL.md` - Skill definition and workflow instructions
- `scripts/` - Python search engine (BM25)
- `data/` - CSV databases (8 domains + 7 stacks)

## Requirements

- Node.js 18+
- Python 3.x (for running the search scripts)

## Development

```bash
# Install dependencies
npm install

# Run in development
npm run dev init

# Build
npm run build

# Run built version
npm start init
```
