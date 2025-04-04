#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os
import sys

# Optimized settings for large photos (3000x4000 or 4000x3000)
PHOTOS_FOLDER = "jpeg"
WATERMARK_TEXT = "© All rights reserved"
OPACITY = 0.25  # 25% opacity (balanced)
COLOR = (255, 255, 255)  # Pure white
MARGIN = 0.03  # 3% of image width
BACKUP_FOLDER = "jpeg_originals"  # Folder for backup (optional)


def calculate_font_size(img):
    """
    Calculate appropriate font size for large images
    For 3000x4000 images, will result in a font of approximately 50-60px
    """
    min_dimension = min(img.width, img.height)
    return int(min_dimension * 0.015)  # 1.5% of the smaller dimension


def apply_watermark(make_backup=False):
    """Apply watermark to all images in the specified folder"""
    print("\n=== APPLYING PROFESSIONAL WATERMARK ===\n")

    # Create backup folder if needed
    if make_backup and not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

    processed_photos = 0
    error_photos = 0

    # List all files in the folder
    files = [f for f in os.listdir(PHOTOS_FOLDER)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not files:
        print(f"No images found in folder '{PHOTOS_FOLDER}'")
        return

    print(f"Found {len(files)} images to process...\n")

    for photo in files:
        try:
            path = os.path.join(PHOTOS_FOLDER, photo)

            # Make backup if requested
            if make_backup:
                backup_path = os.path.join(BACKUP_FOLDER, photo)
                with open(path, 'rb') as src, open(backup_path, 'wb') as dst:
                    dst.write(src.read())

            # Open the image
            with Image.open(path) as img:
                # Convert to RGBA to support transparency
                img_rgba = img.convert("RGBA")

                # Create separate layer for watermark
                overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
                draw = ImageDraw.Draw(overlay)

                # Calculate appropriate font size for large images
                font_size = calculate_font_size(img)

                # Load font (with fallbacks)
                try:
                    font = ImageFont.truetype("arialbd.ttf", font_size)
                except OSError:
                    try:
                        font = ImageFont.truetype("arial.ttf", font_size)
                    except OSError:
                        try:
                            # Try to find any sans-serif font on the system
                            font = ImageFont.truetype("DejaVuSans.ttf", font_size)
                        except OSError:
                            font = ImageFont.load_default()
                            # Limit default font size
                            font_size = min(font_size, 72)

                # Calculate text dimensions
                text_width = draw.textlength(WATERMARK_TEXT, font=font)
                text_height = font_size  # Approximation of height

                # Calculate position (bottom right corner)
                margin_pixels = int(img.width * MARGIN)
                pos_x = img.width - text_width - margin_pixels
                pos_y = img.height - text_height - margin_pixels

                # Apply watermark to overlay layer
                draw.text(
                    (pos_x, pos_y),
                    WATERMARK_TEXT,
                    fill=(*COLOR, int(255 * OPACITY)),
                    font=font
                )

                # Combine layers
                result_img = Image.alpha_composite(img_rgba, overlay)

                # Save maintaining maximum quality
                result_img.convert("RGB").save(
                    path,
                    quality=95,
                    optimize=True
                )

            processed_photos += 1
            print(f"✓ {photo} (Font: {font_size}px)")

        except Exception as e:
            error_photos += 1
            print(f"✗ Error in {photo}: {str(e)}")

    # Final report
    print(f"\n--- Report ---")
    print(f"Total processed: {processed_photos} images")
    if error_photos > 0:
        print(f"Errors: {error_photos} images")


if __name__ == "__main__":
    if not os.path.exists(PHOTOS_FOLDER):
        print(f"\nERROR: Folder '{PHOTOS_FOLDER}' not found!")
        print(f"Create the '{PHOTOS_FOLDER}' folder and put your photos inside")
        sys.exit(1)

    # Check if backup is desired
    make_backup = False
    response = input("Do you want to backup original images? (y/n): ").lower()
    if response.startswith('y'):
        make_backup = True
        print(f"Backup will be saved in folder '{BACKUP_FOLDER}'")

    # Apply watermark
    apply_watermark(make_backup)

    print("\n✅ PROCESSING COMPLETED SUCCESSFULLY!")
    print(f"The images are in the '{PHOTOS_FOLDER}' folder")
