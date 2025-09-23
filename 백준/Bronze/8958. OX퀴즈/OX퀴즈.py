test_cases = int(input())

for _ in range(test_cases):
    quiz_result = input()
    
    total_score = 0
    consecutive_score = 0
    for char in quiz_result:
        if char == 'O':
            consecutive_score +=1
            total_score += consecutive_score
        else:
            consecutive_score = 0
    print(total_score)