import os

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

# Tailwind orange to Tailwind green (or officenova green)
color_map = {
    # orange-50 : #fff7ed -> green-50 : #f0fdf4
    '#fff7ed': '#f0fdf4',
    '255 247 237': '240 253 244',
    
    # orange-100: #ffedd5 -> green-100: #dcfce7
    '#ffedd5': '#dcfce7',
    '255 237 213': '220 252 231',
    
    # orange-200: #fed7aa -> green-200: #bbf7d0
    '#fed7aa': '#bbf7d0',
    '254 215 170': '187 247 208',
    
    # orange-300: #fdba74 -> green-300: #86efac
    '#fdba74': '#86efac',
    '253 186 116': '134 239 172',
    
    # orange-400: #fb923c -> green-400: #4ade80
    '#fb923c': '#4ade80',
    '251 146 60': '74 222 128',
    
    # orange-500: #f97316 -> green-500: #22c55e (officenova uses #4CAF50, let's use that for primary)
    '#f97316': '#4caf50',
    '249 115 22': '76 175 80',
    
    # orange-600: #ea580c -> green-600: #16a34a (officenova darker #388E3C)
    '#ea580c': '#388e3c',
    '234 88 12': '56 142 60',
    
    # orange-700: #c2410c -> green-700: #15803d
    '#c2410c': '#15803d',
    '194 65 12': '21 128 61',
    
    # Custom specific orange colors observed in HTML
    '#f79b1c': '#4caf50', # Button colors, etc
    'from-orange': 'from-green',
    'to-orange': 'to-green',
    'via-orange': 'via-green',
    'text-orange': 'text-green',
    'bg-orange': 'bg-green',
    'border-orange': 'border-green',
    'ring-orange': 'ring-green',
    'hover:text-orange': 'hover:text-green',
    'hover:bg-orange': 'hover:bg-green'
}

updated_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(('.html', '.css', '.js')):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                
                # If it's HTML or JS, doing string replacements of class names might not apply the styles if CSS is tree-shaken
                # But we also do HEX color replacements which will modify the CSS file directly!
                for old, new in color_map.items():
                    # For hex codes, sometimes they are uppercase in CSS
                    if old.startswith('#'):
                        new_content = new_content.replace(old, new)
                        new_content = new_content.replace(old.upper(), new.upper())
                    else:
                        new_content = new_content.replace(old, new)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files += 1
            except Exception as e:
                pass

print(f"Updated {updated_files} files.")
