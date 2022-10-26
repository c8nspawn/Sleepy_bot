import discord
from discord.ext import commands
import json

class updateResponse(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["addresponse", "ar"])
    async def addResponse(self, ctx):
        self.client.unload_extension('cogs.events')

        try:
            #read current dictionary into a variable
            responseList = open("./data/response.json", "r")
            responseDict = json.load(responseList)
            responseList.close()

            #ask for responses
            await ctx.send("what would you like me to respond to")
            check = await self.client.wait_for('message', timeout = 30.0, check=lambda message: message.author == ctx.author and "$" not in message.content)
            await ctx.send("how would you like me to respond")
            response = await self.client.wait_for("message", timeout = 30.0, check=lambda message: message.author == ctx.author and "$" not in message.content)
            await ctx.send("ok. when you say {}, i'll say {}".format(check.content, response.content))

            #update the json file and format it using an indent
            responseDict.update({check.content: response.content})
            responseList = open("./data/response.json", "w+")
            json.dump(responseDict, responseList, indent = 4)
            responseList.close()

            #reload the events cog so the bot will immediately start responding without need to be restarted
            self.client.load_extension('cogs.events')
 
        except:
            #fail clause
            await ctx.send("slow down, bucko")



    @commands.command(aliases = ["updateresponse", "ur"])
    async def updateResponse(self, ctx):
        self.client.unload_extension('cogs.events')
        try:
            #read current dictionary into a variable
            responseList = open("./data/response.json", "r")
            responseDict = json.load(responseList)
            responseList.close()

            #ask the user which response they want to remove
            await ctx.send("which response would you like to change")
            response = await self.client.wait_for("message", timeout = 30.0, check=lambda message: message.author == ctx.author and message.content in responseDict)
            await ctx.send("would you like to update or remove this response")
            change = await self.client.wait_for("message", timeout = 30.0, check=lambda message: message.author == ctx.author and message.content in ["update", "remove"])

            #update the value of the chosen key
            if change.content == "update": 
                await ctx.send(f"how would you like me to respond to {response.content}")
                newResponse = await self.client.wait_for("message", timeout = 30.0, check=lambda message: message.author == ctx.author and "$" not in message.content)
                await ctx.send(f"okay, now whenever you say {response.content}, i'll say {newResponse.content}")
                responseDict[response.content] = newResponse.content

            #remove the check and reponse from the dict
            elif change.content == "remove":
                await ctx.send(f"are you sure you no longer want me to respond to {response.content}")
                answer = await self.client.wait_for("message", timeout = 20.0, check=lambda message: message.author == ctx.author and message.content.lower() in ['y', 'ye', 'yes', 'n', 'no'])
                if answer.content.lower() in ['y', 'ye', 'yes']:
                    await ctx.send(f"okay, i will no longer respond to {response.content}")
                    del responseDict[response.content]
                    print(responseDict)
                else:
                    await ctx.send("operation cancelled")
                    return
            
            #update the file with any changes made
            responseList = open("./data/response.json", "w+")
            json.dump(responseDict, responseList, indent = 4)
            responseList.close()

            #reload the events cog so the bot will immediately start responding without need to be restarted
            self.client.load_extension('cogs.events')

        except:
            await ctx.send("slow down, bucko")



def setup(client):
    client.add_cog(updateResponse(client)) 