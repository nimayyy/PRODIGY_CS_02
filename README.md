# PRODIGY_CS_02
Pixel-Manipulation-for-Image-Encryption
Image Encryption and Decryption
This Python script allows you to encrypt and decrypt images using a simple additive encryption technique.

How it Works
Encryption: Each pixel in the image is encrypted by adding a secret key value to its RGB values. The encrypted pixel values are stored in a new image file.
Decryption: The encrypted image is decrypted by subtracting the secret key value from each pixel's RGB values, reversing the encryption process.
Requirements
Python 3.x
PIL (Python Imaging Library)
Usage
Clone or download this repository to your local machine.
Install the required Python libraries using pip install -r requirements.txt.
Run the script by executing python image_encryption.py.
Follow the prompts to enter the path to the image file, encryption/decryption key, and select encryption or decryption operation.
Example
Suppose you have an image named example_image.png that you want to encrypt. You can run the script and provide the path to the image file when prompted. After encryption, the encrypted image will be saved as encrypted_image.png. To decrypt the image, run the script again, select decryption, and provide the encryption/decryption key.

Note
Make sure to remember the encryption/decryption key used for each operation.
Keep the encrypted image (encrypted_image.png) safe, as it will be needed for decryption.
