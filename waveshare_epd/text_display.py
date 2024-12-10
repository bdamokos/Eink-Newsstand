# text_display.py
from waveshare_epd import epd4in2_V2
from PIL import Image, ImageDraw, ImageFont

class TextDisplay:
    def __init__(self, epd, font_path, font_size, max_width, x=0, y=0):
        self.epd = epd
        self.font_path = font_path
        self.font_size = font_size
        self.max_width = max_width
        self.x = x
        self.y = y
        self.font = ImageFont.truetype(self.font_path, self.font_size)

    def get_text_width(self, text):
        bbox = self.font.getbbox(text)
        return bbox[2] - bbox[0]

    def get_text_height(self, text):
        bbox = self.font.getbbox(text)
        return bbox[3] - bbox[1]

    def draw_wrapped_text(self, text):
        adjusted_width = self.max_width - self.x

        words = text.split()
        wrapped_lines = []
        current_line = ""

        for word in words:
            test_line = current_line + (word + " ")
            if self.get_text_width(test_line) <= adjusted_width:
                current_line = test_line
            else:
                wrapped_lines.append(current_line.strip())
                current_line = word + " "
        
        wrapped_lines.append(current_line.strip())

        # Collecting draw.text commands into a single string
        draw_commands = []
        y_position = self.y
        for line in wrapped_lines:
            draw_commands.append(f'draw.text(({self.x}, {y_position}), "{line}", font=self.font, fill=0)')
            y_position += self.get_text_height(line)
        
        # Join all commands into a single string
        command_string = "\n".join(draw_commands)
        
        # Use exec to run the commands
        image = Image.new('1', (self.epd.width, self.epd.height), 255)
        draw = ImageDraw.Draw(image)
        exec(command_string)
        
        # Display the image (optional, for testing purposes)
        if self.epd:
            self.epd.display_Partial(self.epd.getbuffer(image))

        return command_string
