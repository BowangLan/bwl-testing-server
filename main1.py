from fastapi import FastAPI
import uvicorn
import os

# import routes

if __name__ == '__main__':
    certkey = os.path.abspath('./example.com+6-key.pem')
    certfile = os.path.abspath('./example.com+6.pem')
    uvicorn.run(
        'main:app', 
        reload=True, 
        host='192.168.0.26', 
        port=8000, 
        ssl_keyfile=certkey, 
        ssl_certfile=certfile
    )
