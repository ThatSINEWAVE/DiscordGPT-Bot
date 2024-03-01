# utils.py
def read_system_message_from_file(file_path='dataset.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("dataset.txt not found. Using default system message.")
        return "Default system message"
