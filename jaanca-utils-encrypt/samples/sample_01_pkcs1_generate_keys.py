from jaanca_chronometer import Chronometer
from jaanca_utils_encrypt import EncryptionRSA

chronometer=Chronometer()
single_line=False
encryption_rsa=EncryptionRSA()
chronometer.start()
encrypt_publicKey, decrypt_privateKey = encryption_rsa.create_keys_pkcs1(len_key_in_bits=2048,single_line=single_line)
chronometer.stop()

print(" encrypt_publicKey ")
print(encrypt_publicKey)

print(" decrypt_privateKey ")
print(decrypt_privateKey)

print(f"time elapsed {chronometer.get_format_time()}: {chronometer.get_elapsed_time()}")

# output

#  encrypt_publicKey 
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEApzSc83nUScDDjlLaPu7tUfm/L+5NouMsTlCAK8i+AISwcXWzN0Xl
# wR4tOil2d3002K/XZJDw0U1tcRJMejgJSXrqTcUwT4wpXES9mCAav3x6BjFvne3f
# xSdij5cc7+ixbE9ovs0kLb3beUMECQLRQpc/Ac5001rnV5x6/0n9ay0jaHHqWvzU
# uDtCwa+PqNYM7Ir5Vt1Nik+dqsY9yOzGQK6BlTCEYGsEX76g5HmMFK1g9E1mGYJX
# eAq45PUY84xkLNY5sfi65MvxELk2EtNIHRblJCFB/TvNuchh3CpmvNsi9FpVLHvU
# 6MTXubo5IlCV3FECUhF4LU/TxIsFvqz5WQIDAQAB
# -----END RSA PUBLIC KEY-----

#  decrypt_privateKey
# -----BEGIN RSA PRIVATE KEY-----
# MIIEqQIBAAKCAQEApzSc83nUScDDjlLaPu7tUfm/L+5NouMsTlCAK8i+AISwcXWz
# N0XlwR4tOil2d3002K/XZJDw0U1tcRJMejgJSXrqTcUwT4wpXES9mCAav3x6BjFv
# ne3fxSdij5cc7+ixbE9ovs0kLb3beUMECQLRQpc/Ac5001rnV5x6/0n9ay0jaHHq
# WvzUuDtCwa+PqNYM7Ir5Vt1Nik+dqsY9yOzGQK6BlTCEYGsEX76g5HmMFK1g9E1m
# GYJXeAq45PUY84xkLNY5sfi65MvxELk2EtNIHRblJCFB/TvNuchh3CpmvNsi9FpV
# LHvU6MTXubo5IlCV3FECUhF4LU/TxIsFvqz5WQIDAQABAoIBADsiZmfNrICxBfht
# 4PXk9lXJqA5Bj3+OLHs+CTZy9o+kXeqin9FqjQkxrPkm9NjplSkVd23/vMupQI1+
# 1UFcVByCth7vIFjhzzbssMj+gbc7RMSv8zO9jyhg94ClBvzqJOWTaA4i6yqqPNa0
# FtdBAdU1PHldFQAy49JLh8cQ4aCz9YWV28VX2ujg29+L6d9nuQLuDswwAj+rLmWF
# aF8QlEahglVrW8cxjrShkFC5DkKMZCLJ72jf9gi/QcmgGjUFS+h5qaGwadL+PidE
# l1CPcn4P5e0QrjHuAC//Y4djbvmUGF5zRN1qsx+v3Mimx1+iO8vYWm8G9/zhOhve
# nS2YYQkCgYkA4x2/9JFxcIEqda8F9FytH6EyzjCULE7zU42bVSXbd9yXRc7maiCd
# lc8jeP35cm2KFrk8+WWer2hJuKQvqUL7HXs3Egr4tknEj4YqeP7zbbS3pncwl9ky
# 3CHootFDl9YYPyCYUfzbGBTgfCFVcqY4Z1MY1FfeJsletfsBSkQwoK6diTh6VpTM
# 5wJ5ALx4V/abDKWUWBPm5Srh9gahCcJTocN8HBuYnbbIInutr7bOWCSHMJ9Xs1I+
# EpfdcHtJ+IjuopHwKCcPNSdVfOCmR5GJ5Y1jlwl8ZSQhn2zjB057pGNUlZvkS1cG
# 1M+ed6XIyWEHnFMzMd2AHt7Ow2vgOTzt1kL/vwKBiCONXaYYOmzFG3NuoXz+IO+p
# mT1jp15EQZzbtuweT/u0YU3BNJp6XpC76y6eezTpZstl1eCogq2sopWvxfI2FP8p
# cZZ2dzZ517Yr52wnZM3Qk0sQr1+l1WtWN4d9QJp9HjCLlqyG63kak4V65lhbIssx
# 29opoxHpRdUw5KPOhtowW2LGn4f8JRMCeDAIv+qDI9sDjtsrqtaeFnUkD/euFvla
# pVNHN1MBeQBqiPEfcAmHRxYlZPeeCGEaN/PEK4rCvz5QpfsmfhaTTCt5VZ47Nf0u
# F618Pc7Snu5Cgnc3PfNu+F5t9eGtRQnRSo8/OEv5g5cU4i2g3L1OlzHkSNJFj6kt
# wwKBiQCzu8agMoUTEOfiEvbJ6aYf1q1LTwxqcCAjo6ZMujWVKHa6A8+edFwVLPoN
# 0D9YyrFKOPm1LTaBwDzvnsjXQbpZ6iGHVyx1VSG8BkVR5hwEmwfNf2Zxsd6odt0D
# AXo0mIqqo8pnr+6DIu9yqd7Rhf9BVMcIZnXCIf0NQoRYU8VsCrqaB4H9AQMJ    
# -----END RSA PRIVATE KEY-----

# time elapsed HH:mm:ss: 00:00:04
