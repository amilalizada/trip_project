from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from Main.forms import SubscriberForm,ContactForm
from django.views.generic import ListView,CreateView,TemplateView,DetailView
from Main.models import City,ContactInfo,AboutProject
from Hotels.models import Hotel
from Restaurants.models import Restaurants
from Tours.models import Tours
from django.core.paginator import Paginator
# Create your views here.

class MainClassView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['city_list'] = City.objects.all()[:3]
        context['hotels'] = Hotel.objects.all()[:3]
        context['restaurants'] = Restaurants.objects.all()[:3]
        context['tours'] = Tours.objects.all()[:3]
        return context



class SubscriberCreateView(CreateView):
    form_class = SubscriberForm
    template_name = None
    http_method_names = ('post',)
    success_url = reverse_lazy('main:home')

    def get_success_url(self):
        redirect_url = self.request.GET.get('redirect_url',self.success_url)
        return redirect_url

    def form_valid(self, form):
        messages.success(self.request,'Subscribe oldunuz')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,form.errors)
        redirect_url = self.request.GET.get('redirect_url',self.success_url)
        return redirect(redirect_url)


class ContactSubjectView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    # http_method_names = ('post',)
    success_url = reverse_lazy('main:home')

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().post(request, *args, **kwargs)
    #
    # def form_valid(self,form):
    #     return super().form_valid(form)

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contactInfo = ContactInfo.objects.get()
        context['contactInfo'] = contactInfo
        context['form'] = ContactForm()
        return context

class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aboutUs = AboutProject.objects.get()
        context['aboutUs'] = aboutUs
        return context

class PrivacyPolicyView(TemplateView):
    template_name = 'policies.html'
    

class TermsOfUseView(TemplateView):
    template_name = 'terms.html'


class CitySinglePage(DetailView):
    model = City
    template_name = 'city_single_page.html'

class CitiesPage(ListView):
    model = City
    template_name = 'cities-page.html'
    paginate_by = 1
    context_object_name = 'cities'

    
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
        
        return context
    

    

