#from model import user_dict
from datetime import datetime, timedelta
import json
from twilio.rest import Client
from TwilioCred import account_sid, auth_token, from_phone, to_phone

client = Client(account_sid, auth_token)

with open('user_json.json', 'r') as json_file:
        user_list = json.load(json_file)

# Fetch date based on frequency for bill payment Reminder
def date_freq(due_dt, freq):
        util_dt = due_dt
        util_due_dt = datetime.strptime(util_dt, "%Y-%m-%d")     # convert string to time
        new_date = util_due_dt + timedelta(days = freq)
        now_dt = (new_date.strftime("%Y-%m-%d"))         # convert time to string
        return now_dt

def send_SMS(msg, from_phone, to_phone):
    message = client.messages .create(
       body = msg,
       from_ = from_phone,
       to = to_phone
    )
    return message

# Current Date
now = datetime.now()
new_now = (now.strftime("%Y-%m-%d"))
#print(new_now)  

# Reminder for Credit Card
for user in user_list:
    #print(user['Name'])
    for bank in user['CreditCard']:
        if bank['bank_name'] != None and bank['card_no'] != None and bank['due_dt'] != None and bank['freq'] != None:
            #print(bank['bank_name'], bank['card_no'], bank['due_dt'], bank['freq'] )
            now_dt = date_freq(bank['due_dt'], bank['freq']) # get the due date based on freq
            #print(f"CC due date is {now_dt}")

            # Reminder SMS for Credit Card Payment
            if new_now == now_dt:       # Current date ad due date are the same
                msg = f"Credit Card Payment for card no. {bank['card_no']} is due by {now_dt}"
                print(msg)
                message = send_SMS(msg, from_phone, to_phone)
                #print("Hello")
                print(message.sid) 
                
                bank['due_dt']= now_dt      # Update the credit card due_dt for the next cycle

# Reminder for Electricity Bill
for user in user_list:
    #print(user['Name'])
    for eb in user['EB']:
        if eb['serv_no'] !=None and eb['due_dt'] != None and eb['freq'] != None:
            #print( eb['due_dt'], eb['freq'] )
            now_dt = date_freq(eb['due_dt'], eb['freq']) # get the due date based on freq

            # Reminder SMS for Electricity Bill Payment
            if new_now == now_dt:       # Current date ad due date are the same
                msg = f"Electricity Bill Payment for {'serv_no'} is due by {now_dt}"
                print(msg)
                message = send_SMS(msg, from_phone, to_phone)
                #print("Hello")
                print(message.sid) 
                
                eb['due_dt']= now_dt      # Update the electricity bill due_dt for the next cycle            

# Reminder for Mobile Bill
for user in user_list:
   # print(user['Name'])
    for mob in user['Mobile']:
        if mob['number'] != None and mob['due_dt'] != None and mob['freq'] != None:
            #print(mob['number'], mob['due_dt'], mob['freq'] )
            now_dt = date_freq(mob['due_dt'], mob['freq']) # get the due date based on freq

            # Reminder SMS for Mobile Bill Payment
            if new_now == now_dt:       # Current date ad due date are the same
                msg = f"Mobile Bill Payment  for {mob['number']} is due by {now_dt}"
                print(msg)
                message = send_SMS(msg, from_phone, to_phone)
                #print("Hello")
                print(message.sid) 
                        
                mob['due_dt']= now_dt      # Update the Mobile due_dt for the next cycle                

with open("user_json.json", "w") as outfile: 
    json.dump(user_list, outfile)