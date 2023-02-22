# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

list1 = "1 2"#input()
list2 = "5 6 7"#input()

A = map(int, (list1.split(' ')))
B = map(int, (list2.split(' ')))

print(list(A))
print(list(B))

print(' '.join(map(str, itertools.product(A, B))))

