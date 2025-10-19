## Recommended Speckit Command Order

### 1. `/speckit.specify` - START HERE
- Define feature requirements and user stories  
- Establish acceptance criteria  
- Prioritize user stories (P1, P2, P3...)

### 2. `/speckit.plan` - SECOND
- Input: Feature specification from spec step
- Define technical approach and context  
- Determine project structure and dependencies  
- Output: `research.md`, `data-model.md`, `quickstart.md`

### 3. `/speckit.tasks` - THIRD
- Input: `spec.md` (for user stories) and `plan.md` (for technical context)  
- Break down user stories into implementable tasks  
- Organize tasks by user story for independent implementation

### 4. `/speckit.checklist` - OPTIONAL/AS NEEDED
- Create when you need specific verification items  
- Based on feature context from `spec.md`, `plan.md`, and `tasks.md`

### 5. `/speckit.clarify` - AS NEEDED
- Use if you need to refine or clarify any part of your spec/plan

### 6. `/speckit.analyze` - AS NEEDED
- Use to analyze and review your work

### 7. `/speckit.implement` - FINAL
- Execute the tasks and build your feature

### 8. `/speckit.constitution` - REFERENCE/SETUP
- Your project's guidelines and principles (reference/setup file)

**Summary**: `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → (optional: `/speckit.clarify`, `/speckit.analyze`, `/speckit.checklist`) → `/speckit.implement`

**The flow**: *define requirements → plan technically → break into tasks → verify with checklists → implement*