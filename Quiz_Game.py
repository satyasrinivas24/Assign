score = 0

questions = [
    {
       'question':'Who won cricket World cup in 2011?',
       'options': ['A. India', 'B. sri lanka', 'C. England', 'D. Australia'],
       'answer' : 'A'
    },
    {
        'question': 'In city the actor pawan kalyan won as a MLA?',
        'options' : ['A. Kakinada','B. Vijayawada', 'C. Vizag', 'D. Pithapuram'],
        'answer' : 'D'
    },
    
    {
        'question' : 'who was the captain of ICC T20 in 2024 world winner?',
        'options' : ['A. Smith', 'B. Rahul', 'C. Rohit', 'D. Virat'],
        'answer' : 'C'
    }
]
for i, q in enumerate(questions):
    print(f"q{i+1}:{q['question']}")
    for option in q['options']:
        
        
        print(option)
    print(" ")
    user = input("Enter the answer:")
    if user.upper() == q['answer']:
        score += 1
    print(" ")
    
print(f"yours score: {score}")
