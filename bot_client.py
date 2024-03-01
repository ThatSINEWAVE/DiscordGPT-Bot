import discord
from discord.ext import commands
from config import DISCORD_TOKEN, CHANNEL_ID
from openai_integration import get_openai_response
from message_history import MessageHistory
from utils import read_system_message_from_file


class BotClient(commands.Bot):
    def __init__(self, command_prefix, intents, *args, **kwargs):
        super().__init__(command_prefix, intents=intents, *args, **kwargs)
        self.message_history = MessageHistory()

    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def setup_hook(self):
        # Register the slash command here
        self.tree.add_command(self.personality_command)

    @commands.slash_command(name="personality", description="Change the bot's personality")
    async def personality_command(self, ctx, *, text: str):
        """Handles the /personality command"""
        try:
            with open('dataset.txt', 'w') as file:
                file.write(text)
            await ctx.respond("Personality updated successfully!")
        except Exception as e:
            await ctx.respond(f"Failed to update personality: {e}")

    async def on_message(self, message):
        if message.author == self.user or message.channel.id != CHANNEL_ID:
            return

        user_id = str(message.author.id)  # Convert user ID to string for consistency
        processed_message = message.content.strip()
        if processed_message:
            self.message_history.add_message(user_id, {"role": "user", "content": processed_message})

            system_message_content = read_system_message_from_file()

            user_history = self.message_history.get_user_history(user_id)
            messages_for_api = [{"role": "system", "content": system_message_content}] + user_history

            bot_response = get_openai_response(messages_for_api)
            self.message_history.add_message(user_id, {"role": "system", "content": bot_response})
            self.message_history.save_history()

            await message.channel.send(bot_response)


def run_bot():
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    intents.guilds = True

    client = BotClient(command_prefix="/", intents=intents)
    client.run(DISCORD_TOKEN)
