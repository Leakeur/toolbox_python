import uuid
import hashlib

##FONCTION
def main():
        methode_hash = input("""Entrez la méthode de hashage : (ou "help" pour afficher toutes les méthodes possibles)\n""")
        salt = uuid.uuid4().hex

        if methode_hash == "md5" or methode_hash == "MD5":
                result = hashlib.md5(salt.encode() + word_hash.encode())
                print("Le mot hashé en md5 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha1" or methode_hash == "SHA1":
                result = hashlib.sha1(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha1 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha224" or methode_hash == "SHA224":
                result = hashlib.sha224(word_hash.encode())
                print("Le mot hashé en sha224 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha256" or methode_hash == "SHA256":
                result = hashlib.sha256(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha256 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha384" or methode_hash == "SHA384":
                result = hashlib.sha384(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha384 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha512" or methode_hash == "SHA512":
                result = hashlib.sha512(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha512 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "shake_128" or methode_hash == "SHAKE_128":
                longueur_hash = input("Entrez la longueur de hash voulue\n")
                result = hashlib.shake_128(salt.encode() + word_hash.encode())
                print("Le mot hashé en shake_128 est : ")
                print(result.hexdigest(int(longueur_hash)) + ":" + salt)

        elif methode_hash == "shake_256" or methode_hash == "SHAKE_256":
                longueur_hash = input("Entrez la longueur de hash voulue\n")
                result = hashlib.shake_256(salt.encode() + word_hash.encode())
                print("Le mot hashé en shake_256 est : ")
                print(result.hexdigest(int(longueur_hash)) + ":" + salt)

        elif methode_hash == "blake2b" or methode_hash == "BLAKE2B":
                result = hashlib.blake2b(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha256 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "blake2s" or methode_hash == "BLAKE2S":
                result = hashlib.blake2s(salt.encode() + word_hash.encode())
                print("Le mot hashé en blake2s est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_224" or methode_hash == "SHA3_224":
                result = hashlib.sha3_224(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha3_224 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_256" or methode_hash == "SHA3_256":
                result = hashlib.sha3_256(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha3_256 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_384" or methode_hash == "SHA3_384":
                result = hashlib.sha3_384(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha3_384 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "sha3_512" or methode_hash == "SHA3_512":
                result = hashlib.sha3_512(salt.encode() + word_hash.encode())
                print("Le mot hashé en sha3_512 est : ")
                print(result.hexdigest() + ":" + salt)

        elif methode_hash == "help" or methode_hash == "HELP":
                print("Méthodes de hash disponibles :\n{}\n" .format(
                    ", ".join(sorted(hashlib.algorithms_guaranteed))))
                main()

        else:
                print("La méthode de hashage n'est pas reconnue")
                main()

##PROGRAMME
word_hash = input("Entrez le mot à hasher :\n")

main()

