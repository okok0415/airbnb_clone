Django in Window 10

1. python 3.7.3 설치

2. python --version으로 확인

3. pip install --user pipenv

4. pipenv로 확인

인식이 되지 않으면

4.1
pip uninstall virtualenv
pip uninstall pipenv
pip install pipenv
이후
pipenv하면 작동됨

5. mkdir (파일명)

6. cd (파일명)

7.pipenv --three

7.1 anaconda나 python을 비정상적으로 지우게되면 Error발생.
다시 깔고 제어판에서 지우면 정상적으로 찾아감.

\*\*\*8. 컴퓨터를 껐다가 킬 때면 항상 쳐야 하는 것! (가상환경 키기 즉 버블 안에 들어가기)
pipenv shell

9. pipenv install Django==2.2.5

#1.3 git

1. git init

2. git remote https://github.com/okok0415/(만든 git repository명).git

3. git add .

4. git commit -m "alalalal"

5. touch README.md

6. touch .gitignore

(touch 명령어를 알아 듣지 못한다면 그냥 README.md 파일과 .gitignore파일을 만든다

7. README에는 원하는 것들을 쓰고

8. .gitignore은 git에 올리고 싶지 않은 것을 설정할 수 있다
   google에 gitignore python이라고 치고 처음 나오는것 복사 붙여넣기 하자.

#2.0 튜토리얼 형식이 아닌 개발자들이 Django project를 만드는 방법

1. django-admin startproject config // config폴더 생성

2. rename config to Aconfig(or whatever)

3. 안쪽에 있는 config를 바깥으로 내보낸다.

4. Aconfig를 지운다.

5. Python interpreter을 pipenv가 있는 version으로 바꾼다.

6. 파일 -> 기본설정 -> 설정으로 flake8를 enable한다.

or .vscode에 있는 settings.json에 밑에 3줄을 복사 붙여넣기 한다.
/_
{
"python.pythonPath": "C:\\Users\\dlawj\\..."
"python.linting.flake8Enabled": true,
"python.linting.pylintEnabled": false,
"python.linting.enabled": true
}
_/

7. pipenv install flake8 --dev 을 입력해서 flake8 설치

8. pipenv install black --dev --pre 설치

9. 파일 -> 기본설정 -> 설정 python formatting provider -> black으로 바꿈

or
/_
{
"python.pythonPath": "C:\\Users\\dlawj\\.virtualenvs\\airbnb_clone-fNd_eUmz\\Scripts\\python.exe",
"python.linting.flake8Enabled": true,
"python.linting.pylintEnabled": false,
"python.linting.enabled": true,
"python.formatting.provider": "black"
}
_/

10. 파일 -> 기본설정 -> 설정 format on save를 클릭하면 저장할 때마다 format을 한다.(default로 설정되어 있음)

11. settings.py에 들어갔을 때 에러가 4개 뜬다면 정상이다.

12. settings.json에 들어가서
    {
    "python.pythonPath": "C:\\Users\\dlawj\\.virtualenvs\\airbnb_clone-fNd_eUmz\\Scripts\\python.exe",
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.enabled": true,
    "python.formatting.provider": "black",
    "python.linting.flake8Args": ["--max-line-length=88"]
    }
    로 변경하면 에러가 하나로 줄어든다(한개는 그냥 놔두자)

#2.2 Django 설정

1. settings.py 에 들어가서 TIME_ZONE = "Asia/Seoul"로 바꿈

2. python manage.py runserver으로 서버 실행

3. 웹사이트에 들어가서 http://127.0.0.1:8000/admin/으로 접속하면 로그인 창이뜸

4. python manage.py createsuperuser
   blank
   blank
   123
   123

ID -> dlawj
PW -> 123

/\*
Migration이란?

1.  데이터 유형이 변경되면
2.  migration을 생성하고
3.  해당 migration을 적용
4.  Database로 업데이트

-> 데이터베이스와 Django를 동기화 하는 형식

5.  python manage.py migrate // sqlite3 동기화

#2.5 Application

1.Project를 계획하고 만든다.

2. django-admin startapp rooms

3. django-admin startapp users

4. django-admin startapp reviews

5. django-admin startapp conversations

6. django-admin startapp lists

7. django-admin startapp reservations

8. 만든 app들은 이름을 바꾸면 안된다.
   Django는 FrameWork이기 때문(react는 그냥 library를 호출하는 것이지만 이건 아님)

9. admin.py Admin 패널에 적용하기 위한 곳

10. app.py -> configuration(배열 배치)

11. models.py DATABASE!!

12. views.py 유저들이 보는 곳!!

13. config의 url이 너무 많아질걸 우려해 users/urls.py를 만들자

#3.0 Users App

/\*

settings.py AUTH_USER_MODEL

https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

\*/ 2. models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser): # models.Model 상속

    pass

