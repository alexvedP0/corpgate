import urllib.request
import re
from collections import Counter

url = 'https://officenova.in/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"', html)
    print('Found CSS:', css_links)
    
    colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}', html)
    if colors:
        print('Most common hex colors in HTML:', Counter(colors).most_common(10))
        
    for css in css_links:
        if not css.startswith('http'):
            css_url = url.rstrip('/') + '/' + css.lstrip('/')
        else:
            css_url = css
        print('\nFetching', css_url)
        try:
            css_content = urllib.request.urlopen(urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
            css_colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}', css_content)
            if css_colors:
                print('Most common hex colors in', css, ':', Counter(css_colors).most_common(10))
        except Exception as e:
            print("Failed to fetch", css_url, e)
            
except Exception as e:
    print(e)
