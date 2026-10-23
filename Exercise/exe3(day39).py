
questions = [
    [
        "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
        ],
            
[
    "which language is uused to create Instagram? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],

[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],

[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],
[
    "which language is uused to create Facebook? " , "Python" , "French" , "JavaScript" , "Php" , "None" , 4
    ],

]
levels = [1000 , 2000 , 3000 , 4000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000]

money = 0

for i in range(0  , len(questions)) :
    question = questions[i] 
    print(f"Question for rs. {levels[i]}")
    
    
    print(f"a. {questions[i][1]}             b. {questions[i][2]}")
    print(f"c. {questions[i][3]}         d. {questions[i][4]}")

    reply = int(input("Enter your answer (1-4) "))
    if(reply == question[-1]):
        print(f"correct answer , you have won rs. {levels[i]}")
        if(i==4):
            money = 10000
        elif(i == 9):
           money = 320000 
        elif(i == 9):
            money = 10000000 

    else:
        print("wrong answer")
        break    
    
print(f"you take home maney is {money}")    