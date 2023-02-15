vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for character in s:
    if character in vowels:
        count+= 1
print("Number of vowels: ", count)