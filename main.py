import itertools
import random
import time

time_start = time.time()

min_size_box = 2  # Minimum number of objects in each container
max_size_box = 10  # Maximum number of objects in each container

min_size_data = 1  # Minimum element value in each container
max_size_data = 10  # Maximum element value in each container

min_size_required = 15  # Minimum value of the required combination
max_size_required = 25  # Maximum value of the required combination

num_containers = 10  # Number of containers


# For container generator tests
def generate_containers(num_containers, min_size_box, max_size_box, min_size_data, max_size_data):
    containers = []
    for num in range(num_containers):
        max_sample_size = min(max_size_box - min_size_box + 1, max_size_data)
        data_size = random.randint(min_size_data, max_sample_size)
        container_data = random.sample(range(min_size_box, max_size_box + 1), data_size)
        containers.append((f"box {num}", container_data))
    return containers


def get_combinations(boxes, min_size, max_size):
    valid_combinations = []
    for r in range(2, len(boxes) + 1):
        for combination in itertools.combinations(boxes, r):
            size_combinations = list(itertools.product(*(sizes for _, sizes in combination)))
            for sizes in size_combinations:
                total_size = sum(sizes)
                if min_size <= total_size < max_size:
                    valid_combinations.append((combination, sizes))
    return valid_combinations


def main():
    containers = generate_containers(num_containers, min_size_box, max_size_box, min_size_data, max_size_data)

    for container in containers:
        print(f"Containers: {container[0]}, Size: {len(container[1])}, Data: {container[1]}")

    all_combinations = get_combinations(containers, min_size_required, max_size_required)

    time_end = time.time()

    for combination in all_combinations:
        boxes_combination, sizes_combination = combination
        boxes_name = [box[0] for box in boxes_combination]
        print(f"Boxes: {boxes_name}, Combination: {sizes_combination}, Sum: {sum(sizes_combination)}")

    print(f"All combinations count: {len(all_combinations)}")
    print(f"Lead time: {time_end - time_start} seconds")


if __name__ == "__main__":
    main()
