import discord 
from discord.ext import commands
import random

class Magic8ball(commands.Cog):

    def __init__(self, client):
        self.client =  client
        self.responses = ["It is certain", 
                "It is decidedly so", 
                "Without a doubt", 
                "Yes - definitely",
                "You may rely on it", 
                "As I see it, yes", 
                "Most likely", 
                "Outlookin' good 🤠", 
                "Yes", "Signs point to yes",
                "Don't count on it", 
                "My reply is no",
                "My sources say no", 
                "Outlookin' bad 😧",
                "Very doubtful", 
                "Reply hazy, try again", 
                "Ask again later", 
                "Better not tell you now",
                "Cannot predict now", 
                "Concentrate and ask again"
                ]

    @commands.command(name = '8ball')
    async def _8ball(self, ctx, *words):
        #define embed
        ballEmbed = discord.Embed(title = "The Magic 8ball says...", description = '**Question:** \n{}'.format(' '.join(words)))
        ballEmbed.set_image(url ="http://clipart-library.com/new_gallery/76-769420_8-ball-png-battle-for-bfdi-8-ball.png")

        #function that is called to create an additional answer field in the embed
        def addField(str):
            ballEmbed.add_field(name = f'Answer: ', value = f'{str}')

        #decide what kind of message to send        
        if words == (): 
            await ctx.send("please enter a question.")
        elif 'who' and 'asked' in words:
            addField('your mother')
            await ctx.send(embed = ballEmbed)
        elif 'fugma' in words:
            addField('well, can you fugma ass?')
            await ctx.send(embed = ballEmbed)
        else:
            addField(f'{random.choice(self.responses)}')
            await ctx.send(embed = ballEmbed)

    

async def setup(client):
    await client.add_cog(Magic8ball(client)) 