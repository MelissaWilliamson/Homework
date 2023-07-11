#cheese = ('Cheddar', 'Stilton', 'Cornish Yarg')
#cheese += 'Oke'

## The above is not how you add 'Oke' to the cheese list.
## This is how it would be done.

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)

cheese+=['Oke']

print(cheese)

## Below is how I would add additional cheeses to the list
## First create a new variable
extraCheese = ['Brie', 'Edam']
extraCheese+=cheese
print(extraCheese)









