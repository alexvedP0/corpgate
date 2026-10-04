import os
import shutil
import urllib.request
import time

dest_dir = r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\images\shop'

to_download = {
    'stationery.jpg': 'https://picsum.photos/seed/stationery/800/600',
    'mro.jpg': 'https://picsum.photos/seed/mro/800/600',
    'gifting.jpg': 'https://picsum.photos/seed/gifting/800/600'
}

for name, url in to_download.items():
    dst = os.path.join(dest_dir, name)
    print(f"Downloading {name}...")
    
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0'
        }
    )
    
    try:
        with urllib.request.urlopen(req) as response, open(dst, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"Downloaded {name} successfully.")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
    time.sleep(1)

print("Image setup complete.")
