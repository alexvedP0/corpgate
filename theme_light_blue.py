import os
import re

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

# Define replacements for inverting the dark theme back to a light theme
class_replacements = {
    'bg-black': 'bg-white',
    'bg-gray-900': 'bg-gray-50',
    'bg-gray-800': 'bg-gray-100',
    'bg-gray-700': 'bg-gray-200',
    
    'text-white': 'text-black',
    'text-gray-100': 'text-gray-900',
    'text-gray-200': 'text-gray-800',
    'text-gray-300': 'text-gray-700',
    'text-gray-400': 'text-gray-600',
    'text-gray-500': 'text-gray-600',
    
    'border-gray-800': 'border-gray-200',
    'border-gray-700': 'border-gray-300',
    'border-gray-600': 'border-gray-400',
    
    # Colors
    'green-500': 'blue-500',
    'green-400': 'blue-400',
    'green-300': 'blue-300',
    'green-200': 'blue-200',
    'green-100': 'blue-100',
    'bg-indigo-950': 'bg-blue-600',
    'text-green-500': 'text-blue-600',
    'text-green-400': 'text-blue-500',
    
    # Custom hexes
    'bg-[#D4AF37]': 'bg-[#2563EB]',
    'text-[#D4AF37]': 'text-[#2563EB]',
    'border-[#D4AF37]': 'border-[#2563EB]',
    'shadow-[0_0_20px_rgba(212,175,55,1)]': 'shadow-[0_0_20px_rgba(37,99,235,0.6)]',
    
    # About Us dark backgrounds that were hardcoded
    'rgb(15, 15, 15)': 'rgb(249, 250, 251)',
    'rgba(0,0,0,0.75)': 'rgba(255,255,255,0.85)',
    'rgba(0, 0, 0, 0.75)': 'rgba(255, 255, 255, 0.85)',
}

# Hex color replacements (Golden/Dark to Light Blue)
color_replacements = {
    '#D4AF37': '#2563EB',
    '#d4af37': '#2563EB',
    '#000000': '#ffffff',
    '#0f0f0f': '#f9fafb',
    '#141414': '#f3f4f6',
    '#1f1f1f': '#e5e7eb',
    '#ffffff': '#111827', # be careful here, maybe we shouldn't globally swap white to black in CSS...
}

updated_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(('.html', '.js')):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                
                # Remove injected styles
                # Remove <style id="premium-theme">...</style>
                new_content = re.sub(r'<style id="premium-theme">.*?</style>', '', new_content, flags=re.DOTALL)
                
                # Remove the generic extra css block we added
                new_content = re.sub(r'<style>\s*body \{ background-color: #000000;.*?</style>', '', new_content, flags=re.DOTALL)
                
                # Replace classes
                for old, new in class_replacements.items():
                    if 'rgb' in old or 'rgba' in old or '[' in old:
                        new_content = new_content.replace(old, new)
                    else:
                        new_content = re.sub(r'\b' + old + r'\b', new, new_content)
                
                # We won't blindly replace hex codes everywhere to avoid breaking everything.
                # Just replace #D4AF37 to blue
                new_content = new_content.replace('#D4AF37', '#2563EB').replace('#d4af37', '#2563EB')
                new_content = new_content.replace('from-black', 'from-white').replace('via-black', 'via-white').replace('to-black', 'to-gray-100')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files += 1
            except Exception as e:
                pass

print(f"Updated {updated_files} files.")
