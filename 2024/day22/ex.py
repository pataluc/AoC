"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""

    secrets = [int(line) for line in data.split('\n')]

    return secrets

def get_next_secret(secret: int) -> int:
    """Computes next secret"""

    # step 1, multiply by 64 then XOR then mix then prune
    secret = ((secret * 64) ^ secret) % 16777216

    # step 2, divide by 32 then round then mix then prune
    secret = ((secret // 32) ^ secret) % 16777216

    # step 3, multiply by 2048 then XOR then mix then prune
    secret = ((secret * 2048) ^ secret) % 16777216

    return secret


def ex1(data: str) -> int:
    """Solve ex1"""

    secrets = load_data(data)
    ans = 0

    for secret in secrets:
        last = 0
        change_secret = []
        for i in range(2000):
            secret = get_next_secret(secret)
        ans += secret

    return ans

def ex2(data: str) -> int:
    """Solve ex1"""

    secrets = load_data(data)

    changes = defaultdict(int)

    last_diff_4 = last_diff_3 = last_diff_2 = last_diff_1 = last = 0
    for secret in secrets:
        change_secret = set()
        for _ in range(2000):
            last = secret % 10
            last_diff_4 = last_diff_3
            last_diff_3 = last_diff_2
            last_diff_2 = last_diff_1
            secret = get_next_secret(secret)
            last_diff_1 = (secret % 10) - last
            if (last_diff_4, last_diff_3, last_diff_2, last_diff_1) not in change_secret:
                changes[(last_diff_4, last_diff_3, last_diff_2, last_diff_1)] += (secret % 10)
                change_secret.add((last_diff_4, last_diff_3, last_diff_2, last_diff_1))
        # print(secret)

    # print(changes[0][:10])
    # print(prices[0][:10])

    best_changes = (-9, -9, -9, -9)
    best_price = 0
    for i in range(-9, 10):
        for j in range(-9, 10):
            for k in range(-9, 10):
                for l in range(-9, 10):
                    if changes[(i,j,k,l)] > best_price:
                        best_price = changes[(i,j,k,l)]
                        best_changes = (i,j,k,l)

    return best_price

assert get_next_secret(123) == 15887950
assert get_next_secret(15887950) == 16495136
assert get_next_secret(16495136) == 527345
assert get_next_secret(527345) == 704524
assert get_next_secret(704524) == 1553684
assert ex1(load("sample.txt")) == 37327623
print(f'ex1 : {ex1(load("input.txt"))}')

# ex2('123')
# exit()
assert ex2(load("sample2.txt")) == 23
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
