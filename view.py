import getpass
#from datetime import datetime 

def username():
    u_name = input("Enter the username: ")
    return u_name

def userpwd():    
    pwd = (getpass.getpass('Enter the password: '))#input("Enter the password: ")
    return pwd

def show_list():
    print("Choose to set the reminder for: ")   
    print()
    print("1.Credit Card Payment")
    print("2.Mobile Bill Payment")
    print("3.Electricity Bill Payment")
    #print("4. Details")    

def choose_opt(u_name):
    print()
    opt = int(input())
    return opt

def Call_Card(u_name):
    print()
    cc_bank_name = input("Enter the Bank Name: ") 
    cc_card_no = int(input("Enter the Card Number: "))
    cc_due_dt = input("Enter the Due Date for Credit Card payment in(yyyy-mm-dd) format: ") 
    #cc_due_dt = datetime.strptime(cc_du_dt, "%Y-%m-%d")
    cc_freq = int(input("Enter the Frequency of the payment: "))
    return (cc_bank_name, cc_card_no, cc_due_dt, cc_freq)

def Call_EB(u_name):
    print()
    eb_serv_no = input("Enter the service number: ")
    eb_due_dt = input("Enter the Due Date for Electricity Bill payment in(yyyy-mm-dd) format: ")
    eb_freq = int(input("Enter the Frequency of the payment: "))
    return eb_serv_no, eb_due_dt,  eb_freq  

def Call_Mobile(u_name):
    print()
    mob_number = int(input("Enter the Mobile Number: ") )
    mob_due_dt = input("Enter the Due Date for Mobile Bill payment in(yyyy-mm-dd) format: ")
    mob_freq = int(input("Enter the Frequency of the payment: ")) 
    return mob_number, mob_due_dt, mob_freq       

#def display(opt1, opt2,result):
 #   print(f"{result},date: {opt1}, amount: {opt2}")    
