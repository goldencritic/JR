#ah, you're finally awake.
print()
print()
print("""hello user. welcome to the digital phonebook! we have been digging through your personal contacts/info and adding them here. we have also added additional strangers for you to chat with!""")
print()
print()
input("press any button to continue")

#the thing that keeps this train going! CHOO-CHOO!
while range(999):
   
   
   #things i imported to make this whole machine work!
    import random
    import time
    import math
    import phonebookmodule
    from random import choice
 
    #names
    j = phonebookmodule.j
    t = phonebookmodule.t
    c = phonebookmodule.c
    b = phonebookmodule.b
    ny = phonebookmodule.ny

    #secret names
    pe = phonebookmodule.pe
    nwo = phonebookmodule.nwo
    cb = phonebookmodule.cb
    sus = phonebookmodule.sus

    #numbers
    jn = phonebookmodule.jn
    tn = phonebookmodule.tn
    cn = phonebookmodule.cn
    bn = phonebookmodule.bn
    nyn = phonebookmodule.nyn

    #secret numbers, which wont be used sadly but are here and can still be used if you know their number
    pen = phonebookmodule.pen
    nwon = phonebookmodule.nwon
    susn = phonebookmodule.susn
    cbn = phonebookmodule.cbn #sadly probably wont make it, but who knows, maybe Celebrazil might get in here!

    #adresses 
    js = phonebookmodule.js
    ts = phonebookmodule.ts
    cs = phonebookmodule.cs
    nys = phonebookmodule.nys
    bs = phonebookmodule.bs

    
    #incident
    i_n = phonebookmodule.i_n


   #starting list of people in your contacts
    print("please input any phone number or name to select their profile.")
    print()
    print()
    print(""" recent contacts:""")
    print(j)
    print("Jamshid's number:", jn)
    print()
    print(t)
    print("Tombe's number:", tn)
    print()
    print(ny)
    print(ny, "number:", nyn)
    print()
    print(b)
    print(" Blue's number:", bn)
    print(c)
    print("Connor's number:", cn)
    search = "name"



    #capitalizes the first letter
    search = input("enter name/number: ")
    search = search.capitalize()
    
    
   
    
    
    
    if search == sus or search == susn:

        print(""""
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿          
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⢀⠀⠀⠀⢠⠀⠀⠀⠀⠉⠙⠿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠰⡄⠀⣃⣠⣤⣬⣆⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⣠⣀⠀⠀⠈⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⡏⠀⡴⢄⠀⠀⢠⣾⣿⣿⠿⠿⠿⣿⣿⣦⣽⣼⣀⣜⣠⣿⣿⣴⡄⠀⣽⣿
    ⣿⣿⣿⣿⣿⣿⣿⡇⠠⢰⠆⢢⣤⣼⣿⣿⣧⣶⣶⡖⠀⠀⠀⢈⣿⣿⣯⣭⣭⠉⠉⠁⠀⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⡇⠠⡀⢺⠸⢿⣿⣿⣿⣿⣿⣿⣥⣤⣤⣴⣿⣿⣿⣿⣿⣛⣀⣀⡀⣰⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠣⠴⡾⢻⣿⣿⣿⣿⣿⣿⣟⠻⠿⠿⠛⠿⠿⢛⣿⣿⣿⠇⣿⣿⣿         
    ⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⣿⣮⣛⣫⣵⣾⣿⣿⠿⠋⢠⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⡀⢰⣶⣿⣿⣟⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⢸⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢀⢸⣿⣦⣝⠻⡿⣡⣄⠀⠀⠀⠀⠀⠀⢐⠀⠀⢸⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡇⠀⢀⣤⣴⣶⣿⡹⣿⣿⣿⡟⣵⢰⡟⣴⡆⠀⠀⠀⠀⠀⣸⠀⠀⢸⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⠀⢀⣯⡻⣿⣿⣿⣿⣮⣝⣩⣾⣿⢎⣤⣙⣴⣿⣷⡄⠀⠀⣿⡆⠀⢸⣿⣿⣿
    ⣿⣿⣿⣿⣿⡇⠀⠀⣿⣷⣌⡿⠿⣛⠻⢿⣿⣿⣿⢸⣿⣿⣿⡿⣡⡇⠐⠀⣿⣿⠀⣼⣿⣿⣿           
    ⣿⣿⣿⣿⣿⠀⠀⢀⢻⣿⢏⡶⣿⣿⣿⣷⡍⢿⡷⢟⣫⣭⡛⣰⣿⠣⠁⣸⣿⣿⣼⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⢠⠀⡾⣸⣿⣎⢡⣿⢿⣿⡿⢛⣠⣾⣿⣿⣿⡇⣋⣭⣧⢺⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣸⢀⣇⢿⢸⣿⡘⠏⢼⡟⣰⣿⣿⣿⣿⣿⠟⣐⣻⣿⠋⣾⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡁⣿⣿⣦⡘⣿⢸⣿⠌⣸⣿⣿⣿⡿⢋⣴⣿⣝⢿⣿⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡇⣬⣛⠿⣷⡍⣾⣿⠀⣿⣿⠿⣫⣔⢿⣿⣿⣿⢘⣿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡿⢡⣬⣉⣛⠲⠶⠜⣛⣒⣤⣤⣛⣛⣿⣆⣉⡛⠉⣈⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠃⢿⣿⣿⣿⢻⣷⣶⠆⣤⣤⣤⡄⢠⣤⣤⣤⣄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡏⠄⣿⣿⣿⡏⢸⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⢠⢠⣿⣿⣿⠃⣺⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⡇⠄⢸⣿⣿⣿⠀⣿⣿⣿⠀⣿⣿⣿⣧⢸⣿⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣦⡀⣭⣭⣭⣭⣤⣭⡍⠉⠀⠛⠛⠻⠿⠈⣥⣤⣤⠀⠀⠼⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡇⣿⣿⣿⣿⣿⣤⣤⣝⠻⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⢹⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠛⠿⠸⢿⣿⣿⣿⣿⣿⣿⣿⠿⢟⣸⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣮⣍⣛⣛⠛⠿⠿⢛⣋⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿                                                    
                                                
                                                    ⠄⠄⢠⠄⣠⣶⣿⣿⣿⠿⠿⣛⣂⣀⣀⡒⠶⣶⣤⣤⣬⣀⡀⠄⢀⠄⠄⠄⠄⠄⠄⠄ 
                                                    ⠄⠄⢀⣾⣿⣿⣿⡟⢡⢾⣿⣿⣿⣿⣿⣿⣶⣌⠻⣿⣿⣿⣿⣷⣦⣄⡀⠄⠄⠄⠄⠄
                                                    ⠄⠄⣈⣉⡛⣿⣿⣿⡌⢇⢻⣿⣿⣿⣿⣿⠿⠛⣡⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠄⠄⠄
                                                    ⠄⠺⠟⣉⣴⡿⠛⣩⣾⣎⠳⠿⠛⣋⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠄
                                                    ⠄⠄⠄⠘⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄
                                                    ⠄⠄⢀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄
                                                    ⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣀
                                                    ⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠘⠛
                                                    ⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⣀⣀⣠⣤
                                                    ⠄⠄⣀⣀⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣩⠤⠾⠄⠛⠋⠉⢉
                                                    ⠄⠺⠿⠛⠛⠃⠄⠉⠙⠛⠛⠻⠿⠿⠿⠟⠛⠛⠛⠉⠁⠄⠄⣀⣀⣠⣤⣠⣴⣶⣼⣿
                                                    ⣿⣿⣿⣿⣿⠀⠀⢀⢻⣿⢏⡶⣿⣿⣿⣷⡍⢿⡷⢟⣫⣭⡛⣰⣿⠣⠁⣸⣿⣿⣼⣿⣿⣿⣿""")
        input("press any button to SUStinue")



    

    if search == pe or search == pen:
        print("PEWWDIEPIEEEEEEEEE!!!")
        input("press any button to continue")
        print("peewwwwwdieeepieeeee-ah!!!!!")
        input("this continues on for over 3 hours before the call is abruptly ended.")


  
 

    
    
    #call a buddy!
    if search == b or search == bn:
        print(" user", b, "was chosen. what would you like to do?")
        print()
        print("1) get info   2) call   3) go back")
        choice_b = input("")
        if choice_b == "1":
           
            while choice_b != "2" or choice_b != "3":
                print("users bio: hewwo my nawme is Blue :3 i wove to cook and hang out with my buwddies! X3")
                print()
                print("adress:", bs, "number:", bn, "name:", b)
                print()
                input("just looking at the bio makes you sick to the stomach. (press any button to continue)")
                choice_b = input("1) stay    2) call   3) go back ")
                if choice_b == "2": choice_b = "2"
                if choice_b == "2": break
                elif choice_b == "3": break
    
        while choice_b == "2":
            print("calling...")
            time.sleep(2)
            print("hewwwo! who this??? :1")
            choice_b2 = input("1) can you stop speaking like that?     2) oh god dammit-heyyy buddy! ")
            if choice_b2 == "1": print("thats not nice! >:T")
            if choice_b2 == "1": input("god stop speaking like that you wanker! *hang up*")
            if choice_b2 == "1": break
            if choice_b2 == "2": print("oh hewwo friend! i didnt reawise it was you! :3")
            if choice_b2 == "2": choice_b3 = input("1) whatcha doing? 2) can i borrow some money? pweassee :3 ")
            if  choice_b3 == "1": print(" oh nawthin' mooch! just reading the news! i think thewes a typo in it! it has the letters 'WO' for some odd weason! :P")
            if choice_b3 == "1": input("WO you say? hmm that sounds important. gotta go, cya")
            if choice_b3 == "1": print("okiey bwyeeeeeee! X)")
            if choice_b3 == "1": break
            if choice_b3 == "2": print("...seriously? i've given you over 250 dollars in the past week, and you have the audacity to ask for more? |:' ")
            
            if choice_b3 == "2": input("look money has been hard to come by alright? help a friend out!")
            if choice_b3 == "2": print("hmph alright e_e but no more after this mister! i have bills to pay and baking supplies to buy too!")
            if choice_b3 == "2": input("ok thanks so much! *hang up*")
            if choice_b3 == "2": break

        
    
    
    
    
    
    
    
    #call the military!
    
    if search == ny or search == nyn:
        print("user", ny, "was chosen. would you like to call or get info?")
        print()
        choice_ny = input("1) get info   2) call  3) go back ")

        if choice_ny == "3":
            print("...good riddance...")
            time.sleep(2)
        
        
        if choice_ny == "1": 
            while choice_ny == "1":
                print()
                print(""" user bio: United Canadians of Navy seals was formed after the 'war of the powers' ended 2 years ago. this specialized branch of the military exceeds marines in solo combat capabilities and are mainly used for assasination or single-man missions.""")
                print()
                print("additional info about this user is privated.")
                print()
                input("press any button to continue")
                choice_ny = input(" 1) get info  2) call  3) go back ")
                print()
                if choice_ny == "2": print(random.choice(i_n))
                if choice_ny == "2": input("press any button to continue")

                if choice_ny == "3": print("...good...")
                if choice_ny =="3": time.sleep(2)
                if choice_ny == "3": break
        elif choice_ny == "2":
            print(random.choice(i_n))
            input("press any button to exit")
        
        
    
    
    
    
    
    
    
    
    #option to call connor!
    if search == c or search == cn:
        print("user", c, "was chosen. would you like to call or get info?")
        choice_c = input("1) get info   2) call   3)  go back ")

        if choice_c == "1":
            while choice_c != "2" or choice_c != "3":
                print()
                print(" user bio: Hello i'm Connor the smarty pants overlord. My plan is to create a sentient program to destroy humanity.")
                print()
                print(" user adress:", cs, "user number:", cn, "user name:", c)
                print()
                input("press any button to continue")
                print()
                choice_c = input("1) stay here   2) call   3) go back ")
                if choice_c == "3": print("exiting please wait...")
                if choice_c == "3": break
                if choice_c == "2": choice_c = "2"
                if choice_c == "2": break
        
        while choice_c == "2":
            print("calling user")
            time.sleep(2)
            print("entering messenger..")
            time.sleep(2)
            print("who dares to text connor the almighty?")
            choice_c2 = input("1) lets chat you doofus!   2) read your bio. your plan sucks ")
            if choice_c2 == "2": print("my plan does not suck! you suck! *hangs up*")
            if choice_c2 == "2": input("press any button to continue")
            if choice_c2 == "2": break
            elif choice_c2 == "1": print(" you Niave fool. chat with me? the almighty?")
            input("press any button to continue")
            choice_c3 = input("1) wait why did you capitalize the 'n' in your sentence?...   2) you dont really sound that mighty to me. ")
            if choice_c3 == "1": print("crap! i spilled out a hint! *hangs up*")
            
            print()
            if choice_c3 == "1": input("this sounds pretty important. i should probably memorise it! (press any button to continue)")
            if choice_c3 == "1": break
            elif choice_c3 == "2": print("yes i am oh-so mighty! fear me! fearrrr meeee! *hangs up*")
            elif choice_c3 == "2": input("whatever weirdo (press any button to continue)")
            elif choice_c3 == "2": break


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #call tombe!
    
    if search == t or search == tn:
        print("user", t, "was chosen. would you like to call or gain info?")
        choice_t = input("1) info  2) call  3) go back ")

        if choice_t == "1":
            while choice_t != "2" or choice_t != "3":
                print()
                print(" users bio: smart fella whos learning python. best score in alien game is 67 B).")
                print()
                print("adress:", ts, ". number:", tn, ". name:", t)
                print()
                input("press any button to continue")
                choice_t = input("1) stay   2) call   3) go back ")
                if choice_t == "2": choice_t = "2"
                if choice_t == "2": break
                elif choice_t == "3": break
        while choice_t == "2":
            print(" calling user...")
            time.sleep(2)
            print("whats popping random caller")
            choice_t2 = input("1) came here to chat!  2) COOL IT! ")
            if choice_t2 == "2": print("mann who ya think you be talking to? you sussy little SUS!")
            print()
            if choice_t2 == "2": print("sus? lol reminds me of the 'dont call imposter at 3 am' videos! so cringe!.")
            if choice_t2 == "2":input("press any button to continue")
            print()
            if choice_t2 == "2": print("yeah maybe you should try calling sus, you amogus baby! *hangs up*")
            print()
            if choice_t2 == "2": input("press any button to continue")
            if choice_t2 == "2": break
            elif choice_t2 == "1": print("mann i aint got no time for that! *hangs up*")
            print()
            input("press any button to continue")
            break
            
            



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #call me! the most legendary of them all!
    
    if search == j or search == jn:
        print("user", j, "was chosen. would you like to call or gain info?")
        choice_j = input("1) info    2) call   3) go back ")
        
        
        
        
        if choice_j == "1":
             while choice_j != "2" or choice_j != "3":
                  print()
                  print ("users bio: sup, names jamshid but people call me jam. i'm a genius in programming and very big brain.")
                  print("adress:", js, ". number:", jn, ". name:", j)
                  print()
                  input("press any button to continue")
                  choice_j = input("1) stay here   2) call  3) go back ")
                  if choice_j == "2": choice_j = "2"
                  if choice_j == "2":break
                  elif choice_j == "3": break
        
        
        while choice_j == "2":
            if choice_j == "2": print("calling user...")
            if choice_j == "2": print("hello?...")
            if choice_j == "2": choice_j2 = input("1) hi!  2) deez nuts ")
            if choice_j2 == "2": print("....")
            if choice_j2 == "2": time.sleep(2)
            if choice_j2 == "2": print("*hangs up*")
            if choice_j2 == "2": input("press any button to continue")
            if choice_j2 == "2": break
            elif choice_j2 == "1": print("what do you want?")
            choice_j2 = input(" 1) how ya doing?   2) watcha doin? ")
            if choice_j2 == "1": print(" pretty alright. working on a python project for class. its about a digital phonebook or something")
            print()
            if choice_j2 == "1": input("thats wacky (press any button to end phone call)")
            if choice_j2 == "1": break
            elif choice_j2 == "2": print(" taking a break from my coding project right now. watching some guy called 'Pewdiepie'. love that guy. wish there was a way i could contact him!")
            print()
            if choice_j2 == "2": input("sounds like a funny guy! (press any button to end call)")
            break
    

    if search == nwo or search == nwon: print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣤⣾⣿⣽⣿⠿⠿⠛⠛⠛⠻⠯⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀
        ⣠⣿⣿⣿⣿⢿⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⡄⠀⠀⠀⠀⠀⠀
        ⣸⣿⣿⣅⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀
        ⢺⣿⣿⢷⣦⣄⠀⠀⠀⠀⢀⣶⣶⣄⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀
        ⢸⣿⣧⣿⣿⣿⣷⣤⠀⠠⣿⣿⣿⣿⡕⠀⢿⡇⠀⠀⠀⠀⠀⠀
        ⡏⣽⣿⣿⣿⣿⡇⠀⠈⢿⣿⣿⡿⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀
        ⢸⣿⡟⠻⢿⠟⣹⡇⠀⠀⠈⠻⠟⠃⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀
        ⢻⣷⣦⣤⣶⣿⣷⣶⣤⣄⣀⠀⣐⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠈⡆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠙⠑⠀⠀⠀⠀⠀⠀⠀⠀
        ⠸⣄⢻⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢈⡄⣿⣿⣿⣿⣿⣿⣿⠁⠀⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣤⣶⢼⠀⡜⣿⣿⡟⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⢀⡀⣴⣶⣞⣿⡟⢸⢠⣿⣿⣿⡟⠜⢿⣿⡿⠀⢀⠉⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣹⣿⣿⣿⣿⡷⣹⣿⣿⣿⣿⣿⣄⠀⠀⠀⣠⠂⠀⠀⠀⠀""")
 
    if search == nwo or search == nwon:
        input("the entity calls...")
            

        






