from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def daikon(ctx):
    await ctx.send('pythonだって書けちゃう天才なんだよなぁ...')
    
@bot.command()
async def role(ctx):
    await ctx.send('::role')
   
@bot.command()
async def role(ctx):
    await ctx.send('::role')

@bot.command()
async def 1(ctx):
    await ctx.send('1')
    
@bot.command()
async def login(ctx):
    await ctx.send('::login')
    



bot.run(token)
