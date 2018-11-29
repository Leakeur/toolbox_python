import uuid
import hashlib


##FUNCTION WHICH HASH A WORD DEPENDING ON THE METHOD CHOSEN
def main():
        methode_hash = input("Choose one of the following method :\n{}\n" .format(
            ", ".join(sorted(hashlib.algorithms_guaranteed))))
        salt = uuid.uuid4().hex

        if methode_hash == "md5" or methode_hash == "MD5":
                result = hashlib.md5(salt.encode() + word_hash.encode())
                print("The word hashed in md5 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha1" or methode_hash == "SHA1":
                result = hashlib.sha1(salt.encode() + word_hash.encode())
                print("The word hashed in sha1 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha224" or methode_hash == "SHA224":
                result = hashlib.sha224(word_hash.encode())
                print("The word hashed in sha224 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha256" or methode_hash == "SHA256":
                result = hashlib.sha256(salt.encode() + word_hash.encode())
                print("The word hashed in sha256 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha384" or methode_hash == "SHA384":
                result = hashlib.sha384(salt.encode() + word_hash.encode())
                print("The word hashed in sha384 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha512" or methode_hash == "SHA512":
                result = hashlib.sha512(salt.encode() + word_hash.encode())
                print("The word hashed in sha512 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "shake_128" or methode_hash == "SHAKE_128":
                longueur_hash = input("Enter the length of your hash\n")
                result = hashlib.shake_128(salt.encode() + word_hash.encode())
                print("The word hashed shake_128 is : ")
                print(result.hexdigest(int(longueur_hash)) + ":" + salt)

        elif methode_hash == "shake_256" or methode_hash == "SHAKE_256":
                longueur_hash = input("Enter the length of your hash\n")
                result = hashlib.shake_256(salt.encode() + word_hash.encode())
                print("The word hashed in shake_256 is : ")
                print(result.hexdigest(int(longueur_hash)) + ":" + salt)

        elif methode_hash == "blake2b" or methode_hash == "BLAKE2B":
                result = hashlib.blake2b(salt.encode() + word_hash.encode())
                print("The word hashed in sha256 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "blake2s" or methode_hash == "BLAKE2S":
                result = hashlib.blake2s(salt.encode() + word_hash.encode())
                print("The word hashed in blake2s is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_224" or methode_hash == "SHA3_224":
                result = hashlib.sha3_224(salt.encode() + word_hash.encode())
                print("The word hashed in sha3_224 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_256" or methode_hash == "SHA3_256":
                result = hashlib.sha3_256(salt.encode() + word_hash.encode())
                print("The word hashed in sha3_256 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_384" or methode_hash == "SHA3_384":
                result = hashlib.sha3_384(salt.encode() + word_hash.encode())
                print("The word hashed in sha3_384 is : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_512" or methode_hash == "SHA3_512":
                result = hashlib.sha3_512(salt.encode() + word_hash.encode())
                print("The word hashed in sha3_512 is : ")
                print(result.hexdigest() + ":" + salt)

        else:
                print("Unknown method, try another one")
                main()

##PROGRAM
word_hash = input("Enter a word to hash :\n")

main()
