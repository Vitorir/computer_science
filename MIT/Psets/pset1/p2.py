counter = 0
for i in range(len(s)):
    if s[i:].startswith('bob'):
        counter = counter + 1

print("Number of times bob occurs:", counter)