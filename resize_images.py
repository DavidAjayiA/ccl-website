from PIL import Image
import os

# List of images to resize (the exec photos)
images = [
    'ICEYY.jpg',
    'DAVID.jpg',
    'ISRAEL.jpg',
    'PROMISE.jpg',
    'TAOFIKAT.jpg',
    'CBAXTEDx105 - Chidiebere Onwubiko.jpg',
    'IMG-20240913-WA0137(5) - Salawu Idera.jpg',
]

# Reference: first slide image
reference = 'IMG_0569 - salawu Eniola.jpeg'

# Target dimensions based on slideshow CSS (420px width for photo block)
target_width = 420
target_height = 460

ref_img = Image.open(reference)
print(f"Reference image ({reference}): {ref_img.size}")

for img_name in images:
    if not os.path.exists(img_name):
        print(f"[SKIP] {img_name} not found")
        continue

    img = Image.open(img_name)
    print(f"\nProcessing {img_name}...")
    print(f"  Original: {img.size}")

    # Resize using LANCZOS for high quality
    # Maintain aspect ratio, then pad if needed
    img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)

    # Create a new image with the target dimensions
    new_img = Image.new('RGB', (target_width, target_height), (0, 0, 0))

    # Calculate position to center the image
    x = (target_width - img.width) // 2
    y = (target_height - img.height) // 2

    new_img.paste(img, (x, y))

    # Save with high quality
    new_img.save(img_name, 'JPEG', quality=95)
    print(f"  Resized to: {new_img.size} (quality: 95%)")
    print(f"  [OK] Saved")

print("\n[DONE] All images resized successfully!")
