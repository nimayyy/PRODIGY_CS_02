from PIL import Image

def encrypt_image(image_path, key):
    original_image = Image.open(image_path)
    encrypted_image = original_image.copy()

    width, height = original_image.size
    for x in range(width):
        for y in range(height):
            pixel = original_image.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")


def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    decrypted_image = encrypted_image.copy()

    width, height = encrypted_image.size
    for x in range(width):
        for y in range(height):
            pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.show()
    print("Image decrypted successfully!")


def main():
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption/decryption key: "))
    choice = input("Enter 'E' for encryption or 'D' for decryption: ")

    if choice.upper() == 'E':
        encrypt_image(image_path, key)
    elif choice.upper() == 'D':
        decrypt_image("encrypted_image.png", key)  # Provide the path to the encrypted image
    else:
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")


if __name__ == "__main__":
    main()
