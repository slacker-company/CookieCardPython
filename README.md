# CookieCard

CookieCard is module for the api of [CookieCard](https://slackercompany.ml/CarteCookie)

## Example

Get User Info
```python
import CookieCard

try:
    User = CookieCard.UserRemote("name", "password")
    print(f"Name : {User.name}")
    print(f"Money : {User.money}")
    print(f"Mail : {User.mail}")
    print(f"Id : {User.id}")
    print(f"isDev : {User.isDev}")
except CookieCard.NoLogged:
    print("Error on login")
except CookieCard.ApiError as e:
    print(f"error{e.args[1]}") #display error message
    # e.args[0] is Error
```

## Error Type

### NoLogged
the error occurs when the login to an error
### ApiError
this error occurs when the API returns an error
### ObsoletAPI
this error occurs when the python API is out of date
