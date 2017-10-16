# Cryptocurrencies and decentralized ledgers

## Project 1

### Python code
- About finding Bitcoin vanity addresses in parallel
- Convert private key to public key and bitcoin address in various formats (hex, base58, bytes)
- Generate private keys in base58

#### Instructions
1. Make sure you have **Python 3.x** installed. It may also work with Python 2.x.
2. Install the required Python libraries (**ecdsa** and **base58**) by entering the following in a terminal:

   ```
   pip3 install -r requirements.txt
   ```
   
   For Python 2.x, use:
   
   ```
   pip install -r requirements.txt
   ```

3. Edit the bottom part of the code to choose what you want to do. 

4. Run the program on multiple cores with the following from the terminal, in the right directory:

   ```
   python exercise1.py
   ```
   
#### Time required for vanity addresses search
- This program achieves 24 bitcoin addresses checks per second per **core** (2.5GHz Intel processor)
- Each character in the base 58 Bitcoin address represents log(58)/log(2) = 5.857 bits
- Hence for each letter added to the prefix required, the average time required to find the vanity address and the corresponding keypair is multiplied by 5.857.
- For example, requiring *abc* as the prefix would require us 5.857 x 5.857 = 34.3 times more time than having only *a* as the prefix.
- Example case:
	- To find **ab** as a prefix for an address, it took the program 67 seconds on 3 cores (2.5GHz Intel processor), although this is random...