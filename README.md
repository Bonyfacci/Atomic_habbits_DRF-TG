# Atomic_habits_DRF-TG
Атомные привычки: как создавать привычки. Трекер полезных привычек

***
Шаг 1 - установить библиотеки

celery==5.3.4  
coverage==7.3.2  
Django==4.2.7  
django-celery-beat==2.5.0  
django-cors-headers==4.3.0  
django-filter==23.3  
djangorestframework==3.14.0  
djangorestframework-simplejwt==5.3.0  
drf-spectacular==0.26.5  
drf-yasg==1.21.7  
psycopg2==2.9.9  
python-dotenv==1.0.0  
redis==5.0.1  
requests==2.31.0

***
Шаг 2 - Создать проект Django и приложения

django-admin startproject config .  
python manage.py startapp app_habbits  
python manage.py startapp users

***
Шаг 3 - Создать базу данных в Postgres

psql -U postgres  
create database habbits;  
\q

***
Шаг 4 - Настроить config/settings.py

INSTALLED_APPS = [  
    ...  
    # Приложения
    'app_habbits.apps.AppHabbitsConfig',
    'users.apps.UsersConfig'  
]

DATABASES = {  
    'default': {  
        # 'ENGINE': 'django.db.backends.sqlite3',  
        # 'NAME': BASE_DIR / 'db.sqlite3',  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': os.getenv('DATABASE_NAME'),  
        'USER': os.getenv('DATABASE_USER'),  
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),  
        'HOST': os.getenv('DATABASE_HOST'),  
        'PORT': os.getenv('DATA_PORT'),  
    }  
}

***
Шаг 5 - Настройка приложения app_habits
add Model
add Admin
add Serializers
add views
add urls

***
Шаг 5 - Настройка приложения users
add Model
add Admin
add Serializers
add views
add urls

***
Шаг 6 - Миграции
python manage.py makemigrations
python manage.py migrate
python manage.py csu

***
