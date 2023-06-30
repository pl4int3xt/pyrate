import hashlib


class PasswordCracker:
    passwords = []
    hashes = []

    def __init__(self, password_location, hash_location):
        self.password_location = password_location
        self.hash_location = hash_location

    def password_list(self):
        with open(self.password_location, 'r') as f:
            self.passwords = [p.strip() for p in f.readlines()]

    def hash_file(self):
        with open(self.hash_location, 'r') as f:
            self.hashes = [h.strip() for h in f.readlines()]

    def crack_password(self) -> None:
        for h in self.hashes:
            for p in self.passwords:
                hashed_password = hashlib.sha256(p.encode('utf-8')).hexdigest()
                if h == hashed_password:
                    print("=" * 50)
                    print("Trying {}".format(p))
                    print("=" * 50)
                    print("Password found {}".format(p))
                    print("=" * 50)


if __name__ == "__main__":
    password_cracker = PasswordCracker("password.txt", "hash.txt")
    password_cracker.password_list()
    password_cracker.hash_file()
    password_cracker.crack_password()
