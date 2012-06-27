from base_settings import *


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': { # optional
            'DB': 15,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
    },
}
