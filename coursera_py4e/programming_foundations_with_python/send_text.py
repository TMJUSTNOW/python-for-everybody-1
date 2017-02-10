from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC9adfc435ef29acb099ae332da6c001a1"
auth_token  = "82eafe13b81e86053340f0978e99189e"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hice un programa en la compu para mandarte este mensaje. JF",
    to="+821044821153",    # Replace with your phone number
    from_="+12028497809") # Replace with your Twilio number
print message.sid