import math
import random
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
            return user
#print(user_sele(choices, 'c'))   



def value_sort(arr):
    hold = []
    for k,v in arr.items():
        for k_bet, v_bet in v.items():
            if k_bet == 'n':
                hold.append(v_bet)
    for i in range(len(hold)):
        j = i + 1
        for j in range(len(hold)):
            if hold[i] > hold[j]:
                temp = hold[i]
                hold[i] = hold[j]
                hold[j] = temp
    return hold
#print(value_sort(rand_num(choices)))


# Associate user with the value of 'n'.
def value_user(arr, user):           
    for ku, vu in arr.items():
        if user == ku:
            for hi, ho in vu.items():
                if hi == 'n':
                    user = ho
    return user
#print(rand_num(choices))
#print(value_user(rand_num(choices), user_sele(choices, 'c')))


#Calc money won
def prize(hold_sort, user, money): 
    for iter in range(len(hold_sort)):
        if user == hold_sort[iter]:
            if iter == 0:
                return money * 10
            elif  iter == 1:
                return money * 2
            elif iter == 2: 
                return money
            else:
                return 'Nothing'
#print(prize(value_sort(rand_num(choices)), value_user(rand_num(choices), 'a'), 100))   
    
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
def display(arr, tot, user, money):
    print(f"Total votes: {math.floor(tot / 2)}\n")
    for k, v in arr.items():
        for v_dis in v.values():
            x = v_dis
            x = float(x)
            graphic = ' ' * math.floor(x) 
        print (f"Element {k} : {x} %".ljust(20)+f"{BG_WHITE}{graphic}{OFF}\n")
    print(f"User choice: {user}")
    print('-' * 50)
    print(f"You have earned: {money}")
    print('-' * 50)
        
def main(arr):
    flag = False
    user_inp = ''
    while flag is False:
        counter = 1
        for k in arr.keys():
            print(f"Element: {k}")
        bet = input("Enter money to bet: £ ")
        print('-' * 50)
        user_inp = input("Enter your element or 'q' to quit: ") 
        print('-' * 50)
        if bet.isnumeric():
            bet = int(bet)
            for k in arr.keys():
                if user_inp == 'q':
                    if total_inp(arr) == 0:
                        print('END')
                        flag = True
                        break 
                    print('\n')
                    print('LAST:')
                    print('\n')
                    display(arr, total, user_inp, 0)
                    print('END')
                    flag = True
                    break  
            
                if user_inp != k and counter == len(arr):
                    msg = f"{FG_RED}Please, enter valid input!{OFF}" 
                    print(msg)
                    print('-'* 50)
                    
                if user_inp == k:
                    
                    for k,v in arr.items():
                        for kn, vn in v.items():
                            if kn == 'n':
                                vn = random.randint(0,1000)
                                v.update({kn : vn})
                                
                    #arr_n_mod = user_sele(arr, user_inp)
                    total = total_inp(arr)
                    percent = update_per(arr, total)
                    money = prize(value_sort(arr), value_user(arr, user_inp), bet)
                    display(percent, total, user_inp, money)
                    
                    break
                counter += 1
        else:
            print(f"{FG_RED}Digit a number to enter money!{OFF}")
            print('-'* 50)
main(choices)