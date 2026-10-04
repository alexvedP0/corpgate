import os

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

replacements = {
    # Fix inline RGB backgrounds
    'rgb(255, 255, 255)': 'rgb(15, 15, 15)',
    'rgb(254, 215, 170)': 'rgb(45, 38, 20)',
    'rgb(255, 237, 213)': 'rgb(30, 25, 15)',
    'rgb(253, 186, 116)': 'rgb(60, 50, 25)',
    
    # Fix gradient classes in HTML
    'from-green-100': 'from-black',
    'from-green-200': 'from-black',
    'from-white': 'from-black',
    'via-white': 'via-black',
    'to-white': 'to-black',
    'to-green-100': 'to-black',
    'to-green-200': 'to-black',
    'via-green-100': 'via-black',
    
    # There might be other light background classes
    'bg-green-50': 'bg-black',
    
    # Just to ensure the gradient looks premium, we can change some to a dark gray
    'from-gray-50': 'from-gray-900',
    'to-gray-50': 'to-gray-900',
}

updated_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old, new in replacements.items():
                    new_content = new_content.replace(old, new)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files += 1
            except Exception as e:
                pass

print(f"Updated {updated_files} HTML files.")
