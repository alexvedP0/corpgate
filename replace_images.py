import glob
import re

html_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.html', recursive=True)
js_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\_next\static\chunks\pages\*.js')

# Pattern map to local images
replacements = {
    r'([\'"])[^\'"]*storage\.googleapis\.com[^\'"]*catalog-groups/hygiene[^\'"]*([\'"])': r'\1images/shop/hygiene.jpg\2',
    r'([\'"])[^\'"]*storage\.googleapis\.com[^\'"]*catalog-groups/one-time-setup[^\'"]*([\'"])': r'\1images/shop/electronics.jpg\2',
    r'([\'"])[^\'"]*storage\.googleapis\.com[^\'"]*catalog-groups/stationery[^\'"]*([\'"])': r'\1images/shop/stationery.jpg\2',
    r'([\'"])[^\'"]*storage\.googleapis\.com[^\'"]*catalog-groups/mro[^\'"]*([\'"])': r'\1images/shop/mro.jpg\2',
    r'([\'"])[^\'"]*storage\.googleapis\.com[^\'"]*catalog-groups/gifting[^\'"]*([\'"])': r'\1images/shop/gifting.jpg\2',
    r'([\'"])[^\'"]*storage\.googleapis\.com[^\'"]*catalog-groups/packaging[^\'"]*([\'"])': r'\1images/shop/packaging.jpg\2'
}

for file in html_files + js_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for pattern, repl in replacements.items():
        content = re.sub(pattern, repl, content)
    
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated images in", file)

print("Replacement complete.")
