class WordsFinder:

    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        symbol_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                list_words = []
                for words in file:
                    words = words.lower()
                    for symbol in symbol_punctuation:
                        words = words.replace(symbol, ' ')
                    list_words.extend(words.split())
            all_words[file_name]= list_words
        return all_words

    def find (self, word):
        counter = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                counter[name] = words.index(word) + 1
            else:
                counter[name] = 0
        return counter

    def count(self, word):
        counter = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            counter[name] =  words.count(word)
        return counter


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего