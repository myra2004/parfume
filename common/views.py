from datetime import datetime, timedelta

from django.views.generic import TemplateView

from products.models import Category, ProductVariant, Product


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
        return context
