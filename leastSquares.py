from basicFunctions.py import *

#The following statements will ask the user to two vectors x and y
# The user will enter a list of number seperated by comma
# Each element of the eneterd string will be stroed in the form of integer in
# a list x and y
x_value=input("please enter the values of the 1st vector using comma: ")
x_split=x_value.split(",")
x=[]
for i in x_split:
    x.append(int(i))



y_value=input("please enter the values of the 2nd vector using comma: ")
y_split=y_value.split(",")
y=[]
for i in y_split:
    y.append(int(i))


print("The result of thhe vandermode matrix is ",vandermode(x))
print("The result of thhe gram_schmit matrix is ",gram_Schmitt(vandermode(x)))
print("The result of thhe conjugate transpose matrix is ",conjugate_transpose(gram_Schmitt(vandermode(x))))
print("The result of thhe backsubtituion is ",bacsub(conjugate_transpose(gram_Schmitt(vandermode(x)))),y)
print("The result of thhe last part is ",degree4(bacsub(conjugate_transpose(gram_Schmitt(vandermode(x)))),y))


      
