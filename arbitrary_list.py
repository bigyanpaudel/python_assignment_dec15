num_list = [1, 2, 3, 4, 6, 7, 8, 9]

def power(num_list):
    cubed_list = list();
    for num in num_list:
        cube = num ** 3
        cubed_list += [cube]

    return cubed_list

cubed_list = power(num_list)

print('Original list\t = {}\nCubed list\t = {}'.format(num_list, cubed_list))