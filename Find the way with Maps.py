triple= lambda x: x*3

list1= list(map(int, input("Enter list element separated by space: ").split()))
result= list(map(triple, list1))
print(result)