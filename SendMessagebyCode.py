#pip install pywhatkit #library

#load module
import pywhatkit

mobiles = [
    "+919399751398",
    "+927788776655",
    "+931234567856",
    "+959876543477",
]

for mobile in mobiles:
    if mobile.startswith("+91"):
        pywhatkit.sendwhatmsg(mobile, "hello this message is send by python code", 19, 27)
    
