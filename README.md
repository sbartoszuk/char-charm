# char-charm
Create ``ASCII`` art from images, ```strings```, text files, or ```Pillow``` images and save them as images, or display them in windows terminal. WARNING display in terminal works ONLY in windows os.

# Setup

```
git clone https://github.com/sbartoszuk/char-charm.git
cd char-charm
pip install .
```

# Example usage

```python
from char_charm.main import AsciiImage

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
from char_charm.main import AsciiImage

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
- ```canvas_heigth (int)```: Lines of text to make ```ASCII``` art. It set size of characters canvas.
- ```seed_size (int)```: Set how much space each character takes of the canvas. Smallest seed, better details.

Example:

```python
from char_charm.main import AsciiImage

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

- ```image (PIL.Image)```: ```PIL``` image type data.
- ```canvas_heigth (int)```: Lines of text to make ```ASCII``` art. It set size of characters canvas.
- ```seed_size (int)```: Set how much space each character takes of the canvas. Smallest seed, better details.

Example:

```python
from char_charm.main import AsciiImage

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
from char_charm.main import AsciiImage

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
from char_charm.main import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_string(ascii_string)

ascii_art.to_console()
```
## Exporting data

there are couple of exporting methods too, just choose what suits you

### ```save_as_image()```

saves ```ASCII``` character set as image file

```python
save_as_image(file_path: str, image_height: int = 1600)
```

Parameters:

- ```file_path (str)```: Output image file path.
- ```image_height (int)```: Output image heigth in pixels. For image with height less than 1600px there may be deformations. Width will be automatically scaled.

Example:

```python
from char_charm.main import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_image('input_image.jpg')

ascii_art.save_as_image('output_image.png')
```

### ```to_console()```

prints ```ASCII``` art to ```windows``` console (works only in ```windows```)

```python
to_console()
```

Parameters:

- none

Example:

```python
from char_charm.main import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_image('input_image.jpg')

ascii_art.to_console()
```

### ```save_to_txt()```

saves ```ASCII``` character set to text file

```python
save_to_txt(file_path: str)
```

Parameters:

- ```file_path (str)```: Output txt file path.

Example:

```python
from char_charm.main import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_image('input_image.jpg')

ascii_art.save_to_txt('output_text_file.txt')
```

### ```to_string()```

works like ```save_to_txt()``` but saves ```ASCII``` character set in ```string``` variable

```python
to_string()
```

Parameters:

- none

Example:

```python
from char_charm.main import AsciiImage

ascii_art = AsciiImage()
ascii_art.load_image('input_image.jpg')

ascii_string_character_set = ''

ascii_string_character_set = ascii_art.to_string()
```

# Example output results

here are some example output results of ```char-charm```

![](https://github.com/sbartoszuk/char-charm/blob/main/media_examples/example_1.png?raw=true)

![](https://github.com/sbartoszuk/char-charm/blob/main/media_examples/example_2.png?raw=true)

![](https://github.com/sbartoszuk/char-charm/blob/main/media_examples/example_3.png?raw=true)

![](https://github.com/sbartoszuk/char-charm/blob/main/media_examples/example_4.png?raw=true)
