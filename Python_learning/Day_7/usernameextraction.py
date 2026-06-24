# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh

email=input("enter an email_id:")
position=email.find('@')
username=email[:position]
print("username:",username)
