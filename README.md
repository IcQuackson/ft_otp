
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
      <img alt="42" src="https://i.imgur.com/FBTPTt0.png" width="300px"/>
    </div>
  </div>

  <h2>What is HOTP?</h2>
  <p>HOTP is a method to generate a one-time password using a secret key and a counter to ensure secure authentication.</p>

  <h2>Why is it important?</h2>
  <p>It prevents password reuse and ensures that each login attempt is unique, enhancing security against unauthorized access.</p>
  
  <h2>How it works</h2>
  <p>
    This program allows you to store an initial password in file and is also capable of generating a new one time password every time it is requested.
  </p>
  <p>Usage:</p>
  <pre>
    <code>
      ft_otp -g file_with_hexadecimal_key.txt
      ft_otp -k key_file.key
    </code>
  </pre>
  <p> <strong>-g:</strong> The program receives as argument a hexadecimal key of at least 64 characters. The program stores this key safely in a file called ft_otp.key, which
    is encrypted.</p>
  <p> <strong>-k:</strong> The program generates a new temporary password based on the key given</p>
  <p>Below is an example of use:</p>
  <pre>
    <code>
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
    </code>
  </pre>

  <h2>Features</h2>
  <p>The program uses the HOTP algorithm <a href="https://www.ietf.org/rfc/rfc4226.txt">RFC 4226</a></p>
  <p>The generated one-time password is random and always contains the same format, i.e. 6 digits.</p>
  <p>The program creates a QR Code with seed generation.</p>

  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
