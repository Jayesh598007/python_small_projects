# this program is used to know the location and service provider of the mobile number


# firstly, we need to install below in terminal
import phonenumbers

#import test file which we have created in the same folder
from test import number1 
from test import number2
from test import number3
from test import number4


# to check the country
from phonenumbers import geocoder

ch_number1 =phonenumbers.parse(number1, "CH")
con1= geocoder.description_for_number(ch_number1,"en")

ch_number2 =phonenumbers.parse(number2, "CH")
con2=geocoder.description_for_number(ch_number2,"en")

ch_number3 =phonenumbers.parse(number3, "CH")
con3= geocoder.description_for_number(ch_number3,"en")

ch_number4 =phonenumbers.parse(number4, "CH")
con4= geocoder.description_for_number(ch_number4,"en")



# to check the service provider
from phonenumbers import carrier

ser_number1 =phonenumbers.parse(number1, "RO")
ser1 =carrier.name_for_number(ser_number1,"en")

ser_number2 =phonenumbers.parse(number2, "RO")
ser2 =carrier.name_for_number(ser_number2,"en")

ser_number3 =phonenumbers.parse(number3, "RO")
ser3 =carrier.name_for_number(ser_number3,"en")

ser_number4 =phonenumbers.parse(number4, "RO")
ser4 =carrier.name_for_number(ser_number4,"en")

print("         Country for num1: ", con1)
print("service provider of num1: ", ser1)
print()
print("         Country for num2: ", con2)
print("service provider of num2: ", ser2)
print()
print("         Country for num3: ", con3)
print("service provider of num3: ", ser3)
print()
print("         Country for num4: ", con4)
print("service provider of num4: ", ser4)