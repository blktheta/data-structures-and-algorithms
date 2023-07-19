"""
Suppose a customer puts in a dollar bill and purchases an item for 37 cents.
What is the smallest number of coins you can use to make change?
"""
from typing import TypeVar


T = TypeVar("T")


def make_change_1(coin_denoms: list[int], change: int) -> int:
    """Greedy method.
    Try to solve as big a piece of the problem as possible right away.

    Extremely inefficient, Takes ~67,716,925 recursive calls to find the
    optimal solution of 6 coins for 63 cents problem.
    """
    if change in coin_denoms:
        return 1
    min_coins = float("inf")
    # for coins less then change
    for i in [c for c in coin_denoms if c <= change]:
        num_coins = 1 + make_change_1(coin_denoms, change - i)
        min_coins = min(num_coins, min_coins)
    return min_coins


def make_change_2(coin_denoms: list[int], change: int, known_results: int) -> int:
    """ Solution: remember some of the past result to avoid recomputing
        results. The solution is not dynamic programming, it
        uses memoization/caching to improve preformance. Reduces the number of
        recursive calls to 221 for 63 cents problem.
    """
    min_coins = change
    if change in coin_denoms:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_denoms if c <= change]:
            num_coins = 1 + make_change_2(coin_denoms, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


def make_change_3(coin_denoms: list[int], change: int, min_coins: list[int]) -> int:
    """ Solution: dynamic programming algorithm
        min_coins parameter is a list of the minimum number of caoins needed
        to make each value. When the functions is done, min_coins will
        contain the solutions for all values from 0 to change.

        This is not a recursive function
    """
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_denoms if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]


def make_change_4(
    coin_denoms: list[int],
    change: int,
    min_coins: list[int],
    coins_used: list[int],
) -> int:
    """Extend solution 3 to keep track of used coines."""
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_denoms if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used: list[int], change: int):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


amnt = 63
clist = [1, 5, 10, 21, 25]
coins_used = [0] * (amnt + 1)
coin_count = [0] * (amnt + 1)

print(make_change_4(clist, amnt, coin_count, coins_used))
print(coin_count)
print(coins_used)
print_coins(coins_used, amnt)
print(make_change_3(clist, amnt, coin_count))
print(make_change_2(clist, amnt, coin_count))
print(make_change_1(clist, amnt))  # will take seconds to finish
