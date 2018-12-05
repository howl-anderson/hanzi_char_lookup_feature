import pathlib
import collections

import pygtrie
from tokenizer_tools.tagset.NER.BILUO import BILUOEncoderDecoder

t = pygtrie.CharTrie()

# input_files = pathlib.Path('./data').glob('*.txt')

input_files = [pathlib.Path('./data/Ancient_Names_Corpus（25W）.txt')]

for input_file in input_files:
    with input_file.open('rt') as fd:
        for line in fd:
            name = line.strip()

            t[name] = ['person']

print(t['李白'])

print()

input_data = '李白和白居易在喝酒'

offset_data = []

for i in range(len(input_data)):
    frame_data = input_data[i:]
    data = t.longest_prefix(frame_data)
    print(data.key)
    print(data.value)

    prefix = data.key
    entity = data.value
    if prefix:
        offset_data.append((i, i + len(prefix), entity))

print(offset_data)

channel_offset_data = collections.defaultdict(list)
for offset in offset_data:
    channel_list = offset[2]
    for channel in channel_list:
        channel_offset_data[channel].append((offset[0], offset[1], channel))


channel_tag_data = {i: ['O'] * len(input_data) for i in channel_offset_data}

print(channel_tag_data)

for name, data_list in channel_offset_data.items():
    encoder = BILUOEncoderDecoder(name)

    tag_seq_list = []

    for data in data_list:
        tag_data = input_data[data[0]: data[1]]

        tag_seq = encoder.encode(tag_data)
        tag_seq_list.append(tag_seq)

        channel_tag_data[name][data[0]: data[1]] = tag_seq

print(channel_tag_data)
