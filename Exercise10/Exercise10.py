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
#
#variables
pin = 2023
attempts = 0
max_attempts = 3

print('Welcome to Aurora Bank')

enter_pin = input("enter PIN")

while attempts < max_attempts:
    # users pic guess
    print('Please enter your 4 digit PIN.')
    print('You have', max_attempts - attempts, 'attempt(s) remaining!')
    guess = input("PIN:")
    # convert the guess to a number (input gives us a string)
    if len(guess) != 4:
        print('Incorrect amount of digits! Please enter your 4 digit PIN!')
        print('')
    else:
        guess = int(guess)
        # if the guess is identical to the pin, print 'Correct' & exit
        if guess == pin:
            print('Success, you may withdraw your money!')
            exit()
        # else, print line & +1 to attempts
        else:
            print('Wrong, please try again.')
            attempts += 1
            print('')
        print('Max number of attempts reach, account blocked!')






