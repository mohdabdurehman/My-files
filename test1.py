multilines = '''
hey man wagwan
                  am just checking
        
        
     you good   
'''

print(multilines)
print(multilines.title())
print(len(multilines))
multilines += '                                         '
multilines = '                 '+ multilines
print(len(multilines)) 


title = "menu".upper()
print (title.center(30,"="))
print ("coffee".ljust(20,"-") + "$4".rjust(11))
print("")

zip_value = int("9999")
print(zip_value)

print("")
import random
print("")

playerchoice = input("Enter ...\n 1 for Rock,\n 2 for paper or \n 3 for scissors:\n\n")
compchoice = random.choice("1,2,3")
computer = int(compchoice)
print("")
print("you chose"+ playerchoice)
print("you choose {}".format(playerchoice)) 
print("comp chose"+ compchoice)

print("")


