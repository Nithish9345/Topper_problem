def topper_num(n):
    a, b, flag = 0, 0, 0
    while(n!=0):
        s = n%10
        if(flag == 0):
            a += s
            flag = 1
        else:
            b+=s
            flag = 0
        n=n//10

    return a==b

print(topper_num(3442))
