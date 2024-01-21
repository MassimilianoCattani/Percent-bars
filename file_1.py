import math
BG_WHITE = '\033[47m'
FG_RED = '\033[31m'
OFF = '\033[0m'
choices = {'a':{'n': 0, 'per': 0},
        'b':{'n': 0, 'per': 0},
        'c':{'n': 0, 'per': 0},
        'd':{'n': 0, 'per': 0},
        'e':{'n': 0, 'per': 0},
        'f':{'n': 0, 'per': 0},
        'g':{'n': 0, 'per': 0},
}

# Catch the preference.
def user_sele(arr, user):
    for k,v in arr.items():
        if user == k:
            for k1, v2 in v.items():
                if k1 == 'n':
                    v2 += 1    
                    v.update({k1 : v2})
                    return arr
                
# get total preferences/inputs.
def total_inp(arr):
    tot = 0
    for k,v in arr.items():
        for k1, v2 in v.items():
            if k1 == 'n':
                tot = tot + v2
    return tot

# update %
def update_per (arr, tot):
    if tot == 0:
        return
    for k, v in arr.items():
        for k_per, v_per in v.items():
            if k_per == 'n':
                hold = v_per
            if k_per == 'per':
                v_per = (hold / tot) * 100
                v.update({k_per : "{:.2f}".format(v_per)}) 
    return arr
#Display.
def display(arr, tot):
    print(f"Total preferences: {math.floor(tot / 2)}\n")
    for k, v in arr.items():
        for v_dis in v.values():
            x = v_dis
            x = float(x)
            graphic = ' ' * math.floor(x) 
        print (f"Element {k} : {x} %".ljust(20)+f"{BG_WHITE}{graphic}{OFF}\n")
        
def main(arr):
    flag = False
    user_inp = ''
    while flag is False:
        counter = 1
        for k in arr.keys():
            print(f"Option: {k}")
        user_inp = input("Select one among the above options or 'q' to quit: ").lower()
        print('-' * 50)
        
        for k in arr.keys():
            
            if user_inp == 'q':
                if total_inp(arr) == 0:
                    print('END')
                    flag = True
                    break 
                print('\n')
                print('FINAL OUTPUT:')
                print('\n')
                display(arr_per_mod, total)
                print('END')
                flag = True
                break  
        
            if user_inp != k and counter == len(arr):
                msg = f"{FG_RED}Please, enter valid input!{OFF}" 
                print(msg)
                print('-'* 50)
                
            if user_inp == k:
                arr_n_mod = user_sele(arr, user_inp)
                total = total_inp(user_sele(arr, user_inp))
                arr_per_mod = update_per(arr_n_mod, total)
                display(arr_per_mod, total)
                break
            counter += 1
main(choices)