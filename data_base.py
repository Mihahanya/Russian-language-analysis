from tqdm import tqdm
import re


def prepare_text(text):
    n_text = text.lower()
    n_text = re.sub(r'\n+', '', n_text)
    n_text = re.sub(r'\s+', ' ', n_text)

    return n_text


class DataBase:
	def __init__(self, summary=False, max_size=-1):
		readed_text = open('data/whole_data_text.txt', 'r', encoding='utf-8').read()
		self.whole_text = readed_text
		if max_size != -1: self.whole_text = self.whole_text[:max_size]
		self.text_size = len(self.whole_text)

		self.alphabet = list(open('data/whole_alphabet.txt', 'r', encoding='utf-8').read())
		self.alphabet.sort()
		self.alph_len = len(self.alphabet)
		self.letter_index = {self.alphabet[i]: i for i in range(self.alph_len)}

		if summary:
			print('Whole text size:', len(readed_text), 'so used', self.text_size)
			print('Alphabet length:', self.alph_len)
			print('Alphabet:', ''.join(self.alphabet))

