# find_text_action
A little script to find text in image and make action

# Description
This script try to find a text in one or more image and make an action like:
rename: the file based on word1_word2---.extension
verbose: Print the text he found for evry image

# Requirement
## Pytesseract
```pip install pytesseract```
or for linux users (tested only in Debian)
```apt install tesseract-ocr```
## Pillow
```pip install Pillow```

## Command
```
usage: main.py [-h] [-a {rename,verbose}] [-l LANG] [-c CONFIG] [--list]
               [path ...]

Process images.

positional arguments:
  path                  Path to image(s)

options:
  -h, --help            show this help message and exit
  -a {rename,verbose}, --action {rename,verbose}
                        Action to perform on images
  -l LANG, --lang LANG  Language for OCR
  -c CONFIG, --config CONFIG
                        Tesseract configuration
  --list                Show available PSM values
```

## Example 
### Single file 
```python3 main.py img/image.png -a verbose```
### Multiple file
```python3 main.py img/*.png -a verbose``` 
