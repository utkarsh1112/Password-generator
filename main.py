#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letter_seq = ''
# symbol_seq =''
# number_seq = ''
# for number in range(1, nr_letters+1):
#   random_letter = random.choice(letters)
#   letter_seq+=random_letter

# for number in range(1, nr_symbols+1):
#   random_symbol = random.choice(symbols)
#   symbol_seq+=random_symbol

# for number in range(1, nr_numbers+1):
#   random_number = random.choice(numbers)
#   number_seq+=random_number

# print(f"Here is your password: {letter_seq+symbol_seq+number_seq}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
seq = []

for number in range(1, nr_letters+1):   # letters ki range
  random_letter = random.choice(letters)      #list se random letter uthaya
  seq.append(random_letter)                    #ek doosri seq naam ki list mein append kar diya

for number in range(1, nr_symbols+1):       #for symbols
  random_symbol = random.choice(symbols)
  seq.append(random_symbol)

for number in range(1, nr_numbers+1):     #for numbers
  random_number = random.choice(numbers)
  seq.append(random_number)


random.shuffle(seq)      # randomly shuffles the list seq

password=''
for number in seq:     #loop to run till seq length
  password+=number    # concatenate every item of list sequentially into string password

print(f"Here is your password: {password}")






##not using shuffle, using loop
# random_seq = []
# for number in range(0,len(seq)):              #a loop to run times the no. of items in seq
#   item = random.choice(seq)                 # stored a random item from list in "item"
#   random_seq.append(item)                      # appended it to a new list "random_seq"
#   seq.remove(item)      # removed that item from seq so that in next iteration it doesnt randomly select it again

# password=''
# for number in random_seq:     #loop to run till random_seq length
#   password+=number    # concatenate every item of list sequentially into string password

# print(f"Here is your password: {password}")

