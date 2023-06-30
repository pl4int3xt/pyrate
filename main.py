import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-P", help="password file path")
parser.add_argument("-H", help="hash file path")
parser.add_argument("-alg", help="hash type")
parser.add_argument("-v", help="increase output verbosity", action="store_true")
args = parser.parse_args()


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
                if args.alg == "SHA-256":
                    hashed_password = hashlib.sha256(p.encode('utf-8')).hexdigest()
                elif args.alg == "SHA-1":
                    hashed_password = hashlib.sha1(p.encode('utf-8')).hexdigest()
                elif args.alg == "SHA-512":
                    hashed_password = hashlib.sha512(p.encode('utf-8')).hexdigest()
                else:
                    hashed_password = hashlib.md5(p.encode('utf-8')).hexdigest()

                if args.v:
                    print("=" * 50)
                    print("Trying {}".format(p))
                if h == hashed_password:
                    print("Password found {}".format(p))
                    print("=" * 50)


if __name__ == "__main__":
    password_cracker = PasswordCracker(args.P, args.H)
    print("""
       ________  ________  ________  ________  ________  ________ 
      /        \/    /   \/        \/        \/        \/        \/
     /         /         /         /         /        _/         /
    //      __/\__      /        _/         //       //        _/ 
    //_____/     \_____/\____/___/\___/____/ \______/ \________/      
    """)
    password_cracker.password_list()
    password_cracker.hash_file()
    password_cracker.crack_password()
