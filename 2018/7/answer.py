from collections import defaultdict
import string
import re

input = open('input.txt').readlines()
input_list = []
for line in input:
    a, b = re.findall(r' ([A-Z]) ', line)
    input_list.append((a, b))


def part_1(rules):
    tasks, deps = get_tasks_and_deps(rules)
    done = []
    for _ in tasks:
        done.append(
            min(x for x in tasks if x not in done and deps[x] <= set(done)))
    return ''.join(done)


def part_2(rules):
    tasks, deps = get_tasks_and_deps(rules)
    done = set()
    seconds = 0
    counts = [0] * 5
    work = [''] * 5
    while True:
        for i, count in enumerate(counts):
            if count == 1:
                done.add(work[i])
            counts[i] = max(0, count - 1)
        while 0 in counts:
            i = counts.index(0)
            candidates = [x for x in tasks if deps[x] <= done]
            if not candidates:
                break
            task = min(candidates)
            tasks.remove(task)
            counts[i] = ord(task) - ord('A') + 61
            work[i] = task
        if sum(counts) == 0:
            break
        seconds += 1
    return seconds


def get_tasks_and_deps(rules):
    tasks = set()
    deps = defaultdict(set)
    for rule in rules:
        a, b = rule
        tasks |= {a, b}
        deps[b].add(a)
    return tasks, deps


print(part_1(input_list))
print(part_2(input_list))
