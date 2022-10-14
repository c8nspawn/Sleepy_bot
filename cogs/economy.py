import discord
from discord.ext import commands

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    #mongodb profileschema for economy: wallet, ID; might need to go into its own profileschema file

    #gamba mini-games, maybe this time add some roulette people can play together
    

def setup(client):
    client.add_cog(Economy(client)) 