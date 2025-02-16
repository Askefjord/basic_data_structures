import string


class WordsFinder:

    def __init__(self, *txt_file: str):
        self.txt_file = txt_file

    def get_all_words(self):
        dict_of_words = {}

        for files in self.txt_file:
            with open(files, encoding='utf-8') as file:
                file.seek(0)
                word = file.read()

                for chars_of_punctuation in string.punctuation:  # create "for" generator
                    word = word.replace(chars_of_punctuation, ' ')
                    dict_of_words[files] = word.split()
        return dict_of_words

    def find(self, word):
        dict_founded_words = {}

        for file_name, words in self.get_all_words().items():

            try:
                dict_founded_words[file_name] = words.index(word.lower())
            except ValueError:
                dict_founded_words[file_name] = 'Not found'

        return dict_founded_words

    def count(self, word):
        dict_counted_words = {}

        for file_name, words in self.get_all_words().items():
            dict_counted_words[file_name] = words.count(word.lower())
        return dict_counted_words


finder = WordsFinder('text.txt')
finder.get_all_words()
print(finder.find('TExt'))
print(finder.count('TEXT'))
