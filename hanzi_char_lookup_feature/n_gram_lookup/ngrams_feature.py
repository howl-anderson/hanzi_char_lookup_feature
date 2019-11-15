import collections

import numpy as np

from hanzi_char_lookup_feature.load_dictionary import load_flatten_set_from_files
from hanzi_char_lookup_feature.load_dictionary import load_flatten_set_from_text
from hanzi_char_lookup_feature.n_gram_lookup.char_n_grams import find_ngrams
from hanzi_char_lookup_feature.n_grams import find_all_ngrams


def ngrams_structure_feature(text, ngrams, dict_, output_type_func=int):
    feature = []
    for ngrams_group in find_ngrams(text, ngrams):
        raw_encoding = []
        for index, ngrams in enumerate(ngrams_group):
            raw_encoding.append(
                [''.join(i) in dict_[index + 2] if i is not None else False for
                 i in ngrams]
            )

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


def ngrams_structure_feature_using_set(text, ngrams, dict_, output_type_func=int, dropout_rate=0):
    all_ngrams = [''.join(i) for i in find_all_ngrams(text, ngrams)]
    found_ner_list = [i for i in all_ngrams if i in dict_]

    # apply dropout
    need_to_remove = []
    for i in found_ner_list:
        keep_it = np.random.uniform() > dropout_rate
        if not keep_it:
            need_to_remove.append(i)
    dropout_dict = set(dict_) - set(need_to_remove)

    feature = []
    for ngrams_of_a_word in find_ngrams(text, ngrams):
        raw_encoding = []
        for index, ngrams in enumerate(ngrams_of_a_word):
            # raw_encoding.append(
            #     [''.join(i) in dict_ if i is not None else False for
            #      i in ngrams]
            # )

            ngram_encoding = []
            for i in ngrams:
                code = None
                if i is not None:
                    code = ''.join(i) in dropout_dict
                else:
                    code = False
                ngram_encoding.append(code)

            raw_encoding.append(ngram_encoding)

            # convert data type if any
            encoding = [[]]
            if output_type_func:
                encoding = [list(map(lambda x: output_type_func(x), i)) for i in raw_encoding]
            else:
                encoding = raw_encoding

        feature.append(encoding)

    return feature


def ngrams_feature(text, ngrams, dict_, output_type_func=int, dropout_rate=0):
    feature = ngrams_structure_feature_using_set(text, ngrams, dict_, output_type_func, dropout_rate)

    flat_feature = []
    for i in feature:
        char_feature = []
        for j in i:
            char_feature.extend(j)

        flat_feature.append(char_feature)

    return flat_feature


def ngrams_feature_mapping(text, ngrams, mapping, output_type_func=int, dropout_rate=0):
    feature_mapping = {}
    for feature_name, feature_dict_files in mapping.items():
        if isinstance(feature_dict_files, list):
            feature_dict = load_flatten_set_from_files(feature_dict_files)
        else:
            feature_dict = feature_dict_files
        feature_mapping[feature_name] = ngrams_feature(text, ngrams, feature_dict, output_type_func, dropout_rate)

    return feature_mapping


def load_data_set(mapping):
    feature_mapping = {}
    for feature_name, feature_dict_files in mapping.items():
        feature_dict = load_flatten_set_from_files(feature_dict_files)
        feature_mapping[feature_name] = feature_dict

    return feature_mapping


def generate_lookup_feature(text, ngrams, mapping, used_feature, output_type_func=int, dropout_rate=0):
    feature_mapping = ngrams_feature_mapping(text, ngrams, mapping, output_type_func, dropout_rate)
    used_feature_mapping = {k: v for k, v in feature_mapping.items() if k in used_feature}

    feature_list = []
    for k, v in used_feature_mapping.items():
        for index, item in enumerate(v):
            if len(feature_list) <= index:
                feature_list.append({})

                feature_list[index][k] = item

    feature = []
    for feature_dict_per_item in feature_list:
        feature_in_order = [
            v
            for k, v in sorted(feature_dict_per_item.items(), key=lambda x: used_feature.index(x[0]))
        ]
        feature_per_item = [i for feature in feature_in_order for i in feature]

        feature.append(feature_per_item)

    return feature


if __name__ == "__main__":
    import os

    text = "李白和白居易在南京西路喝酒。"

    # dictionary = [
    #     [],
    #     [],
    #     ['李白'],
    #     ['白居易'],
    #     ['南京中路', '北京西路']
    # ]

    current_dir = os.path.dirname(__file__)
    sample_data = os.path.join(current_dir, '../../data/sample.txt')

    dictionary = load_flatten_set_from_text(sample_data)

    result = ngrams_feature(text, 4, dictionary, dropout_rate=0.5)
    print(result)

    result = ngrams_feature_mapping(text, 4, {'person': [sample_data]})
    print(result)

    result = generate_lookup_feature(text, 4, {'person': [sample_data]}, ['person'])
    print(result)
