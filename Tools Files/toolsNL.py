''' 
isEven takes a single integer paramenter a >= 0 returning True
if a is even then return true otherwise turn false
'''



def isEven(a):

		if a % 2 == 0:
			return True
		return False
	

'''
missing_char will take a letter away from a word in a given position
'''

def missing_char(str, n):
  newStr = "" #create an empty string
  newStr = str[0:n] + str[n + 1: len(str)] #create limit of print
  return newStr

'''
sumDigits takes a single positive integer paramenter and returns the sum of the digits
Parameters: i >= 0
return: returns sum of the digits

precondition: i is a valid integer greater than 0
'''

def sumDigits(a):

    total = 0
    #Casting is the change of type of variable
    a = str(a)

    #Looping through string
    
    #Count, check, change
    for i in range(0, len(a),1):
        print(a[i])
        total = total + int(a[i])

    return total

    #Trace Table:
    #a = "1234"
    # i | i < len(a)|
    # 0 | 0 < 4| T RUN LOOP | total = 0 + a[0] = 1
    # 1 | 1 < 4| T RUN LOOP | total = 1 + a[1] = 3
    # 2 | 2 < 4| T RUN LOOP | total = 3 + a[2] = 6
    # 3 | 3 < 4| T RUN LOOP | total = 6 + a[3] = 10
    # 4 | 4 < 4| F EXIT LOOP

''' Different approach of sumDigits '''
def sumDigitsA(a):

  total = 0

  while (a > 0):
    total = total + a % 10 #access the ones digit
    a = a // 10 #cut down the ones digit from the number

  return total

  #Trace
  # a = 57
  # a | a > 0 |
  # 57| 57 > 0 | TRUE RUN LOOP total = total + 57%10 = 7
  # 5 | 5 > 0 | TRUE RUN LOOP total = total + 5%10 = 12
  # 0 | 0 > 0 | FALSE EXIT LOOP


''' scaleElementsA takes an integer value a and a list reference b. 
This function should scale each elemnt of b'''

def scaleElementA(int, b):
    for i in range(0,len(int)):
        int[i] = int[i]*b #Change value inside the array
        
''' scaleElementsB will create another list with the equal length of the previous
array.

For example if the list is [1,2,3,4] and the scale factor a = 2 then the returned array
should be [2,4,6,8]'''

def scaleElementB(int,b):
    array = []
    for i in range(0,len(int)):
        int[i] = int[i]*b #Calculate new value 
        array.append(int[i]) #Insert value into new array
    return array



'''addStringsSmallLarge will take two strings as arguements.
The function should return a new string consisting of the two strings
combined with the largest string first. If the strings are of equal length it
will return the first argument followed by the second argument'''

def addStringsSmallLarge(string1,string2):
    string = ""#Empty string to combine 2 arguements later
    
    string1 = str(string1)
    string2 = str(string2)

    a = len(string1)
    b = len(string2)

    if a > b or a == b:
        string = string1 + " " + string2
    elif a < b:
        string = string2 + " " + string1

    return string

