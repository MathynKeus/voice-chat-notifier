import discord
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN"  # Replace with your actual bot token
GUILD_ID = 123456789012345678  # Replace with your server ID
VOICE_CHANNEL_ID = 123456789012345678  # Replace with your target voice channel ID
TEXT_CHANNEL_ID = 123456789012345678  # Replace with your text channel to send messages

intents = discord.Intents.default()
intents.voice_states = True  # Enable voice state updates
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

active_voice_channels = set()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_voice_state_update(member, before, after):
    text_channel = bot.get_channel(TEXT_CHANNEL_ID)
    if not text_channel:
        return
    
    if after.channel and after.channel.id == VOICE_CHANNEL_ID:
        if VOICE_CHANNEL_ID not in active_voice_channels:
            active_voice_channels.add(VOICE_CHANNEL_ID)
            await text_channel.send(f"@everyone {member.display_name} has started the voice channel!")
    elif before.channel and before.channel.id == VOICE_CHANNEL_ID:
        voice_channel = bot.get_channel(VOICE_CHANNEL_ID)
        if voice_channel and len(voice_channel.members) == 0:
            active_voice_channels.discard(VOICE_CHANNEL_ID)
            await text_channel.send(f"@everyone Everyone has left the voice channel. The last user to leave was {member.display_name}.")

bot.run(TOKEN)