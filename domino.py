Color_Off="\033[0m"
info_color = "\033[0;37m"
green_color = "\033[9;36m"
green_color2 = "\033[3;36m"
detect_color = "\033[0;31m"
print(detect_color+'''
              █████████   █████                   █████                                                
  ███░░░░░███ ░░███                   ░░███                                                 
 ░███    ░███  ░███████  █████ ████    ░███         ██████   █████ ████  ██████   ████████  
 ░███████████  ░███░░███░░███ ░███     ░███        ░░░░░███ ░░███ ░███  ░░░░░███ ░░███░░███ 
 ░███░░░░░███  ░███ ░███ ░███ ░███     ░███         ███████  ░███ ░███   ███████  ░███ ░███ 
 ░███    ░███  ░███ ░███ ░███ ░███     ░███      █ ███░░███  ░███ ░███  ███░░███  ░███ ░███ 
 █████   █████ ████████  ░░████████    ███████████░░████████ ░░███████ ░░████████ ████ █████
░░░░░   ░░░░░ ░░░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░░░   ░░░░░███  ░░░░░░░░ ░░░░ ░░░░░ 
                                                              ███ ░███                      
                                                             ░░██████                       
                                                              ░░░░░░                        
          
''')

print (green_color2 + '''
##### ##### ##### ##### ##### ##### ##### ##### ##### #####                                                                                                                                                                                                                                                 
developer : Abu Layan
developer_snapchat : abu_layan554                                                                                                                        
##### ##### ##### ##### ##### ##### ##### ##### ##### #####  
''')
print("اختر اللغه للبدء \n للعربيه اكتب 1 \n للانجليزيه اكتب 2")
print("Choose the language to start For Arabic, type 1 For English, type 2 \n")
choose = int(input("=> "))
Ar = 1
Us = 2
if choose == Ar:
    name_player_one = input(info_color + "ادخل اسم اللاعب الاول:\n =>")
    name_player_two  = input("ادخل اسم اللاعب الثاني:\n =>")
    num_player_one = int(input("ادخل نتيجه اللاعب الاول:\n =>"))
    num_player_two = int(input("ادخل نتيجه اللاعب الثاني:\n =>"))
    print(detect_color + name_player_one + " " + str(num_player_one))
    print(name_player_two + " " + str(num_player_two)) 
    print("---------------------------------------------") 
    if num_player_one >= 110:
        print(green_color + "الفائز " + name_player_one + " (" + str(num_player_one) + ")")
        print(detect_color + "---------------------------------------------")
        print(detect_color + "رساله من ابوليان\n")
        print(green_color + "شكرا لاستخدامك برنامجي \n Bye")
        print(Color_Off)
        exit(0)
    if num_player_two >= 110:
        print(green_color +"الفائز " + name_player_two + " (" + str(num_player_two) + ")")
        print(detect_color + "---------------------------------------------")
        print(detect_color + "رساله من ابوليان\n")
        print(green_color + "شكرا لاستخدامك برنامجي \n Bye")
        print(Color_Off)
        exit(0)
    while num_player_one or num_player_two <= 110:
        new_num_one = int(input(info_color + "ادخل النتيجه الجديده للاعب الاول :\n =>"))
        num_player_one = num_player_one + new_num_one
        new_num_two = int(input("ادخل النتيجه الجديده للاعب الثاني:\n =>"))
        num_player_two = num_player_two + new_num_two
        print(detect_color + "---------------------------------------------")
        if num_player_one <= 110:
            print(detect_color + name_player_one + " " + str(num_player_one))
        if num_player_two <= 110:
            print(detect_color + name_player_two + " " + str(num_player_two))  
            print(detect_color +  "---------------------------------------------")
        if num_player_one >= 110:
            print(green_color + "الفائز " + name_player_one + " (" + str(num_player_one) + ")")
            print(detect_color + "---------------------------------------------")
            print(Color_Off)
            break
        if num_player_two >= 110:
            print(green_color + "الفائز " + name_player_two + " (" + str(num_player_two) + ")")
            print(detect_color + "---------------------------------------------")
            print(Color_Off)
            break
    print(detect_color + "رساله من ابوليان\n")
    print(green_color + "شكرا لاستخدامك برنامجي \n Bye")
    print(Color_Off)
elif choose == 2:
    name_player_one = input(info_color + "Enter The Name Of First Player's:\n =>")
    name_player_two  = input("Enter The Name Of Second player's:\n =>")
    num_player_one = int(input("Enter the First Player's Score:\n =>"))
    num_player_two = int(input("Enter the Second Player's Score:\n =>"))
    print(detect_color + name_player_one + " " + str(num_player_one))
    print(name_player_two + " " + str(num_player_two)) 
    print("---------------------------------------------") 
    if num_player_one >= 110:
        print(green_color + "The Winer " + name_player_one + " (" + str(num_player_one) + ")")
        print(detect_color + "---------------------------------------------")
        print(detect_color + "Message From Abu Layan\n")
        print(green_color + "Thanks For Useing My Script \n Bye")
        print(Color_Off)
        exit(0)
    if num_player_two >= 110:
        print(green_color +"The Winer " + name_player_two + " (" + str(num_player_two) + ")")
        print(detect_color + "---------------------------------------------")
        print(detect_color + "Message From Abu Layan\n")
        print(green_color + "Thanks For Useing My Script \n Bye")
        print(Color_Off)
        exit(0)
    while num_player_one or num_player_two <= 110:
        new_num_one = int(input(info_color + "Enter New score Of First Player's :\n =>"))
        num_player_one = num_player_one + new_num_one
        new_num_two = int(input("Enter New score Of Second Player's:\n =>"))
        num_player_two = num_player_two + new_num_two
        print(detect_color + "---------------------------------------------")
        if num_player_one <= 110:
            print(detect_color + name_player_one + " " + str(num_player_one))
        if num_player_two <= 110:
            print(detect_color + name_player_two + " " + str(num_player_two))  
            print(detect_color +  "---------------------------------------------")
        if num_player_one >= 110:
            print(green_color + "The Winer " + name_player_one + " (" + str(num_player_one) + ")")
            print(detect_color + "---------------------------------------------")
            print(Color_Off)
            break
        if num_player_two >= 110:
            print(green_color + "The Winer " + name_player_two + " (" + str(num_player_two) + ")")
            print(detect_color + "---------------------------------------------")
            print(Color_Off)
            break
    print(detect_color + "Message From Abu Layan")
    print(green_color + "Thanks For Useing My Script \n Bye")
    print(Color_Off)
else:
    print("You did not choose a language \n Bye")