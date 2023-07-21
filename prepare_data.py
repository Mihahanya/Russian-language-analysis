from os import walk
from data_base import *

# Dataset - https://www.kaggle.com/datasets/d0rj3228/russian-literature
DATA_PATH = 'd:/Downloads/Russian texts database/prose/'

data_text = ''
for dirpath, dirnames, filenames in walk(DATA_PATH):
    for file_name in filenames:
        if file_name[-4:] != '.txt': continue

        print('Read:', file_name)
        current_text = open(dirpath + '/' + file_name, 'r', encoding='utf-8').read()
        data_text += current_text

print('---')

data_text = prepare_text(data_text)

alphabet = list(set(data_text))
alphabet.sort()

text_file = open('data/data_text.txt', 'w', encoding='utf-8')
text_file.write(data_text)
text_file.close()

alph_file = open('data/alphabet.txt', 'w', encoding='utf-8')
alph_file.write(''.join(alphabet))
alph_file.close()

print('Data text size:', len(data_text))
print('alphabet length:', len(alphabet))
print('alphabet:', ''.join(alphabet))