3. settings.py INSTALLED_APPS를 지우고 위와같이 분리

DJANGO_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
]

PROJECT_APPS = [
"users.apps.UsersConfig"
]
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

4.  db.sqlite3 삭제

5.  서버 닫음

6.  settings.py 에 추가
    AUTH_USER_MODEL = "users.User"

7.  python manage.py makemigrations

8.  python manage.py migrate

9.  서버 열기

10. 새로운 터미널 창을 열고
    pipenv shell
    python manage.py createsuperuser
    lim
    (blank)
    123
    123

        ID -> lim
        PassWord -> 123

USER Model Design (회원가입에 bio 추가하는 과정)

11. admin.py

from django.contrib import admin
from . import models

/ # Register your models here.

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
pass

12. models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

/ # Create your models here.

class User(AbstractUser): # models.Model 상속

    bio = models.TextField(default="")

https://docs.djangoproject.com/en/3.1/ref/models/fields/

13. python manage.py makemigrations

14. python manage.py migrate

Database에 Default가 있어야 하는 이유:
그 전에 만들어 진 것들을 채워야 하기 때문

or null=True (빈칸 신경쓰지 말아라)

----이제 본격적으로 만들 것을 추가해 봅시다---------

15. models.py

class User(AbstractUser): # models.Model 상속

    """ Custom User Model """

    avatar = models.ImageField(null=True)
    gender = models.CharField(max_length=10, null=True)
    bio = models.TextField(default="")

16. python manage.py makemigrations

-> Pillow를 깔아라고 뜬다

17. pipenv install Pillow

18. python manage.py makemigrations

19. python manage.py migrate

---

----Gender에 3가지만 선택하자-------------------------

class User(AbstractUser): # models.Model 상속

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    avatar = models.ImageField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="")

-----------필수로 요구하는게 아니라 선택해도되는 것 구현----------

class User(AbstractUser): # models.Model 상속

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"

    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)

20. python manage.py makemigrations

21. python manage.py migrate

#3.4 django Admin을 어떻게 설정할 수 있을지

https://docs.djangoproject.com/en/3.1/ref/contrib/admin/

1.  admin.py
    @admin.register(models.User) # user control
    class CustomUserAdmin(admin.ModelAdmin):

        """ Custom User Admin """

        list_display = ("username", "email", "gender", "language", "currency", "superhost")
        list_filter = ("language", "currency", "superhost")

2.  admin.py
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from . import models

    /# Register your models here.
    @admin.register(models.User) # user control
    class CustomUserAdmin(UserAdmin):

        """ Custom User Admin """

        fieldsets = UserAdmin.fieldsets + (
            (
                "Custom profile",
                {
                    "fields": (
                        "avatar",
                        "gender",
                        "bio",
                        "birthdate",
                        "language",
                        "currency",
                        "superhost",
                    )
                },
            ),
        )

#4.0 ROOM APP

1. settings.py

수정합시다.

PROJECT_APPS = ["users.apps.UsersConfig", "rooms.apps.RoomsConfig"]

