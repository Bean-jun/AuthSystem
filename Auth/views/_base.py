from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from Auth.common import response


@method_decorator(csrf_exempt, "dispatch")
class BaseView(View):

    @staticmethod
    def exception_func(request, *args, **kwargs):
        return JsonResponse(response(code=400, msg=f"{request.method}请求方式被禁止"))

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), None)
        else:
            handler = None

        if handler:
            return handler(request, *args, **kwargs)
        else:
            return BaseView.exception_func(request, *args, **kwargs)
