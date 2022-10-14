import discord
from discord.ext import commands
import random

class RollTheDice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name = "d")
    async def _dice(self, ctx, args):
        # decide whether or not proper args were passed
        if not self.is_int(args): 
            await ctx.send("enter the number of sides on the die you want to roll.") 
            return

        faces = int(args)
        # dice roll
        roll = random.randrange(1, faces)
        await ctx.send(roll)


    # function to decide whether or not command should continue
    def is_int(self, args):
        try:
            int(args)
            return True
        except:
            return False

def setup(client):
    client.add_cog(RollTheDice(client)) 