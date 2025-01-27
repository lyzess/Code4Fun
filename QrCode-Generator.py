import qrcode
from urllib.parse import urlparse
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Function to generate QR code with a custom border color
def generate_qr_code():
    # Ask the user for the link
    link = input("Enter the link: ")

    # Extract the website name
    parsed_url = urlparse(link)
    web_name = parsed_url.netloc.replace('www.', '').split('.')[0]

    # Create the QR code
    qr_code = qrcode.QRCode(
        version=1,  # QR code size
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,  # Thin border
    )
    qr_code.add_data(link)
    qr_code.make(fit=True)

    # Generate the QR code image
    img = qr_code.make_image(fill_color="black", back_color="white").convert("RGBA")

    # Add a custom border to the QR code
    border_color = _generate_color_from_link(link)  # Get border color from the link
    img_with_border = _add_border(img, border_color)

    # Display the QR code in a non-blocking popup using Matplotlib
    _show_image_non_blocking(img_with_border)

    # Ask user if they want to save the QR code
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    save = messagebox.askyesno("Save QR Code", f"Do you want to save the QR code as {web_name}_qrcode.png?")

    if save:
        # Save the QR code image
        file_name = f"{web_name}_qrcode.png"
        img_with_border.save(file_name)
        print(f"QR code saved as {file_name}")
    else:
        print("QR code was not saved.")

# Function to generate a color from the website link
def _generate_color_from_link(link):
    # Generate an RGB color from the ASCII values of the link
    r = sum(ord(char) for char in link if char.isalpha()) % 256
    g = sum(ord(char) for char in link if char.isdigit()) % 256
    b = len(link) % 256
    return (r, g, b)

# Function to add a border with a custom color
def _add_border(img, border_color):
    border_width = 20  # Customize the border width
    new_size = (img.size[0] + 2 * border_width, img.size[1] + 2 * border_width)

    # Create a new image with the custom border color
    bordered_img = Image.new("RGBA", new_size, border_color)
    bordered_img.paste(img, (border_width, border_width))
    return bordered_img

# Function to display an image in a non-blocking popup using Matplotlib
def _show_image_non_blocking(img):
    plt.imshow(img)
    plt.axis('off')  # Turn off axes
    plt.title("Generated QR Code")
    plt.show(block=False)  # Make the window non-blocking

# Run the function
generate_qr_code()
