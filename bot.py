import nextcord
from nextcord.ext import commands
import os, keep_alive
from dotenv import load_dotenv
load_dotenv()

keep_alive.keep_alive()

bot = commands.Bot(command_prefix=['='], intents= nextcord.Intents.all())

for folder in os.listdir("modules"):
    if os.path.exists(os.path.join("modules", folder, "cog.py")):
        bot.load_extension(f"modules.{folder}.cog")

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f'{bot.user} has connected to nextcord!')
        
bot.run(os.getenv("TOKEN"))
