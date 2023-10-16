import requests
import os 
import time
from colorama import Fore,init
#MMLIX
init()
os.system("cls")
print(Fore.GREEN+" { < Welcome To AdminFinder > From : MMLIX > }  \n ")
attacklist = ['/admin/','/webmail/','/administrator/','/admin1/','/admin3/','/admin4/','/admin5/','/administrator/'
,'/moderator/','/webadmin/','/bb-admin/','/adminarea/','/user/admin/','/admin-login/','/adminlogin/','/admin-panel/','/panel/'
,'/instadmin/','/adm/','/memberadmin/','/administatorlogin/','/admin/account.php','/login.php/','/admin/admin.php/','/admin/index.php/'
,'/admin/account.php/','/admin_area/admin.php/','/siteadmin/login.php/','/admin/index.html/','/admin/login.html/','/admin.php/',
'/admincp/index.asp/','/admincp/login.asp/','/admincp/index.html/','/admin/accountx.html/','/admin/admin_login.html',
'/panel-administracion/login.html/'
,'/cp.php/','/admin-login.php/','/bb-admin/index.html/','/bb-admin/login.html/','/account.php/','/pages/admin/admin-login.html/'
,'/admin/admin-login.html/'
,'/admin-login.html/','/controlpanel.php/','/admin/adminLogin.html/','/home.html/','/adminarea/index.html/','/webadmin.php',
'/webadmin/index.php','/webadmin/admin.php'
,'/admin/controlpanel.html/','/moderator.html/','/administrator/login.html/',
'/user.html/','/administrator/account.html/','/modelsearch/login.html/','/adminarea/login.html/'
,'/panel-administracion/index.html/','/adm/index.html/','/moderator/admin.html/','/user.php/','/wp-login.php/','/adminLogin.php/',
'/home.php/','/admin.php/','/affiliate.php/','/adm_auth.php/','/memberadmin.php/','/administratorlogin.php/']
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.LIGHTMAGENTA_EX+"    _       _           _       _____ _           _           ")
print(Fore.LIGHTMAGENTA_EX+"   / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ ")
print(Fore.LIGHTMAGENTA_EX+"  / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|")
print(Fore.LIGHTMAGENTA_EX+" / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |  ") 
print(Fore.LIGHTMAGENTA_EX+"/_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_| \n \n ")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")

target = input(Fore.LIGHTBLUE_EX+"<<<<----Enter Target @example---->>>>> "+Fore.GREEN+": http://site.Domain"+Fore.LIGHTBLUE_EX+" > : ")
print("The tool is finding the admin page . . . ")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
for i in attacklist:
    http = requests.get(target+i).status_code
    if http == 200:
        Active=print(Fore.BLUE+i+Fore.GREEN+"> > > > > Finded ! < < < < <  ")
    else:
        Disable=print(Fore.BLUE+i+Fore.RED+"> > > > > DISABLE ! < < < < <  ")

os.system("CLS")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.LIGHTMAGENTA_EX+"    _       _           _       _____ _           _           ")
print(Fore.LIGHTMAGENTA_EX+"   / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ ")
print(Fore.LIGHTMAGENTA_EX+"  / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|")
print(Fore.LIGHTMAGENTA_EX+" / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |  ") 
print(Fore.LIGHTMAGENTA_EX+"/_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_| \n \n ")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.RED+"[0]"+Fore.LIGHTGREEN_EX+" - - > Show Finded URLs \n")
print(Fore.RED+"[1]"+Fore.LIGHTGREEN_EX+" - - > Show Disable URLs \n")
print(Fore.RED+"[2]"+Fore.LIGHTGREEN_EX+" - - > Exit \n")
print(Fore.BLUE+"┌──("+Fore.RED+"root㉿MMLIX"+Fore.BLUE+")-[~]")
a=(input(Fore.BLUE+"└─"+Fore.RED+"#"))
if a == 0:
    print("Active Urls's : > \n"+target+Active)
elif a== 1:
    print("Disable Urls's : > \n"+target+Disable)
elif a== 2:
    exit()