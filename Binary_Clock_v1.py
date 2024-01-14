## binary clock attempt 1

#import datetime
from datetime import datetime
#from datetime import date

temp = datetime.now().timetuple().tm_hour * 3600
temp = temp + datetime.now().timetuple().tm_min * 60
temp = temp + datetime.now().timetuple().tm_sec

decimal_date = datetime.toordinal(datetime.now()) # days since 01/01/0001
#decimal_time = int(datetime.now().strftime("%H%M%S")) # concatenated string including hour, minute, and second, converted to decimal (not seconds since midnight)
decimal_time = temp # Seconds since midnight :)
decimal_year = datetime.now().timetuple().tm_year
decimal_daynumber = datetime.now().timetuple().tm_yday 
decimal_month = datetime.now().timetuple().tm_mon
decimal_day = datetime.now().timetuple().tm_mday
decimal_hour = datetime.now().timetuple().tm_hour
decimal_minute = datetime.now().timetuple().tm_min
decimal_second = datetime.now().timetuple().tm_sec

binary_date = bin(datetime.toordinal(datetime.now()))[2:] # days since 01/01/0001
#binary_time = bin(int(datetime.now().strftime("%H%M%S")))[2:].zfill(18) # concatenated string including hour, minute, and second, in BCD format
binary_time = bin(temp)[2:].zfill(17)
binary_year = bin(datetime.now().timetuple().tm_year)[2:].zfill(12)
binary_daynumber = bin(datetime.now().timetuple().tm_yday)[2:].zfill(9)
binary_month = bin(datetime.now().timetuple().tm_mon)[2:].zfill(4)
binary_day = bin(datetime.now().timetuple().tm_mday)[2:].zfill(5)
binary_hour = bin(datetime.now().timetuple().tm_hour)[2:].zfill(5)
binary_minute = bin(datetime.now().timetuple().tm_min)[2:].zfill(6)
binary_second = bin(datetime.now().timetuple().tm_sec)[2:].zfill(6)

bcd_date = str(binary_year) + "." + str(binary_month) + "." + str(binary_day)
bcd_time = str(binary_hour) + "." + str(binary_minute) + "." + str(binary_second)

if decimal_hour >= 10:
    decimal_hour_tens = decimal_hour / 10

print("")
print("Decimal:")
print(" Date:       %d" % (decimal_date))
print(" Time:       %d" % (decimal_time))
print(" Year:       %d" % (decimal_year))
print(" Day Number: %d" % (decimal_daynumber))
print(" Month:      %d" % (decimal_month))
print(" Day:        %d" % (decimal_day))
print(" Hour:       %d" % (decimal_hour))
print(" Minute:     %d" % (decimal_minute))
print(" Second:     %d" % (decimal_second))

print("")
print("Binary:")
print(" Date:       %s" % (binary_date))
print(" Time:       %s" % (binary_time))
print(" Year:       %s" % (binary_year))
print(" Day Number: %s" % (binary_daynumber))
print(" Month:      %s" % (binary_month))
print(" Day:        %s" % (binary_day))
print(" Hour:       %s" % (binary_hour))
print(" Minute:     %s" % (binary_minute))
print(" Second:     %s" % (binary_second))

print("")
print("FQ Binary Stardate: %s.%s" % (binary_date, binary_time))
print("FQ BCD Stardate:    %s.%s" % (bcd_date, bcd_time))
print("")