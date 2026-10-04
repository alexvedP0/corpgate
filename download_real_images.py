import re
import urllib.request
import urllib.parse
import json
import os
import time

def download_ddg_image(query, filename):
    url = 'https://duckduckgo.com/?q=' + urllib.parse.quote(query) + '&t=h_&iar=images&iax=images&ia=images'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Extract vqd token
        vqd_match = re.search(r'vqd=([\d-]+)', html)
        if not vqd_match:
            print(f"No vqd found for {query}")
            return False
            
        vqd = vqd_match.group(1)
        
        # Request images
        search_url = f"https://duckduckgo.com/i.js?q={urllib.parse.quote(query)}&o=json&vqd={vqd}"
        req2 = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        data = json.loads(urllib.request.urlopen(req2).read().decode('utf-8'))
        
        if 'results' in data and len(data['results']) > 0:
            img_url = data['results'][0]['image']
            print(f"Found image for {query}: {img_url}")
            
            # Download image
            req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_img) as response, open(filename, 'wb') as out_file:
                out_file.write(response.read())
            return True
    except Exception as e:
        print(f"Error for {query}: {e}")
    return False

dest_dir = r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\images\shop'

queries = {
    'stationery.jpg': 'premium corporate office stationery supplies desk',
    'mro.jpg': 'industrial MRO maintenance repair tools gears equipment',
    'gifting.jpg': 'luxury corporate gift boxes ribbon premium'
}

for name, query in queries.items():
    dst = os.path.join(dest_dir, name)
    print(f"Downloading {name}...")
    success = download_ddg_image(query, dst)
    if not success:
        print(f"Failed to download {name}")
    time.sleep(2)

print("Real Image setup complete.")
