#!/bin/env python3


def parse_input(file_path):
    with open(file_path) as file:
        data = file.read().strip()
    lines = data.split('\n')
    parts = data.split('\n\n')
    seed, *others = parts
    seed = [int(x) for x in seed.split(':')[-1].split()]
    functions = [parse_function(s) for s in others]
    return seed, functions

def parse_function(s):
    lines = s.split('\n')[1:]
    tuples = [[int(x) for x in line.split()] for line in lines]
    return tuples

def apply_one(x, tuples):
    for (dst, src, sz) in tuples:
        if src <= x < src + sz:
            return x + dst - src
    return x

def apply_range(R, tuples):
    A = []
    for (dest, src, sz) in tuples:
        src_end = src + sz
        NR = []
        while R:
            (st, ed) = R.pop()
            before = (st, min(ed, src))
            inter = (max(st, src), min(src_end, ed))
            after = (max(src_end, st), ed)
            if before[1] > before[0]:
                NR.append(before)
            if inter[1] > inter[0]:
                A.append((inter[0] - src + dest, inter[1] - src + dest))
            if after[1] > after[0]:
                NR.append(after)
        R = NR
    return A + R

def main():
    seed, functions = parse_input("input")

    P1 = []
    for x in seed:
        for func in functions:
            x = apply_one(x, func)
        P1.append(x)
    print(min(P1))

    P2 = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for st, sz in pairs:
        R = [(st, st + sz)]
        for func in functions:
            R = apply_range(R, func)
        P2.append(min(R)[0])
    print(min(P2))

if __name__ == "__main__":
    main()

