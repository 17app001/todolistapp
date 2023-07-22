##  建立專案  
- django-admin startproject todolist

### 啟動Server 
- python manage.py runserver 

### 同步資料庫 
- python manage.py migrate

### 建立超級使用者 
- python manage.py createsuperuser

### 新增功能 
- python manage.py startapp user

### 進行註冊
- settings.py
    - INSTALLED_APPS 
        -  "user.apps.UserConfig"

## git 流程

### add .gitignore
- 排除db.sqlite3

### git add .

### git commit -m "message"