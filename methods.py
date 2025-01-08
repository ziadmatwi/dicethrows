import random

"""def seconds_to_clock(seconds:int):
    seconds_input:int = seconds
    hours:int = 0
    minutes:int = 0
    if seconds > 60:
        minutes = seconds // 60
        seconds = seconds % 60
    if minutes > 60:
        hours = minutes // 60
        minutes = minutes % 60
    seconds_str = str(seconds)
    minutes_str = str(minutes)
    hours_str = str(hours)
    
    if seconds < 10 or minutes < 10 or hours < 10:
        if seconds < 10:
            seconds_str= "0"+str(seconds)
        if minutes < 10:
            minutes_str= "0"+str(minutes)
        if hours < 10:
            hours_str= "0"+str(hours)
    
    
    finaltext:str = f"{hours_str}:{minutes_str}:{seconds_str}"
    return finaltext

def clock_to_seconds(hours:int,minutes:int,seconds:int):
    seconds = hours*3600+minutes*60+seconds
    finaltext = str(seconds)+"mp"
    return finaltext
"""

def dice_throw(throw):
    throw_list=[]
    sum = 0
    for i in range(throw):
        dice1 = (int(random.random()*6)+1)
        dice2 = (int(random.random()*6)+1)
        sum = dice1 + dice2
        throw_list.append(sum)
    print(throw_list)
    return throw_list

'''def data_stucture(data_list):
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    list8=[]
    list9=[]
    list10=[]
    list11=[]
    list12=[]
    for i in range(data_list):
        if data_list[i] % 2 == 0:
            if data_list[i] > 6:
                if data_list[i] == 8:
                    list8.append(data_list[i])
                elif data_list[i] == 10:
                    list10.append(data_list[i])
                else:
                    list12.append(data_list[i])
            else:
                if data_list[i] == 6:
                    list6.append(data_list[i])
                elif data_list[i] == 4:
                    list4.append(data_list[i])
                else:
                    list2.append(data_list[i])
        else: 
            if data_list[i] > 6:
                if data_list[i] == 7:
                    list7.append(data_list[i])
                elif data_list[i] == 9:
                    list9.append(data_list[i])
                else:
                    list11.append(data_list[i])
            else:
                if data_list[i] == 5:
                    list5.append(data_list[i])
                elif data_list[i] == 3:
                    list3.append(data_list[i])
    for i in range(data_list):'''

def data_structure(data_list):
    for i in range (2,12):
        if data_list.count(i) > 0:
            db = data_list.count(i)
            print(i,"*"*(db//len(data_list)),f"({db} db)")






thrown_list = dice_throw(30)
data_structure(thrown_list)

        
        

