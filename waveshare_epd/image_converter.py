from PIL import Image, ImageEnhance

class ImageConverter:
    def __init__(self, contrast=5):
        self.contrast = contrast

    def convert(self, img_file, percentage):
        img = Image.open(img_file)
        
        # Increase contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(self.contrast)
        
        # Convert to black & white
        img = img.convert('1')
        
        # Calculate new dimensions
        width, height = img.size
        new_width = int(width * (percentage / 100))
        new_height = int(height * (percentage / 100))
        
        # Resize image with aspect ratio maintained
        img = img.resize((new_width, new_height), Image.LANCZOS)
        
        return img
