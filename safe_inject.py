import glob

html_files = glob.glob(r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\**\*.html', recursive=True)

script_to_inject = """
<script>
document.addEventListener('click', function(e) {
    var a = e.target.closest('a');
    if (a && a.href && a.href.startsWith(window.location.origin)) {
        var url = new URL(a.href);
        // Only modify if it doesn't already have an extension and isn't a hash link
        if (!url.pathname.endsWith('.html') && !url.pathname.endsWith('/') && !url.pathname.includes('.')) {
            e.preventDefault();
            e.stopImmediatePropagation();
            window.location.href = url.pathname + '.html' + url.search + url.hash;
        }
    }
}, true);
</script>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Don't inject twice
    if 'document.addEventListener(\'click\'' not in content:
        # inject before </body>
        if '</body>' in content:
            new_content = content.replace('</body>', script_to_inject + '</body>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
        else:
            with open(file, 'a', encoding='utf-8') as f:
                f.write(script_to_inject)

print("Injected safe routing script into all HTML files.")
