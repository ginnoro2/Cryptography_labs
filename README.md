# Cryptography_labs
### 1. Clone the Repository

```bash
git clone https://github.com/ginnoro2/Cryptography_labs.git
cd Cryptography_labs
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```


### 3. Install Python3.10
```bash
apt install Python3.10
```
All three Python files only use Python's standard library modules (itertools and built-in functions like chr, ord, zip, etc.).

### 4. Run the Script for Simple Symmetric Substitute Cipher
```bash
python3.10 Simple_sub_cipher.py

```
### OUTPUT
```bash
Original message: BAD
Encrypted message: XMT
```

### 5. Run the Script for XOR encryption 
```bash
python3.10 enc_xor.py
```

### OUTPUT
```bash
Original message: BADDAD
Encrypted message: ]^[[^[
```

### 6. Run the Script for brute force that only tries the letters 'A', 'B', and 'D' for mappings
 Limited alphabet: Only uses letters 'A', 'B', and 'D' instead of the full alphabet
The script will try all permutations of A, B, D mapped to the unique cipher letters (X, Y, Z). Since there are only 3 letters, there will be just 6 permutations total (3! = 6), making it much more manageable.
```bash
python3.10 brute_set.py
```

### OUTPUT
```bash 
Trying mapping {'X': 'A', 'Y': 'B', 'Z': 'D'}: 'BADDAD' #found the plaintext 
Trying mapping {'X': 'A', 'Z': 'B', 'Y': 'D'}: 'DABBAB'
Trying mapping {'Y': 'A', 'X': 'B', 'Z': 'D'}: 'ABDDBD'
Trying mapping {'Y': 'A', 'Z': 'B', 'X': 'D'}: 'ADBBDB'
Trying mapping {'Z': 'A', 'X': 'B', 'Y': 'D'}: 'DBAABA'
Trying mapping {'Z': 'A', 'Y': 'B', 'X': 'D'}: 'BDAADA'
```

### 7. Run the Script for brute force that decryption script for a simple substitution cipher from 26 letter alphabet

Identifies unique characters in the ciphertext (Y, X, Z)
Generates all possible permutations of 3 characters from the 26-letter alphabet ( Tries all possible injective mappings from the unique cipher characters to alphabet characters)
For each permutation, creates a mapping and applies it to decrypt the message ( Permutations: Tests all 26P3 = 26!/(26-3)! = 15,600 possible mappings )
Outputs each mapping attempt with its resulting plaintext

This is a comprehensive brute force approach that will eventually find the correct decryption by testing every possible character substitution for the cipher's unique letters.

```bash
python3.10 brute.py
```

### OUTPUT
```bash
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'I'}: 'YZIIZI'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'J'}: 'YZJJZJ'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'K'}: 'YZKKZK'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'L'}: 'YZLLZL'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'M'}: 'YZMMZM'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'N'}: 'YZNNZN'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'O'}: 'YZOOZO'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'P'}: 'YZPPZP'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'Q'}: 'YZQQZQ'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'R'}: 'YZRRZR'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'S'}: 'YZSSZS'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'T'}: 'YZTTZT'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'U'}: 'YZUUZU'
Mapping {'X': 'Z', 'Y': 'Y', 'Z': 'V'}: 'YZVVZV'
...............................................
...............................................
```

### Grep "BADDAD" 
```bash
python3.10 brute.py | grep "BADDAD"
```
### OUTPUT
```bash
Mapping {'Y': 'B', 'Z': 'D', 'X': 'A'}: 'BADDAD' #filtered output
```


