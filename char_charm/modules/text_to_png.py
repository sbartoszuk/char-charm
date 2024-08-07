from PIL import Image, ImageDraw, ImageFont
import io
import os

def load_font_as_bytes():
    try:
        font_file_path = None
        if os.name == "nt":  # Windows
            font_file_path = os.path.join(os.environ.get("WINDIR"), "Fonts", "cour.ttf")
        elif os.name == "posix":  # Unix-like systems (Linux, macOS)
            font_file_path = "/usr/share/fonts/truetype/nimbus/NimbusMono-Regular.ttf"
        if font_file_path is None or not os.path.isfile(font_file_path):
            raise FileNotFoundError("System font file not found.")
        
        with open(font_file_path, "rb") as font_file:
            font_bytes = io.BytesIO(font_file.read())
        return font_bytes
    except Exception as e:
        print("Failed to load system font:", e)
        return None

def create_text_image(text, output_path, height):

    longest_line = ''
    for line in text:
        if len(line) > len(longest_line):
            longest_line = line

    font_data = load_font_as_bytes()
    font = ImageFont.truetype(font_data, 1)
    line_char_test = '█'
    line_height = font.getbbox(line_char_test)[3]/1.888
    text_length = len(text)
    font_size = 1
    while (line_height*text_length) < height:
        font_size += 1
        del font
        font_data = load_font_as_bytes()
        font = ImageFont.truetype(font_data, font_size)
        line_height = font.getbbox(line_char_test)[3]/1.888

    width = font.getbbox(longest_line)[2]
    new_height = int(line_height)*len(text)

    img = Image.new("RGB", (width, new_height), "black")
    draw = ImageDraw.Draw(img)
    
    for i, line in enumerate(text):
        draw.text((0, i*line_height), line, fill="white", font=font)

    output_width, output_height = img.width, img.height
    image_ratio = output_width/output_height
    img = img.resize((int(height*image_ratio), height))
    
    img.save(output_path)