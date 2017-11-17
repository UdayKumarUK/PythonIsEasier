#How To Determine Even Or Odd
a = 24 
#Old way
print('Normal way of Evaluation:-')
print('-------------------------')
if a%2==0:
    print('Even')
else:
    print('Odd')
    
#Ternary Operator
print('Even' if a%2==0 else 'Odd')     # a= 24 Result Even, a=25 Result Odd

#Bit wise Operator
print("\nBit-wise Evaluation:-")
print('------------------------')
print('Even' if not a&1 else 'Odd')   #Even
a=11
print('Even' if not a&1 else 'Odd')   #Odd

#Why to use bit-wise operator ? 
#   Bit-wise operations are much faster.
