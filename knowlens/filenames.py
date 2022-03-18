import os
from collections import defaultdict
from transformers import BertTokenizer, XLNetTokenizer

# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokenizer = XLNetTokenizer.from_pretrained("xlnet-base-cased")


def preprocess(text: str) -> str:
    # TODO: docstring
    text = text.replace(".md", "")
    return text.replace("_", "").replace(" ", "").replace("-", "").replace(".", "")


def tokenize(text: str) -> str:
    text = preprocess(text)
    return "".join(tokenizer.tokenize(text))


def get_token_to_paths_mapping(directories: list):
    # TODO: docstring

    token_to_paths_mapping = defaultdict(list)

    for directory in directories:
        for file_name in os.listdir(directory):
            if not file_name.endswith(".md"):
                raise ValueError("Right now only markdown files are supported")

            # tokenize filename in case there are files with similar, but not exactly similar, names
            token = tokenize(file_name)
            path = os.path.join(directory, file_name)
            token_to_paths_mapping[token].append(path)

    return dict(token_to_paths_mapping)


