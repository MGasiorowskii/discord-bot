import discord
import config
import asyncio

from utils import calculate_rsi

from datetime import datetime
from discord.ext import tasks, commands


RSI_LOWER_BOUND = 30
RSI_UPPER_BOUND = 70

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.default()
)


@bot.event
async def on_ready():
    print("The bot is ready!")
    send_rsi_signal.start()


@tasks.loop(hours=1, reconnect=True)
async def send_rsi_signal():
    channel = bot.get_channel(config.CHANNEL_ID)
    rsi = await calculate_rsi(
        symbol="SOLUSDT",
        interval=60,  # 1 hour
    )

    if rsi < RSI_LOWER_BOUND or rsi > RSI_UPPER_BOUND:
        await channel.send(f"RSI is in the overbought or oversold zone! - {round(rsi, 2)}")


@send_rsi_signal.before_loop
async def wait_for_full_hour():
    await bot.wait_until_ready()
    while True:
        now = datetime.now()
        if now.minute == 0 and now.second < 10:
            break

        await asyncio.sleep(10)


if __name__ == "__main__":
    bot.run(config.TOKEN)
