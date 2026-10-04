import glob
import re
import shutil

html_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.html', recursive=True)

# First, fix the images by duplicating the good ones over the bad ones
img_dir = r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\images\shop'
try:
    shutil.copy(img_dir + r'\hygiene.jpg', img_dir + r'\stationery.jpg')
    shutil.copy(img_dir + r'\electronics.jpg', img_dir + r'\mro.jpg')
    shutil.copy(img_dir + r'\packaging.jpg', img_dir + r'\gifting.jpg')
except Exception as e:
    print("Error copying images:", e)

# Now, update the HTML to fix the height and add descriptions
descriptions = {
    'Hygiene, Housekeeping &amp; Healthcare': 'Premium hygiene solutions and housekeeping supplies<br/>designed to keep your workspace pristine and safe.',
    'Hygiene, Housekeeping & Healthcare': 'Premium hygiene solutions and housekeeping supplies<br/>designed to keep your workspace pristine and safe.',
    'One Time Setup, Capex &amp; Electronics': 'High-end corporate electronics, office automation,<br/>and long-term capex solutions for your business.',
    'One Time Setup, Capex & Electronics': 'High-end corporate electronics, office automation,<br/>and long-term capex solutions for your business.',
    'Stationery &amp; Office Supplies': 'Top-quality stationery, pens, organizers, and<br/>essential office supplies for everyday productivity.',
    'Stationery & Office Supplies': 'Top-quality stationery, pens, organizers, and<br/>essential office supplies for everyday productivity.',
    'MRO': 'Industrial-grade tools, machinery parts, and MRO<br/>supplies to ensure seamless operational continuity.',
    'Gifting': 'Luxurious, thoughtful corporate gifting options<br/>and premium rewards to appreciate your clients.',
    'Packaging': 'Durable and cost-effective packaging materials<br/>including corrugated boxes, tapes, and bubble wrap.'
}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix image height (border box fix)
    # Replace class="h-full w-full object-cover object-center" with class="h-64 w-full object-cover object-center"
    content = re.sub(r'class="h-full w-full object-cover object-center"', r'class="h-64 w-full object-cover object-center"', content)
    
    # Inject descriptions
    # The structure is: <h1 class="text-2xl font-extrabold text-gray-900">TITLE</h1></div><div class="space-y-6 pt-4"><p class="text-sm"></p>
    for title, desc in descriptions.items():
        pattern = r'(<h1[^>]*>\s*' + re.escape(title) + r'\s*</h1>\s*</div>\s*<div[^>]*>\s*<p class="text-sm">)\s*(</p>)'
        content = re.sub(pattern, r'\g<1>' + desc + r'\g<2>', content)
        
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated HTML in", file)

print("HTML Fixes complete.")
