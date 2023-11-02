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

def bubble_sort(items: list, sort="asc"):
    def swap(arr, left_index, right_index):
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

def selection_sort(items: list, sort="asc"):
    for i in range(len(items) - 1): # ignore the last element with -1
        # Find the smallest (or largest) element in the remaining portion of the list.
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

def insertion_sort(items: list, sort="asc"):
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

        items[j + 1] = current

    return items

#region: buh
# items = [3,1,7,0]
# bubble_sort(items, "asc")
# print(items)

# print("-"*12)

# items = [3,1,7,0]
# bubble_sort(items, "dsc")
# print(items) 

# print("-"*12)

# items = [17,3,10,25,23,12,6,4,26,7,68,56,243,52345]
# selection_sort(items, "asc")
# print(items)

# print("-"*12)

# items = [17,3,10,25,23,12,6,4,26,7,68,56,243,52345]
# selection_sort(items, "dsc")
# print(items)

# print("-"*12)
#endregion

items = [17,3,10,25,23,12,6,4,26,7,68,56,243,52345]
insertion_sort(items, "asc")
print(items)

print("-"*12)

items = [17,3,10,25,23,12,6,4,26,7,68,56,243,52345]
insertion_sort(items, "dsc")
print(items)