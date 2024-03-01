# DiscordGPT - ChatGPT inside your Discord server!

This project is a Discord chatbot that integrates OpenAI's GPT models to interact with users in a Discord channel. It allows for dynamic responses based on user input, leveraging OpenAI's powerful natural language processing capabilities. The bot also supports updating its "personality" through a specific command, making it versatile in its interactions.

## Features

- **Discord Integration**: Utilizes the discord.py library to connect and interact within a Discord server.
- **OpenAI GPT Integration**: Leverages OpenAI's GPT models for generating responses to user messages.
- **Dynamic Personality**: Allows the bot's personality to be changed on the fly via a special command.
- **Message History Management**: Keeps track of recent messages to provide context to the AI model for more relevant responses.

## Usage

To run the bot, just execute the following command:
```
python main.py
```

## Commands

At the moment the bot is just a prototype so it only has 1 command:

- `/personality`: Updates the bot's personality based on the provided text. This affects how the bot responds to messages.
- More coming soon.

## Installation

Clone the Repository
```
git clone https://github.com/ThatSINEWAVE/DiscordGPT.git
cd chatbot-integration-framework
```

### Install Dependencies

Ensure you have Python 3.6 or higher installed, then run:

```
pip install -r requirements.txt
```

### Configuration

- **Discord Token & OpenAI API Key**: You need to create a config.py file or use the provided one at the root of the project directory and add your Discord token and OpenAI API key as follows:

```python
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
```

- **Channel ID**: Update the config.py file with the ID of the Discord channel where the bot should be active.

```python
CHANNEL_ID = YOUR_CHANNEL_ID
```

## Contributing

Contributions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

### License

This project is released under the MIT License. See the LICENSE file for more details.
