from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.models import Basket


@login_required
def basket(request):
    title = "Корзина"
    basket_items = Basket.objects.filter(user=request.user).order_by("product__category")
    content = {
        "title": title,
        "basket_items": basket_items,
        "media_url": settings.MEDIA_URL,
        "project_settings": settings
    }
    return render(request, "basket/basket.html", content)

