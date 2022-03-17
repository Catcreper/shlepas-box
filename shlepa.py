s = input("введите номер телефона:  ")
i = len(s)
while i != 11 or s.isnumeric() != True:
    s = input("на что ты жал!? ")
    i = len(s)
print(s[0]+" ("+s[1]+s[2]+s[3]") " "+s[4]+s[5]+s[6]+"-"+s[7]+s[8]+s[9]")
