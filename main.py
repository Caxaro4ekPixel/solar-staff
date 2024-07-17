import itertools


def get_combinations(boxes, min_size, max_size):
    valid_combinations = []
    seen_combinations = set()

    for r in range(1, len(boxes) + 1):
        for combination in itertools.combinations(boxes, r):
            size_combinations = list(itertools.product(*(sizes for _, sizes in combination)))
            for sizes in size_combinations:
                total_size = sum(sizes)
                if min_size <= total_size < max_size:
                    combination_with_sizes = [(box[0], size) for box, size in zip(combination, sizes)]
                    if any(size == 0 for _, size in combination_with_sizes):
                        continue
                    sizes_used = [size for _, size in combination_with_sizes]
                    if len(sizes_used) != len(set(sizes_used)):
                        continue
                    combination_values = tuple(sorted(sizes_used))
                    if combination_values not in seen_combinations:
                        seen_combinations.add(combination_values)
                        valid_combinations.append(combination_with_sizes)

    return valid_combinations


def main():
    containers = [
        ("box a", [0, 1, 0, 12]),
        ("box b", [0, 1, 0, 1]),
        ("box c", [0, 1, 0, 2]),
    ]

    start_end = [
        [10, 25],
        [1, 2],
        [2510, 2540]
    ]

    all_combinations = []

    for start, end in start_end:
        all_combinations.append(get_combinations(containers, start, end))

    for combination in all_combinations:
        print("Combination:", end="\n++++++++++++\n")
        for box in combination:
            print(box)


if __name__ == "__main__":
    main()
