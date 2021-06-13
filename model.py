from view import Call_Card, Call_EB,Call_Mobile
import json

user_login = {'name' : 'Yamini', 'password': "Welcome"}

def w_page():
    print()
    print("My Reminder !!!")
    print()   

def check(u_name, pwd):
    if(user_login['name'] == u_name and user_login['password'] == pwd):  
            print() 
            print(f"Welcome {u_name} !!!") 
            print()  
            return True
    else:
        #print(f"{u_name}, {user_dict['name']} ")
        #print(f"name= {user_dict[u_name]}, uname = {u_name} Invalid UserName or Password. Try Again !!!")
        print("Invalid UserName or Password. Try Again !!!")
        return False

def update_json_file(user, cc_bank_name=None, cc_card_no=None, cc_due_dt=None, cc_freq=None,  eb_serv_no = None,eb_due_dt=None, eb_freq=None, mob_number=None, mob_due_dt=None, mob_freq=None):

    with open('user_json.json', 'r') as json_file:
        user_list = json.load(json_file)
    
    #print(user_list)
#     user_list
    
    user_dict = {"Name" : user, 'CreditCard': [], "EB":[], "Mobile": []}
    #user_dict = {'CreditCard': [], "EB":[], "Mobile": []}

    # Creating Credit Card data for Json
    cc_dict = {}
    cc_dict['bank_name'] = cc_bank_name
    cc_dict['card_no'] = cc_card_no
    cc_dict['due_dt'] = cc_due_dt
    cc_dict['freq'] = cc_freq
    user_dict['CreditCard'].append(cc_dict)

    # Creating EB data for Json
    eb_dict = {}
    eb_dict['serv_no'] = eb_serv_no
    eb_dict['due_dt'] = eb_due_dt
    eb_dict['freq'] = eb_freq
    user_dict['EB'].append(eb_dict)
            
    # Creating Mobile data for Json 
    mob_dict = {}
    mob_dict['number'] = mob_number
    mob_dict['due_dt'] = mob_due_dt
    mob_dict['freq'] = mob_freq
    user_dict['Mobile'].append(mob_dict)    
        
    user_list.append(user_dict)
    
    with open("user_json.json", "w") as outfile: 
        json.dump(user_list, outfile)

def choice(opt, u_name):
    if opt == 1:
        cc_bank_name, cc_card_no, cc_due_dt, cc_freq = Call_Card(u_name)
        update_json_file(u_name, cc_bank_name, cc_card_no, cc_due_dt, cc_freq,None,None,None,None,None,None)
               
    elif opt == 3:
        eb_serv_no, eb_due_dt, eb_freq = Call_EB(u_name)
        update_json_file(u_name, None, None,None,None, eb_serv_no,eb_due_dt, eb_freq,None,None,None)
        
    elif opt == 2 :
        mob_number, mob_due_dt, mob_freq  = Call_Mobile(u_name)
        update_json_file(u_name, None, None,None,None,None,None, None,mob_number, mob_due_dt, mob_freq)
        #(user, cc_bank_name, cc_card_no, cc_due_dt, cc_freq, eb_due_dt, eb_freq, mob_number, mob_due_dt, mob_freq)
   # elif opt == 4 :
    #    with open('user_cc_json.json', 'r') as json_file:
     #   user_list = json.load(json_file)
      #  print(user_list)            

    else:
        print("Invalid option!! Please choose from the Option List available !!")     


                   



         
