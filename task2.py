def calculate_sum(numbers):

    total = 0
    for number in numbers:
        total += number

    return total

user_input = input('Enter digits separated by commas: ')

numbers = list(map(int, user_input.split(',')))

totalSum = calculate_sum(numbers)

print("The total sum of the numbers is: %d" % totalSum)
