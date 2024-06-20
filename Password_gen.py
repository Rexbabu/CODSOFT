import random
cap_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
low_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['~','!','@','#','$','%','^','&','*','_']
len_cap_letters=int(input("How many capital letters do you want..??\n"))
len_low_letters=int(input("How many lower letters do you want..??\n"))
len_numbers=int(input("How many numbers do you want..??\n"))
len_symbols=int(input("How many symbols do you want..??\n"))
password_list=[]
for char in range(1,len_cap_letters + 1):
    password_list.append(random.choice(cap_alphabets))
for char in range(1,len_low_letters + 1):
    password_list+=(random.choice(low_alphabets))
for char in range(1,len_numbers + 1):
    password_list+=(random.choice(numbers))
for char in range(1,len_symbols + 1):
    password_list+=(random.choice(symbols))

random.shuffle(password_list)

password=" "
for i in password_list:
    password+=i

print(f"The Generated Password is- {password}")