from collections import Counter

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k), where k is the range of numbers (max-min)
    Memory usage: Depends on len(numbers)
    """
    frequency_count = Counter(numbers)

    index = 0
    for value in range(min(numbers), max(numbers)+1):
        count = frequency_count[value]
        numbers[index:index+count] = [value] * count
        index += count

    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+k), where k is `num_buckets`
    Memory usage: Depends on len(numbers) and num_buckets, the more moving pieces the more complex.
    """
    min_val = min(numbers)
    max_val = max(numbers)

    bucket_range = (max_val - min_val + 1) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in numbers: # actually bucketing
        bucket_index = int((num - min_val) / bucket_range)
        buckets[bucket_index].append(num)

    for bucket in buckets:
        bucket.sort() # each bucket needs to be sorted, im just going to use pythons.

    return [num for bucket in buckets for num in bucket]

to_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted  = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

a = counting_sort(to_sort)
assert a == sorted, "Counting sort failed"
b = bucket_sort(to_sort)
assert b == sorted, "Bucket sort failed"

print("Done :)")