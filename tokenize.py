import os



def get_token_to_paths_mapping(directories: list):
    # TODO: docstring

    for directory in directories:
        for file in os.listdir(directory):
            if not file.endswith(".md"):
                raise ValueError("Right now only markdown files are supported")
                
            print(file)


if __name__ == "__main__":
    tokens_to_paths = get_token_to_paths_mapping(["./data/knowledge_base1", "./data/knowledge_base2"])