2.  models.py

    from django.db import models

    /# Create your models here.
    class Room(models.Model):
    """ Room Model Definition"""

        pass

3.  admin.py

    from django.contrib import admin
    from . import models

    @admin.register(models.Room)
    class RoomAdmin(admin.ModelAdmin):

        pass

4.  models.py 수정하는데 이제 모든 reservations, reviews, room에 동시에 필요한걸 한번에 만들기 위해 core이라는 새로운 app 을 만들자

5.  django-admin startapp core

6.  core models.py

    from django.db import models

    class TimeStampedModel(models.Model):

        """ Time Stamped Definition """

        created = models.DateField()
        updated = models.DateField()

        class Meta:
            abstract = True  # Database로 가지 않게 하기 위한 절차

7.  settings.py

PROJECT_APPS = ["core.apps.CoreConfig", "users.apps.UsersConfig", "rooms.apps.RoomsConfig"]

8.  models.py

    from django.db import models
    from core import models as core_models

    /# Create your models here.
    class Room(core_models.TimeStampedModel):
    """ Room Model Definition"""

        pass

#4.1 Room Model part one

1. country를 다운 받자!

pipenv install django-countries

2. settings.py

add

THIRD_PARTY_APPS = ["django_countries"]

3.  models.py

    from django.db import models
    from django_countries.fields import CountryField
    from core import models as core_models

    class Room(core_models.TimeStampedModel):
    """ Room Model Definition"""

        name = models.CharField(max_length=140)  # require
        description = models.TextField()
        country = CountryField()
        city = models.CharField(max_length=80)
        price = models.IntegerField()
        address = models.CharField()
        guests = models.IntegerField()
        beds = models.IntegerField()
        bedrooms = models.IntegerField()
        baths = models.IntegerField()
        check_in = models.TimeField()
        check_out = models.TimeField()
        instant_book = models.BooleanField(default=False)
        host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

4.  DateField(auto_now, auto_now_add)

    auto_now = True 필드가 model을 save할 때 date랑 time을 기록할거야
    모델을 저장할 때 마다 날짜와 시간을 입력해준다.

    auto_now_add 모델을 만들면 현재 날짜랑 시간을 넣어준다.

5.  models.py

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

6.  python manage.py makemigration

7.  python manage.py migrate

#4.3 Many to Many

models.py

    def __str__(self):
        return self.name

로 admin에 나오는 이름을 자기 자신으로 바꿀 수 있다.

1.  models.py

    from django.db import models
    from django_countries.fields import CountryField
    from core import models as core_models
    from users import models as user_models

    class AbstractItem(core_models.TimeStampedModel):

        """ Abstract Item """

        name = models.CharField(max_length=80)

        class Meta:
            abstract = True

        def __str__(self):
            return self.name

    class RoomType(AbstractItem):

        pass

    class Room(core_models.TimeStampedModel):
    """ Room Model Definition"""

        name = models.CharField(max_length=140)  # require
        description = models.TextField()
        country = CountryField()
        city = models.CharField(max_length=80)
        price = models.IntegerField()
        address = models.CharField(max_length=140)
        guests = models.IntegerField()
        beds = models.IntegerField()
        bedrooms = models.IntegerField()
        baths = models.IntegerField()
        check_in = models.TimeField()
        check_out = models.TimeField()
        instant_book = models.BooleanField(default=False)
        host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
        room_type = models.ManyToManyField(RoomType, blank=True)

        def __str__(self):
            return self.name

2.  python manage.py makemigration

3.  python manage.py migrate

4.  admin.py

    @admin.register(models.RoomType)
    class ItemAdmin(admin.ModelAdmin):
    pass

Roomtype에 +를 만들기 위해 한 것

5. Roomtypes에
   Hotel room
   Shared room
   private room
   entire room
   추가

6. Foreignkey on_delete = models.CASCADE

만약 user을 삭제하면 Room도 삭제된다는 말

PROTECT

그가 업로드한 rooms를 지우기 전까지는 자신의 User을 지울수 없음

