# Future Skills - Documentation Generation Status

This document tracks the status of documentation skills in development.

## Status Legend

- ✅ Skill generated - Full documentation skill created
- ⏳ Generation pending - Config ready for scraping  
- ⚠️ Anti-scraping - Site blocks automated access
- 📋 Config ready - Configuration file created

---

## UI / Components

- [shadcn/ui](https://ui.shadcn.com/docs) ✅ skill generated
- [Radix UI](https://www.radix-ui.com/docs) ✅ skill generated
- [Chakra UI](https://chakra-ui.com/docs) ⚠️ anti-scraping detected
- [Material UI](https://mui.com/material-ui/getting-started/overview/) ✅ skill generated
- [Ant Design](https://ant.design/docs/react/introduce) ✅ skill generated
- [Mantine](https://mantine.dev/docs/) ✅ skill generated, 148 pages
- [DaisyUI](https://daisyui.com/docs/) ⚠️ anti-scraping detected
- [Headless UI](https://headlessui.com/react) ✅ skill generated, 27 pages
- [Bootstrap](https://getbootstrap.com/docs/) ⚠️ anti-scraping, 1 page
- [Tailwind CSS](https://tailwindcss.com/docs) ⚠️ manual approach needed

## Frontend Frameworks

- [React](https://react.dev) ✅ skill generated, 150+ pages
- [Next.js](https://nextjs.org/docs) ✅ skill generated, 150+ pages
- [Vue.js](https://vuejs.org/guide/introduction.html) ✅ skill generated, 150+ pages
- [Nuxt](https://nuxt.com/docs) ⚠️ blocked, 1 page
- [Svelte](https://svelte.dev/docs) ✅ skill generated, ~20 pages
- [Angular](https://angular.dev) ⚠️ blocked, 1 page

## Backend / Fullstack

- [Express](https://expressjs.com/en/starter/installing.html) ⚠️ config created, blocked
- [NestJS](https://docs.nestjs.com) ⚠️ config created, blocked
- [Django](https://docs.djangoproject.com/en/stable/) ⏳ config ready, ~20 pages
- [FastAPI](https://fastapi.tiangolo.com/) ✅ skill generated, 150+ pages

## Databases / ORMs

- [Prisma](https://www.prisma.io/docs) ✅ skill generated, 150+ pages
- [Sequelize](https://sequelize.org/docs/) ⚠️ config created, blocked
- [Supabase](https://supabase.com/docs) ✅ skill generated, 150+ pages

## Infrastructure / DevOps

- [Kubernetes](https://kubernetes.io/docs/) ⏳ config ready, ~20 pages
- [Terraform](https://developer.hashicorp.com/terraform/docs) ⚠️ config created, blocked
- [Vercel](https://vercel.com/docs) ✅ skill generated, ~20 pages

## Languages

- [Python](https://docs.python.org/3/) ⏳ config ready, ~20 pages
- [TypeScript](https://www.typescriptlang.org/docs/) ✅ skill generated, ~20 pages

## AI / LLMs

- [LangChain](https://python.langchain.com/docs/) ✅ skill generated, 150+ pages

## Tools

- [Storybook](https://storybook.js.org/docs) ✅ skill generated, ~20 pages

---

## Summary

- **Total Generated**: 19 skills
- **Ready for Generation**: 3 configs (Django, Kubernetes, Python)
- **Total Configs**: 40+
- **Blocked**: 12+ sites

## Generate a Skill

```bash
python3 .github/copilot-skills/tools/docs-to-skill/scripts/scrape_docs.py \
  --config .github/copilot-skills/tools/docs-to-skill/configs/[name].json
```
