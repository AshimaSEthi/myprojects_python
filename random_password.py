import random
import string
import string_utils

# Let's assume that I want to have 
# -> 4 alphabets
# -> 4 Numbers
# -> 3 special characters
# we will split our main string into 3 parts str1,str2,str3

str1 = []
for i in range (4):
    alphabet = random.choice(string.ascii_letters)
    str1.append(alphabet)


str2 = []
for j in range (4):
    num = random.choice(string.digits)
    str2.append(num)


str3 = []
for k in range (3):
    symbolss = random.choice(string.punctuation)
    str3.append(symbolss)


final_string = str1+str2+str3
final_string = ''.join(final_string)
final_password = string_utils.shuffle(final_string)
print("The final password generated is : ",final_password)


