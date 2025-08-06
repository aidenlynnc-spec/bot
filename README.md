# Discord Voice & Repeat Bot

This Discord bot can:
- Join your voice channel with `!join`, play `mes.ogg`, then leave.
- Repeat any message from the user with ID `1315870841296126013`.

## Setup

1. **Clone this repository** and add your `mes.ogg` file in the root folder.
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** and add your bot token:
   ```
   DISCORD_TOKEN=your-bot-token-here
   ```
4. **Run the bot:**
   ```
   python discord_bot.py
   ```

## Commands

- `!join`: Bot joins your voice channel, plays `mes.ogg`, and leaves.
- If the user with ID `1315870841296126013` sends a message, the bot repeats it.

## Notes

- Place your `mes.ogg` sound file in the same folder as `discord_bot.py`.
- Make sure your bot has the necessary permissions in your Discord server.

## Requirements

- Python 3.8+
- [discord.py](https://pypi.org/project/discord.py/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [PyNaCl](https://pypi.org/project/PyNaCl/)

## Example requirements.txt

```text
discord.py[voice]
python-dotenv
PyNaCl
```