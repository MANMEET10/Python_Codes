from random import choice
questions=["why is sky blue? ","where are all the dinosaurs? ","why we can't touch sky? "]
question=choice(questions)
answer=input(question).lower()
while(answer!="just because"):
    answer= input("why?").lower()

print("oh..okAYY")
