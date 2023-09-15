ALLOWED_HOSTS = ['techproducts.com']

SECRET_KEY = 'your-secret-key'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'techproducts',
        'USER': 'root',
        'PASSWORD': 'your-database-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
