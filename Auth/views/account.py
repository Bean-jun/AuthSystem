from http import HTTPStatus

from django.http import JsonResponse

from Auth.common import response, auth_encode
from Auth.form.account import UserRegisterForm, UserLoginForm
from ._base import BaseView


class RegisterView(BaseView):

    @staticmethod
    def post(request, *args, **kwargs):

        form = UserRegisterForm(request=request, data=kwargs)

        if form.is_valid():

            form.instance.save()

            return JsonResponse(response(code=HTTPStatus.OK,
                                         msg="注册成功",
                                         data={
                                             "token": auth_encode(username=form.cleaned_data["username"],
                                                                  email=form.cleaned_data["email"]),
                                             "username": form.cleaned_data["username"],
                                             "email": form.cleaned_data["email"],
                                         }))
        else:
            return JsonResponse(response(code=HTTPStatus.EXPECTATION_FAILED, msg="校验数据异常", data=request.error))


class LoginView(BaseView):

    @staticmethod
    def post(request, *args, **kwargs):

        form = UserLoginForm(request=request, data=kwargs)

        if form.is_valid():

            user = form.cleaned_data["inner_user"]

            return JsonResponse(response(code=HTTPStatus.OK,
                                         msg="登录成功",
                                         data={
                                             "token": auth_encode(username=user.username,
                                                                  email=user.email),
                                             "username": user.username,
                                             "email": user.email,
                                         }))

        else:
            return JsonResponse(response(code=HTTPStatus.UNAUTHORIZED, msg="登录数据异常", data=request.error))
