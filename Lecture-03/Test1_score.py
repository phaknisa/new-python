# if condition:
    # code to execute if condition is True
    
score_1 = int(input("Enter the score for test 1: "))
score_2 = int(input("Enter the score for test 2: "))
score_3 = int(input("Enter the score for test 3: "))
average_score = (score_1 + score_2 + score_3) / 3
print(f"Your average score is {average_score:.1f}")

if average_score >= 95:
    print("Congratulations!")