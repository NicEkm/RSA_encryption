import json
import asyncio
import jwt
from urllib.parse import urlparse
from aiohttp import web
from components.Encryption import RSA
from components.Generate_keys import Generate_keys
from components.Keys import keys


decoding_key = 'asd123'



async def key_generation(request):
    """ 
    This will return public key and the modulus, and will 
    save those + private key to Keys.py file for further use. 
    """
    public_key = Generate_keys().Generate_keys()
    print(public_key)
    return web.Response(text=json.dumps(public_key))    

""" 
    This is waiting request AKA message. After it gets the encrypted message it
    starts parsing the URL to gain JWT that first needs to be decoded in order
    to gain the RSA encrypted message. Afer decoding JWT this loads
    the private key and modulus and then calls 'decrypt function' in 
    RSA module to decrypt the message and sets parameters as it is (private key, modulus (N), message).
    After decryption it will print decrypted message! 
"""

async def receive_message(request):
    if request.method == 'POST':
        url = str(request.url)
        o = urlparse(url)
        encoded_token = o.query[14:]
        decoded_token = jwt.decode(encoded_token, decoding_key, algorithms='HS256')
        private_key = keys().load()[1]
        N = keys().load()[2]
        message = decoded_token['message']
        decrypted_message = RSA().decrypt(private_key, N, message)
        print('Message received from the sender: ',decrypted_message)
        return web.Response(text='OK')


app = web.Application()
app.add_routes([
    web.get('/generate_keys', key_generation, name='key_generation'),
    web.post('/receive_message', receive_message,name='receive_message'),
])


if __name__ == '__main__':
    web.run_app(app)