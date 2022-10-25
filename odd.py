number_list = [1, 2, 3, 4]


def get_even_numbers(number_list):
    even_list = []
    for num in number_list:

        if num % 2 == 0:
            even_list.append(num)

        else:
            pass
    return even_list


print(get_even_numbers(number_list))
