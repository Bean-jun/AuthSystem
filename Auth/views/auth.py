from http import HTTPStatus
import base64
import time
import hashlib
from django.conf import settings
from django_redis import get_redis_connection
from django.http import JsonResponse

from Auth.common import response
from ._base import BaseAuthView
from Auth.form.auth import UserInfoForm


class UserInfo(BaseAuthView):
    """
    用户基本信息设定
    """

    @BaseAuthView.auth
    def get(self, request, *args, **kwargs):
        user = kwargs.get("inner_user")

        data = {
            "username": user.username,
            "email": user.email,
        }

        if user.is_developer:
            data.update({
                "secret_id": user.secret_id,
                "secret_value": user.secret_value
            })

        return JsonResponse(response(code=HTTPStatus.OK,
                                     msg="获取成功",
                                     data=data))

    @BaseAuthView.auth
    def patch(self, request, *args, **kwargs):

        user = kwargs.get("inner_user")

        data = {
            "username": user.username,
            "email": user.email,
        }

        form = UserInfoForm(kwargs)
        if form.is_valid():
            user.is_developer = form.cleaned_data["is_developer"]

            if user.is_developer:
                user.secret_id = base64.b64encode(str(time.time()).encode()).decode()
                hash = hashlib.sha256(settings.SECRET_KEY.encode())
                hash.update(user.secret_id.encode())
                user.secret_value = hash.hexdigest()

                user.save()
                data.update({
                    "secret_id": user.secret_id,
                    "secret_value": user.secret_value
                })

            return JsonResponse(response(code=HTTPStatus.OK,
                                         msg="修改成功",
                                         data=data))
        else:
            return JsonResponse(response(code=HTTPStatus.OK,
                                         msg="修改成功",
                                         data=data))
