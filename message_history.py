# message_history.py
from collections import deque
import json

class MessageHistory:
    def __init__(self, file_path='cache.json', maxlen=50):
        self.file_path = file_path
        self.maxlen = maxlen
        self.history = self.load_history()

    def load_history(self):
        try:
            with open(self.file_path, 'r') as file:
                history_data = json.load(file)
                # Ensure data is converted to a dict of deques
                for user_id in history_data:
                    history_data[user_id] = deque(history_data[user_id], maxlen=self.maxlen)
                return history_data
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def add_message(self, user_id, message):
        # Ensure there's a deque for the user_id
        if user_id not in self.history:
            self.history[user_id] = deque(maxlen=self.maxlen)
        self.history[user_id].append(message)
        self.save_history()

    def get_user_history(self, user_id):
        return list(self.history.get(user_id, deque(maxlen=self.maxlen)))

    def save_history(self):
        # Convert deques to lists for JSON serialization
        history_data = {user_id: list(messages) for user_id, messages in self.history.items()}
        with open(self.file_path, 'w') as file:
            json.dump(history_data, file)
