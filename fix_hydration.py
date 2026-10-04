import glob

html_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.html', recursive=True)

script_payload = """
<script>
// Force fix for React Hydration overriding text and styles
setInterval(function() {
    const descs = {
        'Hygiene': 'Premium hygiene solutions and housekeeping supplies<br/>designed to keep your workspace pristine and safe.',
        'One Time Setup': 'High-end corporate electronics, office automation,<br/>and long-term capex solutions for your business.',
        'Stationery': 'Top-quality stationery, pens, organizers, and<br/>essential office supplies for everyday productivity.',
        'MRO': 'Industrial-grade tools, machinery parts, and MRO<br/>supplies to ensure seamless operational continuity.',
        'Gifting': 'Luxurious, thoughtful corporate gifting options<br/>and premium rewards to appreciate your clients.',
        'Packaging': 'Durable and cost-effective packaging materials<br/>including corrugated boxes, tapes, and bubble wrap.'
    };
    
    document.querySelectorAll('h1').forEach(h1 => {
        for (const [key, desc] of Object.entries(descs)) {
            if (h1.innerText.includes(key)) {
                let p = h1.parentElement.nextElementSibling ? h1.parentElement.nextElementSibling.querySelector('p.text-sm') : null;
                if (p && !p.innerHTML.includes(desc)) {
                    p.innerHTML = desc;
                }
            }
        }
    });

    document.querySelectorAll('img').forEach(img => {
        if (img.src.includes('images/shop/')) {
            img.style.setProperty('height', '16rem', 'important');
            img.style.setProperty('object-fit', 'cover', 'important');
            img.style.setProperty('width', '100%', 'important');
            img.classList.remove('h-full');
        }
    });
}, 300);
</script>
"""

for file in html_files:
    if 'shop' in file or 'index' in file:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '// Force fix for React Hydration' not in content:
            content = content.replace('</body>', script_payload + '</body>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Injected hydration fix into", file)

print("Hydration fix applied.")
