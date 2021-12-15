import os
import sys
import datetime

# RUN FROM TERMINAL WITH LINE: python3 main.py name_of_text_file.txt

# OPEN TEXT FILE FROM ARGUMENT AND PARSE VALUES 
with open(sys.argv[1]) as f:
    lines = f.readlines()
    # print(lines) # debug to see if lines were read

    values = []

    i = 0
    for line in lines:
        line.strip() # clean up lines
        # FIRST 4 LINES ARE TICKER, PUT/CALL, OPTION DATE, EXPIRATION DATE. 5TH LINE IS BLANK.
        if i < 5:
            info = line.split(':')
            if i == 0:
                ticker = info[1].strip().upper()
            elif i == 1:
                put_call = info[1].strip().lower()
            elif i == 2:
                optiondate = info[1].strip()
            elif i == 3:
                expdate = info[1].strip()
            elif i == 4:
                print()
        else:
            info = line.split(' ')
            info[2] = info[2].strip('\n')
            values.append(info)
        i += 1

# PRINT PARSED AND CLEANED TEXT FILE INFO
print(ticker, put_call, optiondate, expdate) 

# CALCULATE TOTAL DAYS BETWEEN OPTION DATE AND EXPIRATION DATE
start = optiondate.split('/')
dt1 = datetime.date(int(start[2]), int(start[0]), int(start[1]))
stop = expdate.split('/')
dt2 = datetime.date(int(stop[2]), int(stop[0]), int(stop[1]))
num_days = (dt2 - dt1).days
print("Number of days:", str(num_days))
if num_days % 7 == 0:
    weeks = num_days / 7
else:
    weeks = (num_days // 7) + 1
print("Number of weeks:", weeks)
# ANNUALIZATION CONSTANT
ac = weeks / 52

# CALCULATE EV FOR PUT
if put_call == 'put': 
    values.sort(key=lambda y: y[0])
    for row in range(len(values)):
        print(values[row])
    for row in range(len(values)):
        # print(values[row]) # uncomment to test output
        # print(row) # debug
        if row == 0:
            base_ev = (1 - float(values[0][1])) * float(values[0][2])
            base_ev = round(base_ev, 4)
            return_percent = float(values[row][2])/float(values[row][0])
            return_percent = round(return_percent, 4)
            annualized_return = round(return_percent/ac, 4)
            print(values[row][0], base_ev, return_percent, annualized_return) # uncomment to test output
        else:
            ev_x = ((1 - float(values[row][1])) * float(values[row][2])) \
                 - (float(values[row][1])) * (((float(values[row][0]) - float(values[row][2]))) - (float(values[0][0]) - float(values[0][2])))
            ev_x = round(ev_x, 4)
            return_percent = float(values[row][2])/float(values[row][0])
            return_percent = round(return_percent, 4)
            annualized_return = round(return_percent/ac, 4)
            print(values[row][0], ev_x, return_percent, annualized_return)

# CALCULATE EV FOR CALL
if put_call == 'call':
    values.sort(key=lambda y: y[0], reverse=True)
    for row in range(len(values)):
        print(values[row])
    for row in range(len(values)):
        # print(values[row]) # uncomment to test output
        # print(row) # debug
        if row == 0:
            base_ev = (1 - float(values[0][1])) * float(values[0][2])
            base_ev = round(base_ev, 4)
            return_percent = float(values[row][2])/float(values[row][0])
            return_percent = round(return_percent, 4)
            annualized_return = round(return_percent/ac, 4)
            print(values[row][0], base_ev, return_percent, annualized_return) # uncomment to test output
        else:
            ev_x = ((1 - float(values[row][1])) * float(values[row][2])) \
                 - (float(values[row][1]) * ((float(values[0][0]) + float(values[0][2])) - (float(values[row][0]) + float(values[row][2]))))
            ev_x = round(ev_x, 4)
            return_percent = float(values[row][2])/float(values[row][0])
            return_percent = round(return_percent, 4)
            annualized_return = round(return_percent/ac, 4)
            print(values[row][0], ev_x, return_percent, annualized_return)