7. Amenity, Facility, Houserule 추가

from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):

    """ RoomType Object Definition """

    pass

class Amenity(AbstractItem):
""" Amenity Object Definition """

    pass

class Facility(AbstractItem):
""" Facility Model Definition """

    pass

class HouseRule(AbstractItem):
""" HouseRule Model Definition """

    pass

class Room(core_models.TimeStampedModel):
""" Room Model Definition"""

    name = models.CharField(max_length=140)  # require
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name

8. migration으로 적용하고 확인

9. 추가할 버튼이 없다!! (admin이 없기 때문)
10. admin.py

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
pass

11. Amenitys 등등 바꾸는 법

class RoomType(AbstractItem):

    """ RoomType Object Definition """

    class Meta:
        verbose_name = "Room Type"

class Amenity(AbstractItem):
""" Amenity Object Definition """

    class Meta:
        verbose_name_plural = "Amenities"

class Facility(AbstractItem):
""" Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):
""" HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"

12. 생성된 것들의 순서 정하는 법 Order

    ordering = ["name"] 알파벳 순서
    ordering = ["created"] 생성된순서 -> core

13. blank 지정 (blank=True)

14. Photo 모델 만들기

class Photo(core_models.TimeStampedModel):
""" Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

이렇게 만들면 문제가 있다.
python은 위에서 밑으로 읽기 때문에 Room이 정의 되어있지 않다!

해결책 1. 밑에다가 쓴다 2. ""string 형태로 쓴다....

15. admin에 추가!
    @admin.register(models.Photo)
    class PhotoAdmin(admin.ModelAdmin):

        pass

16. migrate통해 확인한다.

17. 최종코드

    models.py

    from django.db import models
    from django_countries.fields import CountryField
    from core import models as core_models
    from users import models as user_models

    class AbstractItem(core_models.TimeStampedModel):

        """ Abstract Item """

        name = models.CharField(max_length=80)

        class Meta:
            abstract = True

        def __str__(self):
            return self.name

    class RoomType(AbstractItem):

        """ RoomType Object Definition """

        class Meta:
            verbose_name = "Room Type"
            ordering = ["name"]

    class Amenity(AbstractItem):
    """ Amenity Object Definition """

        class Meta:
            verbose_name_plural = "Amenities"

    class Facility(AbstractItem):
    """ Facility Model Definition """

        class Meta:
            verbose_name_plural = "Facilities"

    class HouseRule(AbstractItem):
    """ HouseRule Model Definition """

        class Meta:
            verbose_name = "House Rule"

    class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

        caption = models.CharField(max_length=80)
        file = models.ImageField()
        room = models.ForeignKey("Room", on_delete=models.CASCADE)

        def __str__(self):
            return self.caption

    class Room(core_models.TimeStampedModel):
    """ Room Model Definition"""

        name = models.CharField(max_length=140)  # require
        description = models.TextField()
        country = CountryField()
        city = models.CharField(max_length=80)
        price = models.IntegerField()
        address = models.CharField(max_length=140)
        guests = models.IntegerField()
        beds = models.IntegerField()
        bedrooms = models.IntegerField()
        baths = models.IntegerField()
        check_in = models.TimeField()
        check_out = models.TimeField()
        instant_book = models.BooleanField(default=False)
        host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
        room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
        amenities = models.ManyToManyField(Amenity, blank=True)
        facilities = models.ManyToManyField(Facility, blank=True)
        house_rules = models.ManyToManyField(HouseRule, blank=True)

        def __str__(self):
            return self.name

    admin.py

    from django.contrib import admin
    from . import models

    @admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
    class ItemAdmin(admin.ModelAdmin):

        """ Item Admin Definition """

        pass

    @admin.register(models.Photo)
    class PhotoAdmin(admin.ModelAdmin):

        pass

    @admin.register(models.Room)
    class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

        pass

#5.0 Review Model

1. settings.py

PROJECT_APPS = [
"core.apps.CoreConfig",
"users.apps.UsersConfig",
"rooms.apps.RoomsConfig",
"reviews.apps.ReviewsConfig",
]

2. models.py

from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accurancy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'

3. admin.py

from django.contrib import admin
from . import models

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    pass

4. migrate하고 확인

#5.1 Reservation Model

1.

from django.db import models
from core import models as core_models

class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

2.

from django.contrib import admin
from . import models

@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition """

    pass

