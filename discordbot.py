from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def daikon(ctx):
    await ctx.send('大根ちゃんはPythonも書けちゃう天才なんだよなぁ...')
    
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def yamaha(ctx):
    await ctx.send('やまはさんはただのJS....')
    
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def taruru(ctx):
    await ctx.send('ク○ニ所望してるひといますか？')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def pomuai(ctx):
    await ctx.send('おいおい純粋悪の悪口はやめとけよ、消されるぞ')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def kuruchan(ctx):
    await ctx.send('ふごふごふごふごふごふご！ふごふご！！ふごっ！！ふごふご！！')
    
    
    
    @bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def akira(ctx):
    await ctx.send('【極彰マクロ】
                   ```/p  [基本散会]  l  [メテオ・バハ線　四隅捨て]
/p 　   MT         l MTD3　　H２D4
/p    D3   D4     l
/p H1        H2   l※召喚十字：バハ線捨ても同位置
/p    D1   D2     l
/p        ST          l H１D1　　STD２
/p [LB２ 東西4:4]
/p 西MTD1D3H1　STD2D4H2東
/p [ブレイバー]　北タンク　南DPS　西H１ 東H２
/p [幻光　暗黒]
/p  タンク：北　ヒラ：東西　DPS：南　頭割り：中央
/p [幻光　黒魔・召喚十字・忍者]
/p 　　MTD3
/p D1H1　H2D4
/p 　　STD2```')

    


bot.run(token)
