# Convert to PNG

This Python script converts all image files in the directory where the script is located to PNG format. It supports a variety of image file extensions, including both lowercase and uppercase formats.

## Features

- Automatically finds and converts all image files in the script's directory.
- Supports common image formats: jpeg, jpg, webp, bmp, gif, tiff, and their uppercase variants.
- Skips conversion for files already in PNG format.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository or download the script.

   ```sh
   git clone https://github.com/sunwoo-j/convert-to-png.git
   cd convert-to-png
   ```

2. Install the required Python package.

   ```sh
   pip install pillow
   ```

## Usage

1. Place the script (`convert_images.py`) in the directory containing the images you want to convert.
2. Run the script.

   ```sh
   python convert_images.py
   ```

3. The script will automatically find all supported image files in the directory, convert them to PNG format, and save the converted images in the same directory.

## Example

If you have the following files in your directory:

```
example1.jpeg
example2.JPG
example3.webp
example4.PNG
```

After running the script, you will get:

```
example1.png
example2.png
example3.png
example4.PNG (unchanged)
```
