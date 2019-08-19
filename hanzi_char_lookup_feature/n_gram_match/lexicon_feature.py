import os

import pygtrie

from tokenizer_tools.tagset.NER.BILUO import BILUOEncoderDecoder

from hanzi_char_lookup_feature.n_grams import find_ngrams
from hanzi_char_lookup_feature.load_dictionary import load_from_text

text = "李白和白居易在南京西路喝酒。"

# dictionary = [
#     [],
#     [],
#     ['李白'],
#     ['白居易'],
#     ['南京中路', '北京西路']
# ]

current_dir = os.path.dirname(__file__)
sample_file = os.path.join(current_dir, '../../data/sample.txt')

dictionary = load_from_text(sample_file)


trie = []
for item in dictionary:
    t = pygtrie.CharTrie()
    for i in item:
        t[i] = True

    reversed_t = pygtrie.CharTrie()
    for i in item:
        t[''.join(reversed(i))] = True

    trie.append((t, reversed_t))

encoding = ['O'] * len(text)

for ngram_size in range(3, len(dictionary) + 1):

    ngrams = list(enumerate(find_ngrams(text, ngram_size)))

    for offset, ngram in reversed(ngrams):
        ngram = ''.join(ngram)
        print(ngram)
        half_index = len(ngram) // 2
        prefix_gram = ''.join(ngram[:half_index])
        suffix_gram = ''.join(ngram[half_index:])

        print(prefix_gram)
        print(suffix_gram)

        for i, dict_ in enumerate(dictionary[:len(ngram)+1]):
            for item in dict_:
                if item == ngram:
                    print('{} == {}'.format(item, ngram))
                    encoder = BILUOEncoderDecoder(None)
                    encoding[offset: offset + len(item)] = encoder.encode(ngram)
                else:
                    if item.startswith(prefix_gram):
                        print('startswith')
                        common_prefix = os.path.commonprefix([prefix_gram, item])
                        common_prefix_len = len(common_prefix)
                        encoder = BILUOEncoderDecoder(None)
                        encoding[offset: offset + common_prefix_len] = encoder.encode(item)[:common_prefix_len]
                    if item.endswith(suffix_gram):
                        print('endswith')
                        common_suffix = os.path.commonprefix([''.join(reversed(suffix_gram)), ''.join(reversed(item))])
                        common_suffix_len = len(common_suffix)
                        encoder = BILUOEncoderDecoder(None)
                        encoding[offset + len(ngram) - common_suffix_len: offset + len(ngram)] = encoder.encode(item)[-common_suffix_len:]

print(encoding)
