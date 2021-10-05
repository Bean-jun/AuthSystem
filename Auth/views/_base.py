import json
from functools import wraps
from http import HTTPStatus

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from Auth.models import User

from Auth.common import response, auth_decode


@method_decorator(csrf_exempt, "dispatch")
class BaseView(View):

    @staticmethod
    def exception_func(request, *args, **kwargs):
        return JsonResponse(response(code=HTTPStatus.METHOD_NOT_ALLOWED, msg=f"{request.method}请求方式被禁止"))

    @staticmethod
    def parse_request_body(request, *args, **kwargs):
        try:
            dict = json.loads(request.body.decode())
        except Exception as e:
            try:
                dict = request.POST
            except Exception as e:
                raise e
            else:
                for k, v in dict.items():
                    kwargs[k] = v
        else:
            for k, v in dict.items():
                kwargs[k] = v

        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), None)
        else:
            handler = None

        # 解析前端请求
        kwargs = BaseView.parse_request_body(request, *args, **kwargs)

        if handler:
            return handler(request, *args, **kwargs)
        else:
            return BaseView.exception_func(request, *args, **kwargs)


class BaseAuthView(BaseView):

    @staticmethod
    def auth(f):
        @wraps(f)
        def inner(request, *args, **kwargs):
            flag, msg = auth_decode(request.headers.get("Authorization"))
            if not flag:
                return JsonResponse(msg)
            try:
                email = msg.get("data").get("email")
            except Exception as e:
                return response(HTTPStatus.INTERNAL_SERVER_ERROR, "服务器内部异常")

            user = User.objects.filter(email=email).first()
            kwargs["inner_user"] = user

            return f(request, *args, **kwargs)

        return inner
