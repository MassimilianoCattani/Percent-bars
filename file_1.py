import math
BG_WHITE = '\033[47m'
OFF = '\033[0m'
choices = {'a':{'n': 0, 'per': 0},
        'b':{'n': 0, 'per': 0},
        'c':{'n': 0, 'per': 0}
}

TOT = 0
FLAG = False
USER = ''
while FLAG is False:
    counter = 1
    USER = input("Enter choice: ")
    for k,v in choices.items():
        if USER == 'q':
            FLAG = True
            print('_' * 50)
            print("Final result: ")
            break
        if counter < len(choices):
            
            if USER == k:
                TOT = TOT + 1
                for k1, v2 in v.items():
                    if k1 == 'n':
                        v2 += 1    
                        v.update({k1 : v2}) 
                       
            else:
                continue
        else:
            print('_' * 50)
            print("Pleae, enter valid input!")
            print('_' * 50)
            if TOT == 0:
                TOT = 1
            else:
                TOT = TOT
        counter += 1
    # update %
    for k, v in choices.items():
        for k_per, v_per in v.items():
            if k_per == 'n':
                HOLD = v_per
            if k_per == 'per':
                v_per = (HOLD / TOT) * 100
                v.update({k_per : "{:.2f}".format(v_per)}) 
    # Display.
    print(f"Total preferences: {TOT}\n")
    for k, v in choices.items():
        for k_dis, v_dis in v.items():
            x = v_dis
            x = float(x)
            graphic = ' ' * math.floor(x) 
        print(f"Element {k} : {x} %".ljust(20)+f"{BG_WHITE}{graphic}{OFF}\n")
       