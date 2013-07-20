DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'hf604^)*+x&amp;qq6%t9o*#0ceq(ky6=mg@a)0tju)rxpf%8x$zyk'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'qualita',                          
        'USER': 'vagrant',                                      
        'PASSWORD': 'latest0',                                  
        'HOST': '',                                      
        'PORT': '',                                  
    }
} 

# Amazon S3 Support
AWS_ACCESS_KEY_ID = "AKIAI7JJVSA4PR37C6HA"
AWS_SECRET_ACCESS_KEY = "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"

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = "static"
AWS_STORAGE_BUCKET_NAME = "qualita-dei-assets"

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'