# Expertly AI Demos

Interactive demonstrations and prototypes for Expertly AI.

## Purpose

This application serves static HTML/JS demo pages. It provides a simple landing page with links to various interactive demos that can be added over time without code changes.

## Deployment

- **Platform**: Coolify on DigitalOcean
- **Method**: Docker container auto-deployed on push to main branch
- **URL**: http://rgs4ssgs4skocsg0kkck0o0g.174.138.81.31.sslip.io

## Environment Variables

None required. This is a static file server with no database or external service dependencies.

## Database Usage

None.

## Adding New Demos

1. Create a new HTML file in `static/` (e.g., `static/demo-chatbot.html`)
2. Add a link to the demo in `static/index.html`
3. Push to GitHub - auto-deploys via Coolify

No code changes to the FastAPI app are needed for new static demos.

## Local Development

### Run with Docker

```bash
docker build -t expertly-demos .
docker run -p 8000:8000 expertly-demos
```

Visit http://localhost:8000

### Run without Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Project Structure

```
expertly-ai-demos/
├── README.md
├── Dockerfile
├── requirements.txt
├── .gitignore
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI app serving static files
└── static/
    ├── index.html           # Landing page
    ├── css/
    │   └── style.css        # Shared styles
    └── js/
        └── common.js        # Shared JavaScript utilities
```

## Background/Cron Jobs

None.

## Migration Instructions

N/A - no database.

## Operational Notes

- Static file server with minimal resource requirements
- No state stored on server - all important content is in Git
- To add demos: create HTML files in `static/`, push to GitHub
