from filenames import get_token_to_paths_mapping
from transformers import pipeline


summarizer = pipeline("summarization")


def merge(paths: list, output_file_path: str):
    for path in paths:
        with open(path, "r") as f:
            summarization = summarizer(f.readlines())
            print(summarization)



if __name__ == "__main__":
    tokens_to_paths = get_token_to_paths_mapping(["./data/knowledge_base1", "./data/knowledge_base2"])

    for token, paths in tokens_to_paths.items():
        merge(paths, f"./test_data/merged_knowledge/{token}.md")