from django.http import JsonResponse

from Auth.common import response
from ._base import BaseView


class RegisterView(BaseView):

    @staticmethod
    def post(request, *args, **kwargs):
        return JsonResponse(response(code=200, msg="register"))


class LoginView(BaseView):

    @staticmethod
    def post(request, *args, **kwargs):
        return JsonResponse(response(code=200, msg="login"))
