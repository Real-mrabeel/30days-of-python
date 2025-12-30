first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

text = 'python'
# Use the string directly instead of converting to float which raises ValueError
text1 = text
print(text1)
print(len(text))

#side of triangle

sideA = float(input('Enter the value of side A: '))
sideB = float(input('Enter the value of side B: '))
sideC = float(input('Enter the value of side C: '))

perimeter = sideA + sideB + sideC
print('The perimeter of a given angles are: ', perimeter)

#get the raduis
length = float(input('Enter the length of the circle: '))
width = float(input('Enter the width of the circle: '))

area = length * width
perimeter = 2*(length + width)

print("the area of the circle is: ", area)
print("the perimeter of the circle is: ", perimeter)
