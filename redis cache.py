# settings.py

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Replace with your Redis server location
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}



from django.core.cache import cache
from django.utils.crypto import get_random_string
from datetime import timedelta

def generate_and_store_token():
    # Generate a random token
    token = get_random_string(length=64)

    # Set the token in the cache with an expiration time of 7 hours (timedelta)
    cache.set('my_global_token', token, timeout=timedelta(hours=7))

    return token






from django.core.cache import cache

def get_token():
    token = cache.get('my_global_token')
    return token

