### 一、用户注册

`/register/` POST

所需参数

| username | 用户名 |      |
| -------- | ------ | ---- |
| email    | 邮箱   |      |
| password | 密码   |      |

返回数据格式

```json
{
    "code": 200,
    "message": "注册成功",
    "data": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ilx1NWMwZlx1NjYwZSIsImVtYWlsIjoiMTczNzE0MzgyMjdAMTIyLmNvbSIsImV4cCI6MTYzMzQyOTc2MH0.wOlkq43bbxqCwE7j8AgWUoAGdJN66Mg-sGMethZxw1s",
        "username": "小明",
        "email": "17371438227@122.com"
    }
}
```



### 二、用户登录

`/login/` POST

所需参数

| username | 用户名 | usernam和email二选一 |
| -------- | ------ | -------------------- |
| email    | 邮箱   |                      |
| password | 密码   |                      |

返回数据格式

```json
{
    "code": 200,
    "message": "登录成功",
    "data": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ilx1NWMwZlx1NjYwZSIsImVtYWlsIjoiMTczNzE0MzgyMjdAMTIyLmNvbSIsImV4cCI6MTYzMzQyOTc4NX0.gjkOlPy_uM2DJBkI2WJZyvzKYbkDaQbUyNct3DKJMwA",
        "username": "小明",
        "email": "17371438227@122.com"
    }
}
```



### 三、用户鉴权

`/auth/` GET

所需参数

| Authorization | 用户token |      |
| ------------- | --------- | ---- |

返回数据格式

```json
{
    "code": 200,
    "message": "登录成功",
    "data": {
        "username": "小明",
        "email": "17371438227@122.com"
    }
}
```

