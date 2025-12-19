from pqcrypto.kem import mceliece6960119
from Crypto.Cipher import AES
import hashlib

print("=== POST-QUANTUM SECURE MESSAGING (Classic McEliece + AES) ===\n")

# ======================================
# 1. KEY GENERATION (Receiver)
# ======================================
public_key, secret_key = mceliece6960119.generate_keypair()

print("[Receiver] Key pair generated")
print("Public Key Length :", len(public_key))
print("Secret Key Length :", len(secret_key))

# ======================================
# 2. ENCAPSULATION (Sender)
# ======================================
ciphertext_kem, shared_secret_sender = mceliece6960119.encrypt(public_key)
print("[Sender] Shared secret encapsulated")

# ======================================
# 3. KEY DERIVATION
# ======================================
aes_key_sender = hashlib.sha256(shared_secret_sender).digest()

# ======================================
# 4. MESSAGE ENCRYPTION
# ======================================
message = b"Secure Messaging menggunakan Post-Quantum Cryptography (Classic McEliece)"
cipher = AES.new(aes_key_sender, AES.MODE_GCM)
ciphertext_msg, tag = cipher.encrypt_and_digest(message)

print("[Sender] Message encrypted")

# ======================================
# 5. DECAPSULATION (Receiver)
# ======================================
shared_secret_receiver = mceliece6960119.decrypt(secret_key, ciphertext_kem)
print("[Receiver] Shared secret decapsulated")

aes_key_receiver = hashlib.sha256(shared_secret_receiver).digest()

# ======================================
# 6. MESSAGE DECRYPTION
# ======================================
cipher_dec = AES.new(aes_key_receiver, AES.MODE_GCM, nonce=cipher.nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext_msg, tag)

print("[Receiver] Message decrypted")
print("\nPLAINTEXT :", plaintext.decode())

# ======================================
# 7. VERIFICATION
# ======================================
if plaintext == message:
    print("\nSUCCESS Post-Quantum Secure Messaging berhasil")
else:
    print("\nFAILED")
