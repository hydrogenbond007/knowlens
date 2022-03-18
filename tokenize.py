import os
from collections import defaultdict



def get_token_to_paths_mapping(directories: list):
    # TODO: docstring

    token_to_paths_mapping = defaultdict(list)

    for directory in directories:
        for file_name in os.listdir(directory):
            if not file_name.endswith(".md"):
                raise ValueError("Right now only markdown files are supported")

            token = file_name # TODO
            path = os.path.join(directory, file_name)
            token_to_paths_mapping[token].append(path)

    return dict(token_to_paths_mapping)


if __name__ == "__main__":
    tokens_to_paths = get_token_to_paths_mapping(["./data/knowledge_base1", "./data/knowledge_base2"])
    print(tokens_to_paths)