import os
import re

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

new_style_block = """<style id="premium-theme">
    body { background-color: #0f0f0f; color: #e5e7eb; }
    
    /* Backgrounds */
    .bg-black { background-color: #000000 !important; }
    .bg-white { background-color: #0f0f0f !important; }
    .bg-gray-50, .bg-gray-100 { background-color: #141414 !important; }
    .bg-gray-200, .bg-gray-300 { background-color: #1f1f1f !important; }
    
    /* Text Colors */
    .text-black { color: #ffffff !important; }
    .text-white { color: #ffffff !important; }
    .text-gray-900, .text-gray-800 { color: #f3f4f6 !important; }
    .text-gray-700, .text-gray-600 { color: #d1d5db !important; }
    .text-gray-500, .text-gray-400 { color: #9ca3af !important; }
    
    /* Handle the hardcoded dark text on cards */
    .text-\[\#1F2937\] { color: #f3f4f6 !important; }
    
    /* Golden Accents */
    .text-green-500, .text-green-600, .hover\:text-green-500:hover { color: #D4AF37 !important; }
    .bg-black0, .bg-green-600, .hover\:bg-black0:hover { background-color: #D4AF37 !important; color: #000000 !important; }
    .bg-green-100, .bg-green-200, .bg-green-50 { background-color: #1a150b !important; }
    .border-green-500 { border-color: #D4AF37 !important; }
    
    /* Golden Gradients override */
    .from-green-500 { --tw-gradient-from: #D4AF37 !important; --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(212, 175, 55, 0)) !important; }
    .to-green-300 { --tw-gradient-to: #ffd700 !important; }
    .from-green-400 { --tw-gradient-from: #ffd700 !important; --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(255, 215, 0, 0)) !important; }
    .to-green-600 { --tw-gradient-to: #b5952f !important; }
    
    /* Fix buttons and interactive elements */
    .corpgate-button { background-color: #D4AF37 !important; color: #000000 !important; font-weight: bold; border: 1px solid #D4AF37; }
    .corpgate-button:hover { background-color: #b5952f !important; border-color: #b5952f !important; }
    
    /* Cards / Borders */
    .border-gray-200, .border-gray-300 { border-color: #333333 !important; }
    .shadow-lg, .shadow-2xl { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.3) !important; }
</style>"""

updated = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Use regex to find and replace the style block
                pattern = re.compile(r'<style id="premium-theme">.*?</style>', re.DOTALL)
                new_content = re.sub(pattern, new_style_block, content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated += 1
            except Exception as e:
                pass

print(f"Updated style block in {updated} HTML files.")
