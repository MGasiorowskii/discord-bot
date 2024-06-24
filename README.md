# Discord Bot

Discord Bot is a Python-based project that uses the Discord API to interact with users on a Discord server.
Bot fetches spot K-line data for SOL/USDT pair from Bybit API and 
sends a text message to Discord channel if the calculated RSI value is over 70 or below 30.

## Requirements

- Python 3.12
- Docker
- Docker Compose

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mateusz-gasiorowski/discord-bot.git
```
2. Navigate to the project directory:
```bash
cd discord-bot
```
3. Complete `.env` file with your `DISCORD_TOKEN` and `DISCORD_CHANNEL_ID`
4. Build the Docker image:
```bash
docker-compose build
```
5. Run the Docker container:
```bash
docker-compose up
```

## Usage

Once running, the bot will be available on your Discord server.
