# Chat Assistant for SQLite Database

This project is a chat assistant that interacts with an SQLite database to answer user queries using natural language processing.

## Features
- Supports queries like:
  - "Show me all employees in the Sales department."
  - "Who is the manager of the Engineering department?"
  - "List all employees hired after 2021-01-01."
  - "What is the total salary expense for the Marketing department?"
- Handles case-insensitive queries and flexible date formats.
- Provides a user-friendly interface for interacting with the chatbot.

## How It Works
The chat assistant uses FastAPI as the backend framework and SQLite as the database. It parses natural language queries, converts them into SQL queries, and fetches results from the database. The frontend is a simple HTML page served via the `/static` endpoint.

## Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/farshadabdulazeez/Chat-Assistant-for-SQLite-Database.git
   cd Chat-Assistant-for-SQLite-Database
