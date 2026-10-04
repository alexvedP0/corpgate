import glob
import re

html_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.html', recursive=True)

# The pattern is the slanted stripes div
pattern = re.compile(
    r'<div class="w-\[125\%\] -rotate-6.*?</div></div>',
    re.DOTALL
)

# New stripes using orange tailwind colors that match the screenshot
new_stripes = """<div class="w-[125%] -rotate-6"><div class="h-12 w-full bg-orange-300"></div><div class="h-12 w-full bg-orange-400"></div><div class="h-12 w-full bg-orange-500"></div></div>"""

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'w-[125%] -rotate-6' in content:
        # We need to be careful. The original string is:
        # <div class="w-[125%] -rotate-6"><div class="h-12 w-full bg-blue-300"></div><div class="h-12 w-full bg-blue-400"></div><div class="h-12 w-full bg-black0"></div></div>
        
        # Simple replace for the exact string
        old_exact = '<div class="w-[125%] -rotate-6"><div class="h-12 w-full bg-blue-300"></div><div class="h-12 w-full bg-blue-400"></div><div class="h-12 w-full bg-black0"></div></div>'
        if old_exact in content:
            new_content = content.replace(old_exact, new_stripes)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print("Updated stripes in", file)

print("Updated", count, "files.")
