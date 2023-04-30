''' OTP Generator:
One-time Passwords (OTP) is a password that is valid for only one login session or
transaction in a computer or a digital device. Now a days OTP’s are used in almost every service like
Internet Banking, online transactions, etc. They are generally combination of 4 or 6 numeric digits or
a 6-digit alphanumeric. '''
import random
n=int(input("Enter the number of digits of OTP:"))
res=random.random()
otp=str(res)
otp=otp[2:n+2]
print("Your OTP: ",otp)
