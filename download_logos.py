import os
import urllib.request
from urllib.error import URLError, HTTPError

clients = [
    {"name": "Brookfield", "file": "Brookfield.png", "domain": "brookfield.com"},
    {"name": "CBRE", "file": "CBRE.png", "domain": "cbre.com"},
    {"name": "Colliers", "file": "Colliers.png", "domain": "colliers.com"},
    {"name": "Cushman & Wakefield", "file": "cushman-wakefield.png", "domain": "cushmanwakefield.com"},
    {"name": "Cult Fit", "file": "Cult-Fit.png", "domain": "cult.fit"},
    {"name": "Dream11", "file": "Dream11.png", "domain": "dream11.com"},
    {"name": "DTSS", "file": "DTSS.png", "domain": "dtss.in"},
    {"name": "EFS", "file": "EFS.png", "domain": "efs.com"},
    {"name": "GMR", "file": "GMR.png", "domain": "gmrgroup.in"},
    {"name": "Grihum Housing and Finances", "file": "Grihum.png", "domain": "grihum.com"},
    {"name": "Knight Frank", "file": "Knight-Frank.png", "domain": "knightfrank.com"},
    {"name": "krsnaa diagnostics", "file": "Krsnaa.png", "domain": "krsnaadiagnostics.com"},
    {"name": "PVR", "file": "PVR-Inox.png", "domain": "pvrcinemas.com"},
    {"name": "Reliance", "file": "Reliance-Nippon.png", "domain": "reliancenipponlife.com"},
    {"name": "Sterling and Wilson", "file": "Sterling-and-wilson.jpg", "domain": "sterlingwilson.com"},
    {"name": "Tata", "file": "Tata-digital.png", "domain": "tatadigital.com"},
    {"name": "Walson", "file": "Walsons.png", "domain": "walsons.com"},
    {"name": "yes bank", "file": "Yes-bank.png", "domain": "yesbank.in"}
]

output_dir = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com\images\client-logos"
os.makedirs(output_dir, exist_ok=True)

def download_logo(domain, filename):
    filepath = os.path.join(output_dir, filename)
    # Clearbit API
    url1 = f"https://logo.clearbit.com/{domain}"
    # Icon.horse API (fallback)
    url2 = f"https://icon.horse/icon/{domain}"
    
    req = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            print(f"Downloaded {domain} from Clearbit")
            return True
    except HTTPError as e:
        print(f"Clearbit failed for {domain}: {e.code}")
    except URLError as e:
        print(f"Clearbit failed for {domain}: {e.reason}")
        
    req = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            print(f"Downloaded {domain} from Icon.horse")
            return True
    except Exception as e:
        print(f"Both failed for {domain}: {e}")
        return False

for client in clients:
    download_logo(client["domain"], client["file"])
