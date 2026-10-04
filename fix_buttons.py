import os
import glob

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

# The old class string used for the buttons
old_class = "rounded-full border border-primary bg-black p-4 text-primary shadow-lg transition-all duration-300 hover:bg-primary hover:text-white"
# And another variation just in case (like p-2 or p-3)
old_class2 = "rounded-full border border-white bg-black p-1 text-primary shadow-lg transition-all duration-300 hover:bg-primary hover:text-white"
old_class3 = "fixed bottom-4 right-4 z-50 rounded-full border border-primary bg-black p-4 text-primary shadow-lg transition-all duration-300 hover:bg-primary hover:text-white"
old_class4 = "rounded-full border border-primary bg-black p-3 text-primary shadow-lg transition-all duration-300 hover:bg-primary hover:text-white"

# The new highly visible golden class
new_class = "rounded-full border-2 border-[#D4AF37] bg-[#D4AF37] p-4 text-black shadow-[0_0_20px_rgba(212,175,55,1)] transition-all duration-300 hover:bg-white hover:text-black hover:border-white font-extrabold"

# For the smaller p-1/p-3 variants
new_class2 = "rounded-full border-2 border-[#D4AF37] bg-[#D4AF37] p-1 text-black shadow-[0_0_20px_rgba(212,175,55,1)] transition-all duration-300 hover:bg-white hover:text-black hover:border-white font-extrabold"
new_class3 = "fixed bottom-4 right-4 z-50 rounded-full border-2 border-[#D4AF37] bg-[#D4AF37] p-4 text-black shadow-[0_0_20px_rgba(212,175,55,1)] transition-all duration-300 hover:bg-white hover:text-black hover:border-white font-extrabold"
new_class4 = "rounded-full border-2 border-[#D4AF37] bg-[#D4AF37] p-3 text-black shadow-[0_0_20px_rgba(212,175,55,1)] transition-all duration-300 hover:bg-white hover:text-black hover:border-white font-extrabold"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        content = content.replace(old_class, new_class)
        content = content.replace(old_class2, new_class2)
        content = content.replace(old_class3, new_class3)
        content = content.replace(old_class4, new_class4)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
    except Exception as e:
        pass

for ext in ('*.html', '*.js'):
    for filepath in glob.glob(os.path.join(directory, '**', ext), recursive=True):
        process_file(filepath)
