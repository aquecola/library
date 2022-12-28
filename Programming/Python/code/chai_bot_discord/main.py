from logging import exception
import nextcord
from nextcord.ext import commands

from dotenv import load_dotenv, find_dotenv
import os

from nextcord.ext import commands, tasks


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

        # start the task to run in the background
        self.my_background_task.start()
        intents = nextcord.Intents.default()

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(1057720328182308966)  # channel ID goes here
        self.counter += 1
        players = len(channel.members)
        print(channel.members.)
        await channel.edit(name='Sanya5555')
        await channel.send(players)
    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


bot = Bot()
bot.run("OTU5ODU2Mjc3MzczMTk4MzU2.GhjpIO.4XT8Ud9RxSWVsxRaFmljiX36YtehNi0vZv5vG0")
