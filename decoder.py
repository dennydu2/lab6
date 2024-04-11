def decode(password2):
    tempstr = ""
    for i in password2:
        temp = int(i)-3
        if temp < 0:
            temp = 10-temp
        tempstr+=str(temp)
    return tempstr