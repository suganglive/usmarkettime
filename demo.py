a = 1
date = 13
int(input("what date to day? you can answer YYMMDD format ex) 220102"))
if a:
    print("Yes, US stock market open to day.")
    if date > 3 or date < 11:
        print("And the open time is 22:30 ~ 05:00")
    else:
        print("And the open time is 23:30 ~ 06:00")
else:
    print("No They closed The next market time is")
