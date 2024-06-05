from jaanca_chronometer import Chronometer
from jaanca_utils_encrypt import EncryptionRSA

chronometer=Chronometer()
single_line=False
encryption_rsa=EncryptionRSA()

chronometer.start()
encrypt_publicKey, decrypt_privateKey = encryption_rsa.create_keys_pkcs1(len_key_in_bits=2048,single_line=single_line)
chronometer.stop()
create_keys_pkcs1=chronometer.get_elapsed_time()

chronometer.start()
plane_text="Hello World"
encrypted_text = encryption_rsa.encrypt_with_private_key_pkcs1(plane_text,encrypt_publicKey)
chronometer.stop()
encrypt_with_private_key_pkcs1=chronometer.get_elapsed_time()

chronometer.start()
decrypted_text = encryption_rsa.decrypt_with_private_key_pkcs1(encrypted_text,decrypt_privateKey)
chronometer.stop()
decrypt_with_private_key_pkcs1=chronometer.get_elapsed_time()

print(f"encrypted_text: {encrypted_text}")
print(f"decrypted_text: {decrypted_text}")
print(f"time elapsed for create_keys_pkcs1: {create_keys_pkcs1}")
print(f"time elapsed for encrypt_with_private_key_pkcs1 {chronometer.get_format_time()}: {encrypt_with_private_key_pkcs1}")
print(f"time elapsed for decrypt_with_private_key_pkcs1 {chronometer.get_format_time()}: {decrypt_with_private_key_pkcs1}")

