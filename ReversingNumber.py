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

#Other way to Returning reverse of a Number. Below code is applicable only for positive numbers as of now
num_str = str(number)
print(num_str[::-1])
