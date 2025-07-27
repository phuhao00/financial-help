# Financial News Crawler

This project is a financial news crawler that aims to provide real-time financial news and events.

## Features

- Crawl financial news from various sources.
- Monitor social media for updates from key figures.
- Provide a calendar of future financial events.
- AI-powered chat for summarizing information and generating content.

## Tech Stack

- **Frontend:** Next.js, Tailwind CSS
- **Backend:** Golang, Gin
- **Crawler:** Python, Flask, crawl4ai
- **Database:** MongoDB

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. **Install dependencies:**
   - **Backend:** `cd backend && go mod tidy`
   - **Crawler:** `cd crawler && pip install -r requirements.txt`
   - **Frontend:** `cd frontend && npm install`
3. **Run the services:**
   - **Crawler:** `cd crawler && python app.py`
   - **Backend:** `cd backend && go run main.go`
   - **Frontend:** `cd frontend && npm run dev`
