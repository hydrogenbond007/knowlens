from filenames import get_token_to_paths_mapping
import os
from transformers import pipeline


summarizer = pipeline("summarization")


def merge(paths: list, output_file_path: str):
    all_files = ""

    # load all files into one string
    for path in paths:
        with open(path, "r") as f:
            all_files += f.read() + "\n"
    
    summarization = summarizer(all_files)[0]["summary_text"]
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, "w") as f:
        f.write(summarization)



if __name__ == "__main__":
    tokens_to_paths = get_token_to_paths_mapping(["./test_data/knowledge_base1", "./test_data/knowledge_base2"])

    for token, paths in tokens_to_paths.items():
        merge(paths, f"./outputs/merged_knowledge/{token}.md")