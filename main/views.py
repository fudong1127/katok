#coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import models
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from models import Record, Foto, Gallery

from django.conf import settings

from django.http import HttpResponseRedirect

from django.core.mail import send_mail
from katok.main.forms import RecordForm

def get_page(request, klass, count):
    paginator = Paginator(klass.objects.all(), count)

    try:
        page_number = int(request.GET.get('page', '1'))
    except ValueError:
        page_number = 1

    try:
        page = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        page = paginator.page(paginator.num_pages)

    return (page, page_number)


def pages(request, template_name):
    return render_to_response(template_name, context_instance=RequestContext(request))


def comment(request):
     if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            new_comment = form.save()        
            return HttpResponseRedirect('/comment/')
        
     else:
         form = RecordForm()
         
     comments = Record.objects.all()
    
     return render_to_response('comment.html', {'form': form, 'comments': comments}, context_instance=RequestContext(request))   
    
def view_gallery(request):
    page, page_number = get_page(request, Gallery, settings.GALLERY_COUNT)
    return render_to_response('gallery.html', {'gallery': True, 'page': page, 'page_number': page_number},
                              context_instance=RequestContext(request))