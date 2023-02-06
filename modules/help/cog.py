import nextcord
from nextcord.ext import commands


class Helpmenu(commands.Cog, name="Help"):
    """Shows help info"""

    COG_EMOJI = "❔"

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
    
    @commands.command()
    async def help(self, ctx):
        """Opens Help Menu
		
		Displays all the available commands
		"""
        emb=nextcord.Embed(title="Help Menu",description="These are the available commands you can use in MiniGPT",color=0x3c71e2)
        emb.set_author(name=f"{self.bot.user}",icon_url=self.bot.user.display_avatar)
        emb.add_field(name="1. =chat <query>", value="Ask anything to MiniGPT\nShort command: `=c <query>`", inline=False)
        emb.add_field(name="2. =save <conversation_name>", value="Save your conversation\nShort command: `=s <conversation_name>`", inline=False)
        emb.add_field(name="3. =load <conversation_name>", value="Load your previous conversation\nShort command: `=l <conversation_name>`", inline=False)
        emb.add_field(name="4. =reset", value="Reset your current conversation\nShort command: `=r`", inline=False)
        emb.add_field(name="5. =query", value="Shows your current query\nShort command: `=q`", inline=False)
        emb.add_field(name="6. =savefile <file_name>", value="Save all your conversation in a file\nShort command: `=sf <file_name>`", inline=False)
        emb.add_field(name="7. =loadfile <file_name>", value="Load all conversations from a file\nShort command: `=lf <file_name>`", inline=False)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Helpmenu(bot))