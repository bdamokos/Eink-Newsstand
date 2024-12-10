import pkg_resources

# Get the path to the 'fonts' directory
def _get_font_files():
    font_files = []
    font_dir = pkg_resources.resource_filename(__name__, '')
    with pkg_resources.resource_stream(__name__, '') as resource:
        for entry in pkg_resources.resource_listdir(__name__, ''):
            if entry.endswith('.ttf'):
                font_files.append(entry)
    return font_files

# Create a dictionary to hold font paths
fonts_dict = {}
for font_name in _get_font_files():
    fonts_dict[font_name] = pkg_resources.resource_filename(__name__, font_name)

# Expose fonts dynamically as attributes
for font_name, font_path in fonts_dict.items():
    setattr(__import__(__name__), font_name[:-4], font_path)
