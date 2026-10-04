import os
import re

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

# Premium Dark Theme CSS
premium_css = """
<style id="premium-theme">
    body { background-color: #0f0f0f; color: #e5e7eb; }
    
    /* Backgrounds */
    .bg-black { background-color: #000000 !important; }
    .bg-white { background-color: #0f0f0f !important; }
    .bg-gray-50, .bg-gray-100 { background-color: #1a1a1a !important; }
    .bg-gray-200, .bg-gray-300 { background-color: #262626 !important; }
    
    /* Text Colors */
    .text-black { color: #ffffff !important; }
    .text-white { color: #ffffff !important; }
    .text-gray-900, .text-gray-800 { color: #f3f4f6 !important; }
    .text-gray-700, .text-gray-600 { color: #d1d5db !important; }
    .text-gray-500, .text-gray-400 { color: #9ca3af !important; }
    
    /* Handle the hardcoded dark text on cards */
    .text-\\[\\#1F2937\\] { color: #f3f4f6 !important; }
    
    /* Golden Accents */
    .text-green-500, .text-green-600, .hover\\:text-green-500:hover { color: #D4AF37 !important; }
    .bg-green-500, .bg-green-600, .hover\\:bg-green-500:hover { background-color: #D4AF37 !important; color: #000000 !important; }
    .bg-green-100, .bg-green-200 { background-color: #2d2614 !important; } /* Dark golden tint for light backgrounds */
    .border-green-500 { border-color: #D4AF37 !important; }
    
    /* Fix buttons and interactive elements */
    .corpgate-button { background-color: #D4AF37 !important; color: #000000 !important; font-weight: bold; border: 1px solid #D4AF37; }
    .corpgate-button:hover { background-color: #b5952f !important; border-color: #b5952f !important; }
    
    /* Cards / Borders */
    .border-gray-200, .border-gray-300 { border-color: #333333 !important; }
    .shadow-lg, .shadow-2xl { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.3) !important; }
</style>
"""

# Let's remove the previous `<style>` block and add this one.
old_style_regex = re.compile(r'<style>\s*body \{ background-color: #000000;.*?</style>', re.DOTALL)

updated_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                
                # Remove the old style block
                new_content = old_style_regex.sub('', new_content)
                
                # Also remove any previously injected premium-theme style block just in case
                new_content = re.sub(r'<style id="premium-theme">.*?</style>', '', new_content, flags=re.DOTALL)
                
                # Also fix instances of hardcoded black text strings
                new_content = new_content.replace('text-[#1F2937]', 'text-gray-100')
                new_content = new_content.replace('text-black', 'text-white')
                
                # Inject the new premium style block before </head>
                if '</head>' in new_content:
                    new_content = new_content.replace('</head>', premium_css + '\n</head>')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files += 1
            except Exception as e:
                pass

print(f"Updated {updated_files} HTML files.")
