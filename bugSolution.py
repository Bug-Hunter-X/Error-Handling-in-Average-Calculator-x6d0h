def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

data = [10, 20, 30, 40, 'abc']
average = calculate_average(data)
print(f"The average is: {average}")

data2 = []
average2 = calculate_average(data2)
print(f"The average of an empty list is: {average2}")

data3 = [10,20,30,40]
average3 = calculate_average(data3)
print(f"The average of a list with only numbers is: {average3}") 