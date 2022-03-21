from django_request_mapping import UrlPattern
from shop.views import MyView

urlpatterns = UrlPattern()
urlpatterns.register(MyView)