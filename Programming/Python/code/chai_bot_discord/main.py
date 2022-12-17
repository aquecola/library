from logging import exception
import nextcord
from nextcord.ext import commands

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    get_channel(1053405191388528710)
    await 



#@bot.command()
#@bot.slash_command(description="Создать канал")
#async def ticket(ctx, member, name):
#  await create_text_channel(name = f'{member}', subject = "test channel")




bot.run(os.environ.get('TOKEN'))