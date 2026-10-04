import os

filepath = r'c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com\_next\static\chunks\pages\about-us-6db222fbbc0b83bc.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the gradient on top of about page
content = content.replace('rgb(255, 255, 255)', 'rgb(15, 15, 15)')
content = content.replace('rgb(254, 215, 170)', 'rgb(45, 38, 20)')
content = content.replace('rgb(255, 237, 213)', 'rgb(30, 25, 15)')

# Fix the About Us text wrapper to have a dark overlay
target = 'className:"absolute inset-0 top-20 flex flex-col items-center px-4 md:px-24 lg:top-32 lg:px-64"'
replacement = 'className:"absolute inset-0 top-20 flex flex-col items-center px-4 md:px-24 lg:top-32 lg:px-64",style:{backgroundColor:"rgba(0,0,0,0.75)",backdropFilter:"blur(10px)",paddingTop:"4rem"}'
content = content.replace(target, replacement)

# Fix the Meet Our Team gradient wrapper
target2 = 'className:"flex flex-col items-center justify-center bg-gradient-to-b from-green-100 via-white to-white px-8 py-8 md:px-12 md:py-16"'
replacement2 = 'className:"flex flex-col items-center justify-center bg-black px-8 py-8 md:px-12 md:py-16"'
content = content.replace(target2, replacement2)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('JS updated!')
