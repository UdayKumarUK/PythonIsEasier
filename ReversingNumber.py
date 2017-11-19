# Reversing a number

# input from user
number=128
print('user Input : ',number)
# variable to store the reversed number
rev_num=0
print('rev_num',rev_num)
while(int(number) > 0):
    rev_num=int(rev_num)*10+int(number)%10
    print('rev_num',rev_num)
    number=int(number)/10
print('Number After reversing : ',rev_num)

#Other way to Returning reverse of a Number.
isNegative= False
if number<0:
    isNegative=True    
    num_str = str(number)[1:]
else:
    num_str=str(number)
print('-'+num_str[::-1] if isNegative else num_str[::-1])
