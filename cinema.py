films={
    "Ghost Busters":[15,5],
    "Emma":[18,5],
    "Stranger Things":[18,5],
    "Mission Impossible":[18,5]
}
while True:
   choice= input("which film do you want to watch? ").strip().title()
   if(choice in films):
      age = int(input("what is your age? ".strip()))
      if age>= films[choice][0]:
         if films[choice][1]>0:
            print("enjoy the film")
            films[choice][1]=films[choice][1]-1
         else:
            print("we are sold out..")
      else:
         print("you are too young to watch that film")
   else:
      print("we don't have that film...")
