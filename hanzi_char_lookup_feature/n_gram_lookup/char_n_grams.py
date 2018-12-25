# copied from http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/

input_list = ['all', 'this', 'happened', 'more', 'or', 'less']


def find_ngrams(input_list, n):
    input_length = len(input_list)
    for i in range(input_length):
        char_n_gram = []
        for j in range(2, n+1):
            left_span = input_list[i-j+1: i+1] if i-j+1 >= 0 else None
            right_span = input_list[i: i+j] if i+j <= input_length else None

            char_n_gram.append((left_span, right_span))

        yield char_n_gram


if __name__ == "__main__":
    data = list(find_ngrams(input_list, 3))
    print(data)
