import collections
from typing import List


def load_from_text(input_file) -> List[List]:
    raw_dictionary = collections.defaultdict(list)
    with open(input_file, "rt") as fd:
        for line in fd:
            word, *_ = line.strip().split()
            len_of_word = len(word)
            raw_dictionary[len_of_word].append(word)

    dictionary = [
        raw_dictionary.get(i, []) for i in range(1, max(raw_dictionary.keys()) + 1)
    ]

    return dictionary


def load_flatten_set_from_text(input_file):
    dictionary = set()
    with open(input_file, "rt") as fd:
        for line in fd:
            word, *_ = line.strip().split()
            dictionary.add(word)

    return dictionary


def load_flatten_set_from_files(input_files):
    data = set()
    for input_file in input_files:
        data.update(load_flatten_set_from_text(input_file))

    return data


if __name__ == "__main__":
    import os
    from pathlib import Path

    current_dir = Path(os.path.dirname(__file__))
    data = load_from_text(current_dir / "../data/THUOCL_lishimingren.txt")
    print(data)