3.

PROJECT_APPS = [
"core.apps.CoreConfig",
"users.apps.UsersConfig",
"rooms.apps.RoomsConfig",
"reviews.apps.ReviewsConfig",
"reservations.apps.ReservationsConfig",
]

4. migrate

#5.2 lists

1.  PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
    "reviews.apps.ReviewsConfig",
    "reservations.apps.ReservationsConfig",
    "lists.apps.ListsConfig",
    ]

2.  from django.db import models
    from core import models as core_models

class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

3.  from django.contrib import admin
    from . import models

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    pass

4. migrate

#5.3 conversations

1.  PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
    "reviews.apps.ReviewsConfig",
    "reservations.apps.ReservationsConfig",
    "lists.apps.ListsConfig",
    "conversations.apps.ConversationsConfig",
    ]

2.  from django.db import models
    from core import models as core_models

class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)

class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"

3.

from django.contrib import admin
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
pass

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
pass

-----------------------------드디어 Apps 끝!!!!!---------------

#6.0 Room Admin Panel

    @admin.register(models.Room)
    class RoomAdmin(admin.ModelAdmin):
        """ Room Admin Definition """

        list_display = (
            "name",
            "country",
            "city",
            "price",
            "guests",
            "beds",
            "bedrooms",
            "baths",
            "check_in",
            "check_out",
            "instant_book",
        )

        list_filter = ("instant_book", "city", "country")

        search_fields = ("city","^host__username")

#6.1

1.  admin 패널에서 filter설정하는 거

    @admin.register(models.Room)
    class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

        list_display = (
            "name",
            "country",
            "city",
            "price",
            "guests",
            "beds",
            "bedrooms",
            "baths",
            "check_in",
            "check_out",
            "instant_book",
        )

        list_filter = (
            "instant_book",
            "host__superhost",
            "room_type",
            "amenities",
            "facilities",
            "house_rules",
            "city",
            "country",
        )

        search_fields = ("city", "^host__username")

2.  Many to Many 를 선택할 수 있게 만드는 창

        filter_horizontal = ("amenities", "facilities", "house_rules")  # many to many

3.  소 제목과 파트 분류

        fieldsets = (
            (
                "Basic Info",
                {"fields": ("name", "description", "country", "address", "price")},
            ),
            ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
            ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
            (
                "More About the Space",
                {
                    "classes": ("collapse",),
                    "fields": ("amenities", "facilities", "house_rules"),
                },
            ),
            ("Last Details", {"fields": ("host",)}),
        )

4.  복수개의 정렬

            ordering = ("name", "price", "bedrooms")

5.  amenities, facilities, rules 갯수

    def count_amenities(self, obj): # self -> class RoomAdmin object -> first row
    return obj.amenities.count()

#7.0 Database에 있는 것들을 어떻게 가져올까???????????

1.  cd airbnb_clone

2.  pipenv shell

3.  python manage.py shell

4.  from users.models import User

5.  1)dir(User) 클래스안에 names리스트 반환
    2)vars(User) -> dictionary또는 클래스 리스트 안에 있는 것을 return

6.  User.objects

7.  User.objects.all() ->쿼리셋으로 유저들을 다 보여준다.

8.  > > > all_user = User.objects.all()
    > > > all_user.filter(superhost=True)
    > > > <QuerySet [<User: lim>]>

9.  > > > lim = User.objects.get(username="lim")
    > > > print(lim)
    > > > lim

