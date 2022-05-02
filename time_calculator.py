

def abs(n):
    if n > 0:
        return n
    else:
        return -(n)   
def add_zero(n):
    if n == 0:
        return f"{n}0" 
    else:
        return n            

def add_time(start, duration, day = ""):
    time = start.split(' ')
    time1 = time[0].split(':')
    moment = time[1]

    hour1 = int(time1[0])
    minute1 = int(time1[1])
    moment = time[1]
    time2 = duration.split(':')
    hour2 = int(time2[0])
    minute2 = int(time2[1])

    days = ['Monday', 'Tuesday', 'Wednesday','Thusday','Friday','Saturday','Sunday']

    hour = hour1 + hour2
    minute = minute1 + minute2
    if minute >= 60:
        minute = add_zero(abs(minute1 - minute2))
        hour += 1
    if moment == 'AM':
        if hour > 12:
            moment = 'PM'
            hour = abs(hour - 12)
    if moment == 'PM':
        if hour > 12:
            moment = 'AM' 
            hour = abs(hour - 12) 
            for day in days:
                if day == days[day]:
                    return days[day + 1]        
    print(f'{add_zero(hour)}:{minute} {moment}')
    if day != None:
        print("{day}") 

add_time('9:30 PM', '1:45', 'Tuesday')