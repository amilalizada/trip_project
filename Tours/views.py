from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView , DetailView , View
from Tours.models import *
from django.core.paginator import Paginator

# Create your views here.

class ToursPage(ListView):
    model = Tours
    template_name = 'tourspage.html'
    paginate_by = 1
    def get_context_data(self,*args , **kwargs):
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        context = super().get_context_data(**kwargs)
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index - 5 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
        context["tours"] = Tours.objects.all
        return context
    


class ToursSinglePage(DetailView):
    model = Tours
    template_name = 'tours_single_page.html'
    
   
class SavedTourView(View):
    def get(self,*args,**kwargs):
        tour_id = kwargs.get('pk')
        print(tour_id)
        message = 'Tour added to wishlist.'
        tour = get_object_or_404(Tours,id=tour_id)
        if self.request.user.is_authenticated:
            save_tour,created= SavedArticleTour.objects.get_or_create(user=self.request.user,tour=tour)
            if not created:
                message='Tour was added already'
            response = HttpResponse(message)
        else:
            saved_tours = self.request.COOKIES.get('saved_tours', '')
            if str(tour_id) not in saved_tour.split(';'):
                saved_tours += str(tour_id) + ";"
            response = HttpResponse(message)
            response.set_cookie('saved_tours', saved_tours)
            # messages.success(self.request, message)
        return response

class SavedTourListView(ListView):
    model = Tours
    template_name = 'save_tours.html'
    context_object_name = 'tours_list'
    def get_queryset(self, ):
        if self.request.user.is_authenticated:
            user_saved_articles_ids = self.request.user.tour_saved_articles.values_list('tour__id', flat=True)
            queryset = super().get_queryset().filter(id__in=user_saved_articles_ids)
            print(queryset)
            print(user_saved_articles_ids)
            return queryset
        else:
            saved_tours = self.request.COOKIES.get('saved_tours')
            if saved_hotels:
                saved_tours_ids = [int(id) for id in saved_tours.split(';') if id and id != 0]
                queryset = super().get_queryset()
                return queryset.filter(id__in=saved_tours_ids)
            return None

