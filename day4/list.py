'''lst = ['item1','item2','item3', 'item4', 'item1']
doesExit = 'name' in lst
print(doesExit)
lst.append('name')
print(lst)
lst.insert(2, 'site')
print(lst)
lst.remove('item1')
print(lst)
lst.pop(3)
print(lst)
lst.clear()
print(lst)
'''
fruits = ['banana', 'orange', 'apple']
fCopy = fruits.copy()
print(fruits)
print(fCopy)
fCopy[1] = 'lemon'
print(fruits)
print(fCopy)
fruits[1] = 'melon'
print(fruits)
print(fCopy)


print()

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
countries[2] = 'Nigeria'
print(countries)
lastC = len(countries) -1
countries[lastC] = 'spain'
print(countries)