import os

css_file = r'c:\Users\Hp\Downloads\cropgate\www.corpgate.com\_next\static\css\82db39a5ff6f275f.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The user wants "dynamic high feature" design for the slanted stripes.
# Let's add premium CSS animations!
animation_css = """
/* Dynamic High-Feature Stripe Animations */
@keyframes stripe-slide-1 {
  0% { transform: translateX(-5%); }
  50% { transform: translateX(2%); }
  100% { transform: translateX(-5%); }
}
@keyframes stripe-slide-2 {
  0% { transform: translateX(2%); }
  50% { transform: translateX(-5%); }
  100% { transform: translateX(2%); }
}
@keyframes stripe-slide-3 {
  0% { transform: translateX(-2%); }
  50% { transform: translateX(5%); }
  100% { transform: translateX(-2%); }
}

.bg-blue-300 { 
    background: linear-gradient(90deg, #FDBA74, #FCD34D, #FDBA74) !important;
    background-size: 200% 200% !important;
    animation: stripe-slide-1 8s ease-in-out infinite, gradient-shift 6s ease infinite !important;
    box-shadow: 0 0 15px rgba(253, 186, 116, 0.5);
    transition: all 0.3s ease;
}
.bg-blue-400 { 
    background: linear-gradient(90deg, #FB923C, #F97316, #FB923C) !important;
    background-size: 200% 200% !important;
    animation: stripe-slide-2 10s ease-in-out infinite, gradient-shift 8s ease infinite !important;
    box-shadow: 0 0 20px rgba(251, 146, 60, 0.6);
    transition: all 0.3s ease;
}
.bg-black0 { 
    background: linear-gradient(90deg, #EA580C, #C2410C, #EA580C) !important;
    background-size: 200% 200% !important;
    animation: stripe-slide-3 12s ease-in-out infinite, gradient-shift 10s ease infinite !important;
    box-shadow: 0 0 25px rgba(234, 88, 12, 0.7);
    transition: all 0.3s ease;
}

@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Add hover effect for the parent container if possible, but since we can't easily target it without HTML changes, we apply hover to stripes */
.bg-blue-300:hover, .bg-blue-400:hover, .bg-black0:hover {
    filter: brightness(1.2);
    transform: scaleY(1.2) !important;
    z-index: 10;
}
"""

# Replace the previous static definitions
if '/* Fix for slanted stripes */' in content:
    # We will just append the new animations at the end, which will override the previous ones due to CSS specificity (being later in the file)
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write("\n" + animation_css)
else:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write("\n" + animation_css)

print("Dynamic animations added to CSS!")
