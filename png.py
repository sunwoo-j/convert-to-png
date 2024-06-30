from PIL import Image
import glob
import os

def convert_to_png(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'PNG')

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    image_extensions = ['*.jpeg', '*.jpg', '*.webp', '*.png', '*.bmp', '*.gif', '*.tiff',
                        '*.JPEG', '*.JPG', '*.WEBP', '*.PNG', '*.BMP', '*.GIF', '*.TIFF']

    input_images = []
    for ext in image_extensions:
        input_images.extend(glob.glob(os.path.join(script_dir, ext)))

    for input_image in input_images:
        if input_image.endswith('.png'):
            continue  # Skip if image is already a PNG
        output_image = os.path.splitext(os.path.basename(input_image))[0] + '.png'
        output_path = os.path.join(script_dir, output_image)
        convert_to_png(input_image, output_path)
        print(f"Converted {input_image} to {output_path}")

if __name__ == "__main__":
    main()