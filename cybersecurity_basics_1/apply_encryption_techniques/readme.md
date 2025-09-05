# Encryption Techniques – AES, MD5, and SHA Examples

## Summary of Key Points
![SHA](https://github.com/Jnapfx/Javier-6-months-projects/blob/main/semester_3/documentation/cybersecurity_basics_1/apply_encryption_techniques/SHA.png?raw=true)
### MD5 Hash
- Generates a 128-bit fingerprint from input data.
- Produces consistent output for the same input, making it useful for file integrity checks.
- Commonly used to store sensitive data (e.g., passwords, credit card numbers) in a hashed form.
- MD5 is not an encryption method; it is a one-way process and cannot be reversed easily.

### SHA (Secure Hash Algorithm)
- An improved version of MD5, widely used for hashing sensitive data and digital certificates.
- Operates similarly to MD5 but with stronger security.
- Uses bitwise operations, modular additions, and compression functions.
- Produces significantly different hashes even with minor changes in input data (e.g., "Heaven" vs. "heaven").
- Like MD5, SHA is also a one-way hashing method and irreversible under normal circumstances.

### Key Differences Between Hashing and Encryption
- **Hashing** is a one-way function; hashes cannot be reversed to recover the original input.
- **Encryption** is reversible; encrypted data can be decrypted using the appropriate key and algorithm.

### Common Use Cases in Cybersecurity
- Secure password storage.
- Ensuring file and data integrity.
- Verifying digital certificates and identities.

---

## AES Encryption and Decryption Example

In the following example, the Advanced Encryption Standard (AES) was used to encrypt and decrypt a message.

**Plaintext input:**
```
Why did the hacker break up with the Wi-Fi?  
Because there was no connection.
```

**Encryption details:**
- Secret key: `DAE`
- Algorithm: AES

The encryption process generates a ciphertext from the input, which can then be decrypted using the same key and algorithm to recover the original message.

**Demonstration Screenshot:**

![AES Encryption Example](https://github.com/Jnapfx/Javier-6-months-projects/blob/main/semester_3/documentation/cybersecurity_basics_1/apply_encryption_techniques/AES_encryption_example.png?raw=true)

This confirms that AES encryption is **reversible**, making it suitable for protecting sensitive data in transit or storage when decryption is required.

---

## MD5 and SHA Hashing Example

In this example, the input string was hashed using both the MD5 and SHA1 algorithms.

**Input string:**
```
Hello DAE!
```

**Output hashes:**
- MD5: `07370ab53e968f61718137547510e946`
- SHA1: `07ad921f734bacb67fb34cf10255b99e71b5125e`

**Demonstration Screenshot:**

![MD5 Hash Example](https://github.com/Jnapfx/Javier-6-months-projects/blob/main/semester_3/documentation/cybersecurity_basics_1/apply_encryption_techniques/MD5_hash.png?raw=true)

This demonstrates that hashing produces fixed-length outputs that are not reversible, making them appropriate for integrity verification and secure storage of authentication data.

---

## Conclusion

| Technique    | Reversible | Common Use Cases                              | Output Type                 |
|-------------|------------|-----------------------------------------------|-----------------------------|
| AES          | Yes        | Secure communications, encrypted storage      | Encrypted text (ciphertext) |
| MD5 / SHA1   | No         | Password storage, data integrity checks       | Hash value (digest)         |

Both encryption and hashing play essential roles in cybersecurity. While encryption ensures confidentiality through reversible encoding, hashing ensures integrity and secure data verification through irreversible transformation.

