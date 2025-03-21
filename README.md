# How to Set Up and Run the Discord Voice Channel Notifier Bot

This guide will help you set up and run a Discord bot that sends a message to a text channel when users join or leave a specific voice channel. The guide assumes no prior knowledge of Python or Discord bot development.

---

## 1. Install Python

The bot runs on Python, so you need to install it first.

### Windows:
1. Download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Run the installer and **check the box** that says `Add Python to PATH`.
3. Click `Install Now` and wait for the installation to complete.

### macOS/Linux:
- macOS: Python is usually pre-installed. Check by running:
  ```sh
  python3 --version
  ```
  If not installed, download it from [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)

- Linux: Install Python via package manager:
  ```sh
  sudo apt install python3
  ```

---

## 2. Install Required Dependencies

You need to install the `discord.py` library to interact with Discord.

Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run:
```sh
pip install discord
```

If `pip` is not recognized, try using:
```sh
python -m pip install discord
```

---

## 3. Create a Discord Bot

You need to set up the bot in the Discord Developer Portal.

### Step 1: Create a New Application
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click `New Application` and enter a name for your bot.
3. Click `Create`.

### Step 2: Create the Bot
1. In the left sidebar, click `Bot`.
2. Click `Add Bot`, then confirm.
3. Click `Reset Token`, copy the token, and **store it safely** (you will need it later).

### Step 3: Enable Intents
1. Scroll down to `Privileged Gateway Intents`.
2. Enable `Server Members Intent` and `Presence Intent`.
3. Click `Save Changes`.

### Step 4: Get the Bot Invite Link
1. In the left sidebar, go to `OAuth2` > `URL Generator`.
2. Under `Scopes`, select `bot`.
3. Under `Bot Permissions`, check:
   - `Read Messages`
   - `Send Messages`
   - `Connect`
   - `Speak`
   - `Use Voice Activity`
4. Copy the generated URL and paste it in your browser.
5. Select your server and click `Authorize`.

---

## 4. Set Up the Python Script

Create a new file called `bot.py` and paste the following code:

```python
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
```

Replace:
- `YOUR_BOT_TOKEN` with the token from the Discord Developer Portal.
- `GUILD_ID` with your server ID (right-click your server name > `Copy ID`).
- `VOICE_CHANNEL_ID` with your target voice channel ID (right-click the channel > `Copy ID`).
- `TEXT_CHANNEL_ID` with the text channel ID where messages should be sent.

---

## 5. Run the Bot

Save the `bot.py` file and open a terminal in the same folder.

Run:
```sh
python bot.py
```

If everything is set up correctly, you should see:
```
Logged in as YourBotName!
```

---

## 6. Keep the Bot Running 24/7

To keep the bot online:
- **Use a Cloud Service** (like AWS, DigitalOcean, or a Raspberry Pi)
- **Use a Windows Task Scheduler / Cron Job** to restart it automatically if it stops
- **Use `nohup` on Linux:**
  ```sh
  nohup python bot.py &
  ```

---

## 7. Troubleshooting

### `ModuleNotFoundError: No module named 'discord'`
Run:
```sh
pip install discord
```

### `Invalid Token` Error
Check that you copied the bot token correctly and it hasn't expired.

### Bot is Online, But Doesn't Respond
- Check if the bot has permission to read/send messages in the text channel.
- Make sure the bot is in the correct server.

---

## 8. Contributing

Feel free to contribute to this bot by forking the repository, making improvements, and submitting a pull request!

---

## 9. License

This bot is open-source and licensed under the MIT License.

---

This guide should help even a beginner set up and run the bot successfully! 😊

