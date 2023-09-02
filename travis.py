known={"Alice", "Bob","Claire","Dan","Emma","Fred","Georgie","Harry"}
print(len(known))
while True:
    print("hii!my name is tarvis")
    name = input("what is your name?  ").strip().capitalize()

    if(name in known):
        print("Hello {} your name is recognized".format(name))
        remove=input("would you like to be removed from system?(y/n)").lower()
        if (remove=='y'):
            known.remove(name)
        elif(remove=='n'):
            print("anyway i don't want to remove you")
          
    else:
        print("Hii {} your name NOT recognized".format(name))
        add= input("would you like to added to the list(y/n)? ").lower()
        if(add=='y'):
            known.add(name)
        elif(add=='n'):
            print("see you around")

          
            
        
