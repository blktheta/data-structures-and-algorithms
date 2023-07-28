from graph import Graph


def build_graph(filename):
    buckets = {}
    the_graph = Graph()
    with open(filename, "r", encoding="utf-8") as file_in:
        all_words = file_in.readlines()
    # create buckets of words that differ by 1 letter
    for line in all_words:
        word = line.strip()
        for i, _ in enumerate(word):
            bucket = f"{word[:i]}_{word[i + 1 :]}"
            buckets.setdefault(bucket, set()).add(word)

    # add edges between different words in the same bucket
    for similar_words in buckets.values():
        for word1 in similar_words:
            for word2 in similar_words - {word1}:
                the_graph.add_edge(word1, word2)
    return the_graph


def main():
    g = build_graph("word_ladder_words.txt")
    for v in g:
        for w in v.get_neighbors():
            print(f"({v.get_key()}, {w.get_key()})")


if __name__ == "__main__":
    main()
