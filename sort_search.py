from random import randint
import sort
import search

A = [randint(1, 100) for i in range(10)]
print(A)

sort.bubble_sort(A)
print(A)

val = int(input("Введите значение для поиска: "))
search.binary_search(A, val)
