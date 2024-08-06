# char-charm
Create ``ASCII`` art from images, strings, text files, or ```Pillow``` images and save them as images, or display them in windows terminal. WARNING display in terminal works ONLY in windows os.

# Setup
To make it work, you need to install ```Pillow```

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

![](https://github.com/sbartoszuk/char-charm/blob/main/media_examples/example_4.png?raw=true)

# AsciiImage object usage

All the fun is contained in ```AsciiImage``` class. To get your ```ASCII``` art ready, just load data with chosen method for loading data provided below, and show/export ```ASCII``` image with selected method for exporting images (provided below too). In order to use ```char-charm```, you need to create ```AsciiImage``` object first:

```python
from char_charm import AsciiImage

ascii_art = AsciiImage()
```

## Loading data

there are number of ways of how you can load data to ```char-charm```

### ```load_image()```

loads data from existing image (photo, drawing etc.), and generate ```ASCII``` character set

```python
load_image(file_path: str, canvas_heigth: int = 400, seed_size: int = 2)
```

Parameters:

- ```file_path (str)```: Path of image file to import.
- ```canvas_heigth (int)```: Lines of text to make ASCII art. It set size of characters canvas.
- ```seed_size (int)```: Set how much space each character takes of the canvas. Smallest seed, better details.

Example:

```python
from char_charm import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_image('some_image.jpg')

ascii_art.to_console()
```

### ```load_pil_image()```

works like ```load_image()```, but instead of getting data from image file, it gets it from ```Pillow``` type image

```python
load_pil_image(image: Image.Image, canvas_heigth: int = 400, seed_size: int = 2)
```

Parameters:

- ```image (PIL.Image)```: PIL image type data.
- ```canvas_heigth (int)```: Lines of text to make ASCII art. It set size of characters canvas.
- ```seed_size (int)```: Set how much space each character takes of the canvas. Smallest seed, better details.

Example:

```python
from char_charm import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_pil_image(pillow_image)

ascii_art.to_console()
```

### ```load_from_text_file()```

loads ```ASCII``` data (previously generated ```ASCII``` character set) from text file

```python
load_from_text_file(file_path: str)
```

Parameters:

- ```file_path (str)```: Path of text file to import.

Example:

```python
from char_charm import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_from_text_file('ascii_dog.txt')

ascii_art.to_console()
```

### ```load_string()```

works same as ```load_from_text_file()```, but instead of getting data from file, it gets it from string variable

```python
load_string(text: str, separator: str = '\n')
```

Parameters:

- ```text (str)```: String to import.
- ```separator (str)```: Text variable is splitted to lines. Separator character tells where the text sould be splitted.

Example:

```python
from char_charm import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_string(ascii_string)

ascii_art.to_console()
```
