first_result = "результат операции: 10"
second_result = "результат операции: 514"
third_result = "результат работы программы: 9999"

first_index = first_result.index('10')
second_index = second_result.index('514')
third_index = third_result.index('9999')

print(int(first_result[first_index:]) + 10)
print(int(second_result[second_index:]) + 10)
print(int(third_result[third_index:]) + 10)
