import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
print(glob.glob(pattern))

# TODO: use os.path.getsize to find each file's size
# create a list from glob.glob(pattern)
list = glob.glob(pattern)

for x in list:
    print(os.path.getsize(x))
list = glob.glob(pattern)

for x in list:
    print(x, os.path.getsize(x))

# TODO: Add a test to only display files that are not zero length
# add the condition that if its greater than 0 then print.
list = glob.glob(pattern)
for x in list:
    if os.path.getsize(x) > 0:
        print(x, os.path.getsize(x))

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
#gets the last file name in the directory
list = glob.glob(pattern)
for x in list:
    print(os.path.basename(x), os.path.getsize(x))

print('')
print('')
print('')

## PIN checking mechanism

input('enter your PIN')
"supplied_pin = input(“Enter your PIN: “)

guess = getpass.getpass(prompt='PIN:')