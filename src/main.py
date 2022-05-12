import pywhatkit

# syntax: phone number with country code, message, hour and minutes

phone_number = "+2348035781521"
message = "I am testing whatsapp automation"
hour = 17
minutes = 58

pywhatkit.sendwhatmsg(phone_number, message, hour, minutes)

# .sendwhatmsg_instantly
# .sendwhatmsg_to_group_instantly
# close the tab 2 seconds after sending the message
# import pywhatkit
# pywhatkit.sendwhatmsg(“+1xxxxxxx”, “Message 2”, 18, 55, 15, True, 2)