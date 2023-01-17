from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter
import sys
import re
import random
import requests, threading, os
import os.path
import threading
import json
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init, Style
init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')
print("""

╭━━━╮╱╱╱╱╭━━┳━━━╮
┃╭━╮┃╱╱╱╱╰┫┣┫╭━╮┃
┃╰━╯┣━━┳╮╭┫┃┃╰━╯┃
┃╭╮╭┫┃━┫╰╯┃┃┃╭━━╯
┃┃┃╰┫┃━╋╮╭┫┣┫┃Coded By Tegal1337
╰╯╰━┻━━╯╰┻━━┻╯
Reverse IP And Subdomain Scanner
1.Reverse
""")
select = input("senpai@tegalsec:~# ")
s = requests.Session()
ua = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' #user gent
	}

names = []

if select == "1":
        def cut(text='',leng=False):
            if leng == False:
                ret = text
            else:
                length_string = len(text)
                if length_string > leng:
                    ret = text[0:leng]
                else:
                  neko = leng-length_string
                  ret = text+' '*neko
            return str(ret)

        def revip(target):
            try:
             response = s.get("https://rapiddns.io/sameip/" + target + "?full=1#result", headers=ua).content.decode("utf-8")
             pattern = r"</th>\n<td>(.*?)</td>"
             results = re.findall(pattern, response)
             print ("[+] {} => {} Domains".format(cut(str(target) ,15), len(results)))
             for line in results:
				             line = line.strip()  #delete ' '			             
				             if line not in names:
					              names.append(line)
					              with open('reversed.txt', 'a+') as f:
						               f.write('http://'+ line + "\n") #write output
            except:
                pass
        print ("{}Reverse IP".format(Fore.RED))
        print("===============================")
        os.system('dir' if os.name == 'nt' else 'ls')
        target = open(input(Fore.WHITE+'List:~# '),'r').read().replace('http://', '').replace('https://', '').splitlines()
        Thread = input(Fore.WHITE+'Thread:~# ')
        pool = ThreadPool(int(Thread))
        pool.map(revip, target)
        pool.close()
        pool.join()
        print("===============================")
        count_result = len(open("reversed.txt").readlines())
        print(((("[ + ] Total Result : "+str(count_result))(count_result))))