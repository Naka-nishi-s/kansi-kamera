import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # ログイン成功: トークンや成功メッセージを返す
            return JsonResponse({'status': 'success', 'token': 'your-token'})
        else:
            # ログイン失敗: エラーメッセージを返す
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)