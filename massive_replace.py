import os
import re

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

# Replacements (case-sensitive to preserve casing if possible, but let's do a smart replace)
def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        
        # Replace specific known cases first
        new_content = new_content.replace('Procura Business', 'CORPGATE')
        new_content = new_content.replace('Procura connect', 'CORPGATE Connect')
        new_content = new_content.replace('Procura Insights', 'CORPGATE Insights')
        new_content = new_content.replace('Procura Enterprise', 'CORPGATE Enterprise')
        
        # Replace Procura (Title case)
        new_content = new_content.replace('Procura', 'Corpgate')
        
        # Replace PROCURA (UPPERCASE)
        new_content = new_content.replace('PROCURA', 'CORPGATE')
        
        # Replace procura (lowercase)
        new_content = new_content.replace('procura', 'corpgate')
        
        # The script above also replaced some phone numbers and addresses
        new_content = new_content.replace('+91 99205 57157', '')
        new_content = new_content.replace('+91 97698 68448', '')
        
        # Specifically update logo paths if any are missed
        new_content = new_content.replace('brand-logo.svg', 'corpgate-logo.png')
        new_content = new_content.replace('images/brand-logo.png', 'images/corpgate-logo.png')
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    except Exception as e:
        pass
    return False

updated_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(('.html', '.js', '.json', '.css', '.txt')):
            file_path = os.path.join(root, file)
            if replace_in_file(file_path):
                updated_files += 1

print(f"Updated {updated_files} files.")
