import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
from src.Bot import Bot

load_dotenv()

intents = discord.Intents.default()

# Add message intents
intents.message_content = True

bot = Bot(command_prefix="!", description="example", intents=intents)

async def main():
    await bot.start(os.getenv("BOT_TOKEN"))
    pass

asyncio.run(main())
    

