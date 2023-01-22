# Syniah Peterson
sum = 0
numbers = []
# While the number of valid integers is below 5 the user must continue to input numbers
while len(numbers) != 5:
    try:
        num = int(input("Enter an integer: "))
    except:
        print("Error: Please enter an integer!")
    else:
        numbers.append(num)
# After the user inputs the correct number of valid integers then the sum is calculated and then output
for i in range(len(numbers)):
    sum += numbers[i]
print("The sum is: " + str(sum))