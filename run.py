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
    print("puthere folder is ready")
else :
    os.mkdir("puthere")
    print("puthere folder is ready")

    
banner()
print("now running ...")
while True:
    item = os.listdir("./puthere")
    # print(item)
    # print(len(item))
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
