import hashlib


class PasswordCracker:
    passwords = []
    hashes = []
    hashed_passwords = []

    def __init__(self, password_location, hash_location):
        self.password_location = password_location
        self.hash_location = hash_location

    def password_list(self):
        with open(self.password_location, 'r') as f:
            self.passwords = [p.strip() for p in f.readlines()]

    def hash_file(self):
        with open(self.hash_location, 'r') as f:
            self.hashes = [h.strip() for h in f.readlines()]

    def get_hashes(self):
        self.hashed_passwords = [hashlib.sha256(p.encode('utf-8')).hexdigest() for p in self.passwords]

    def crack_password(self) -> str:
        for h in self.hashes:
            for p in self.hashed_passwords:
                print(h, p)
                if h == p:
                    print("=============")
                    return "Password found {}".format(p)
                else:
                    print("=" * 50)
                    return "Not found"


if __name__ == "__main__":
    password_cracker = PasswordCracker("password.txt", "hash.txt")
    password_cracker.password_list()
    password_cracker.hash_file()
    password_cracker.get_hashes()
    password_cracker.crack_password()
    print(password_cracker.crack_password())

