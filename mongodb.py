from pymongo import MongoClient
import ssl

def check_mongodb_connection():
    # MongoDB connection parameters for a remote server with certificate and username/password authentication
    mongodb_host = 'your_remote_mongodb_host'
    mongodb_port = 'your_remote_mongodb_port'
    certificate_file = 'path/to/your/certificate.pem'
    mongodb_username = 'your_mongodb_username'
    mongodb_password = 'your_mongodb_password'

    # Configure SSL certificate options
    ssl_options = {
        'ssl': True,
        'ssl_ca_certs': certificate_file,
    }

    try:
        # Create a MongoDB client with certificate and username/password authentication
        uri = f'mongodb://{mongodb_username}:{mongodb_password}@{mongodb_host}:{mongodb_port}/'
        client = MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE, ssl=ssl_options)

        # Check if the connection was established (no exception raised)
        return True
    except Exception as e:
        # Connection error with details
        return str(e)

# Check the MongoDB connection status
connection_status = check_mongodb_connection()
if connection_status is True:
    print("Connected to MongoDB")
elif connection_status is False:
    print("Failed to connect to MongoDB")
else:
    print(f"Error: {connection_status}")




==================================================================\\



from pymongo import MongoClient
import urllib.parse

def check_mongodb_connection():
    # MongoDB connection parameters for a remote server with certificate and username/password authentication
    mongodb_host = 'your_remote_mongodb_host'
    mongodb_port = 'your_remote_mongodb_port'
    certificate_file = 'path/to/your/certificate.pem'
    mongodb_username = 'your_mongodb_username'
    mongodb_password = 'your_mongodb_password'

    # Escape username and password
    escaped_username = urllib.parse.quote_plus(mongodb_username)
    escaped_password = urllib.parse.quote_plus(mongodb_password)

    try:
        # Create a MongoDB client with certificate and username/password authentication
        uri = f'mongodb://{escaped_username}:{escaped_password}@{mongodb_host}:{mongodb_port}/?ssl=true&ssl_ca_certs={certificate_file}'
        client = MongoClient(uri)

        # Check if the connection was established (no exception raised)
        return True
    except Exception as e:
        # Connection error with details
        return str(e)

# Check the MongoDB connection status
connection_status = check_mongodb_connection()
if connection_status is True:
    print("Connected to MongoDB")
elif connection_status is False:
    print("Failed to connect to MongoDB")
else:
    print(f"Error: {connection_status}")




==============================================================================================
The error message [SSL: CERTIFICATE _VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:997) means that the SSL/TLS certificate verification process failed because the certificate being presented by the server is self-signed.

A self-signed certificate is a certificate that has been signed by the same entity that created it. This means that the certificate is not trusted by any trusted certificate authority (CA).

By default, most clients will verify the SSL/TLS certificate presented by the server before establishing a connection. This is done to ensure that the server is who it claims to be and to protect the client from man-in-the-middle attacks.

If you are getting this error message, it means that the client is refusing to connect to the server because the server's certificate is self-signed. There are two ways to resolve this issue:

Install the server's certificate in the client's trust store. This will tell the client to trust the server's certificate, even though it is self-signed.
Disable SSL/TLS certificate verification. This is not recommended, as it will leave the client vulnerable to man-in-the-middle attacks.
If you are not sure how to install the server's certificate in the client's trust store, you should consult the documentation for the client software you are using.

Here are some additional things you can do to troubleshoot this error:

Make sure that the server's certificate is valid. You can do this by checking the certificate's expiration date and by verifying the certificate's signature.
Make sure that the client's trust store is up to date. If the client's trust store does not contain the server's certificate, then the client will not be able to verify the certificate.
Try restarting the client software. This can sometimes fix minor software glitches.
Try connecting to the server from a different computer. If you can connect to the server from a different computer, then the problem is with the client computer.
If you are still having problems, you should contact the server administrator for assistance.
