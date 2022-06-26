from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Stajaliste, Linija
from .forms import StajalisteForm, LinijaForm
from django.urls import reverse


from django.views.generic import(
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
    )


# Function based views

# =============================================================================
# def AutobuskeLinijeView(request):
#     sva_stajalista = Stajaliste.objects.all()
#     sve_linije = Linija.objects.all()
#     # return HttpResponse('Hello from the other side!')
#     # return render(request, 'autobuske_linije.html')
#     context = {'sva_stajalista': sva_stajalista, 'sve_linije': sve_linije}
#     return render(request, 'autobuske_linije/autobuske_linije.html', context)
# 
# def AddStajalisteView(request):
#     new_naziv = request.POST['naziv']
#     new_stajaliste = Stajaliste(naziv = new_naziv)
#     new_stajaliste.save()
#     return HttpResponseRedirect('/autobuske_linije/')
# 
# def AddLinijaView(request):
#     new_naziv = request.POST['naziv']
#     new_linija = Linija(naziv = new_naziv)
#     new_linija.save()
#     return HttpResponseRedirect('/autobuske_linije/')
# =============================================================================



# Create Form

# =============================================================================
# def stajaliste_create_view(request):
#     form = StajalisteForm(request.POST or None)  # form is arbitrary name
#     if form.is_valid():
#         form.save()
#     context = {'form':form}
#     return render(request, 'autobuske_linije/stajaliste_create_form.html', context)
#         
# 
# def linija_create_view(request):
#     my_form = LinijaForm(request.POST or None)
#     if my_form.is_valid():
#         my_form.save()
#     context = {'form':my_form}
#     return render(request, 'autobuske_linije/linija_create_form.html', context)
# =============================================================================



# Class based views - create view

class LinijaCreateView(CreateView):
    template_name = 'autobuske_linije/linija_create.html'
    form_class = LinijaForm
    queryset = Linija.objects.all()
    # success_url = '/autobuske_linije'  # could replace "Sačuvaj" in /linija_create/
    
    def get_success_url(self):
        return reverse('linija_create')
    
    
class StajalisteCreateView(CreateView):
    template_name = 'autobuske_linije/stajaliste_create.html'
    form_class = StajalisteForm
    queryset = Stajaliste.objects.all()
    # success_url = '/autobuske_linije/stajalista/'  # could replace "Sačuvaj" in /stajaliste_create
    
    def get_success_url(self):
        return reverse('stajaliste_create')
    
    
    
    
# Class based views - list view

class LinijaListView(ListView):
    template_name = 'autobuske_linije/linija_list.html'
    queryset = Linija.objects.all()


class StajalisteListView(ListView):
    template_name = 'autobuske_linije/stajaliste_list.html'
    queryset = Stajaliste.objects.all()




# Class based views - detail view

class LinijaDetailView(DetailView):
    template_name = 'autobuske_linije/linija_detail.html'
    queryset = Linija.objects.all()


class StajalisteDetailView(DetailView):
    template_name = 'autobuske_linije/stajaliste_detail.html'
    queryset = Stajaliste.objects.all()    




# Class based views - update view

class LinijaUpdateView(UpdateView):
    template_name = 'autobuske_linije/linija_create.html'
    form_class = LinijaForm
    queryset = Linija.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Linija, id = id_)
    
    def get_success_url(self):
        return reverse('linija_create')


class StajalisteUpdateView(UpdateView):
    template_name = 'autobuske_linije/stajaliste_create.html'
    form_class = StajalisteForm
    queryset = Stajaliste.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Stajaliste, id = id_)
    
    def get_success_url(self):
        return reverse('stajaliste_create')




# Class based views - delete view

class LinijaDeleteView(DeleteView):
    template_name = 'autobuske_linije/linija_delete.html'
    form_class = LinijaForm
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Linija, id = id_)
    
    def get_success_url(self):
        return reverse('linija_list')


class StajalisteDeleteView(DeleteView):
    template_name = 'autobuske_linije/stajaliste_delete.html'
    form_class = StajalisteForm
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Stajaliste, id = id_)

    def get_success_url(self):
        return reverse('stajaliste_list')

