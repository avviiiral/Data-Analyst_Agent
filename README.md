# Data Analyst Agent (backend)

Backend-only Python project for an agent-based data analysis workflow built on FastAPI. It contains dataset profiling and statistics modules, a planning and orchestration framework, and agent services.

## Layout

| Path | Contents |
|---|---|
| `backend/app/main.py` | FastAPI application entry point |
| `backend/app/api/v1/` | HTTP API routes |
| `backend/app/agents/` | Agent implementations |
| `backend/app/services/ai`, `backend/app/services/ml` | AI and machine-learning services |
| `backend/app/repositories`, `backend/app/db`, `backend/app/models`, `backend/app/schemas` | Data access, persistence and schemas |
| `backend/framework/planning`, `backend/framework/orchestration` | Planner and workflow orchestration |
| `backend/analytics/` | Profiling, data quality, statistics, correlation, distribution, outlier, insight and recommendation modules |

Dependencies are listed in `backend/requirements.txt`. This repository has no frontend and no automated tests, and setup instructions have not been verified, so none are documented here.

## Related

- [InsightForge-AI](https://github.com/avviiiral/InsightForge-AI): a documented data-analyst agent platform from the same author.
- [AI Data Analyst Agent case study](https://aviral-goyal.netlify.app/projects/ai-data-analyst-agent.html)
- Author: [Aviral Goyal](https://aviral-goyal.netlify.app/) · [GitHub](https://github.com/avviiiral) · [LinkedIn](https://www.linkedin.com/in/avviiiral/)
