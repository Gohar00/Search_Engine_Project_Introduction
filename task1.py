import re

class Word:
    def __init__(self, word):
        self.word = word
        self.files = set()

    def add_file(self, file_index):
        self.files.add(file_index)

    def __str__(self):
        file_indices = ','.join(str(file_index) for file_index in self.files)
        return f"{self.word}:{file_indices}"

class Text:
    def __init__(self):
        self.words = {}

    def add_word(self, word, file_index):
        if word in self.words:
            self.words[word].add_file(file_index)
        else:
            new_word = Word(word)
            new_word.add_file(file_index)
            self.words[word] = new_word

    def parse_text_file(self, file_path, file_index):
        with open(file_path, 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            for word in words:
                word = word.lower()
                self.add_word(word, file_index)

    def write_to_file(self, file_path):
        with open(file_path, 'w') as file:
            for word in self.words.values():
                file.write(str(word) + '\n')

def main():
    text = Text()
    file_paths = ['1.txt', '2.txt']
    db_file_path = 'db.txt'

    for i, file_path in enumerate(file_paths, start=1):
        text.parse_text_file(file_path, i)

    text.write_to_file(db_file_path)

if __name__ == '__main__':
    main()
