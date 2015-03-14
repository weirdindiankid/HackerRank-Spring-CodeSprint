hours = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

minutes = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

H = input()
M = input()
h = int(H)
m = int(M)

if m <= 30:
    if m == 0:
        print(hours[h] + " o' clock")
    elif m == 30:
        print("half past " + hours[h])
    elif m == 1:
        print("one minute past " + hours[h])
    elif m == 15:
        print("quarter past " + hours[h])
    else:
        print(minutes[m] + " minutes past " + hours[h])
elif m > 30:
    newM = 60 - m
    if newM == 1:
        print("one minute to " + hours[h+1])
    elif newM == 15:
        print("quarter to " + hours[h+1])
    else:
        print(minutes[newM] + " minutes to " + hours[h+1])

