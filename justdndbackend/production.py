DEBUG = False

ALLOWED_HOSTS = ['justrolldnd.com',
                 'https://justrolldnd.herokuapp.com/', 'justrolldnd.herokuapp.com']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
