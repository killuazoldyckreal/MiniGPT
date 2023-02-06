import revopenai
import nextcord
from nextcord.ext import commands
import traceback
class Prefixcommands(commands.Cog, name="Prefix Commands"):
    """These are prefix commands you can use for MiniGPT"""

    COG_EMOJI = "❗"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['c'])
    async def chat(self,ctx, *query:str):
        """Ask anything to MiniGPT\nShort command: =c <query>"""
        query=" ".join(query)+" but while writing if your response contain a program add 3 backticks and program language name in the starting and 3 backticks at the end of the program"
        try:
            if ctx.message.author == self.bot.user:
                return
            if ctx.message.author.bot:
                return
            msg = await ctx.send("MiniGPT is thinking...")
            response = revopenai.make_request(query)
            await msg.delete()
            await ctx.reply(response)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await ctx.reply("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @commands.command(aliases=['s'])
    async def save(self,ctx,*conversation_name:str):
        """Save your conversation using this command\nShort command: =s <conversation_name>"""
        conversation_name=" ".join(conversation_name)
        try:
            if ctx.message.author == self.bot.user:
                return
            if ctx.message.author.bot:
                return
            msg = await ctx.send("MiniGPT is thinking...")
            message = revopenai.make_request(f"!save_c {conversation_name}")
            await msg.delete()
            await ctx.reply(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await ctx.reply("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()
    
    @commands.command(aliases=['l'])
    async def load(self,ctx,*conversation_name:str):
        """Load your previous conversations using this command\nShort command: =l <conversation_name>"""
        conversation_name=" ".join(conversation_name)
        try:
            if ctx.message.author == self.bot.user:
                return
            if ctx.message.author.bot:
                return
            msg = await ctx.send("MiniGPT is thinking...")
            message = revopenai.make_request(f"!load_c {conversation_name}")
            await msg.delete()
            await ctx.reply(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await ctx.reply("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @commands.command(aliases=['r'])
    async def reset(self,ctx):
        """Reset your current conversation\nShort command: =r"""
        try:
            if ctx.message.author == self.bot.user:
                return
            if ctx.message.author.bot:
                return
            msg = await ctx.send("MiniGPT is thinking...")
            message = revopenai.make_request("!reset")
            await msg.delete()
            await ctx.reply(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await ctx.reply("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @commands.command(aliases=['q'])
    async def query(self,ctx):
        """Shows your current query\nShort command: =q"""
        try:
            if ctx.message.author == self.bot.user:
                return
            if ctx.message.author.bot:
                return
            msg = await ctx.send("MiniGPT is thinking...")
            message = revopenai.make_request("!query")
            await msg.delete()
            await ctx.reply(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await ctx.reply("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @commands.command(aliases=['sf'])
    async def savefile(self,ctx, *file_name:str):
        """Save all your conversation in a file\nShort command: =sf <file_name>"""
        file_name=" ".join(file_name)
        try:
            if ctx.message.author == self.bot.user:
                return
            if ctx.message.author.bot:
                return
            msg = await ctx.send("MiniGPT is thinking...")
            message = revopenai.make_request(f"!save_f {file_name}")
            await msg.delete()
            await ctx.reply(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await ctx.reply("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()


    @commands.command(aliases=['lf'])
    async def loadfile(self,ctx, *file_name:str):
        """Load all conversations from a file\nShort command: =lf <file_name>"""
        file_name=" ".join(file_name)
        try:
            if ctx.message.author == self.bot.user:
                return
            if ctx.message.author.bot:
                return
            msg = await ctx.send("MiniGPT is thinking...")
            message = revopenai.make_request(f"!load_f {file_name}")
            await msg.delete()
            await ctx.reply(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await ctx.reply("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()


def setup(bot: commands.Bot):
    bot.add_cog(Prefixcommands(bot))


