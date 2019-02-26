#time module
#defines time related functions
import time
print(time.time())  #difference in seconds from Jan 1, 1970 in float
print(time.ctime(),end='\n\n') #current time in readable format

#struct_time format
''' tm_year: Current year
    tm_month: Current month (1-12)
    tm_mday: Current date of month  (1-31)
    tm_hour: Current hour   (0-23)
    tm_min: Current minute  (0-59)
    tm_sec: Current Second  (0-61)
    tm_yday: Current day of year (1-366) 
    tm_wday: Current day of week (0-6, 0 is Monday)
    tm_isdst: DST status (0 for false, 1 for true, -1 for not found)
'''
print(time.gmtime())    #GMT time (also Known as UTC)
print(time.localtime()) #local time
print(time.mktime(time.localtime()))    #converts struct_time format to float representation
print('Current Year:',time.localtime().tm_year)
print('Current Hour:',time.localtime().tm_hour)
print('Current Day:',time.localtime().tm_wday)
print('DST:',time.localtime().tm_isdst)
print(time.strftime('%a %b %d %y',time.gmtime()))   #converts struct_time to string based on format
print(time.strptime('Feb 26 19','%b %d %y'))   #converts string to struct_time based on format