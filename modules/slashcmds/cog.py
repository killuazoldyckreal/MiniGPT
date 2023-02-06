import revopenai
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import traceback
class Slashcommands(commands.Cog, name="Slash Commands"):
    """These are slash commands you can use for MiniGPT"""

    COG_EMOJI = "✔"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="chat", description="Ask anything from MiniGPT")
    async def _chat(self,interaction:Interaction, message:str =SlashOption(required=True,description="Enter your question")):
        message=message+" but while writing if your response contain a program add 3 backticks and program language name in the starting and 3 backticks at the end of the program"
        try:
            await interaction.response.defer(with_message=True)
            if interaction.user == self.bot.user:
                return
            if interaction.user.bot:
                return
            response = revopenai.make_request(message)
            await interaction.followup.send(response)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await interaction.followup.send("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @nextcord.slash_command(name="save", description="Save your conversation")
    async def _save(self,interaction:Interaction, conversation_name:str =SlashOption(required=True,description="Enter any name to save this conversation with")):
        try:
            await interaction.response.defer(with_message=True)
            if interaction.user == self.bot.user:
                return
            if interaction.user.bot:
                return
            message = revopenai.make_request(f"!save_c {conversation_name}")
            await interaction.followup.send(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await interaction.followup.send("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()
    
    @nextcord.slash_command(name="load", description="Load your previous conversation")
    async def _load(self,interaction:Interaction, conversation_name:str =SlashOption(required=True,description="Enter the conversation name to load")):
        try:
            await interaction.response.defer(with_message=True)
            if interaction.user == self.bot.user:
                return
            if interaction.user.bot:
                return
            message = revopenai.make_request(f"!load_c {conversation_name}")
            await interaction.followup.send(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await interaction.followup.send("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @nextcord.slash_command(name="reset", description="Reset your current conversation")
    async def _reset(self,interaction:Interaction):
        try:
            await interaction.response.defer(with_message=True)
            if interaction.user == self.bot.user:
                return
            if interaction.user.bot:
                return
            message = revopenai.make_request("!reset")
            
            await interaction.followup.send(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await interaction.followup.send("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @nextcord.slash_command(name="query", description="Shows your current query")
    async def _query(self,interaction:Interaction):
        try:
            await interaction.response.defer(with_message=True)
            if interaction.user == self.bot.user:
                return
            if interaction.user.bot:
                return
            message = revopenai.make_request("!query")
            
            await interaction.followup.send(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await interaction.followup.send("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()

    @nextcord.slash_command(name="savefile", description="Save your conversation in a file")
    async def _savefile(self,interaction:Interaction, file_name:str =SlashOption(required=True,description="Enter any filename to save this conversation with")):
        try:
            await interaction.response.defer(with_message=True)
            if interaction.user == self.bot.user:
                return
            if interaction.user.bot:
                return
            message = revopenai.make_request(f"!save_f {file_name}")
            
            await interaction.followup.send(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await interaction.followup.send("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()


    @nextcord.slash_command(name="loadfile", description="Load all conversations from a file")
    async def _loadfile(self,interaction:Interaction, file_name:str =SlashOption(required=True,description="Enter filename to load conversation with")):
        try:
            await interaction.response.defer(with_message=True)
            if interaction.user == self.bot.user:
                return
            if interaction.user.bot:
                return
            message = revopenai.make_request(f"!load_f {file_name}")
            
            await interaction.followup.send(message)
        except nextcord.Forbidden:
            print("Missing Perms")
        except nextcord.HTTPException:
            await interaction.followup.send("I am on cooldown, try again after some time")
        except:
            traceback.print_exc()


def setup(bot: commands.Bot):
    bot.add_cog(Slashcommands(bot))


