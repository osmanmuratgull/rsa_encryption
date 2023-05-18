import random
import math

# Bir sayının asal olup olmadığını kontrol eden fonksiyon
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Anahtar çiftini oluşturan fonksiyon
def generate_key_pair(p, q):
    n = p * q  # Modül
    phi = (p - 1) * (q - 1)  # Euler phi fonksiyonu
    e = random.randrange(1, phi)  # Açık anahtar
    while math.gcd(e, phi) != 1:  # EBOB kontrolü
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)  # Özel anahtar

    return (e, n), (d, n)  # Açık anahtar, Özel anahtar

# Modüler tersini hesaplayan fonksiyon
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('Modüler ters bulunamadı.')
    return x % m

# Genişletilmiş EBOB algoritması
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

# Mesajı şifreleyen fonksiyon
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Şifreli mesajı çözen fonksiyon
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Ana program
print("RSA Şifreleme Programına Hoş Geldiniz!")
print("Lütfen asal sayılar p ve q girin.")

while True:
    try:
        p = int(input("p: "))
        if not is_prime(p):
            raise ValueError("p bir asal sayı olmalıdır.")
        q = int(input("q: "))
        if not is_prime(q):
            raise ValueError("q bir asal sayı olmalıdır.")
        break
    except ValueError as ve:
        print("Hata:", ve)

public_key, private_key = generate_key_pair(p, q)  # Açık ve özel anahtar çiftini oluştur

message = input("Şifrelenecek mesajı girin: ")
encrypted_message = encrypt(message, public_key)  # Mesajı şifrele
decrypted_message = decrypt(encrypted_message, private_key)  # Şifreli mesajı çöz

print("Şifrelenmiş mesaj:", encrypted_message)

