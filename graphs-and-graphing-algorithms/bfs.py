from queue import Queue
from bfs_graph import Graph


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


def bfs(start):
    start.distance = 0
    start.previous = None
    start.color = "gray"
    vertices_queue = Queue()
    vertices_queue.enqueue(start)
    while vertices_queue.size() > 0:
        current = vertices_queue.dequeue()
        for neighbor in current.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current.distance + 1
                neighbor.previous = current
                vertices_queue.enqueue(neighbor)
        current.color = "black"


def traverse(starting_vertex):
    current = starting_vertex
    while current:
        print(current.key)
        current = current.previous


def main():
    g = build_graph("word_ladder_words.txt")
    for v in g:
        for w in v.get_neighbors():
            print(f"({v.get_key()}, {w.get_key()})")

    bfs(g.get_vertex("fool"))

    traverse(g.get_vertex("sage"))


if __name__ == "__main__":
    main()
