--- RSA_encryption ---

	My aim is to show as clearly as possible, how to use RSA to encrypt messages between two clients that are communicating for example via messages.

--- Scenario ---

	There is 2 clients. Client_1 and Client_2. Client_1 is the creator of RSA keypairs and he only have access to private key. Client_2 has some very
	secret message it wants to share privately with Client_1. Client_2 asks public key and modulus from Client_1 and then encrypts the message with it and then
	sends the message to Client_1 over HTTP JWT-token. JWT-token contains encrypted RSA message. 

--- Usage ---

	First install libraries in requirements.txt

	Then go into Client_2.py file and change "secret_message"-part to be your message that you want privately share with Client_1. It needs to be in str format!
	Then run ('$python Client_1.py') and ('$python Client_2.py'). This will start 2 aiohttp servers that exposes Client_1 to port 8080 and Client_2 to port 7070.
	Then when you have you message written in the Client_2.py and you have both servers running go into - http://localhost:7070/send_message - url and it will start encryption process
	and send the message to client_1.  !! Both servers needs to run in order to send the message !!

--- License ---

	This is for educational purposes only. Do not use this in illegal activities in any circumstances!

--- Resources ---

	https://www.youtube.com/watch?v=KS169C845aU

	https://docs.aiohttp.org/en/stable/

--- Authors ---

	Niclas Ekman