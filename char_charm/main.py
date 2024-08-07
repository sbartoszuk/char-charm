#!/usr/bin/env python

from PIL import Image
import os

try:
    from .modules.font_sizer import change_font_size
    from .modules.text_to_png import create_text_image

except:
    from modules.font_sizer import change_font_size
    from modules.text_to_png import create_text_image

class CharCharmLoadError(Exception):
    def __init__(self):
        self.message = 'There is no data loaded. Load data first.'
        super().__init__(self.message)

class AsciiImage:
    def __init__(self):
        self.ascii_data = None

    def load_from_text_file(self, file_path: str):
        """
        Load data from text file

        Args:
            file_path (str): Path of text file to import.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            ascii_text = file.read()
        self.load_string(ascii_text)
    
    def load_string(self, text: str, separator: str = '\n'):
        """
        Load data from text (string)

        Args:
            text (str): String to import.
            separator (str): Text variable is splitted to lines. Separator character tells where the text sould be splitted.
        """
        self.ascii_data = text.split(separator)
        
        canvas_width = 0
        for item in self.ascii_data:
            if len(item) > canvas_width:
                canvas_width = len(item)
        
        self.canvas_height = len(self.ascii_data)
        self.canvas_width = canvas_width
        self.seed_size = 2


    def load_image(self, file_path: str, canvas_heigth: int = 400, seed_size: int = 2):
        """
        Load data from image file

        Args:
            file_path (str): Path of image file to import.
            canvas_heigth (int): Lines of text to make ASCII art. It set size of characters canvas.
            seed_size (int): Set how much space each character takes of the canvas. Smallest seed, better details.
        """

        image = Image.open(file_path)
        
        self.load_pil_image(image, canvas_heigth, seed_size)

    def load_pil_image(self, image: Image.Image, canvas_heigth: int = 400, seed_size: int = 2):
        """
        Load data from PIL image

        Args:
            image (PIL.Image): PIL image type data.
            canvas_heigth (int): Lines of text to make ASCII art. It set size of characters canvas.
            seed_size (int): Set how much space each character takes of the canvas. Smallest seed, better details.
        """
        if not isinstance(image, Image.Image):
            raise TypeError("Argument must be a PIL image")
        
        image = image.convert("L")

        not_allowed_seed_sizes = [4, 12]
        non_allowed = False

        if 40 >= seed_size >= 2:
            if seed_size in not_allowed_seed_sizes:
                non_allowed = True
        else:
            non_allowed = True
        if non_allowed:
            raise Exception(f"Seed size must be between 2 - 40 excluding {not_allowed_seed_sizes}")

        new_height = canvas_heigth
        aspect_ratio = image.width / image.height

        new_width = int(new_height * aspect_ratio)
        
        image = image.resize((new_width//(seed_size//2), new_height//(seed_size//2)))

        image_data = image.load()

        width, height = image.size

        hue_value = []

        for y in range(height):
            pixel_line = []
            for x in range(width):

                pixel_value = image_data[x, y]
                pixel_line.append(pixel_value)
                
            hue_value.append(pixel_line)

        ascii_list = []

        for line in hue_value:
            temp_line = ''
            for pixel in line:

                # ------- tweak those numbers to get better result

                if pixel >= 240:
                    temp_line += '█'
                elif pixel >= 190:
                    temp_line += 'W'
                elif pixel >= 180:
                    temp_line += 'w'
                elif pixel >= 150:
                    temp_line += 'o'
                elif pixel >= 120:
                    temp_line += ':'
                elif pixel >= 100:
                    temp_line += '^'
                elif pixel >= 95:
                    temp_line += '~'
                elif pixel >= 80:
                    temp_line += '\''
                elif pixel >= 60:
                    temp_line += '-'
                elif pixel >= 30:
                    temp_line += '.'
                else:
                    temp_line += ' '
                
                # -------------------------------------------------
            
            ascii_list.append(temp_line)

        self.ascii_data = ascii_list
        self.seed_size = seed_size
        self.canvas_width = width
        self.canvas_height = height

    def save_as_image(self, file_path: str, image_height: int = 1600):
        """
        Saves ASCII art as image

        Args:
            file_path (str): Output image file path.
            image_height (int): Output image heigth in pixels. For image with height less than 1600px there may be deformations. Width will be automatically scaled.
        """
        if self.ascii_data == None:
            raise CharCharmLoadError
        
        create_text_image(self.ascii_data, file_path, image_height)

    def save_to_txt(self, file_path: str):
        """
        Save ASCII art to txt file

        Args:
            file_path (str): Output txt file path.
        """
        if self.ascii_data == None:
            raise CharCharmLoadError
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(self.ascii_data))

    def to_string(self) -> str:
        """
        Returns string with ASCII art data.
        """
        if self.ascii_data == None:
            raise CharCharmLoadError
        
        return '\n'.join(self.ascii_data)
    
    def to_console(self):
        """
        Prints ASCII art in current console window

        NOTE - works for ms windows os only
        """
        if self.ascii_data == None:
            raise CharCharmLoadError

        change_font_size(self.seed_size)
        os.system('mode ' + str(self.canvas_width) + ', ' + str(self.canvas_height+1))

        print('\n'.join(self.ascii_data))
        input()
        os.system('cls')

        change_font_size(16, 'normal width')
        os.system('mode ' + str(100) + ', ' + str(30))