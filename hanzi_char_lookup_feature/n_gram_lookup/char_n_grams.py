# copied from http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
from hanzi_char_lookup_feature.context_gram_feature import Feature, GramFeature, TokenGramFeature, create_feature, \
    ContextGramFeature


def find_ngrams(input_list, n):
    for i in range(len(input_list)):
        char_n_gram = find_ngrams_at_offset(input_list, i, n)

        yield char_n_gram


def find_ngrams_v2(input_list: str, n_gram: int) -> ContextGramFeature:
    token_feature_list = []
    for token_index in range(len(input_list)):
        char_n_gram = find_ngrams_at_offset_v2(input_list, token_index, n_gram)

        token_feature_list.append(char_n_gram)

    return ContextGramFeature(token_feature_list)


def find_ngrams_at_offset(data, offset, n):
    """

    :param data:
    :param offset:
    :param n:
    :return:
        [
            (left_span_of_2_gram, right_span_of_2_gram),
            (left_span_of_3_gram, right_span_of_3_gram),
            ...,
            (left_span_of_n_gram, right_span_of_n_gram)
        ],
        each span is None (for no such legal span exists) or
        [X_{-(n-1)}, X_{-...}, X_{-1}, X_0] for left span, [X_0, X_1, X_{...}, X_(n-1)] for right span
    """
    char_n_gram = []
    for j in range(2, n + 1):  # range from 2 (included) to n (included)
        left_index = offset - j + 1  # + 1 for n-grams include current char too
        left_span = data[left_index : offset + 1] if left_index >= 0 else None

        right_index = offset + j
        right_span = data[offset:right_index] if right_index <= len(data) else None

        char_n_gram.append((left_span, right_span))

    return char_n_gram


def find_ngrams_at_offset_v2(data: str, offset: int, n: int):
    token_gram_feature = TokenGramFeature(data[offset])

    for j in range(2, n + 1):  # range from 2 (included) to n (included)
        left_index = offset - j + 1  # + 1 for n-grams include current char too
        left_span = data[left_index : offset + 1] if left_index >= 0 else None

        right_index = offset + j
        right_span = data[offset:right_index] if right_index <= len(data) else None

        gram_feature = GramFeature(create_feature(left_span), create_feature(right_span))

        token_gram_feature.n_gram_feature[j] = gram_feature

    return token_gram_feature


if __name__ == "__main__":
    input_list = ["all", "this", "happened", "more", "or", "less"]

    data = find_ngrams(input_list, 3)
    # data = find_ngrams_v2(input_list, 3)

    print("")

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
