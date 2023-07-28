from queue import Queue
from graph import Graph, Vertex


def build_graph(filename):
    buckets = {}
    the_graph = BFSGraph()
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


class BFSVertex(Vertex):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.distance = 0
        self.previous = None
        self.color = "white"


class BFSGraph(Graph):
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = BFSVertex(key)


def bfs(start):
    start.distance = 0
    start.previous = None
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current = vert_queue.dequeue()
        for neighbor in current.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current.distance + 1
                neighbor.previous = current
                vert_queue.enqueue(neighbor)
        current.color = "black"


def traverse(starting_vertex):
    current = starting_vertex
    while current:
        print(current.key)
        current = current.previous


def main():
    g = build_graph("four_test.txt")

    for v in g:
        for w in v.get_neighbors():
            print(f"({v.get_key()}, {w.get_key()})")

    traverse(g.get_vertex("sage"))


if __name__ == "__main__":
    main()
