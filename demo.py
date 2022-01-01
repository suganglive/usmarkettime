from datetime import date

a = 1
dat = 13
int(input("what date today? you can answer YYMMDD format ex) 220102"))
if a:
    print("Yes, US stock market open today.")
    if dat > 3 or dat < 11:
        print("And the open time is 22:30 ~ 05:00")
    else:
        print("And the open time is 23:30 ~ 06:00")
else:
    print("No They closed The next market time is")

print(date)