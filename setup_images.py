import os
import shutil
import urllib.request
import time

dest_dir = r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\images\shop'
os.makedirs(dest_dir, exist_ok=True)

# 1. Copy generated images
generated_dir = r'C:\Users\Hp\.gemini\antigravity-ide\brain\7a23c7ba-2a62-44a9-aa69-a2a5c6f46639'
generated = {
    'hygiene.jpg': 'shop_hygiene_1791139882393.jpg',
    'electronics.jpg': 'shop_electronics_1791139921238.jpg',
    'packaging.jpg': 'shop_packaging_1791139898666.jpg'
}

for out_name, in_name in generated.items():
    src = os.path.join(generated_dir, in_name)
    dst = os.path.join(dest_dir, out_name)
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"Copied {in_name} to {out_name}")

# 2. Download missing images using LoremFlickr
to_download = {
    'stationery.jpg': 'https://loremflickr.com/800/600/stationery,office',
    'mro.jpg': 'https://loremflickr.com/800/600/machinery,gear,tools',
    'gifting.jpg': 'https://loremflickr.com/800/600/gift,luxury,box'
}

for name, url in to_download.items():
    dst = os.path.join(dest_dir, name)
    print(f"Downloading {name}...")
    
    # We add a fake User-Agent because some sites block python-urllib
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )
    
    try:
        with urllib.request.urlopen(req) as response, open(dst, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"Downloaded {name} successfully.")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
    time.sleep(1) # Prevent being blocked

print("Image setup complete.")
