

### Some Random Team Work
# my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
my_str = "Although 8 that way may not be obvious at THE first unless you're Dutch"

res = my_str.split(" ")
print(res)

output = []
for word in res : 
    if word.lower().startswith("t"):
        output.append(word)

print( output )

print()
print()


output = []
for word in res : 
    if word.lower()[0] == "t":
        output.append(word)

print( output )
### Some Random Team Work


## They want to use my_space to perform some activity


## Approach 1 : import packageName
## Approach 1 : import folderName.pyFileName
## Approach 1 : import pyFileName

## Approach 2 : from packageName import ModuleName
## Approach 2 : from pyFileName import ModuleName


## Approach 3 : from packageName import *  # Calling all the modules / functions
## Approach 3 : from pyFileName import *  # Calling all the modules / functions



# function to find the email address from the message below : 
import my_space  # packageName / pyFileName

message = "Dear User Your complaint have been registered. Kindly connect with us at below email care@company.com or support-online@nitish.com"
# print( my_space.extract_mail_1(message) )


print( my_space.get_date_time() )





















