# copied from http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/


def find_ngrams(input_list, n):
    return list(
        zip(*[input_list[i:] for i in range(n)])
    )


if __name__ == "__main__":
    input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

    data = find_ngrams(input_list, 3)
    print(data)
