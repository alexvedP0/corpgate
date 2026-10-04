import glob
import shutil
import os

base_dir = r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com'
logo_path = os.path.join(base_dir, 'images', 'corpgate-logo.png')

# 1. Favicon updates
for fav in ['favicon-32x32.png', 'favicon-16x16.png', 'apple-touch-icon.png', 'favicon.ico']:
    shutil.copy(logo_path, os.path.join(base_dir, fav))

# 2. SEO & Contact updates for all HTML files
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

seo_meta = """<meta name="description" content="CORPGATE is a premier B2B procurement and supply chain solutions provider. We transform procurement into a strategic, value-driven function."/>
<meta name="keywords" content="corpgate, b2b procurement, supply chain, office supplies, it equipment"/>
<meta property="og:title" content="CORPGATE - One Pass. All Access."/>
<meta property="og:description" content="Your trusted partner for all corporate procurement needs."/>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Inject SEO tags before </head> if not already there
    if 'og:title' not in content and '</head>' in content:
        content = content.replace('</head>', seo_meta + '</head>')
    
    # Update Contact Form action (simple formsubmit placeholder)
    # Most forms have action="/" or action="#"
    content = content.replace('action="#"', 'action="https://formsubmit.co/info@corpgate.com" method="POST"')
    content = content.replace('action="/"', 'action="https://formsubmit.co/info@corpgate.com" method="POST"')
    
    # Write back
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update About Us Content
about_file = os.path.join(base_dir, 'about-us.html')
if os.path.exists(about_file):
    with open(about_file, 'r', encoding='utf-8') as f:
        about_content = f.read()
    
    # Replace the old mission paragraph with the new presentation summary
    old_p = "At CORPGATE, our mission is to transform procurement into a strategic, value-driven function for businesses. We eliminate inefficiencies, enabling organizations to operate with transparency, efficiency, and cost-effectiveness. Our goal is to empower businesses to focus on their core competencies while we handle procurement complexities, driving growth and success. Leveraging advanced technology and a vast network of trusted vendors, we deliver unparalleled service, ensuring precise and excellent procurement solutions. Our commitment is to continuously adapt and evolve, meeting current demands and anticipating future needs. CORPGATE is dedicated to creating a seamless procurement experience that fosters strong partnerships, enhances operational efficiencies, and contributes to our clients"
    old_p_part = old_p[:100]
    
    # The actual text might have HTML encoded chars like clients&#x27; 
    # Let's just find the div containing it.
    import re
    # We will look for "At CORPGATE, our mission" and replace up to "overall success."
    about_content = re.sub(
        r'At CORPGATE, our mission is to transform procurement.*?overall success\.',
        """<strong>CORPGATE: ONE PASS. ALL ACCESS.</strong><br/><br/>
        <b>Our Mission:</b> To empower businesses to focus entirely on their core competencies by taking over their procurement complexities. We leverage advanced technology and a vast network of trusted vendors to deliver precise and excellent solutions.<br/><br/>
        <b>The Solution:</b> Instead of dealing with multiple vendors, our clients deal exclusively with CORPGATE. We offer a single platform for everything from Electronics & IT to Housekeeping, Hygiene, and MRO. Our customized B2B Tech Platform enforces your company's approval workflows, ensuring transparent and cost-optimized procurement.""",
        about_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    with open(about_file, 'w', encoding='utf-8') as f:
        f.write(about_content)

print("Favicons, SEO, Forms, and About Us content updated successfully!")
