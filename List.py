lst = ['Apple','Guava','Mango','Banana','Kiwi']

print("Lenght of the list:", len(lst))
print("First Element:",lst[0])
print("Last Element:",lst[-1])

lst.append('Papaya')
print("Updated List :",lst)

lst.remove('Guava')
print("Updated List :",lst)
lst.sort()
print("Sort List:",lst)

lst.pop(1)
print("Update List",lst)

lst.reverse()
print("Reverse List :",lst)

print("Multiplication on List :",lst*2)

lst = lst[:4]
print("Sliced List :",lst)

lst.clear()
print("Updated list :",lst)