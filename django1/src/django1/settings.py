"""
Django settings for django1 project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls.base import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGIN_URL = reverse_lazy('cl:signin')

LOGIN_REDIRECT_URL = reverse_lazy('blog:index')

#인증관련 모듈
AUTHENTICATION_BACKENDS = (
    #구글로그인 처리 관련 파이썬 클래스 추가
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    
    #소셜로그인 정보를 django의 User모델클래스에 저장하기위한 클래스
    'django.contrib.auth.backends.ModelBackend',
)

#구글 개발자 사이트에서 발급받은 ID, PASSWORD 저장
SOCIAL_AUTH_GOOGLE_PLUS_KEY = '960796369438-daavhhdhi8sptprj120d6vb8mklq6cpi.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = '7bOtnGsvxwAxtfP3U-VT0Voq'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b=2q!!ocv!vana!y_lhot@7$y37l*_#u9%&by8i_z6k01a)lw5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
#프로젝트 내에서 실행할 어플리케이션을 등록/관리하는 변수
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark',
    'vote',
    'customlogin',
    'blog',
    #pip install social-auth-app-django 명령어 필요
    'social_django'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                #소셜로그인 처리를 위한 탬플릿관련함수 추가
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'django1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#클라이언트의 요청으로 저장하는 미지어 파일 (이미지, 첨부파일) 설정
#MEDIA_URL:  URL 주소로 파일 주소를 접근할 때 사용하는 URL을 저장하는 변수
MEDIA_URL = '/files/'
#MEDIA_ROOT: 실저 파일이 저장되는 하드웨어 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
#C:/files/폴더에 저장되도록 설정
#MEDIA_ROOT = 'c:/files'
#MEDIA_URL과 MEDIA_ROOT를 설정한 뒤, 메인 URLconf에서 URL과 하드웨어 경로를 메칭하는 작업을 수행해야함