from PIL import Image
import os

def resize_images(input_dir, output_dir, size=(1024, 1024)):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get all files in input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Open image
            with Image.open(os.path.join(input_dir, filename)) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize image
                resized_img = img.resize(size, Image.Resampling.LANCZOS)
                
                # Save resized image
                output_path = os.path.join(output_dir, filename)
                resized_img.save(output_path, quality=95)
                print(f"Resized {filename}")

# Set your directories using the correct paths
input_dir = os.path.join(os.getcwd(), "datasets", "impressionist", "trainA_diff")
output_dir = os.path.join(os.getcwd(), "datasets", "impressionist", "trainA")

print(f"Looking for images in: {input_dir}")
print(f"Will save resized images to: {output_dir}")

# Count total images
total_images = len([f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
print(f"Found {total_images} images to process")

# Resize all images
resize_images(input_dir, output_dir)

print("Script completed!")