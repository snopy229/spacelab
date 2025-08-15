def if_leap_year(start_date:list)->list:
    if (start_date[0] % 4 == 0 and start_date[0] % 100 != 0) or (start_date[0] % 400 == 0):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def gen(days:int, work_days:int, rest_days: int, start_date:list)->list:
    schedule=[]
    mdays=if_leap_year(start_date)  
    cur_year=start_date[0] 
    cur_month=start_date[1]
    cur_day=start_date[2]
    for day in range(days):
        if cur_day==31 and cur_month==12:
            cur_day=1
            cur_month=1
            schedule.append(f"datetime.datetime({cur_year}, {cur_month}, {cur_day})")
        elif cur_day==mdays[cur_month-1]:    
                    
            schedule.append(f"datetime.datetime({cur_year}, {cur_month}, {cur_day})")
            cur_day=1
            cur_month+=1
        else:
            schedule.append(f"datetime.datetime({cur_year}, {cur_month}, {cur_day})")
            cur_day+=1

    final_schedule = []
    cycle_length = work_days + rest_days
    for i in range(len(schedule)):
        if (i % cycle_length) < work_days:
            final_schedule.append(schedule[i])
            
    return final_schedule





if __name__=="__main__":
   print(gen(5, 2, 1, [2020, 1, 30]))