def load_dicts_from_files(input_mapping):
    dicts = {}
    for channel_name, input_files in input_mapping.items():
        dict_ = []
        for input_file in input_files:
            with open(input_file, 'rt') as fd:
                for line in fd:
                    word = line.strip()
                    dict_.append(word)

        dicts[channel_name] = dict_

    return dicts
