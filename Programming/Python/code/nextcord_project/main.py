from contextvars import Context
from distutils.command.build_ext import extension_name_re
from json import load
import nextcord
from dotenv import load_dotenv, find_dotenv
import os
from nextcord.ext import commands

load_dotenv(find_dotenv())

COGS_FOLDER = 'cogs'


class Keanu(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.load_extensions

def load_extensions(self) -> None:
    for filename in os.listdir(COGS_FOLDER):
        if filename.endswith ('.py'):
            try:    
                self.load_extension(f'cogs.{filename[:-3]}')
            except Exception as e:
                print(f'Cant load cog {filename[:-3]}, Error: {e}')

async def on_error(self, event, *args):
    print(f'Error in {event}')


async def on_ready(self):
    print('Bot is connected to server')


bot = Keanu(command_prefix = '!', intents = nextcord.Intents.all(), owner_ids = [284734701556727808])

@bot.command(
    name = 'load'
)

@commands.is_owner()
async def _load(ctx:commands.Context, ext_name:str):
    if not ext_name.startwith('cogs'):
        ext_name = 'cogs.'+ext_name
    
    try:
        bot.load_extension(ext_name)
        await ctx.send('Расширение успешно загружено')
    except Exception as e:
        print(e)
        await ctx.send('Ошибка загрузки расширения')


@bot.command(
    name = 'unload'
)

@commands.is_owner()
async def _unload(ctx:commands.Context, ext_name:str):
    if not ext_name.startwith('cogs'):
        ext_name = 'cogs.'+ext_name
    
    try:
        bot.unload_extension(ext_name)
        await ctx.send('Расширение успешно отключено')
    except Exception as e:
        print(e)
        await ctx.send('Ошибка отключения расширения')


@bot.command(
    name = 'reload'
)

@commands.is_owner()
async def _load(ctx:commands.Context, ext_name:str):
    if not ext_name.startwith('cogs'):
        ext_name = 'cogs.'+ext_name
    
    try:
        bot.unload_extension(ext_name)
        bot.load_extension(ext_name)
        await ctx.send('Расширение успешно перезагружено')
    except Exception as e:
        print(e)
        await ctx.send('Ошибка перезагрузки расширения')







if __name__ == '__main__':
    bot.run(os.environ.get('TOKEN'))