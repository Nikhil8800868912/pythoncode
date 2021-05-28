def check_three_digit(x,y,z):
    total= set([x,y,z])
    if len(total)==3:
        return 0
    else:
        return(4-len(total))

print(check_three_digit(1,1,1))
print(check_three_digit(1,2,2))
print(check_three_digit(-1,-2,-3))
print(check_three_digit(-1,-1,-1))


