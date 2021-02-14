import requests
import asyncio
import json
import urllib
import jwt
from components.Encrypt_message import Encryption
from aiohttp import web

RSA_key_endpoint = 'http://127.0.0.1:8080/generate_keys'
encoding_key = 'asd123'
receiver_url = 'http://127.0.0.1:8080/receive_message?'
secret_message = str('Very secret message that no one can see!') # <-- this is the message that is sended. It needs to be str!


async def get_public_key(request):
    """
    This will ask public key and modulus from the client 1.
    These are safe to share since they are used to encrypt 
    messages in RSA. You can encrypt anything with them,
    but only Private key (that is only known by client 1 in this example)
    can decrypt messages that has been encrpyted with this specific public key
    and modulus. 
    """
    response = requests.get(RSA_key_endpoint).json()
    public_key = response['pk']
    modulus = response['N']
    data = {'pk':public_key,
            'N':modulus}
    return data


async def create_message_that_you_want_to_encrypt(request):
    message = secret_message 
    public_key = await get_public_key(request)
    print('Public Key and modulus that were generated: ', public_key)
    pk = public_key['pk']
    N = public_key['N']
    encrypted_message = Encryption().encrypt(pk, N, message)
    print('Enrypted message with RSA: ', encrypted_message) 
    payload = {
        "message":encrypted_message
    }

    """
    Now you can either send this 'encrypted message'- that was just created to the receiver through
    any resource (message, email, HTTP.. etc.) and it will be safe to send.
    It is fully encrypted with RSA and it's nearly impossible to decrypt without the private key, that is only known
    from the client 1. 

    This is okay but usually when we are working especially with HTTP - requests this 'encrypted message'- is not pretty to send over 
    HTTP. That's why we use standard JWT (JSON WEB TOKENS), to make it pretty to send it through HTTP, and it still 
    remains safe and untouchtable. 

    Let's create Json Web Token that can be sent to client 1. 

    !!! Remember that there is 'Encoding_key' created at the beginning of this file and this needs to be known for both
    sender and receiver to be able to encode and decode the JWT. You can change it what ever you like, but keep it
    safe from everyone else beside you and receiver. !!!
    """

    # This creates JWT
    encoded_token = jwt.encode(payload, encoding_key, algorithm='HS256')
    data = {
        'encoded_token':encoded_token
    }
    
    # Make JWT to fit to the url by creating url parameter out of it. 
    data_to_param = urllib.parse.urlencode(data)
    new_receiver_url = receiver_url + data_to_param

    try:
        requests.post(new_receiver_url)
    except Exception as e:
        return print(e)
    return web.Response(text='Encrypted message was succesfully encrypted with RSA and is now sent to the receiver.')
 


app = web.Application()
app.add_routes([
    web.get('/gain_keys', get_public_key, name='key_gaining'),
    web.get('/send_message', create_message_that_you_want_to_encrypt, name='send_message'),
])


if __name__ == '__main__':
    web.run_app(app, port=7070)