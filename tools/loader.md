# How to Load giri-skills into AI Tools

To maintain consistent engineering standards across different AI agents (Gemini CLI, Claude Code, etc.), use the following instructions.

## For Claude Code / Other CLI Agents
Copy and paste the following into your system prompt or `.clauderc`:

```markdown
Follow the engineering standards and coding principles defined in the local repository: ~/IdeaProjects/giri-skills.
- Use `core/general.md` for response style and philosophy.
- Use `stacks/spring-boot.md` for Spring Boot/Kotlin standards.
- Use `patterns/api-design.md` for API design.
- Always prioritize official documentation and maintain backward compatibility.
```

## For IDE Plugins (GitHub Copilot, etc.)
Add the contents of `core/general.md` and relevant `stacks/` files to your custom instruction settings (e.g., `.github/copilot-instructions.md`).

## Maintenance
- Run `git pull` in `~/IdeaProjects/giri-skills` to stay updated with the latest principles.
- If you identify better patterns during development, update the markdown files in this repository.
