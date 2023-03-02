
import os 
import time

def banner():
     print("""
     :'######:::'#######::'########::'########::::::::::'####:'########:
     '##... ##:'##.... ##: ##.... ##:... ##..:::::::::::. ##::... ##..::
     :##:::..:: ##:::: ##: ##:::: ##:::: ##:::::::::::::: ##::::: ##::::
     . ######:: ##:::: ##: ########::::: ##::::'#######:: ##::::: ##::::
     :..... ##: ##:::: ##: ##.. ##:::::: ##::::........:: ##::::: ##::::
     '##::: ##: ##:::: ##: ##::. ##::::: ##:::::::::::::: ##::::: ##::::
     . ######::. #######:: ##:::. ##:::: ##:::::::::::::'####:::: ##::::
     :......::::.......:::..:::::..:::::..::::::::::::::....:::::..:::::
     """)

ls = os.listdir()

if "puthere" in ls:
    print("puthere folder is already there")
else :
    os.mkdir("puthere")
    print("puthere folder is ready now .")

banner()

print("press ctrl + c to exit ....")
print("now running ...")

i = 0

while True:
    item = os.listdir("./puthere")
    if len(item) > 0:
        for i in range(len(item)):
            x,e = item[i].split(".")
            ls = os.listdir()
            if e in ls:
                os.system("move .\\puthere\\"+x+"."+e+" .\\"+e+"\\")
            else :
                os.mkdir(e)
                os.system("move .\\puthere\\"+x+"."+e+" .\\"+e+"\\")
                      
    else :
        time.sleep(3)