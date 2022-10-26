import discord 
from discord.ext import commands
import random as rd
import json


class Events(commands.Cog):

    def __init__(self, client):
        self.client =  client
        self.messageList = list()
        self.loop_guard = False


    #let the terminal know that the bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        print("god i'm so tired")


    #create profanity lists
    profanityFile = open("./data/profanity.txt", "r")
    naughtyWords = []
    prenaughtyWords = profanityFile.readline().split(" ")
    for e in prenaughtyWords: 
        naughtyWords.append(e.strip('\n'))
    prefixes = []
    preprefixes = profanityFile.readline().split(" ") + [""] + naughtyWords
    for e in preprefixes: 
        prefixes.append(e.strip('\n'))
    suffixes = []
    presuffixes = profanityFile.readline().split(" ") + [""] + naughtyWords
    for e in presuffixes: 
        suffixes.append(e.strip('\n'))

    #pull response list from txt file
    responseFile = open("./data/response.json", "r")
    responseDict = json.load(responseFile)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('$'): return
        if not message.author.bot: 
            self.loop_guard = False
        
        #swear detector
            for prefix in self.prefixes:
                for word in self.naughtyWords:
                    for suffix in self.suffixes:
                        #combine lists to make a swear word, then check that word against the content on the message broken up by spaces into a lsit
                        naughtyWord = ''.join([prefix, word, suffix])
                        if  naughtyWord in message.content.split(' '):
                            await message.add_reaction("🤬")

            #repsonses
            for response in self.responseDict:
                if response in message.content and message.author is not self.client.user:
                    await message.channel.send(self.responseDict[response])
                    
            #copy random messages
            #notes:
            #make this one always copy if the message has been sent twice before, ignore its own text, and not dog pile after
            #spongebob text a random message with a low chance, but if it decides to copy it has to spongebob
            #1/10* chance to send a meme version of the text with the actual spongebob meme image, this ones more of a pipedream but doable
            if message.content.lower() not in self.messageList:
                self.messageList.clear()
                random_number = rd.choices([0,1,2,3], weights = [.4, .32, .32 ,.32])[0]
                self.messageList.append(random_number)
                self.messageList.append(message.content.lower())
                self.loop_guard = True

            if message.content.lower() == self.messageList[1] and not self.loop_guard:
                self.messageList.append(message.content.lower())

            if (self.messageList[0] != 0) and (self.messageList[0] + 2 == len(self.messageList)):
                self.messageList.clear()
                await message.channel.send(message.content)
            elif self.messageList[0] == 0:
                sponge_message = str()
                sponge_list = [*message.content.lower()]
                count = 0
                for i,x in enumerate(sponge_list):
                    if x == " ": continue
                    count+=1
                    if count % 2 == 0: sponge_list[i] = x.upper()
                sponge_message = ''.join(sponge_list)    
                await message.channel.send(sponge_message)

            #bruh mining event from js bot, worked p well.
            #think about ways to improve it

def setup(client):
    client.add_cog(Events(client)) 