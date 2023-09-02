name=input("what is your name?")
age=input("what is your age?")
city=input("which city do you live in?")
love=input("what do you love doing most?")
string="your name is {} and you are {} years old.you live in {} and you love {}"
output = string.format(name,age,city,love)
print(output)