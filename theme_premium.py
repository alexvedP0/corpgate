import os
import re

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

# Define replacements for inverting the light theme to a dark theme
class_replacements = {
    'bg-white': 'bg-black',
    'bg-gray-50': 'bg-gray-900',
    'bg-gray-100': 'bg-gray-900',
    'bg-gray-200': 'bg-gray-800',
    'bg-gray-300': 'bg-gray-700',
    
    'text-black': 'text-white',
    'text-gray-900': 'text-gray-100',
    'text-gray-800': 'text-gray-200',
    'text-gray-700': 'text-gray-300',
    'text-gray-600': 'text-gray-400',
    
    'border-gray-200': 'border-gray-800',
    'border-gray-300': 'border-gray-700',
    'border-gray-400': 'border-gray-600',
    
    # We replaced orange with green previously. Let's replace 'green' strings with 'yellow' (to represent golden)
    # But wait, it's safer to just replace the hex values in the CSS.
}

# Hex color replacements (Green to Golden)
# We mapped orange to green previously. Now green to golden.
color_replacements = {
    '#f0fdf4': '#fffdf5',
    '#dcfce7': '#fff9e6',
    '#bbf7d0': '#ffecb3',
    '#86efac': '#ffe082',
    '#4ade80': '#ffd54f',
    '#4caf50': '#d4af37', # The main golden color
    '#388e3c': '#b5952f',
    '#15803d': '#8c7324',
    
    # Also uppercase versions
    '#F0FDF4': '#FFFDF5',
    '#DCFCE7': '#FFF9E6',
    '#BBF7D0': '#FFECB3',
    '#86EFAC': '#FFE082',
    '#4ADE80': '#FFD54F',
    '#4CAF50': '#D4AF37',
    '#388E3C': '#B5952F',
    '#15803D': '#8C7324',
}

# We also need to add a generic CSS rule to ensure the body is black if it isn't covered by classes
extra_css = """
<style>
    body { background-color: #000000; color: #ffffff; }
    .bg-white { background-color: #000000 !important; }
    .text-black { color: #ffffff !important; }
    .text-gray-900 { color: #f3f4f6 !important; }
    .text-gray-800 { color: #e5e7eb !important; }
    .text-gray-700 { color: #d1d5db !important; }
    .text-gray-600 { color: #9ca3af !important; }
    .bg-gray-100 { background-color: #111827 !important; }
    .bg-gray-200 { background-color: #1f2937 !important; }
</style>
"""

updated_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(('.html', '.js', '.css')):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                
                # Replace classes in HTML/JS
                if file.endswith(('.html', '.js')):
                    for old, new in class_replacements.items():
                        # Use regex to replace exact words to avoid partial matches
                        # e.g., text-black doesn't replace text-black-500 (though tailwind doesn't have that)
                        new_content = re.sub(r'\b' + old + r'\b', new, new_content)
                        
                    # Inject extra CSS just before </head>
                    if file.endswith('.html'):
                        if '</head>' in new_content and 'body { background-color: #000000;' not in new_content:
                            new_content = new_content.replace('</head>', extra_css + '</head>')
                
                # Replace hex colors in CSS and HTML
                for old, new in color_replacements.items():
                    new_content = new_content.replace(old, new)
                    
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files += 1
            except Exception as e:
                pass

print(f"Updated {updated_files} files.")
