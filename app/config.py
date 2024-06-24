from dotenv import load_dotenv
import os

load_dotenv()

# Discord
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

