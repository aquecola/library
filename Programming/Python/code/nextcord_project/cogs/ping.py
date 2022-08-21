import nextcord
from nextcord.ext import commands


class Ping(commands.Cog):

    def __init__(self, bot:commands.Bot):  

        self.bot = bot

@commands.command(
    name='ping'
)
    async def _ping(self, ctx:commands.Context):
        return await ctx.send(f'Bot ping is {int(self.bot.latency*1000)} ms')


def setup(bot:commands.Bot):
    bot.add_cog(Ping(bot))