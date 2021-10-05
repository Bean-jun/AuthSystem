from http import HTTPStatus

from django.http import JsonResponse

from Auth.common import response
from ._base import BaseAuthView


class AuthView(BaseAuthView):

    @staticmethod
    @BaseAuthView.auth
    def get(request, *args, **kwargs):
        user = kwargs.get("inner_user")
        return JsonResponse(response(code=HTTPStatus.OK,
                                     msg="登录成功",
                                     data={
                                         "username": user.username,
                                         "email": user.email,
                                     }))
