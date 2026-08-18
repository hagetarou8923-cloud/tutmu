import asyncio
import logging
import os
import sys

import discord
from discord.ext import commands

from config import config

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('bot.log')
    ]
)
logger = logging.getLogger(__name__)

class TsumTsumBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix=config.PREFIX,
            intents=intents,
            help_command=None
        )
        
        self.start_time = None
    
    async def setup_hook(self):
        """Cogをロード"""
        self.start_time = discord.utils.utcnow()
        
        cogs = [
            "cogs.orders",
            "cogs.admin", 
            "cogs.stats",
            "cogs.autoplay",
            "cogs.payment"
        ]
        
        for cog in cogs:
            try:
                await self.load_extension(cog)
                logger.info(f"Loaded cog: {cog}")
            except Exception as e:
                logger.error(f"Failed to load cog {cog}: {e}")
        
        # スラッシュコマンド同期
        await self.tree.sync()
        logger.info("Slash commands synced")
    
    async def on_ready(self):
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        logger.info(f"Connected to {len(self.guilds)} guilds")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="ツムツム代行注文"
            )
        )

def main():
    bot = TsumTsumBot()
    
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("⚠️ 権限がありません。")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"⚠️ 引数が不足しています: `{error.param.name}`")
        else:
            logger.error(f"Command error: {error}")
            await ctx.send(f"⚠️ エラー: {str(error)}")
    
    bot.run(config.TOKEN)

if __name__ == "__main__":
    main()