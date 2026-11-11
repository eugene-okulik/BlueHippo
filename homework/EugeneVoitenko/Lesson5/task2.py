first_result = "результат операции: 10"
second_result = "результат операции: 514"
third_result = "результат работы программы: 9999"

first_index = first_result.index(':')
second_index = second_result.index(':')
third_index = third_result.index(':')

print(int(first_result[first_index + 2:]) + 10)
print(int(second_result[second_index + 2:]) + 10)
print(int(third_result[third_index + 2:]) + 10)
