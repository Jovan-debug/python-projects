import secrets
import string

class PasswordGenerator:
    def __init__(self, length: int = 8, use_digit: bool = True, use_uppercase: bool = True, use_symbols: bool = True):
        self.length = length
        self.use_digit = use_digit
        self.use_uppercase = use_uppercase
        self.use_symbols = use_symbols

    def build_pool(self) -> str:
        chars = string.ascii_lowercase
        if self.use_digit:
            chars += string.digits
        if self.use_symbols:
            chars += string.punctuation
        if self.use_uppercase:
            chars += string.ascii_uppercase
        return chars

    def generate(self) -> str:
        pool = self.build_pool()
        if not pool:
            raise ValueError("Character pool cannot be empty!")
        
        return "".join(secrets.choice(pool) for _ in range(self.length))


def get_input(prompt: str) -> int:
    while True:
        raw_num = input(prompt).strip()
        if raw_num.isdigit() and int(raw_num) >= 8:
            return int(raw_num)
        print("Enter a valid number >= 8.")


def get_bool_choice(prompt: str) -> bool:
    choice = input(f"{prompt} (y/n): ").strip().lower()
    return choice == "y"


def main():
    print("**** Welcome to the Password Generator ****")

    length = get_input("Enter desired password length (minimum 8): ")
    use_upper = get_bool_choice("Include uppercase letters?")
    use_digits = get_bool_choice("Include numbers?")
    use_symbols = get_bool_choice("Include special symbols?")

    generator = PasswordGenerator(
        length=length,
        use_uppercase=use_upper,
        use_digit=use_digits,
        use_symbols=use_symbols,
    )

    password = generator.generate()
    print(f"\n🔑 Generated Password: {password}")


if __name__ == "__main__":
    main()