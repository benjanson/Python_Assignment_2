#to show list is mutable or not

#creating a list
Fruits = ["Apple","Banana","Mango","Strawberry","Watermelon"]
print(id(Fruits))
print(Fruits)

Vegetables = Fruits
Vegetables[1]='Orange'

print(id(Vegetables))
print(Vegetables)
