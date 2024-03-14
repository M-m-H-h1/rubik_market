from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView, View
import jdatetime
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import json

from account.models import Address

from products.models import Products,Category,Top_Product,Special_Sale
from star_ratings.models import AbstractBaseRating
from django.views.generic import ListView
from . import models



class HomeProductsView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.session.get('is_authenticated_to_see_fp') == True:
            self.request.session['is_authenticated_to_see_fp'] = False


        context['most_visited'] = Products.objects.order_by('-views')[:4]

        context['top_products'] = Top_Product.objects.all()
        context['special_sales'] = Special_Sale.objects.all()
        return context



class FrequentlyAskedQuestionsView(TemplateView):
    template_name = 'home/FrequentlyAskedQuestions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = models.Questions.objects.all()

        return context











