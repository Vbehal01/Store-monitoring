from datetime import datetime, timedelta

def business_hour_string_to_time(time, timezone):
    time = datetime.strptime(time, "%H:%M:%S")

    if(timezone[0]=="-"):
        if(len(timezone)<=2):
            time_1=time + timedelta(hours= int(timezone[1]))
        else:
            data=timezone.split(":")
            time_1=time + timedelta(hours= int(data[0][1]), minutes=int(data[1]))
    else:
        if(len(timezone)<=2):
            time_1=time - timedelta(hours= int(timezone[1]))
        else:
            data=timezone.split(":")
            time_1=time - timedelta(hours= int(data[0][1]), minutes=int(data[1]))
            
    return (time_1.time())

def last_hour_time_interval():
    current_time=datetime.now()
    one_hour_ago=current_time - timedelta(minutes=60)
    time_range={"current_time": current_time, "one_hour_ago": one_hour_ago}
    return time_range

def string_to_time(string_time):
    string_time=datetime.strptime(string_time, "%H:%M:%S")
    return(string_time.time())