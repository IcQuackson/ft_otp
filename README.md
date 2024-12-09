
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <div class="center-text">
    <h1 align="center">
    	🔓 ft_otp 🔓
    </h1>
    <h3 align="center">
      <i>
    	  Introductory project to the notion of OTP with the use of the RFC HOTP. 
      </i>
    </h3>
    <div align="center">
      <img alt="hotp" src="https://github.com/user-attachments/assets/dce405cb-a33d-41ed-94a8-0f4e5b73d6d5" />
    </div>
  </div>


## What is HOTP?

HOTP (HMAC-Based One-Time Password) is a method to generate a one-time password using a secret key and a counter to ensure secure authentication.

## Why is it important?

It prevents password reuse and ensures that each login attempt is unique, enhancing security against unauthorized access.

## How it works

This program allows you to store an initial password in a file and is also capable of generating a new one-time password every time it is requested.

### Usage:

```
ft_otp -g file_with_hexadecimal_key.txt
ft_otp -k key_file.key
```

- **`-g:`** The program receives as an argument a hexadecimal key of at least 64 characters. The program stores this key safely in a file called `ft_otp.key`, which is encrypted.
- **`-k:`** The program generates a new temporary password based on the key given.

Below is an example of use:

```
$ echo -n "NEVER GONNA GIVE YOU UP" > key.txt
$ ./ft_otp -g key.txt
./ft_otp: error: key must be 64 hexadecimal characters.
$ [..]
$ cat key.hex | wc -c
64
$ ./ft_otp -g key.hex
Key was successfully saved in ft_otp.key.
$ ./ft_otp -k ft_otp.key
836492
$ sleep 60
$ ./ft_otp -k ft_otp.key
123518
```

## Features

- The program uses the HOTP algorithm as described in [RFC 4226](https://www.ietf.org/rfc/rfc4226.txt).
- The generated one-time password is random and always contains the same format, i.e., 6 digits.
- The program creates a QR Code with seed generation.

## More about RFC HOTP

### Key components:

- **Secret Key (K):** A shared private key known by both the client (user) and the server.
- **Counter (C):** A moving number, incremented each time a password is generated. Both the client and server must keep the same counter.
- **HMAC-SHA1:** A cryptographic function used to combine the secret key and counter into a hash.
- **Digits (d):** The length of the OTP (6 digits in our case).

### Steps to generate an HOTP:

Refer to the detailed steps above for generating an HOTP.


1. **Take the counter value:**
   - The counter (C) is an integer, but it is treated as an 8-byte (64-bit) binary value for processing.

2. **Compute the HMAC:**
   - Use the secret key (K) and the counter (C) to compute the HMAC. The result is a 20-byte hash (since SHA-1 produces a 160-bit hash).

3. **Perform dynamic truncation:**
   - Extract a 4-byte portion of the hash:
     - Take the last nibble (4 bits) of the HMAC to determine an offset value (o).
     - Extract the 4 bytes starting at the offset (o) in the HMAC.
     - Convert these 4 bytes into a 31-bit positive integer (code).
      ![image](https://github.com/user-attachments/assets/e177fdec-848b-4440-b0fb-3f5a9553b4ff)



4. **Reduce the code to the desired number of digits:**
   - Take `code % 10^d` to reduce to 6 digits.


  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
