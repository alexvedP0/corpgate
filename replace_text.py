import os
import re

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

replacements = [
    (r'Procura Business', r'CORPGATE'),
    (r'Procura connect', r'CORPGATE Connect'),
    (r'Procura Insights', r'CORPGATE Insights'),
    (r'Procura Enterprise', r'CORPGATE Enterprise'),
    (r'Procura', r'CORPGATE'),
    (r'procurabusiness\.com', r'corpgate.com'),
    (r'\+91 99205 57157', r'&nbsp;'),
    (r'\+91 97698 68448', r'&nbsp;'),
    (r'1st Floor, Premises CHS 101, Garnet Palladium, <br/>Western Express Hwy, behind EXPRESS ZONE, <br/>opposite Oberoi Mall, Dindoshi, Malad East, <br/>Mumbai, Maharashtra 400097 <br/>', r'&nbsp;'),
    (r'1st Floor, Premises CHS 101, Garnet Palladium, Western Express Hwy, behind EXPRESS ZONE, opposite Oberoi Mall, Dindoshi, Malad East, Mumbai, Maharashtra 400097', r'&nbsp;'),
    (r'images/brand-logo\.svg', r'images/corpgate-logo.png')
]

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(('.html', '.js', '.json')):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old, new in replacements:
                    new_content = re.sub(old, new, new_content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print("Replacement complete.")
