numbers = []
num = 0
total = 0 

while num != -1:
    num = int(input('Enter a number (-1 to stop): '))
    if num != -1:
        numbers.append(num)
        total += num
        print('Your entered number is: ', num)
        print('Sum of the entered numbers: ', total)

if len(numbers) > 0:
    average = float(total / len(numbers))
    formatted_average = "{:.2f}".format(average)

    print('Numbers entered: ', numbers)
    print('Average: ', formatted_average)
else:
    print('No numbers were entered.')


