from django.conf import settings
from store.models import Product


class Wishlist:
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = []
        self.wishlist = wishlist

    def change_wishlist(self, product_id):
        product_id = str(product_id)
        if product_id not in self.wishlist:
            self.wishlist.append(product_id)
        else:
            self.wishlist.remove(product_id)
        self.save()

    def save(self):
        self.session.modified = True

    def wishlist_len(self):
        return len(self.wishlist)

    def wishlist_elem(self):
        product_ids = self.wishlist
        products = Product.objects.filter(id__in=product_ids)
        return products


