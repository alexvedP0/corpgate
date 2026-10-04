import glob
import re

html_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.html', recursive=True)

# We replaced them with orange classes previously, so we need to find those now and replace them with inline styles.
old_exact = '<div class="w-[125%] -rotate-6"><div class="h-12 w-full bg-orange-300"></div><div class="h-12 w-full bg-orange-400"></div><div class="h-12 w-full bg-orange-500"></div></div>'

# Or in case we run it on original
old_exact_2 = '<div class="w-[125%] -rotate-6"><div class="h-12 w-full bg-blue-300"></div><div class="h-12 w-full bg-blue-400"></div><div class="h-12 w-full bg-black0"></div></div>'

new_stripes = """<div class="w-[125%] -rotate-6"><div class="h-12 w-full" style="background-color:#FDBA74;"></div><div class="h-12 w-full" style="background-color:#FB923C;"></div><div class="h-12 w-full" style="background-color:#EA580C;"></div></div>"""

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_exact in content or old_exact_2 in content:
        new_content = content.replace(old_exact, new_stripes).replace(old_exact_2, new_stripes)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print("Updated stripes with inline style in", file)

print("Updated", count, "files.")
