from hanzi_char_lookup_feature.n_gram_lookup.char_n_grams import find_ngrams


def ngrams_structure_feature(text, ngrams, dict_, output_type_func=int):
    """

    :param text:
    :param ngrams:
    :param dict_:
    :param output_type_func:
    :return:
        a list of feature, same length of `text`.
        Each feature has N [N equals size of range: 2 (included) to `ngrams` (included)] size sub-feature.
        Each sub-feature is two element tuple, each element is a True or False.
        First element is True means there is a entity in `dict_` has same value with this pre n-gram.
        Second element is True means there is a entity in `dict_` has same value with this post n-gram.
    """
    feature = []
    for ngrams_group in find_ngrams(text, ngrams):
        raw_encoding = []
        for index, ngrams in enumerate(ngrams_group):
            raw_encoding.append(
                [''.join(i) in dict_ if i is not None else False for
                 i in ngrams]
            )

            # NOTE: maybe moved to post process will be better
            # ngram_encoding = []
            # for i in ngrams:
            #     if i is not None:
            #         keep_it = np.random.uniform() > dropout_rate
            #         code = ''.join(i) in dict_[index + 2] if keep_it else False
            #         ngram_encoding.append(code)
            #
            # raw_encoding.append(ngram_encoding)

            encoding = [[]]
            if output_type_func:
                encoding = [list(map(lambda x: output_type_func(x), i)) for i in raw_encoding]
            else:
                encoding = raw_encoding

        feature.append(encoding)

    return feature


if __name__ == "__main__":
    text = "李白和白居易在喝酒。"
    ngrams = 3
    dict_ = ["李白", "白居易"]

    data = ngrams_structure_feature(text, ngrams, dict_)

    expected = [
        [[0, 1], [0, 0]],
        [[1, 0], [0, 0]],
        [[0, 0], [0, 0]],
        [[0, 0], [0, 1]],
        [[0, 0], [0, 0]],
        [[0, 0], [1, 0]],
        [[0, 0], [0, 0]],
        [[0, 0], [0, 0]],
        [[0, 0], [0, 0]],
        [[0, 0], [0, 0]]
    ]

    # data should equal to expected
