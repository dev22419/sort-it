import os 
import time
time.sleep(5)
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
        print("." , end=" ")

    time.sleep(5)