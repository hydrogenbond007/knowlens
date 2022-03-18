from knowlens.filenames import get_token_to_paths_mapping


def test():
    tokens_to_paths = get_token_to_paths_mapping(["./test_data/knowledge_base1", "./test_data/knowledge_base2"])
    assert len(tokens_to_paths.keys()) == 1
    assert len(list(tokens_to_paths.values())[0]) == 3