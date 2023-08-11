"""
Example comparing Anagram detection algorithms.
"""
import time


def anagram_1(s1: str, s2: str) -> tuple:
    """
    Method: Check off a character
    Order of magnitude: O(n2)

    Each of the n positions in the s2 list of characters will be visited
    once to match a character from the n position in the s1 word.
    """
    start = time.time()
    is_match = True

    if len(s1) is not len(s2):
        is_match = False

    s2_list = list(s2)
    pos_1 = 0

    # first iteration
    while pos_1 < len(s1) and is_match:
        pos_2 = 0
        found = False

        # second iteration
        while pos_2 < len(s2_list) and not found:

            if s1[pos_1] == s2_list[pos_2]:
                found = True
            else:
                pos_2 = pos_2 + 1

        if found:
            s2_list[pos_2] = None
        else:
            is_match = False
        pos_1 = pos_1 + 1

    end = time.time()
    return is_match, end - start


def anagram_2(s1: str, s2: str) -> tuple:
    """
    Method: Sort and compare
    Order of magnitude: O(n log n)

    Each of the n positions of the words are sorted alphabetically then
    compared to each other. The sorting method in Python is typically
    O(n log n) in runtime complexity.
    """
    start = time.time()
    s1_list = list(s1)
    s2_list = list(s2)

    s1_list.sort()  # O(n log n)
    s2_list.sort()  # O(n log n)

    pos = 0
    is_match = True
    while pos < len(s1) and is_match:

        if s1_list[pos] == s2_list[pos]:
            pos = pos + 1
        else:
            is_match = False

    end = time.time()
    return is_match, end - start


def anagram_3(s1: str, s2: str) -> tuple:
    """
    Method: Count and Compare
    Order of magnitude: O(n)

    Each of the n positions of the words are compared to a list of 26
    characters. Each time a particular character is seen on that list,
    the counter on that position is incremented. In the end, if the two
    lists of counters are identical, the strings must be anagrams.
    """
    start = time.time()
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    is_match = True
    while j < 26 and is_match:

        if c1[j] == c2[j]:
            j = j + 1
        else:
            is_match = False

    end = time.time()
    return is_match, end - start


def anagram_4(s1: str, s2: str): -> bool
    """
    Exercise: What is this functions' order of magnitude?
    """
    return (sorted(s1) == sorted(s2))


def anagram_5(s1: str, s2: str): -> bool
    """
    Exercise: What is this functions' order of magnitude?
    """
    from collections import Counter
    return (Counter(s1) == Counter(s2))


def main():
    """
    Unlike the first two solutions the iterations are note nested in
    the 3rd solution. In the 3rd solution the first two iterations are
    used to count the characters based on n. The third iteration
    compares the two lists of counts, and always take 26 steps since
    there are 26 possible characters in the strings. Adding it all up
    gives us T(n) = 2n + 26 steps. That is O(n).
    """
    print("Is an anagram %r required %9.7f seconds" % anagram_1("apple", "pleap"))
    print("Is an anagram %r required %9.7f seconds" % anagram_1("abcd", "dcda"))
    print(
        "Is an anagram %r required %9.7f seconds" % anagram_1(
            "radiocommunications",
            "cormsomontudiciaina"
        )
    )

    print("Is an anagram %r required %9.7f seconds" % anagram_2("apple", "pleap"))
    print("Is an anagram %r required %9.7f seconds" % anagram_2("abcd", "dcda"))
    print(
        "Is an anagram %r required %9.7f seconds" % anagram_2(
            "radiocommunications",
            "cormsomontudiciaina"
        )
    )

    print("Is an anagram %r required %9.7f seconds" % anagram_3("apple", "pleap"))
    print("Is an anagram %r required %9.7f seconds" % anagram_3("abcd", "dcda"))
    print(
        "Is an anagram %r required %9.7f seconds" % anagram_3(
            "radiocommunications",
            "cormsomontudiciaina"
        )
    )


if __name__ == "__main__":
    main()
