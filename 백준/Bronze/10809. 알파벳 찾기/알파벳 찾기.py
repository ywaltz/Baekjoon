result = [-1] * 26

word = input()

for index, char in enumerate(word):
    
    position = ord(char) - ord('a')
    
    if result[position] == -1:
        result[position] = index
        
print(*result)