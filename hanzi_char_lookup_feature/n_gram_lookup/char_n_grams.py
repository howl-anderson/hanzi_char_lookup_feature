# copied from http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/


def find_ngrams(input_list, n):
    for i in range(len(input_list)):
        char_n_gram = find_ngrams_at_offset(input_list, i, n)

        yield char_n_gram


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
        left_span = data[left_index: offset + 1] if left_index >= 0 else None

        right_index = offset + j
        right_span = data[offset: right_index] if right_index <= len(data) else None

        char_n_gram.append((left_span, right_span))

    return char_n_gram


if __name__ == "__main__":
    input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

    data = list(find_ngrams(input_list, 3))
    print(data)
