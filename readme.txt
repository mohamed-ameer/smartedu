
#### 1- Update Agora credentals
In order to use this project you will need to replace the agora credentials in `views.py` and `streams.js`.

Create an account at agora.io and create an `app`.
Once you create your app, you will want to copy the `appid` & `appCertificate` to update `views.py` and `streams.js`.
If you have questions about where to get your app I'd recommend referencing this link `https://youtu.be/HX6AM_1-jNM?t=88`

###### views.py
```
def getToken(request):
    appId = "YOUR APP ID"
    appCertificate = "YOUR APPS CERTIFICATE"
    ......
```

###### streams.js
```
....
const APP_ID = 'YOUR APP ID'
....
```


#### 2 - Start server
```
python manage.py runserver
```


=>python -m venv .\venv
=>venv\scripts\activate
=>pip install -r requirements.txt
=>python manage.py makemigrations
=>python manage.py migrate
=>python manage.py createsuperuser
=>python manage.py runserver