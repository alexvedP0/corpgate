import os

directory = r"c:\Users\Hp\Downloads\cropgate\www.procurabusiness.com"

img_tag = '<img src="images/about.png" alt="about us" class="h-full w-full object-cover pt-80 md:pt-16 lg:pt-4"/>'
overlay_div = '<div class="absolute inset-0 bg-black bg-opacity-80 pointer-events-none" style="z-index: 5;"></div>'
# We need to make sure the text container has a higher z-index if they share the same stacking context.
# The text container is the next div. We can add z-index: 10 to it.

updated_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if img_tag in content and overlay_div not in content:
                    # Inject overlay
                    new_content = content.replace(
                        img_tag, 
                        img_tag + overlay_div
                    )
                    
                    # Also make sure the text container `absolute inset-0 top-20` has a higher z-index
                    new_content = new_content.replace(
                        '<div class="absolute inset-0 top-20 flex flex-col',
                        '<div class="absolute inset-0 top-20 flex flex-col z-10"'
                    )
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files += 1
            except Exception as e:
                pass

print(f"Updated {updated_files} HTML files with overlay.")
