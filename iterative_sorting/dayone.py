def is_sorted(items, sort="asc"):
    """Return a boolean indicating whether given items are in sorted order."""
    for i in range(len(items) - 1):
        current = items[i]
        next = items[i+1]

        if sort == "asc":
            if not current <= next:
                return False
        elif sort == "dsc":
            if not current >= next:
                return False
            
    return True

# O(n^2)
def bubble_sort(items, sort="asc"):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order. Why and under what conditions?"""

    def swap(arr, left_index, right_index):
        print(arr)
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
        return arr

    while not is_sorted(items, sort):
        for i in range(len(items) - 1):
            if sort == "asc":
                if items[i] > items[i+1]:
                    items = swap(items, i, i+1)
            elif sort == "dsc":
                if items[i] < items[i+1]:
                    items = swap(items, i, i+1)

    return items

# O(n^2)
def selection_sort(items: list, sort="asc"):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order."""

    for i in range(len(items) - 1): # ignore the last element with -1
        index = i

        for j in range(i + 1, len(items)):
            if sort == "asc":
                if items[j] < items[index]:
                    index = j
            elif sort == "dsc":
                if items[j] > items[index]:
                    index = j

        if index != i:
            items[i], items[index] = items[index], items[i]

    return items   

# O(n^2)
def insertion_sort(items, sort="asc"):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""

    for i in range(1, len(items)):
        current = items[i]
        j = i - 1

        if sort == "asc":
            while j >= 0 and items[j] > current:
                items[j + 1] = items[j]
                j -= 1
        elif sort == "dsc":
            while j >= 0 and items[j] < current:
                items[j + 1] = items[j]
                j -= 1
        else:
            raise ValueError("Invalid sort order")

        items[j + 1] = current

    return items
