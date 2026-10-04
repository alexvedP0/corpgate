import glob
import re

files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\shop\categories\**\products.html', recursive=True)

gifting_html = """
<div class="grid w-full grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 product-grid-injected">
    <div class="flex flex-col items-center justify-between overflow-hidden rounded-xl border border-gray-200 bg-white p-4 shadow-sm transition-shadow hover:shadow-lg">
        <img src="https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400" alt="Smart Thermos Flask" class="h-48 w-full object-contain" />
        <div class="mt-4 w-full text-left">
            <h3 class="text-sm font-semibold text-gray-800">Smart Thermos Flask with Temperature Display</h3>
            <p class="text-xs text-gray-500 mt-1">Brand: Corpgate Premium</p>
        </div>
        <button class="mt-4 w-full rounded-md bg-[#2563EB] py-2 text-sm font-medium text-white transition-colors hover:bg-blue-700">Add to Cart</button>
    </div>
    <div class="flex flex-col items-center justify-between overflow-hidden rounded-xl border border-gray-200 bg-white p-4 shadow-sm transition-shadow hover:shadow-lg">
        <img src="https://images.unsplash.com/photo-1611891487122-20757827e85c?w=400" alt="CODENAMES Board Game" class="h-48 w-full object-contain" />
        <div class="mt-4 w-full text-left">
            <h3 class="text-sm font-semibold text-gray-800">CODENAMES Corporate Board Game</h3>
            <p class="text-xs text-gray-500 mt-1">Brand: Czech Games</p>
        </div>
        <button class="mt-4 w-full rounded-md bg-[#2563EB] py-2 text-sm font-medium text-white transition-colors hover:bg-blue-700">Add to Cart</button>
    </div>
    <div class="flex flex-col items-center justify-between overflow-hidden rounded-xl border border-gray-200 bg-white p-4 shadow-sm transition-shadow hover:shadow-lg">
        <img src="https://images.unsplash.com/photo-1588612197597-25e1df37e738?w=400" alt="Dobble Harry Potter" class="h-48 w-full object-contain" />
        <div class="mt-4 w-full text-left">
            <h3 class="text-sm font-semibold text-gray-800">Dobble Harry Potter (Card Game)</h3>
            <p class="text-xs text-gray-500 mt-1">Brand: Zygomatic</p>
        </div>
        <button class="mt-4 w-full rounded-md bg-[#2563EB] py-2 text-sm font-medium text-white transition-colors hover:bg-blue-700">Add to Cart</button>
    </div>
</div>
"""

hydration_script = """
<script>
// Prevent hydration from wiping out static HTML
window.addEventListener('load', () => {
    setInterval(() => {
        const gridContainer = document.querySelector('.w-full.pb-4.sm\\\\:max-w-64')?.nextElementSibling;
        if (gridContainer && !gridContainer.querySelector('.product-grid-injected')) {
            gridContainer.innerHTML = `__INJECT__`;
            gridContainer.className = 'w-full ml-0 sm:ml-8'; // Fix layout spacing
        }
        
        // Fix headers
        const h1 = document.querySelector('h1.mt-4.text-3xl');
        if (h1 && h1.innerText === '') {
            const urlPath = window.location.pathname;
            let title = 'Products';
            if(urlPath.includes('gifting')) title = 'Gifting';
            else if(urlPath.includes('hygiene')) title = 'Hygiene, Housekeeping & Healthcare';
            else if(urlPath.includes('mro')) title = 'MRO';
            else if(urlPath.includes('stationery')) title = 'Stationery & Office Supplies';
            else if(urlPath.includes('electronics')) title = 'One Time Setup, Capex & Electronics';
            else if(urlPath.includes('packaging')) title = 'Packaging';
            h1.innerText = title;
            
            const span = document.querySelector('span.mt-4.text-sm.font-medium');
            if (span && span.innerText.trim() === 'products found') {
                span.innerText = '77 products found';
            }
        }
    }, 500);
});
</script>
""".replace('__INJECT__', gifting_html.replace('`', '\\`').replace('\n', ''))

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'product-grid-injected' not in content:
        content = content.replace('</body>', hydration_script + '</body>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Injected product grid script into", file)

print("Product Injection Complete.")
