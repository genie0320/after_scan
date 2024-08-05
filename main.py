from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
import os


def cut_image_in_half(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        try:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(input_directory, filename)

                # Open the image
                image = Image.open(image_path)

                # Get the dimensions of the image
                width, height = image.size

                # Calculate the middle of the image
                middle = width // 2

                # Crop the left half of the image
                left_half = image.crop((0, 0, middle, height))

                # Crop the right half of the image
                right_half = image.crop((middle, 0, width, height))

                # Construct the output file paths
                output_filename_left = filename + "_01.jpg"
                output_filename_right = filename + "_02.jpg"

                output_path_left = output_directory + "/" + output_filename_left
                output_path_right = output_directory + "/" + output_filename_right

                # Save the cropped images
                left_half.save(output_path_left)
                right_half.save(output_path_right)

                print(f"Saved left half to {output_path_left}")
                print(f"Saved right half to {output_path_right}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")


def images_to_pdf(image_folder, pdf_path_and_name):
    if not os.path.exists(image_folder):
        raise ValueError(f"Input directory {image_folder} does not exist")

    # Create a list to store the image paths
    image_files = [
        f
        for f in os.listdir(image_folder)
        if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif"))
    ]

    # Sort the files to maintain order
    image_files.sort()

    if not image_files:
        raise ValueError("No images found in the input directory")

    # Create a canvas object for the PDF
    pagesize = A4
    c = canvas.Canvas(pdf_path_and_name, pagesize=pagesize)
    width, height = pagesize

    for image_file in image_files:
        try:
            image_path = os.path.join(image_folder, image_file)

            # Open the image
            image = Image.open(image_path)
            img_width, img_height = image.size

            # Convert the image to RGB mode if it's not
            if image.mode != "RGB":
                image = image.convert("RGB")

            # Calculate the scaling factor to fit the image within the page size
            scale = min(width / img_width, height / img_height)
            img_width = int(img_width * scale)
            img_height = int(img_height * scale)

            # Center the image on the page
            x = (width - img_width) / 2
            y = (height - img_height) / 2

            # Save the image to a temporary file in PDF format
            # temp_image_path = image_path + ".pdf" # 한페이지 저장
            # image.save(temp_image_path, "PDF")

            # Draw the image on the canvas
            # c.drawImage(temp_image_path, 0, 0, width, height)
            c.drawImage(image_path, x, y, img_width, img_height)

            # Add a new page for the next image
            c.showPage()

            # Remove the temporary file
            # os.remove(temp_image_path)

        except Exception as e:
            print(f"Error processing {image_path}: {e}")

    # Save the PDF
    c.save()
    print(f"PDF saved to {pdf_path_and_name}")


if __name__ == "__main__":
    # input_directory = r"C:\Users\Genie240223\Desktop\test"
    input_directory = input("Input source dirctory : ")
    user_output_directory = input("Output folder or just press enter : ")
    pdf_name = input("Output pdf name : ")

    if user_output_directory != "":
        output_directory = user_output_directory
    else:
        output_directory = os.path.join(input_directory, "out")
        print('Output will be saved in "out" folder in source directory')

    cut_image_in_half(input_directory, output_directory)

    if pdf_name != "":
        pdf_path_and_name = input_directory + pdf_name + ".pdf"
    else:
        pdf_path_and_name = input_directory + "out-12341234.pdf"

    images_to_pdf(output_directory, pdf_path_and_name)
