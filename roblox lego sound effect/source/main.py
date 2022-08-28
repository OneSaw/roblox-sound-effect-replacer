import glob, wget, os ,time

user = os.getlogin() #Gets your PC's username

###################        
####### URL #######
###################   

url = "https://drive.google.com/u/0/uc?id=1q3eguSw7f1yTMaa0zMEB9IEb_r3dGTOk&export=download" #Download URL
path = glob.glob(f"C:/Users/{user}/AppData/Local/Roblox/Versions/*/content/sounds/ouch.ogg")[0] #Gets ur roblox sound effect
os.remove(path) #Removes sound effect so it can replace with the download so it wouldnt be ouch(1).ogg
time.sleep(1) #waits so it doesnt make ouch(1).ogg

##########################    
######## Download ########
########################## 

wget.download(url , path) #Downloads and puts into path which is ur roblox folder