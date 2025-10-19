# Complete Prompt Architecture for Copilot Skills

## Three Types of Prompts

### 1. Workflow Prompts (`speckit.*`)
**Purpose**: Manage the feature development workflow  
**Location**: `.github/prompts/speckit.*.prompt.md`  
**Commands**: `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`

These tell agents how to USE the `.specify/` infrastructure.

### 2. Skill Management Prompts (`skills.*`)
**Purpose**: Create, validate, and manage skills  
**Location**: `.github/prompts/skills.*.prompt.md`  
**Commands**: `/skills.create`, `/skills.validate`, `/skills.discover`, `/skills.use`

These tell agents how to manage the `.github/copilot-skills/` infrastructure.

### 3. Individual Skill Prompts (`skill-{name}`)
**Purpose**: Load and use a specific skill  
**Location**: `.github/prompts/skill-{skill-name}.prompt.md`  
**Commands**: `/skill-hello-skill`, `/skill-pdf-handling`, `/skill-database-migration`

These tell agents HOW to use each individual skill with progressive disclosure.

## Why Each Skill Needs a Prompt

Without a prompt file, Copilot can't:
- Know WHEN to load the skill (relevance detection)
- Know HOW to load it progressively (which files to read first)
- Provide a `/skill-{name}` command for explicit invocation
- Understand the skill's metadata and capabilities

## The Two-Part Skill Structure

Every skill consists of:

### Part 1: Skill Files (in `.github/copilot-skills/`)
```
.github/copilot-skills/{skill-name}/
├── SKILL.md              # Core file (always loaded first)
├── patterns.md           # Detail file (loaded on demand)
├── reference.md          # Detail file (loaded on demand)
└── scripts/              # Bundled scripts (referenced when needed)
    └── example.py
```

### Part 2: Skill Prompt (in `.github/prompts/`)
```
.github/prompts/skill-{skill-name}.prompt.md
```

This prompt tells Copilot:
- **When** to use this skill (relevance keywords)
- **How** to load it progressively (which files in which order)
- **What** each file contains (so it knows what to load)
- **Why** to use this skill (what problems it solves)

## Example: hello-skill

### Skill Files
- `.github/copilot-skills/hello-skill/SKILL.md` - Core overview
- `.github/copilot-skills/hello-skill/patterns.md` - Pattern details
- `.github/copilot-skills/hello-skill/reference.md` - API reference
- `.github/copilot-skills/hello-skill/scripts/hello-example.py` - Script

### Skill Prompt
- `.github/prompts/skill-hello-skill.prompt.md` - Usage instructions

When you type `/skill-hello-skill`:
1. Copilot reads the prompt file
2. Prompt tells it to load SKILL.md first
3. If user asks for patterns → load patterns.md
4. If user asks for API details → load reference.md
5. If user wants to run scripts → reference scripts/

## Implementation Impact

This means the `create-skill.sh` script must:
1. Create skill files in `.github/copilot-skills/{skill-name}/`
2. **ALSO** create prompt file in `.github/prompts/skill-{skill-name}.prompt.md`

Both files generated from templates with same metadata.

## Commands Available After Implementation

### Workflow Management
- `/speckit.specify` - Create feature spec
- `/speckit.plan` - Generate implementation plan
- `/speckit.tasks` - Break into tasks
- `/speckit.implement` - Execute implementation

### Skill Management
- `/skills.create` - Create new skill (generates BOTH skill files AND prompt)
- `/skills.validate` - Check constitution compliance
- `/skills.discover` - Search for skills
- `/skills.use` - Load a skill into context

### Individual Skills
- `/skill-hello-skill` - Use the demo skill
- `/skill-pdf-handling` - Use PDF skill (when created)
- `/skill-database-migration` - Use DB migration skill (when created)
- ... (one command per skill)

## Why This Works

1. **Discoverability**: Type `/` to see all commands (workflow + skills + individual skills)
2. **Progressive Disclosure**: Prompt controls which files load when
3. **Separation of Concerns**: Workflow vs management vs usage
4. **Scalability**: Adding a skill = adding files + adding one prompt
5. **Consistency**: All prompts follow same pattern (from template)

This is the architecture that makes `.specify/` work, now applied to skills! 🎯
