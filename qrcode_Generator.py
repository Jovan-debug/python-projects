import qrcode
from qrcode.constants import ERROR_CORRECT_H

class QRCodeGenerator:
    def __init__(self, box_size: int = 10, border: int = 4):
        self.box_size = box_size
        self.border = border

    def generate(self, data: str, file_name: str = "qrcode.png", fill_color: str = "black", back_color: str = "white") -> bool:
        """Generates and saves a QR code image."""
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=ERROR_CORRECT_H,
                box_size=self.box_size,
                border=self.border,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img.save(file_name)
            return True
        except Exception as e:
            print(f"Error generating QR code: {e}")
            return False


def main():
    print("**** Welcome to the QR Code Generator ****")
    
    data = input("Enter text or URL to encode: ").strip()
    if not data:
        print("Error: Input data cannot be empty!")
        return

    filename = input("Enter output filename (default: my_qr.png): ").strip()
    if not filename:
        filename = "my_qr.png"
    elif not filename.lower().endswith(".png"):
        filename += ".png"

    # Instantiate generator class
    generator = QRCodeGenerator(box_size=10, border=4)
    
    if generator.generate(data, file_name=filename):
        print(f" success! QR code saved as '{filename}'.")


if __name__ == "__main__":
    main()