def  Add ( a , b ):
    return a + b

def  Substract ( a , b ):
    return a - b

def  Multiply ( a , b ):
    return a * b

def  Divide ( a , b ):
    if  b != 0:
        return  a/b
    else:
        print ("cannot Divide by zero")
   
def  Modulas (a,b):
    if  a>= 0:
        return a % b
    else:
        return "Cannot  perform modulas with ZERO! "    
       
       
def Power (a,b):
    return a**b


def Square_root(a):
    if  a >= 0:
        import math
        return math.sqrt(a)
       
     
       

print ("Simple Calculator")   # Heading
print ("1. Additiion")        
print ("2. Substract")
print ("3. Multiply")
print ("4. Divide")
print ("5. Modulas")
print ("6. Power")
print ("7. square root")

choice =   input("Enter  your option (1 - 7)  ")


if  choice  ==  7:
    num = float(input("Enter Num: "))
    print ( "Result : " , Square_root(num))
else :
    num1 = float(input("Enter 1st Num: "))
    num2 = float(input("Enter 2nd Num: "))
   
    if  choice == "1":
        print ("result " ,Add (num1 , num2) )
   
    elif choice == "2":
        print ("result" ,  Substract(num1, num2))
       
    elif choice == "3":
        print ("result" ,  Multiply(num1, num2))    
       
    elif choice == "4":
        print ("result" ,  Divide(num1, num2))
       
    elif choice == "5":
        print ("result" ,  Modulas(num1, num2))    
   
    elif choice == "6":
        print ("result" ,  Power  (num1, num2))
   
    else:
        print("INVALID INPUT")