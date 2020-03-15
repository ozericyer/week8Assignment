import re
file = open("regex_sum_259427.txt","r")  #We open file
sum= 0              #We use sum in for loop
for i in file:    #We set for loop
    numbers=re.findall('[0-9]+',i)
    for number in numbers:  #We set for loop for summing
        sum=sum+int(number)
print(sum)  #Finally we print sum







