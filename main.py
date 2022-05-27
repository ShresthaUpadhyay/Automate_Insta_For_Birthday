from automate_insta import AutomateInsta
from reading_excel import ExtractNamesFromExcel
from gettpass import decodeInitials

password_file = open(r"C:\Users\Shrestha\Desktop\Insta.txt",'r')
data = password_file.readlines()
user_name = data[0].strip() 
passw = data[1].strip()

print("..........Getting the Initials..........\n")

USER = decodeInitials(user_name)
PASS = decodeInitials(passw)


e = ExtractNamesFromExcel()
i = AutomateInsta()
i.login_Into_Instagram(USER,PASS)
li = e.getBirthdayNames()

for name in li :
    print(f"sending message to --------------> {name}")
    i.wishBirthday(name)
    print(f"message sent to --------------> {name}")


i.driver.quit()