#myra ribeiro
#2022/11/29
#the purpose of this code is to translate a users desired text into base 33.7

#citations:

#Desingu, K. (2019, September 25). Inter-convert decimal and any base using Python. CodeSpeedy.
#Retrieved from https://www.codespeedy.com/inter-convert-decimal-and-any-base-using-python/

#Python ord(). Programiz. (n.d.). Retrieved November 29, 2022, from https://www.programiz.com/python-programming/methods/built-in/ord

#Nik. (2022, February 23). Python ord and CHR functions: Working with Unicode • datagy. datagy.
#Retrieved November 29, 2022, from https://datagy.io/python-ord-chr/

#How to convert string to binary in Python. Educative. (n.d.).
#Retrieved November 29, 2022, from https://www.educative.io/answers/how-to-convert-string-to-binary-in-python 


#------------------------------------------------------------------------------------------------------------------------------------------#

#hello statement
print("Hello and welcome to my program! The purpose of this code is to translate a users desired text into base 33.7.")

value = input("please enter your text:") #user inputs text

#convert to binary
def binary(value): #initialize function binary (value is the argument)
  list_1 = [] #define list #1
  list_2 = [] #define list #2
  for i in value: #for i in value
    list_1.append(ord(i)) #converts each element in value into unicode, assigns this to the list_1
  for i in list_1: # for i in list_1
    list_2.append(int(bin(i)[2:])) #converts each element in list_1 (the unicode of the elements of value) into binary (base 2) using bin() function, assigns this to list_2
  return list_2 #returns the values of list_2 (which is the inputted text in binary)

x = binary(value) #call the function, input the variable value into it (which holds the text) - title this variable 'x'

print("Binary: ", x) #print the value of x in binary (this is just a way to check that it is being done correctly)

decimal_value = [int(str(i),2) for i in x] #to convert to decimal (base 10), you use the int function. it only works when each element is a string so make i into a string and use a for loop so each element in x is individually analyzed  

print("Decimal:", decimal_value) #print the decimal value (also just a way to confirm its being done correctly)

#when converting from base ten to any other base, you must divide by the base number (33.7 in this case)
#for example, if you have i (represents an element in a list), then you take i and divide it by 33.7 repeatedly until the quotient is equal to zero
#once the quotient is equal to zero you take the remainders and multiply them by 33.7.
#in base 33.7, there are alpha chars and num chars, so you will need to use both.

def desired_base(num,base):  #define function with arguments num(the number you are convering) and base (the base youd like). Max base is 36
    base_num = "" #make base_num type str - make it open and easily changable, empty string.
    while num>0: #while the number entered is greater than zero (use while loop because it will need to repeat)
        dig = int(num%base) #find the remainder of the number entered with the base - this is important
        if dig<10: #if the remainder is less than 10
            base_num = base_num + str(dig) #reassign base_num and be add to dig(which is converted to type str) - this is for the digits below ten that dont have to be converted to alphabetical numbers (0-9)
        else: #when the remainder is greater than 10 - because past 0-9 it becomes alphabetical 
            base_num = base_num + chr(ord('A')+(dig-10))  #Using uppercase letters. you take the unicode number of the value (use ord('A) - the start of the alphabet) and you add it to dig - 10 (subtracting by 10 because dig is over ten and you need it to be alphabetical now). Use chr() to convert the resulting value into alphabetical numbers - the corresponding str value.
        num = num // base #num (inputted number value) is equal to the quotient of the value divided by the base (to convert to base 33.7, you must divide until quotient is 0)

    base_num = base_num[::-1] #reverse the string and reassign it to base_num
    return base_num #reuturn base_num (aka the value of the inputted number in desired base

for i in decimal_value: #use a for loop with list decimal_value (which has been converted to base 10)
    print(desired_base(i, 33.7), end = '') #call the function and put i in the num section so each element is analyzed individually. Enter 33.7 as desired base. end='' is to make it horizontally outputted instead of vertically.

print("  <-- this is your text in base 33.7. Goodbye! Thank you for using my code!") #goodbye statement
