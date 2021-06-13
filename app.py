from model import w_page, check, choice
from view import username, userpwd, show_list, choose_opt

w_page()
u_name = username()
pwd = userpwd()
r_bool = check(u_name,pwd) # phone???? 
if r_bool:
    show_list()
    opt = choose_opt(u_name)
    choice(opt, u_name)
else:
    pass            
