# char-charm
Create ASCII art from images, strings, text files, or PIL images and save them as images, or display them in windows terminal. WARNING display in terminal works ONLY in windows os.

# Setup
To make it work, you need to install Pillow

```
pip install Pillow
```

After that, just clone this repo and you're good to go

```
git clone https://github.com/sbartoszuk/char-charm.git
```

# Example usage

```python
from char_charm.char_charm import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_image('example_image.jpg')

# if you wanna to print out to console (windows os only)
#ascii_art.to_console()

# if you wanna to save as png file
ascii_art.save_as_image('output.png')
```

Output file

![](https://raw.githubusercontent.com/ProfOak/ascii_py/master/Media/before.jpg)
