import glob

html_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.html', recursive=True)

inline_stripes = """<div class="w-[125%] -rotate-6"><div class="h-12 w-full" style="background-color:#FDBA74;"></div><div class="h-12 w-full" style="background-color:#FB923C;"></div><div class="h-12 w-full" style="background-color:#EA580C;"></div></div>"""
original_stripes = '<div class="w-[125%] -rotate-6"><div class="h-12 w-full bg-blue-300"></div><div class="h-12 w-full bg-blue-400"></div><div class="h-12 w-full bg-black0"></div></div>'

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if inline_stripes in content:
        content = content.replace(inline_stripes, original_stripes)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print("Reverted to class-based stripes in", file)

# NOW append the classes to CSS
css_file = r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\_next\static\css\82db39a5ff6f275f.css'
with open(css_file, 'a', encoding='utf-8') as f:
    f.write("\n/* Fix for slanted stripes */\n.bg-blue-300 { background-color: #FDBA74 !important; }\n.bg-blue-400 { background-color: #FB923C !important; }\n.bg-black0 { background-color: #EA580C !important; }\n")

print("CSS appended.")
