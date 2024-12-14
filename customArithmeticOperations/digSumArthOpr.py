def digSumArthOpr(oprnd):
    while not oprnd.is_integer():
        oprnd*=10
    sum=0
    while oprnd>0:
        sum+=int(oprnd%10)
        oprnd/=10
    return sum