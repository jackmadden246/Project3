from collections import Counter


def find_unique_numbers(numbers):
    unique_num = []  # to store numbers occuring once in list
    count_of_num = Counter(numbers)
    # gives dictionary consisting of each value in the list (key), along with the number of occurences (value)
    for i in numbers:     # looping through all numbers in list
        if count_of_num[i] == 1:
            unique_num.append(i)   # if value from dictionary is exactly one, add key to 'uniques'
    return unique_num


if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3]))
