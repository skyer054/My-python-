
try:
    print(x)
except NameError:
    print("something went wrong x is not defined")
else:
    print("something is wrong")

finally :
    print("the 'try except' is done")
    
x = -1

if x < 0 :
    raise Exception ("Below zero")
