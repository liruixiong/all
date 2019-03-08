"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

#项目路径

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

#当创建项目时，会自动生成 SECRET_KEY 秘钥
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6vc3*k(cl+ao6^bp)6%-(b#yk1*)0or5clm%sz9c7l^(aw#9lx'

#调试模式 ---F ---T
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#允许谁访问 （同一网段下  “*”是所有人都可以访问）
ALLOWED_HOSTS = []


# Application definition
#当前项目下所有应用列表 APP列表
#自动创建项目和应用
INSTALLED_APPS = [
    'django.contrib.admin',#django自带的后台管理APP
    'django.contrib.auth',#django自带的权限认证APP
    'django.contrib.contenttypes',#模型相关的app
    'django.contrib.sessions',#状态保持用到的app
    'django.contrib.messages',#消息相关的app
    'django.contrib.staticfiles',#管理静态资源的app
    'lrx.apps.LrxConfig',#我们创建的应用  （自动）
]
#中间件 ————>影响我们请求和响应用
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#配置url相关的
ROOT_URLCONF = 'mysite.urls'

#配置模板相关
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#配置数据库相关的
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
#配置中英文
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
#配置静态资源
STATIC_URL = '/static/'
