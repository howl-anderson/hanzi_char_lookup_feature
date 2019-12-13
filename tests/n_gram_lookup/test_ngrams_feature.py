import numpy as np

from hanzi_char_lookup_feature.n_gram_lookup.ngrams_feature import (
    ngrams_structure_feature_using_set_v2,
    generate_lookup_feature_v2,
    LookupConfig,
)


def test_ngrams_structure_feature_using_set_v2():
    text = "李白和白居易在喝酒。"
    ngrams = 3
    dict_ = ["李白", "白居易"]

    result = ngrams_structure_feature_using_set_v2(text, ngrams, dict_)

    expected = np.array(
        [
            [[0, 1], [0, 0]],
            [[1, 0], [0, 0]],
            [[0, 0], [0, 0]],
            [[0, 0], [0, 1]],
            [[0, 0], [0, 0]],
            [[0, 0], [1, 0]],
            [[0, 0], [0, 0]],
            [[0, 0], [0, 0]],
            [[0, 0], [0, 0]],
            [[0, 0], [0, 0]],
        ],
        dtype=np.bool,
    )

    assert (result == expected).all()


def test_generate_lookup_feature_v2():
    text = "李白和白居易在喝酒。"

    result = generate_lookup_feature_v2(
        text, [LookupConfig(["李白", "白居易"], 3), LookupConfig(["李白"], 2)]
    )

    expected = np.array(
        [
            [0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        dtype=np.bool,
    )

    assert (result == expected).all()
