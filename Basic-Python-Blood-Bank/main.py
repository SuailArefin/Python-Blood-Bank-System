from admin.adminDashboard import admin_dashboard
from auth.adminLogin import login_as_admin
from auth.userAuth import user_auth
def print_yellow(text):
    return f"\033[93m{text}\033[0m"



while True:
    print("\n\tBlood Bank Menu:")
    print("\t1. Login as Admin")
    print("\t2. Login as User")
    print("\t3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        login_as_admin()
    elif choice == '2':
        user_auth()
    else:
        print(print_yellow("\nInvalid choice. Please enter 1, 2, or 3."))
