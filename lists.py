# name:
# date:
import random

print('----------1----------')
# List Creation

# 1.1 | Create an empty list, l, and print it to the console.
l = list()
print(l)

# 1.2 | Create a pre-populated list of names. Print this list to
#       console. This list should be of at least length 5.
names = ['Linus', 'Torvus', 'NYSE', 'AMX', 'Karl']
print(names)
# 1.3 | Create a pre-populated list of numbers. Print this list to
#       the console. This list should be at least length 5.
nums = [24, 35, 37, 39]
print(nums)
# 1.4 | Using the list of names, modify the element at index 2 to a new
#       name.
names[2] = 'Manhattan'
# 1.5 | Using the list of numbers, modify the element at index 3 to a new
#       number.
nums[3] = 99
print('----------2----------')
# List Indexing / Slicing

# 2.1 | Using the list of names from section 1, print the elements
#       at indices 0, 3, and 4.
selected_names = [names[0], names[3], names[4]]
print(selected_names)
# 2.2 | Using the list of names from section 1, print the elements
#       at indices 1, 2, and 3.
selected_nums = [nums[1], nums[2], nums[3]]
print(selected_nums)

# 2.3 | Print the list of names from section 1 in reverse order.
rev_names = [names[-1], names[-2], names[-3], names[-4], names[-5]]

# 2.4 | Create a slice of the list nums, starting from index 2 to
#       the end of list.
sliced_nums = nums[2:]

# 2.5 | Print the last element of the list below. Note that it's size
#       is random. Hint: Is there and index, that will always give us
#       the last item?
random_numbers = [random.randint(1, 100) for i in range(random.randint(10, 15))]
print(random_numbers[-1])

print('----------3----------')
# List Methods / List Construction

# 3.1 | Using the empty list l from section 1, append five of your favorite
#       foods to the list, using the append method. Print the list.


# 3.2 | Using the list nums from section 1, ask the user to enter a number,
#       and append this value into the list *as an integer.* Print the list.


# 3.3 | Using the list names from section 1, pop the last item in the list.
#       Print this item.


# 3.4 | Using the list names from section 1, pop the second item in the list.
#       Print this item.


# 3.5 | Using the list names from section 1, accept input in the form of a String.
#       This will be a name. Insert this name to the front of the list.


# 3.5 | Accept input in the form of a String, you will be prompting the user
#       for a word. Convert this word into a list, where each letter is it's own
#       element in the list.


# 3.6 | Accept input in the form of a String. You will be prompting the user
#       for a sentence. Convert this sentence into a list, where each word is it's
#       own element in the list.


print('----------4----------')
# 4.1 | Create an empty list, l. Using a for loop, accept input from the user
#       15 times, in the form of a number. Append these numbers into the list.


# 4.2 | Create an empty list, l. Using a for loop, accept input from the user
#       15 times, in the form of a number. If this number is even, insert this number
#       to the front of the list. If it is odd, append this number to this list.


# 4.3 | Create an empty list, words. Using a for loop, accept input from the user
#       15 times, in the form of a String. These will be words. If the word starts
#       with a vowel, insert this word to the front of the list. If it does not,
#       append this word to the list.


# 4.4 | Create a variable named sum and set it to 0. Using a for loop, find the sum of
#       all the numbers added together in the list below. Note that the lists size is
#       random.
random_numbers = [random.randint(1, 100) for i in range(5, 15)]


# 4.5 | Create a variable named product and set it to 0. Using a for loop, find the
#       product of all the numbers multiplied together in the list below. Note that the
#       lists size is random.
random_numbers = [random.randint(1, 100) for i in range(5, 15)]

