ladies = [
        {'name' : 'Emma Woodhouse', 
        'eyes' : 'blue',
        'hair' : 'blonde',
        'wealth' : 'much',
        'novel' : 'Emma'
        },
        {'name' : 'Fanny Price',
        'eyes' : 'green',
        'hair' : 'brown',
        'wealth' : 'little',
        'novel' : 'Mansfield Park'
        },
        {'name' : 'Elizabeth Bennet',
        'eyes' : 'brown',
        'hair' : 'brown',
        'wealth' : 'some',
        'novel' : 'Pride and Prejudice'
        },
        {'name' : 'Anne Elliot',
        'eyes' : 'blue',
        'hair' : 'brown',
        'wealth' : 'some',
        'novel' : 'Persuasion'
        },
        {'name' : 'Marianne Dashwood',
        'eyes' : 'blue',
        'hair' : 'blonde',
        'wealth' : 'little',
        'novel' : 'Sense and Sensibility'
        },
        {'name' : 'Elinor Dashwood',
        'eyes' : 'green',
        'hair' : 'blonde',
        'wealth' : 'little',
        'novel' : 'Sense and Sensibility'
        }
    ]

def check_list(key, key_value):
    ladies_temp = []
    i = 0
    while i < len(ladies):
        if ladies[i][key] == key_value:
            ladies_temp.append(ladies[i])
        i += 1
    if len(ladies_temp) > 0:
        return ladies_temp
    else:
        print "None of the ladies match that description! Guess again."
        key_value = raw_input("Next guess?").lower()
        i = 0
        while i < len(ladies):
            if ladies[i][key] == key_value:
                ladies_temp.append(ladies[i])
            i += 1
        return ladies_temp

def is_final():
    if len(ladies) == 1:
        print "You're thinking of " + ladies[0]['name'] + " from " + ladies[0]['novel'] + "!"
        return True
    else:
        print "Hmmm... I'm still not sure who you're thinking of. I need to ask another question."
        return False

print "Welcome to the Jane Austen heroine selector! I'll be asking you a few questions. Let's begin!"
print "The first question is: What color eyes does your heroine have?"
print "(possible answers: blue, green, brown)"
ladies_eyes = raw_input("What color eyes?").lower()
print ("So, your heroine has " + ladies_eyes + " eyes?")      

ladies = check_list('eyes', ladies_eyes)
if is_final() == True:
    print "That was fun! Let's play again some time."
else:
    print "The second question is: What color hair does your heroine have?"
    print "(possible answers: brown, blonde)"
    ladies_hair = raw_input("What color hair?").lower()
    print ("So, your heroine has " + ladies_hair + " hair?")
    ladies = check_list('hair', ladies_hair)
    if is_final() == True:
        print "That was fun! Let's play again some time."
    else:
        print "The third question is: How much money does your heroine have?"
        print "(possible answers: little, some, much)"
        ladies_wealth = raw_input("How much money?").lower()
        print ("So, your heroine has " + ladies_wealth + " money?")  
        ladies = check_list('wealth', ladies_wealth)
        if is_final() == True:
            print "That was fun! Let's play again some time."




