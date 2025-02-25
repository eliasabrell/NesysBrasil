from datetime import date
from django.utils.deprecation import MiddlewareMixin
from .models import DailyAccess

class ContadorAcessosMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = self.get_client_ip(request)
        user = request.user if request.user.is_authenticated else None
        today = date.today()

        if not DailyAccess.objects.filter(data=today, username=user, ip_address=ip).exists():
            DailyAccess.objects.create(username=user, ip_address=ip, data=today)

    def get_client_ip(self, request):
        """ Obtém o IP real do usuário, mesmo atrás de proxies. """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip