from hanzi_char_lookup_feature.n_grams import find_ngrams


def test_n_grams():
    input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

    result = find_ngrams(input_list, 3)

    expected = [
        ('all', 'this', 'happened'),
        ('this', 'happened', 'more'),
        ('happened', 'more', 'or'),
        ('more', 'or', 'less')
    ]

    assert result == expected
