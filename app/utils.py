import aiohttp
import pandas as pd
import pandas_ta as ta

BYBIT_BASE_URL = 'https://api-testnet.bybit.com'
BYBIT_PRICE_INDEX_URL = BYBIT_BASE_URL + '/v5/market/index-price-kline'
DEFAULT_RSI_PERIOD = 14


async def get_historical_data(symbol: str, interval: int, category: str, period: int):
    params = {
        'symbol': symbol,
        'category': category,
        'interval': interval,
        'limit': period + 1
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BYBIT_PRICE_INDEX_URL, params=params) as response:
            data = await response.json()
    return data


async def calculate_rsi(
        symbol: str,
        interval: int,
        category: str = 'linear',
        period: int = DEFAULT_RSI_PERIOD
):
    data = await get_historical_data(symbol, interval, category, period)

    df = pd.DataFrame(
        data=data['result']['list'],
        columns=['timestamp', 'open', 'high', 'low', 'close']
    )
    df['close'] = df['close'].astype(float)
    rsi = ta.rsi(df['close']).iloc[-1]
    return rsi
