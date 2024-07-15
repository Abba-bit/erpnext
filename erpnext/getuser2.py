import frappe
from frappe import auth
# SELECT   name  FROM `tabPayment Entry` WHERE paid_to = '18401004 - صندوق تحصيل المكتب / انور عبدالله ابوطالب - م-صعدة' ORDER BY calculation_data DESC LIMIT 20;

@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key": 0,
            "message": "Authentication Error!"
        }
        return

    user = frappe.get_doc('User', frappe.session.user)
    fullname = user.full_name
 
    id_email = user.name
 

     
    if user:
#          

        return {
            "success_key": 1,
            "token": user.api_key,
            "message": "Authentication success",
            "ali": user,
            # "sid": listexport,
          
            "phone": user.phone,
            
           
            "email": user.email,
             
        }
    else:
        return {
            "success_key": 0,
            "token": False,
            "message": "Authentication success",
            "ali": False,
            "sid": False,
            "api_key": False,
            "phone": False,
            "username": False,
            "email": False,
            "companys": False
        }