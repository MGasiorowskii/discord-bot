import aiohttp
import pandas as pd
import pandas_ta as ta

import config


async def get_historical_data(symbol: str, interval: int, category: str, period: int):
    params = {
        'symbol': symbol,
        'category': category,
        'interval': interval,
        'limit': period + 1
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(config.BYBIT_PRICE_INDEX_URL, params=params) as response:
            data = await response.json()
    return data


async def calculate_rsi(
        symbol: str,
        interval: int,
        category: str = 'linear',
        period: int = config.DEFAULT_RSI_PERIOD
):
    data = await get_historical_data(symbol, interval, category, period)

    df = pd.DataFrame(
        data=data['result']['list'],
        columns=['timestamp', 'open', 'high', 'low', 'close']
    )
    df['close'] = df['close'].astype(float)
    rsi = ta.rsi(df['close'], period).iloc[-1]
    return rsi
