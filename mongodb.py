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
