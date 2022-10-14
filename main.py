import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import asyncio
async def login():
    intents = discord.Intents.all()
    intents.members = True
    intents.typing = True
    intents.presences = True
    client = commands.Bot(command_prefix = '$', intents = intents)

    #error log initialization
    logging.basicConfig(level=logging.INFO)

    #encryption
    load_dotenv()

    @client.command()
    async def load(ctx, extension):
        await client.load_extension(f'cogs.{extension}')

    @client.command()
    async def unload(ctx, extension):
        await client.unload_extension(f'cogs.{extension}')

    @client.command()
    async def reload(ctx, extension):
        await client.unload_extension(f'cogs.{extension}')
        await client.load_extension(f'cogs.{extension}')

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

    await client.start(os.getenv("DISCORD_TOKEN"))
asyncio.run(login())