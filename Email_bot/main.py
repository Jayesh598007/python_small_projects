# email bot-- Automated emails 

# no need to install any package 
# below is preinstalled package 

import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)    # extension(ie;.gmail.com) 
server.starttls()
server.login('your_email@gmail.com', 'email_password')
server.sendmail('your_email@gmail.com',
                'receiver_email@gmail.com', 
                'YOUR *********MESSAGE********* to the RECEIVER')

print("Your e-mail has been sent")  # print msg for successful code running



'''

**********************
For more information pls see the youtube video -- lin given below

https://youtu.be/u2O9bPyHNOE

***********************
'''