#quiz game:
score = 0

Q1 = "What is the capital of US?"
print(Q1)

user_answer = input("enter you answer: ").strip().lower()
A1 = "Washington DC"

if(A1.lower() == user_answer):
 print("correct")
 score += 1

else:
 print("wrong")


Q2 = "What is the capital of Malaysia?"
print(Q2)
user_answer = input("enter your answer: ").strip().lower()
A2 = "Kuala Lumpur"

if(A2.lower() == user_answer):
  print("correct")
  score +=1

else:
  print("wrong")


Q3 = "What is the capital of Pakistan?"
print(Q3)
user_answer = input("enter your answer: ").strip().lower()
A3 = "Islamabad"

if(A3.lower() == user_answer):
    print("correct")
    score += 1

else:
    print("wrong")


Q4 = "What is the capital of Italy?"
print(Q4)
user_answer = input("enter your answer: ").strip().lower()
A4 = "Rome"

if(A4.lower() == user_answer):
    print("correct")
    score += 1
else:
    print("wrong")


Q5= "What is the capital of Japan?"
print(Q5)
user_answer = input("enter you answer: ").strip().lower()
A5 = "Tokyo"

if(A5.lower() == user_answer):
    print("correct")
    score +=1

else:
    print("wrong")


Q6 = "What is the capital of Australia?"
print(Q6)
user_answer = input("enter your answer: ").strip().lower()
A6 = "Canberra"

if(A6.lower() == user_answer):
    print("correct")
    score += 1

else:
    print("wrong")


Q7 = "What is the capital of South Korea?"
print(Q7)
user_answer = input("enter your answer: ").strip().lower()
A7 = "Seoul"

if(A7.lower() == user_answer):
    print("correct")
    score += 1

else:
    print("wrong")


Q8 = "What is the capital of Indonesia?"
print(Q8)
user_answer = input("enter your answer: ").strip().lower()
A8 = "Jakarta"

if(A8.lower() == user_answer):
    print("correct")
    score += 1
else:
    print("wrong")


Q9 = "What is the capital of Saudia Arabia?"
print(Q9)
user_answer = input("enter your answer: ").strip().lower()
A9 = "Riyadh"

if(A9.lower() == user_answer):
    print("correct")
    score += 1 

else:
    print("wrong")


Q10 = "What is the capital of Canada?"
print(Q10)
user_answer = input("enter your answer: ").strip().lower()
A10 = "Ottawa"

if(A10.lower() == user_answer):
    print("correct")
    score += 1

else:
    print("wrong")


Q11 = "What is the capital of United Kingdom?"
print(Q11)
user_answer = input("enter you answer: ").strip().lower()
A11 = "London"

if(A11.lower() == user_answer):
    print("correct")
    score += 1


else:
    print("wrong")


Q12 = "What is the capital of Oman?"
print(Q12)
user_answer = input("enter your answer: ").strip().lower()
A12 = "Muscat"

if(A12.lower() == user_answer):
    print("correct")
    score += 1

else:
    print("wrong")


Q13 = "What is the capital of Philippines?"
print(Q13)
user_answer = input("enter your answer: ").strip().lower()
A13 = "Manila"

if(A13.lower() == user_answer):
    print("correct")
    score += 1

else:
    print("wrong")


Q14 = "What is the capital of Turkey?"
print(Q14)
user_answer = input("enter your answer: ").strip().lower()
A14 = "Ankara"

if(A14.lower() == user_answer):
    print("correct")
    score += 1
else:
    print("wrong")  

print("I reached the end!")
print("Your final score is" , score, "/14")
if score == 15:
        print("Perfect!")
elif score >= 12:
        print("Excellent!")
elif score >= 9:
        print("Good job!")
else:
        print("Need more practice!")
        

        

        