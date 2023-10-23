import requests
import os 
import time , sys
from colorama import Fore,init
import getpass
#MMLIX
init()
os.system("cls")
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
text=(Fore.GREEN+"< < < < < < DEVELOPED BY MMLIX > > > > > \n")
for char in text:
    print(char,end='',flush=True)
    time.sleep(0.1)
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
print(Fore.LIGHTMAGENTA_EX+"    _       _           _       _____ _           _           ")
print(Fore.LIGHTMAGENTA_EX+"   / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ ")
print(Fore.LIGHTMAGENTA_EX+"  / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|")
print(Fore.LIGHTMAGENTA_EX+" / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |  ") 
print(Fore.LIGHTMAGENTA_EX+"/_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_| \n \n ")
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
txt=(Fore.GREEN+"AdminFinder V 1.0 BY MMLIX ! \n")
ac=[]
dc=[]
request_count = 0
for char in txt:
    print(char,end='',flush=True)
    time.sleep(0.1)
print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
passwd=getpass.getpass(Fore.LIGHTWHITE_EX+"Please Enter License To Start Tools > : "+Fore.BLUE)
if passwd=="mmlix11228" or passwd=="MMLIX11228" or passwd=="Mmlix11228" :
    print(Fore.GREEN+"\nLicense Approved! Welcome ")
    print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
    text2=(Fore.LIGHTBLUE_EX+"Enter Target > "+Fore.GREEN+": http://site.Domain"+Fore.LIGHTBLUE_EX+" > : \n")
    for char in text2:
        print(char,end='',flush=True)
        time.sleep(0.1)
    print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
    print(Fore.BLUE+"┌──("+Fore.RED+"root㉿MMLIX"+Fore.BLUE+")-[~]")
    target=(input(Fore.BLUE+"└─"+Fore.RED+"# "+Fore.BLUE))
    print(Fore.LIGHTGREEN_EX+"The tool is finding the admin page . . . ")
    print(Fore.YELLOW+"------------------------------------------------------------------------------------------------------")
    for i in attacklist:
        time.sleep(1)
        http = requests.get(target+i).status_code
        request_count += 1
        if request_count % 10 ==0:
            print(Fore.YELLOW+"|----------------------------------------------------------|")
            print("\n|< < ! WARNING ! > > : The Program STOPED FOR 15 SEC ! > > |")
            # for i in range(1501):
            #     sys.stdout.write(f'\r{i/100:.2f}')
            #     sys.stdout.flush()
            #     time.sleep(0.01)
            print("\n|----------------------------------------------------------|\n")
            time.sleep(15)
        if http == 200:
            print("[Result : "+Fore.GREEN+"< <  Finded  ! > URL >]\t"+Fore.BLUE+target+i+Fore.YELLOW)
            ac.append(f"{target}{i}")
        else:
            print("[Result : "+Fore.RED+"< <  Disable ! > URL >]\t"+Fore.BLUE+target+i+Fore.YELLOW)
            dc.append(f"{target}{i}")

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
    num=int(input(Fore.BLUE+"└─"+Fore.RED+"# "))
    if num == 0:
        print(Fore.LIGHTBLUE_EX+"Finded URL Url : \n"+Fore.LIGHTGREEN_EX+"\n".join(ac))
        
    elif num== 1:
        print(Fore.LIGHTBLUE_EX+"Not Find Url :\n"+Fore.LIGHTRED_EX+"\n".join(dc))
        
    elif num== 2:
        exit()
else:
    print(Fore.RED+"License Invalid ! \n")
