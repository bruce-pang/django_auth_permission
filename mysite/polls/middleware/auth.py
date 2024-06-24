from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin): # 用于验证用户是否登录
    def process_request(self, request):

        # 0.排除那些不需要登录就能访问的url
        if request.path_info in ["/login/", "/image/code/"]:
            return None

        token = request.session.get("token")
        if not token:
            return JsonResponse({"code": 1001, "error": "用户未登录"})