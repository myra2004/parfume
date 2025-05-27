from django.views.generic import TemplateView

from datetime import datetime, timedelta

from products.models import Category, ProductVariant, Product
from accounts.models import User, Cart, CartItem


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        categories = Category.objects.all()
        products = Product.objects.all()
        latest_products = Product.objects.filter(
            created_at =- timedelta(days=1)
        )
        context['title'] = 'VooCommerce | Home'
        context['categories'] = categories
        context['products'] = products
        context['latest_products'] = latest_products

        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Contact Us'

        users = User.objects.filter(
            is_staff=False
        )
        context['users'] = users
        return context


class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        context = super(ShopDetailsView, self).get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Shop Details'

        products = ProductVariant.objects.all()
        context['products'] = products

        return context


class ShopCart(TemplateView):
    template_name = 'shoping-cart.html'

    def get_context_data(self, **kwargs):
        context = super(ShopCart, self).get_context_data(**kwargs)
        context['title'] = 'VooCommerce | Shopping Cart'

        carts = Cart.objects.all()
        context['carts'] = carts

        cart_items = CartItem.objects.all()
        context['cart_items'] = cart_items

        return context