import os

# Discord
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

# Bybit
BYBIT_BASE_URL = 'https://api-testnet.bybit.com'
BYBIT_PRICE_INDEX_URL = BYBIT_BASE_URL + '/v5/market/index-price-kline'

# RSI
DEFAULT_RSI_PERIOD = 14
RSI_LOWER_BOUND = 30
RSI_UPPER_BOUND = 70