10. Foreign key로 접근 가능

    > > > lim.room_set.all()
    > > > <QuerySet [<Room: The Joshua Tree house>]>
    > > > lim.review_set.all()
    > > > <QuerySet [<Review: i love this house!!! - The Joshua Tree house>]>

11. relatedname : room_set을 원하는 이름으로 바꾸기 -> foreign key한정
    user_models.User, related_name="rooms", on_delete=models.CASCADE

12. migrate

13. 파이선 창을 끄고 다시실행

14. lim.rooms.all()

15.     >>> from rooms.models import Room
        >>> room = Room.objects.get(id=1)
        >>> room
        <Room: The Joshua Tree house>
        >>> room.review_set
        <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x0000014C735AD710>
        >>> room.review_set.all()
        <QuerySet [<Review: i love this house!!! - The Joshua Tree house>]>
        >>> room.amenities
        <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000014C735AD9B0>
        >>> room.amenities.all()
        <QuerySet [<Amenity: Wi-Fi>]>

16. 특정한 단어로 시작하는 찾기

        >>> startswith = User.objects.filter(username__startswith="li")
        >>> print(startswith)
        <QuerySet [<User: lim>]>

#7.2 admin decorate

from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
""" Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules")  # many to many

    def count_amenities(self, obj):  # self -> class RoomAdmin object -> first row
        return obj.amenities.count()

    # count_amenities.short_description = "Hello sexy!"

    def count_photos(self, obj):
        return obj.photos.count()

#8.0

1. user admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User) # user control
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

2. review model

from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accurancy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accurancy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

3. review admin

from django.contrib import admin
from . import models

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    list_display = ("__str__", "rating_average")

4. rooms model

   def total_rating(self):
   all_reviews = self.reviews.all()
   all_ratings = 0
   for review in all_reviews:
   all_ratings += review.rating_average()
   if len(all_reviews) > 0:
   return all_ratings / len(all_reviews)
   else:
   return 0

#8.1 reservation admin

from django.contrib import admin
from . import models

@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition """

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )
    list_filter = ("status", "in")

from django.db import models
from django.utils import timezone
from core import models as core_models

class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

#8.2 list admin

from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"

from django.contrib import admin
from . import models

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("^name",)

2. conversation admin

from django.contrib import admin
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ("__str__", "created")

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )

from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participants"

class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"

#8.3 포토 인식

1. media_root

settings.py

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads") # photo root

.gitignore

uploads/

2. users modles

   avatar = models.ImageField(upload_to="avatars", null=True, blank=True)

3. rooms models

   file = models.ImageField(upload_to="room_photos")

4. migrate

5. url.py

from django.contrib import admin
from django.urls import path
from django.conf import settings # 몰라 장고에서는 from . import settings하면 안됨
from django.conf.urls.static import static

urlpatterns = [
path("admin/", admin.site.urls),
]

if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

6. settings.py

MEDIA_URL = "/media/" # 처음 /는 절대경로

->Amazon에 할 때는 다르게 사용해야함!!!! 너무 많은 디스크 공간 사용 + 서버증가시 대응 불가 나중에 알려줌

#8.5 photo admin 썸네일

from django.utils.html import mark_safe

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width = 50px src={obj.file.url}/>")

    get_thumbnail.short_description = "Thumbnail"

#8.6 seoul을 Seoul으로 인식하는 법

raw_id_fields -> 호스트를 select 대신 검색 가능하게

admin.py

    raw_id_fields = ("host",)

다른 admin패널에서 create하는법

class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
""" Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules")  # many to many

    def count_amenities(self, obj):  # self -> class RoomAdmin object -> first row
        return obj.amenities.count()

    # count_amenities.short_description = "Hello sexy!"

    def count_photos(self, obj):
        return obj.photos.count()

seoul Seoul

super() father class에 접근할 수 있게 만들어줌.

save()

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super.save(*args, **kwargs)

#9.0 django-seed

pipenv install django-seed

settings.py

THIRD_PARTY_APPS = ["django_countries", "django_seed"]
