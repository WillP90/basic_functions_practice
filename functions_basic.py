print("Hello world")

# #1 Countdown - Create Function that takes in number and counts down from it
def countdown(num):
    list1 = []
    for i in range(num, 0, -1):
        list1.append(i)
    print(list1)

countdown(5)

# #2 Print and Return - Create a function that takes 2 numbers, prints the first, returns the second
def print_return(num1, num2):
    print(num1)
    return(num2)

print_return(2,5)

# #3 First Plus Length - Create a function that accepts list and returns sum of index 0 and the list length
def first_plus_length(li):
    return li[0] + len(li)

print(first_plus_length([1,2,3,4,5]))

# #4 Values Greater than Second - Function that takes list and prints new list with only values higher then the second list item. if list has only one item, print false
def values_greater_than_second(li):
    li2 = []
    for i in range(len(li)):
        if len(li) < 2:
            return False
            break
        if i > li[1]:
            li2.append(i)
    print(len(li2))
    print(li2)

values_greater_than_second([5,2,3,2,1,4])
print(values_greater_than_second([3]))

# #5 This Length, That Value - function that takes in two values, creates a list the size of the first value and fills it with the second value

def length_value(si, val):
    new_list = []
    for i in range(si):
        new_list.append(val)
    print(new_list)

length_value(7, 3)