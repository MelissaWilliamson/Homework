#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Count the length of the Belgium string
length = len(Belgium)

# Print a line of hyphens
print('-' * length)

# Replace comma separators with colons
modified_string = Belgium.replace(',', ':')

# Extract population information
popinfo = Belgium.split(',')
pop_belgium = int(popinfo[1])
pop_brussels = int(popinfo[3])
total_pop = (pop_brussels + pop_belgium)

# Print the modified string and population information
print(modified_string)

# Print a line of hyphens
print('-' * length)

print("Population of Belgium: ", pop_belgium)
print("Population of Brussels: ", pop_brussels)
print("Total Population: ", total_pop)





