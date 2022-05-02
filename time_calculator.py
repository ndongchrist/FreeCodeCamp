def  hour12(hour, moment):
    count = 0
    while hour > 12:
        hour = hour - 12
        if moment == 'PM':
            moment = 'AM'
        else:
            moment = 'PM'
        count += 1    
    return moment, hour, count/2


def day_count(day, days):
    for i in range(len(days)):
        if day == days[i]:
            day = days[i+1] 
            break
        elif i > len(days):
            i = 0    
    return day       


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
    var = hour12(hour, moment)
    day = day_count(day, days)  
    print(f'{add_zero(var[1])}:{minute} {var[0]}')
    if day != None:
        print(f"{day} ({var[2]} day(s) later)") 

add_time("6:30 PM", "205:12")