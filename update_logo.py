import glob

files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.*', recursive=True)
files = [f for f in files if f.endswith('.html') or f.endswith('.js')]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Increase logo size in HTML strings (Next.js compiled strings)
    # The original class might be 'h-10 block' or similar.
    # Let's replace 'h-10 block' with 'h-16 w-auto block object-contain' specifically for the logo image.
    if 'corpgate-logo.png' in content:
        # Just simple replace
        new_content = content.replace('class="h-10 block"', 'class="h-16 w-auto block object-contain py-1"')
        new_content = new_content.replace('className:"h-10 block"', 'className:"h-16 w-auto block object-contain py-1"')
        new_content = new_content.replace('class="h-10 w-auto"', 'class="h-16 w-auto object-contain"')
        new_content = new_content.replace('className:"h-10 w-auto"', 'className:"h-16 w-auto object-contain"')
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Updated logo in", file)

print("Done updating logo!")
