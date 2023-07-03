from discord.ext import commands
from src.cogs.Telepathy import Telepathy as Telepathy

class Bot(commands.Bot):
    async def on_ready(self):
        print("Bot is ready")
    
    async def setup_hook(self) -> None:
        await super().setup_hook()
        await self.add_cog(Telepathy(self))
        return