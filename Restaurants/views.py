from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View
from Restaurants.models import Restaurants, OptionsTypeRadio, OptionsTypeCheckbox, RestaurantImages, ToEatReason,ReviewRestaurant, SavedArticleRestaurants
from Restaurants.forms import ReviewForm
from django.urls import reverse_lazy    

class RestaurantsListView(ListView):
    model = Restaurants
    template_name = 'restaurants.html'
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['type_radio'] = OptionsTypeRadio.objects.all()
        context['type_checkbox'] = OptionsTypeCheckbox.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class RestaurantsSinglePageClassView(DetailView):
    model = Restaurants
    template_name = 'restaurant_single_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantsSinglePageClassView,self).get_context_data( *args, **kwargs)
        return context

class ReviewCreateView(CreateView):
    form_class = ReviewForm
    template_name = None
    http_method_names = ('post',)

    def form_valid(self, form,):
        review = form.save(commit=False)
        review.user = self.request.user
        restaurants = Restaurants.objects.filter(is_published='True',name=self.request.POST.get('restaurant')).first()
        review.restaurant = restaurants
        review.save()
        review.save_star()
        messages.success(self.request, 'Comment Added')
        redirect_url = reverse_lazy('restaurants_app:restaurant_single_page',kwargs={'slug':restaurants.slug})
        return redirect(redirect_url) 

    def form_invalid(self, form):
        messages.success(self.request, form.errors)
        redirect_url = self.request.GET.get('redirect_url', self.success_url)
        return redirect(redirect_url) 

class SavedRestaurantView(View):
    def get(self,*args,**kwargs):
        restaurant_id = kwargs.get('pk')
        print(restaurant_id)
        message = 'Restaurant added to wishlist.'
        restaurant = get_object_or_404(Restaurants,id=restaurant_id)
        if self.request.user.is_authenticated:
            save_restaurant,created= SavedArticleRestaurants.objects.get_or_create(user=self.request.user,restaurant=restaurant)
            if not created:
                message='Restaurant was added already'
            response = HttpResponse(message)
        else:
            saved_restaurants = self.request.COOKIES.get('saved_restaurants', '')
            if str(restaurant_id) not in saved_restaurant.split(';'):
                saved_restaurants += str(restaurant_id) + ";"
            response = HttpResponse(message)
            response.set_cookie('saved_restaurants', saved_restaurants)
            # messages.success(self.request, message)
        return response

class SavedRestaurantListView(ListView):
    model = Restaurants
    template_name = 'saved_restaurants.html'
    context_object_name = 'restaurants_list'
    paginate_by = 1
    def get_queryset(self, ):
        if self.request.user.is_authenticated:
            user_saved_articles_ids = self.request.user.restaurant_saved_articles.values_list('restaurant__id', flat=True)
            queryset = super().get_queryset().filter(id__in=user_saved_articles_ids)
            return queryset
        else:
            saved_restaurants = self.request.COOKIES.get('saved_restaurants')
            if saved_restaurants:
                saved_restaurants_ids = [int(id) for id in saved_restaurants.split(';') if id and id != 0]
                queryset = super().get_queryset()
                return queryset.filter(id__in=saved_restaurants_ids)
            return None
    



