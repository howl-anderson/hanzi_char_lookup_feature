from hanzi_char_lookup_feature.n_grams.n_grams import find_ngrams


def find_all_ngrams(input_list, n):
    ngrams = []
    for i in range(2, n+1):  # range from 2 (included) to n (included)
        ngrams.extend(find_ngrams(input_list, i))

    return ngrams


if __name__ == "__main__":
    input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

    data = find_all_ngrams(input_list, 3)
    print(data)

    expected = [
        # 2-grams
        ('all', 'this'),
        ('this', 'happened'),
        ('happened', 'more'),
        ('more', 'or'),
        ('or', 'less'),
        # 3-grams
        ('all', 'this', 'happened'),
        ('this', 'happened', 'more'),
        ('happened', 'more', 'or'),
        ('more', 'or', 'less')
    ]

    # data should equal to expected
