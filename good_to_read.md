```
https://cheatsheetseries.owasp.org/cheatsheets/Django_REST_Framework_Cheat_Sheet.html

```

medium drf 

```
https://deekshasharma2022.medium.com/lets-ace-django-rest-framework-ab9eb22e0bce

https://python.plainenglish.io/the-complete-django-rest-framework-drf-cheat-sheet-a-quick-guide-for-beginners-and-pros-618bd7640187


```

medium django 
```
https://farshadabdulazeez.medium.com/django-commands-cheat-sheet-bdc0f6b088ab
```

django default pass validate 
```
from django.contrib.auth.password_validation import validate_password
```


# django users 

```
Django has three important concepts around user models:

1. `User` – Default concrete user model.
2. `AbstractUser` – Base class containing Django's full user implementation.
3. `AbstractBaseUser` – Minimal foundation for building a completely custom user model.

Let's understand the differences.

## **1. AbstractUser**

```
from django.contrib.auth.models import AbstractUserclass CustomUser(AbstractUser):    phone = models.CharField(max_length=15, blank=True)
```

- Contains all the fields and functionality of Django's default User model.
- Includes username, email, password, first name, last name, permissions, groups, etc.
- You can add your own fields.
- You can override existing behavior.

**Use when:** You want Django's default authentication system but need additional user fields.

## **2. AbstractBaseUser**

```
from django.contrib.auth.models import AbstractBaseUserclass CustomUser(AbstractBaseUser):    email = models.EmailField(unique=True)    USERNAME_FIELD = 'email'
```

- Provides only the core authentication foundation.
- Includes password handling and last login.
- Does NOT automatically provide username, email, first name, groups, permissions, or admin-related fields.
- You must implement additional functionality yourself.

Typically, you also need:

- A custom user manager.
- `USERNAME_FIELD`.
- `REQUIRED_FIELDS`.
- Permission integration if needed.
- Appropriate authentication and admin configuration.

**Use when:** You want complete control over your user model, such as email-only authentication with a custom structure.

## **3. Default User**

```
from django.contrib.auth.models import User
```

Django's ready-made user model.

Contains:

- Username and password.
- Email and personal details.
- Permissions and groups.
- Admin-related flags.

No need to implement authentication yourself.

## **4. Comparison**

| Feature            | User         | AbstractUser      | AbstractBaseUser  |
| ------------------ | ------------ | ----------------- | ----------------- |
| Ready to use       | Yes          | No                | No                |
| Username           | Yes          | Yes               | No                |
| Email              | Yes          | Yes               | No                |
| Password handling  | Yes          | Yes               | Yes               |
| Groups/permissions | Yes          | Yes               | No, add/configure |
| Custom fields      | Not directly | Yes               | Yes               |
| Custom manager     | Built-in     | Usually inherited | Required          |
| Complexity         | Low          | Medium            | High              |



However, in a real project, if you know you'll need a custom user model, it's generally best to create it at the beginning, before your first migrations.

One more important concept:

`get_user_model()` is the recommended way to reference the active user model:

```
from django.contrib.auth import get_user_modelUser = get_user_model()
```

This works whether the project uses Django's default User or a custom user model.

**Remember this hierarchy:**

- `AbstractBaseUser` → Minimal authentication foundation.
- `AbstractUser` → Full default user functionality, customizable.
- `User` → Ready-made default implementation.

```

# validation 

> https://www.django-rest-framework.org/api-guide/validators/

```

serializer me validates 


Remember these 4 concepts

#Method	                       #Responsibility

validate()	                   Validate multiple fields together
validate_email()	           Validate a specific field
create()	                   Create a new database object
serializer.save()	           Calls create() for a new object

One important detail: validate_password checks password strength; it does NOT hash passwords. create_user() handles hashing.

```