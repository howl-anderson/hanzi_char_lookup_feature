from hanzi_char_lookup_feature.n_grams.n_grams import find_ngrams


def find_all_ngrams(input_list, n):
    ngrams = []
    for i in range(2, n+1):
        ngrams.extend(find_ngrams(input_list, i))

    return ngrams


if __name__ == "__main__":
    input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

    data = find_all_ngrams(input_list, 3)
    print(data)
