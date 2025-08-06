import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

TARGET_USER_ID = 1315870841296126013

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        audio_source = discord.FFmpegPCMAudio("mes.ogg")
        voice_client.play(audio_source)
        while voice_client.is_playing():
            await discord.utils.sleep_until(discord.utils.utcnow() + discord.utils.timedelta(seconds=1))
        await voice_client.disconnect()
    else:
        await ctx.send("You need to be in a voice channel!")

@bot.event
async def on_message(message):
    if message.author.id == TARGET_USER_ID and not message.author.bot:
        await message.channel.send(message.content)
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)
