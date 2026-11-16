result1 = "результат операции: 42"
result2 = "результат операции: 54"
result3 = "результат работы программы: 209"
result4 = "результат: 2"

def res(result):
    index = result.index(':')
    print(int(result[index + 2:]) + 10)

res(result1)
res(result2)
res(result3)
res(result4)
