from audioop import reverse
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
# from django.views import generic
# from django.views.generic import TemplateView
from .models import FIO
# --------------------------------------------------
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from app_main.forms   import ContactForm, FioForm
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from app_main.models import FIO ,FIOForm


def get_name(request, fio_id):
    FIOFormSet = modelformset_factory(FIO,form=FIOForm)
  #  FIOFormSet = modelformset_factory(FIO)
    if request.method == 'POST':
        formset = FIOFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = FIOFormSet()
    return render(request, 'app_main/fio_set.html', {
        "formset": formset,
    })

def get_name1(request, fio_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FioForm()

    return render(request, 'app_main/fio.html', {'form': form})

def ret1(request):
    return HttpResponse('Пришли RET1')

# --------------------------------------------------
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!','email': 'uxx@mail.ru'}
        )
    return render(request,'app_main/contact_form.html', {'form': form})


def test1(request):
    return render(request,'app_main/contact_form.html')

def sea1(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            fio1 = FIO.objects.filter(name__icontains=q)
            return render_to_response('app_main/search_results.html',
                                      {'fio1': fio1, 'query': q})

    return render_to_response('app_main/search_form.html',  {'errors': error})



# --------------------------------------------------

def index(request):
    fio_list = FIO.objects.all()
    context = {'fio_list': fio_list}
    return render(request, 'app_main/lst_fio.html', context)


def detail(request, fio_id):
    question = get_object_or_404(FIO, pk=fio_id)
    return render(request, 'app_main/detail.html', {'question': question})


def results(request, fio_id):
    return HttpResponse("Привет, Мир. Это polls index.")
    #   question = get_object_or_404(FIO, pk=fio_id)
    #   return render(request, 'app_main/results.html', {'question': question})


def vote(request, fio_id):
    p = get_object_or_404(FIO, pk=fio_id)
    try:
        selected_choice = p.age
    except (KeyError, FIO.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app_main/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('main1:results', args=(p.id,)))
