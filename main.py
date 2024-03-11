"""
Author: IlMurlocDiplomato
"""
import sys
import glob
import os
import re
import pytesseract
from PIL import Image
import argparse
import subprocess

def rename_image(image_path, lang='ita', config='--psm 6'):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Perform OCR using PyTesseract
        text = pytesseract.image_to_string(image, lang=lang, config=config)

        # Remove special characters, numbers, and newlines
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters, numbers, and newlines

        # Replace spaces with underscores
        cleaned_text = cleaned_text.replace(' ', '_')

        # Remove newline characters from the cleaned text
        cleaned_text = cleaned_text.replace('\n', '')

        # Rename the file with cleaned text
        base_name, extension = os.path.splitext(image_path)
        new_name = f"{cleaned_text.strip()}{extension}"

        new_path = os.path.join(os.path.dirname(image_path), new_name)
        os.rename(image_path, new_path)
        print(f"Renamed {image_path} to {new_path}")

    except pytesseract.pytesseract.TesseractError as e:
        print(f"Tesseract Error: {str(e)}")
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

def extract_text_from_image(image_path, lang='ita', config='--psm 6'):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Perform OCR using PyTesseract
        text = pytesseract.image_to_string(image, lang=lang, config=config)

        print(f"Text extracted from {image_path}:\n{text}\n")

    except pytesseract.pytesseract.TesseractError as e:
        print(f"Tesseract Error: {str(e)}")
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process images.')
    parser.add_argument('path', nargs='*', help='Path to image(s)')
    parser.add_argument('-a', '--action', choices=['rename', 'verbose'], required=False, help='Action to perform on images')
    parser.add_argument('-l', '--lang', default='ita', help='Language for OCR')
    parser.add_argument('-c', '--config', type=int, default=6, help='Tesseract configuration')
    parser.add_argument('--list', action='store_true', help='Show available PSM values')

    args = parser.parse_args()

    if args.list:
        subprocess.run(["tesseract", "--help-psm"])
        sys.exit(0)

    if not args.path:
        print("Usage: python main.py <image1.png> <image2.png> ...")
        sys.exit(1)

    if args.lang not in pytesseract.get_languages():
        print(f"Error: Language '{args.lang}' not supported.")
        sys.exit(1)

    if args.config < 0 or args.config > 13:
        print(f"Error: Invalid config value '{args.config}'. It should be between 0 and 13.")
        sys.exit(1)

    args.config = f"--psm {args.config}"

    if args.action == 'rename':
        for path in args.path:
            for image_path in glob.glob(path):
                rename_image(image_path, args.lang, args.config)

    elif args.action == 'verbose':
        for path in args.path:
            for image_path in glob.glob(path):
                extract_text_from_image(image_path, args.lang, args.config)
