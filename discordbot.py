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
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
async def on_message(message):
    if message.content.startswith("!tnp"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,20)
            m = str(num_random)
            await client.send_message(message.channel, m)

    



bot.run(token)
