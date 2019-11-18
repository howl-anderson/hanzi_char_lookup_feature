from hanzi_char_lookup_feature.context_gram_feature import ContextGramFeature, TokenGramFeature, GramFeature, Feature
from hanzi_char_lookup_feature.n_gram_lookup.char_n_grams import find_ngrams_v2, find_ngrams


def test_find_ngrams_v2():
    input_list = ["all", "this", "happened", "more", "or", "less"]

    data = find_ngrams_v2(input_list, 3)

    expected_data = ContextGramFeature([
        TokenGramFeature(token="all", n_gram_feature={
            2: GramFeature(left_context=None, right_context=Feature(["all", "this"])),
            3: GramFeature(left_context=None, right_context=Feature(["all", "this", "happened"]))
        }),
        TokenGramFeature(token="this", n_gram_feature={
            2: GramFeature(left_context=Feature(["all", "this"]), right_context=Feature(["this", "happened"])),
            3: GramFeature(left_context=None, right_context=Feature(["this", "happened", "more"]))
        }),
        TokenGramFeature(token="happened", n_gram_feature={
            2: GramFeature(left_context=Feature(["this", "happened"]), right_context=Feature(["happened", "more"])),
            3: GramFeature(left_context=Feature(["all", "this", "happened"]), right_context=Feature(["happened", "more", "or"]))
        }),
        TokenGramFeature(token="more", n_gram_feature={
            2: GramFeature(left_context=Feature(["happened", "more"]), right_context=Feature(["more", "or"])),
            3: GramFeature(left_context=Feature(["this", "happened", "more"]), right_context=Feature(["more", "or", "less"])),
        }),
        TokenGramFeature(token="or", n_gram_feature={
            2: GramFeature(left_context=Feature(["more", "or"]), right_context=Feature(["or", "less"])),
            3: GramFeature(left_context=Feature(["happened", "more", "or"]), right_context=None)
        }),
        TokenGramFeature(token="less", n_gram_feature={
            2: GramFeature(left_context=Feature(["or", "less"]), right_context=None),
            3: GramFeature(left_context=Feature(["more", "or", "less"]), right_context=None)
        }),
    ])

    assert data == expected_data


def test_find_ngrams():
    input_list = ["all", "this", "happened", "more", "or", "less"]

    data = list(find_ngrams(input_list, 3))

    expected_data = [
        [  # #1 word
            # left, right
            (None, ["all", "this"]),  # 2-gram
            (None, ["all", "this", "happened"])  # 3-gram
        ],
        [  # #2 word
            # left          , right
            (["all", "this"], ["this", "happened"]),  # 2-gram
            (None, ["this", "happened", "more"])  # 3-gram
        ],
        [  # #3 word
            # left               , right
            (["this", "happened"], ["happened", "more"]),  # 2-gram
            (["all", "this", "happened"], ["happened", "more", "or"]),  # 3-gram
        ],
        [  # #4 word
            (["happened", "more"], ["more", "or"]),
            (["this", "happened", "more"], ["more", "or", "less"]),
        ],
        [  # #5 word
            (["more", "or"], ["or", "less"]),
            (["happened", "more", "or"], None)
        ],
        [  # #6 word
            (["or", "less"], None),
            (["more", "or", "less"], None)
        ],
    ]

    assert data == expected_data
