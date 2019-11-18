from typing import List


def find_ngrams(input_list: List[str], n):
    # copied from http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/

    return list(
        zip(*[input_list[i:] for i in range(n)])
    )


if __name__ == "__main__":
    input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

    data = find_ngrams(input_list, 3)
    print(data)

    expected = [
        ('all', 'this', 'happened'),
        ('this', 'happened', 'more'),
        ('happened', 'more', 'or'),
        ('more', 'or', 'less')
    ]

    # data should equal to expected
