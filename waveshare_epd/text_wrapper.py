from PIL import Image, ImageDraw, ImageFont

class TextWrapper:
    def __init__(self, font_path, font_size, max_width):
        self.font_path = font_path
        self.font_size = font_size
        self.max_width = max_width
        self.font = self.load_font()

    def load_font(self):
        try:
            return ImageFont.truetype(self.font_path, self.font_size)
        except IOError:
            return ImageFont.load_default()

    def wrap_text(self, text, draw, x, y):
        text_wrapped = ''
        words = text.split()
        line = ' '
        for word in words:
            test_line = f'{line} {word}'.strip()
            bbox = draw.textbbox((x, y), test_line, font=self.font)
            text_width = bbox[2] - bbox[0]
            if text_width <= self.max_width:
                line = test_line
            else:
                text_wrapped += line + '\n'
                line = word
                y += self.font_size
        text_wrapped += line
        return text_wrapped, y + self.font_size

    def draw_text(self, canvas, text, x, y):
        draw = ImageDraw.Draw(canvas)
        wrapped_text, final_y = self.wrap_text(text, draw, x, y)
        draw.text((x, y), wrapped_text, font=self.font, fill=0)
        return final_y
