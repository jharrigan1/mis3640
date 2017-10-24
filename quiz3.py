def replace_even(data):
    for i in range(0,len(data),2):
       data[i] = 0
    '''
    Replace all elements at an even index in the list with 0.
    No return is required.
    data: the list of values to process'''

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN)

# Expected output:
# [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]


def remove_middle(data):
    if len(data) % 2 == 0:
        middle1 = int(len(data)/2)  #int at the beginning makes sure it does not return you an odd number with a float such as 4.5, etc)
        middle2 = int(len(data)/2-1)
        del data[middle1]
        del data[middle2]
    else:
        middle = int(len(data)/2)
        del data[middle]


    '''
    Remove the middle element if the list length is odd,
    or the middle two elements if the list length is even.  
    No return is required.
    data: the list of values to process
    '''
    

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN)

# Expected output:
# [1, 2, 3, 4, 7, 8, 9, 10]


def insert_integer(data, number):
    '''
    given a sorted list of integers, insert a new integer into
    its proper position so that the new list stays sorted. 
    Do not use sort function or sorted function inside this function.
    data: a list of integers
    number: a new integer
    return: a new list of sorted integers with previous numbers and 
    the new number
    '''

    for n in range(0, len(data)):
        if (data[n] >= number):
            data.insert(n, number)
            break
    return data

# Uncomment the following lines to test
data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
new_data = insert_integer(data, 2015)
print(new_data)

# Expected output:
# [1, 3, 40, 75, 90, 2000, 2001, 2015, 2016]


def print_hist(data):
    for x in sorted(data):
        g = data[x]
        print (x, ": ", g*'*') 
letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print_hist(letter_counts)

'''
    given a dictionary of letter: positive integer pairs, 
    print rows with the letter and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    data: a dictionary of letter: positive integer pairs
    Example:
letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print_hist(letter_counts)
    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********
'''
