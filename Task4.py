Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.



from random import randint

def list(N):
    list = []
    for i in range(N):
        list.append(randint(-N, N)
    return list

N = int(input('Введите число N: '))
numbers = list(N)
print(num)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)

