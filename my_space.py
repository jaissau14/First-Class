

## This is the PARENT file where I will be writing the codes and functions
# these functions shall be declared here and can be used somewhere else...



# function to find the email address from the message below : 

def extract_mail_1(message) :
    "Function to extract the email address"
    return [word for word in message.split(" ") if '@' in word]

#message = "Dear User Your complaint have been registered. Kindly connect with us at below email care@company.com or support-online@nitish.com"
#print( extract_mail_1(message) )


# Function to find the factorial of a number
def fact(n) : # n represent the number for which factorial needs to be found
    """Function to return Factorial of a NUMBER
        Ex : Input - 5 , Factorial - 120
    """
    
    finalAnswer = 1

    for i in range(1, n+1) : 
        finalAnswer = finalAnswer * i 
    
    return finalAnswer

#number = int(input("Number : "))
#print( fact(number)     )




# Function to get date time
import datetime
def get_date_time() :
    """Return Current Date and Time in format :
        "%d-%m-%Y %H : %M"
    """

    currentTimeStamp = datetime.datetime.now()
    currenTime = currentTimeStamp.strftime("%d-%m-%Y %H : %M")
    return currenTime

# print( get_date_time() )

# function to find palindrome or not

def palin_check(stringName) :
    stringName = stringName.lower().strip()
    if stringName[ : : 1] == stringName[ : : -1] : return "Its Palindrome"
    else : return "Its NOT Palindrome"


#print(palin_check("maDAM") )
#print(palin_check(" 35753 " ) )
#print(palin_check("zoom") )








