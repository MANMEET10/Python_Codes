#get sentence from user
original=input("what is your sentence? ").strip().lower()

# split sentence into words
words=original.split()


#loop through words and convert to pig latin
new_words=[]
# start with vowel add"yay"
for word in words:
    if word[0] in "aeiou":
        # print("yes")
        new_word=word+"yay"
        new_words.append(new_word)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break
        cons=word[:vowel_pos]     
        rest=word[vowel_pos:]
        new_word=rest+cons+"ay"
        new_words.append(new_word)   
    
print(new_words)
# start with consonant then move consonent cluster to end and add "ay"


# stick words back together
output=" ".join(new_words)
# output the final string
print(output)
