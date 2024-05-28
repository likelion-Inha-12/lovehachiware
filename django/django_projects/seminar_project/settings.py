from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# -> 현재 파일의 디렉토리 경로를 기준으로 상위 디렉토리를 참조하여 프로젝트의 기본 디렉토리를 설정


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-le88gilp)+kp94%wmhay!(nk!u^6orjkipr9k0u09fjp4a_38c'
# -> Django 애플리케이션의 보안에 사용되는 비밀 키로, 애플리케이션의 보안을 강화하기 위한 키입니다!
# 실제 프로젝트에서는 노출되어서는 안되는 키입니다!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# -> 디버그 모드를 설정하며, 개발 중에는 True로 유지하여 디버깅 정보를 보여준다.어디서 에러가 나오는지.

ALLOWED_HOSTS = ["*"]
# 허용된 호스트의 목록으로, 배포 환경에서 웹 애플리케이션이 서비스하는 도메인을 설정한다

# Application definition

INSTALLED_APPS = [
    # my app
    'util',
    'lionapp',
    'users',
    # third party app
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    # Basic App
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# -> Django 미들웨어의 목록으로, 요청과 응답 처리 사이에 동작하는 기능들을 제어합니다.


# 인증 인가와 커스텀 유저

AUTH_USER_MODEL = 'users.User' # 커스텀 유저를 장고에서 사용하기 위함

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 인증된 요청인지 확인
        #'rest_framework.permissions.AllowAny',  # 누구나 접근 가능 
				# (기본적으로 누구나 접근 가능하게 설정하고, 인증된 요청인지 확인하는 api를 따로 지정하게 하려면 
				# 이 옵션을 위의 옵션 대신 켜주어도 됩니다!)
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT를 통한 인증방식 사용
    ),
}      # Django REST framework 설정으로, API의 권한 및 인증 방식을 설정합니다.

REST_USE_JWT = True # JWT를 기본 인증 방식으로 사용하도록 설정

SIMPLE_JWT = {  # JWT 설정으로, JSON Web Token의 특정 속성을 설정합니다.
    'SIGNING_KEY': 'hellolikelionhellolikelion',   #숨겨줘야하는 값임
    # JWT에서 가장 중요한 인증키입니다! 
	# 이 키가 알려지게 되면 JWT의 인증체계가 다 털릴 수 있으니 노출되지 않게 조심해야합니다!
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),  #access 토큰 유효기간 1시간
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # refresh 토큰 유효기간 7일
    'ROTATE_REFRESH_TOKENS': False, # True로 설정하면 리프레시 토큰이 사용될 때마다 새로운 리프레시 토큰이 발급됩니다.
    'BLACKLIST_AFTER_ROTATION': True,   # 리프레시 토큰 회전 후, 이전의 리프레시 토큰이 블랙리스트에 추가될지 여부를 나타내는 부울 값입니다. 
		# True로 설정하면 리프레시 토큰이 회전되면서, 이전의 리프레시 토큰은 블랙리스트에 추가되어 더 이상 사용할 수 없게 됩니다.
}

#CORS

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [  # 허용할 옵션
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [  # 허용할 헤더
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'seminar_project.urls'
# -> 프로젝트의 최상위 URL 설정 파일을 지정합니다. 
# (따라서 url은 seminar_project의 urls.py 파일을 항상 먼저 보는 것입니다!)

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
            ],
        },
    },
]           # admin 페이지를 구성할 때 필요합니다!

WSGI_APPLICATION = 'seminar_project.wsgi.application'
# -> 프로젝트의 WSGI 애플리케이션을 지정합니다.

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}       # 데이터베이스 연결 설정으로, 현재는 SQLite를 사용하고 있습니다.


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },# 사용자의 아이디와 유사한 비밀번호를 허용하지 않음
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },# 비밀번호가 설정된 길이 보다 짧지 않도록 검사
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },# 널리 사용되는 암호 목록과 일치하는 비밀번호를 거부합니다. 널리 사용되는 암호를 피하고 보안을 강화합니다. (이거 찾아보면 금지해놓은 재밌는 암호들이 많았던 것으로 기억합니다...ㅋㅋ)
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },# 비밀번호에 숫자가 포함되어 있는지 확인하여, 숫자를 사용하도록 유도합니다.
] # 비밀번호 유효성 검사기 설정으로, 사용자 비밀번호의 강도를 제어합니다.


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True
USE_TZ = True
# 국제화 및 시간대 사용 여부를 설정합니다. 웬만하면 그대로 두시는 것을 추천합니다!


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# 정적 파일(사진 같은..)의 URL을 설정합니다.

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# 기본 자동 생성 필드를 생성합니다.

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'BearerAuth': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': "JWT Token"
        }
    },
    'SECURITY_REQUIREMENTS': [{
        'BearerAuth': []
    }]
}