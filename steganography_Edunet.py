
# Steganography - Hiding Information in an Image using Python

# Install the required library:
# pip install stegano

from stegano import lsb

# === HIDE MESSAGE ===
# Load the input image and hide a secret message in it
secret_image = lsb.hide("input_image.png", "This is a secret message hidden in the image.")
secret_image.save("output_image.png")
print("Secret message successfully hidden in 'output_image.png'")

# === REVEAL MESSAGE ===
# Load the output image and reveal the hidden message
revealed_message = lsb.reveal("output_image.png")
print("Revealed message:", revealed_message)
