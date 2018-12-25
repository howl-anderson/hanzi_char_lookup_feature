import collections

import pygtrie
from tokenizer_tools.tagset.NER.BILUO import BILUOEncoderDecoder


def load_trie_from_files(input_mapping):
    t = pygtrie.CharTrie()
    for channel_name, input_files in input_mapping.items():
        for input_file in input_files:
            with open(input_file, 'rt') as fd:
                for line in fd:
                    name = line.strip()

                    v = t.get(name)
                    if v:
                        v.append(channel_name)
                    else:
                        t[name] = [channel_name]

    return t


def generate_lookup_feature(t, input_data, feature_list):
    offset_data = []

    for i in range(len(input_data)):
        frame_data = input_data[i:]
        data = t.longest_prefix(frame_data)

        prefix = data.key
        entity = data.value
        if prefix:
            offset_data.append((i, i + len(prefix), entity))

    channel_offset_data = collections.defaultdict(list)
    for offset in offset_data:
        channel_list = offset[2]
        for channel in channel_list:
            channel_offset_data[channel].append(
                (offset[0], offset[1], channel))

    channel_tag_data = {i: ['O'] * len(input_data) for i in
                        feature_list}

    for name, data_list in channel_offset_data.items():
        encoder = BILUOEncoderDecoder(None)

        tag_seq_list = []

        for data in data_list:
            tag_data = input_data[data[0]: data[1]]

            tag_seq = encoder.encode(tag_data)
            tag_seq_list.append(tag_seq)

            channel_tag_data[name][data[0]: data[1]] = tag_seq

    return channel_tag_data


if __name__ == "__main__":
    t = load_trie_from_files(
        {
            'ancient_person': ['../data/Ancient_Names_Corpus（25W）.txt'],
            'person': ['../data/Chinese_Names_Corpus（120W）.txt']
        }
    )
    result = generate_lookup_feature(t, '李白在和白居易喝酒呢！', ['ancient_person', 'person'])
    print(result)