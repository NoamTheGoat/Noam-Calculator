def factorialOpr(oprnd):
    temp = oprnd
    oprnd-=1
    while(oprnd>0):
        temp*=oprnd
        oprnd-=1
    return temp