import discord
import random 
from discord.ext import commands

client = commands.Bot(command_prefix ='.')

@client.event 

async def on_ready():
   print('Bot is ready.')



@client.command()
async def ping(ctx):
      await ctx.send(f'Pong ! {round(client.latency * 1000)}ms ')

@client.command(aliases=["8ball",'guess'])
async def _8ball(ctx,*, question):
    responses = ['Yes',"No","My bad"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')  

@client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@client.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@client.command()
async def about(ctx):
    await ctx.send('Still trying to make it hehe')

@client.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

client.run('token')  