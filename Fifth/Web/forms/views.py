# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from . import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from .forms import GoodsForm, GeneralForm
from .models import Form, Good
# from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, ListView, DetailView
from django.http import HttpResponse
# from django.template.loader import get_template
from .pdfGenerator import render_to_pdf


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def viewForms(request):
    forms = Form.objects.all()
    context = {
        'forms': forms,
    }
    return render(request, "forms/formView.html", context)

def formlist(request):
    forms = Form.objects.filter(responsible_worker=request.user.id)
    users = User.objects.all()
    template = loader.get_template('forms/formView.html')
    if request.method == 'POST':
        generalForm = GeneralForm(request.POST)
        if generalForm.is_valid():
            temp = generalForm.save(commit=False)
            temp.responsible_worker = request.user
            temp.save()
            temp.commissioners.add(*(generalForm['commissioners'].value()))
        return redirect("formView")
    else:
        newForm = GeneralForm()
        context = {
            "forms": forms,
            "newForm": newForm,
            "users": users,
        }
        return HttpResponse(template.render(context, request))


def formDetails(request, id):
    form = Form.objects.get(id=id)
    goods = Good.objects.filter(form=id)
    template = loader.get_template('forms/formDetails.html')
    if request.method == 'POST':
        goodForm = GoodsForm(request.POST)
        print(goodForm.is_valid())
        if goodForm.is_valid():
            temp = goodForm.save(commit=False)
            temp.form = form
            temp.total_sum = temp.amount * temp.cost
            temp.save()
        return redirect("formDetails", id=id)
    else:
        newForm = GoodsForm()
        context = {
            "form": form,
            "goods": goods,
            "newForm": newForm,
        }
        return HttpResponse(template.render(context, request))


# def view_as_pdf(request, *args, **kwargs):
#     data_tosend = form_pdf_data(kwargs)
#     pdf = render_to_pdf('forms/pdfDocument.html', data_tosend)
#     return HttpResponse(pdf, content_type='application/pdf')


def force_download_pdf(request, *args, **kwargs):
    template = loader.get_template('forms/pdf.html')
    data_tosend = form_pdf_data(kwargs)
    html = template.render(data_tosend)
    pdf = render_to_pdf('forms/pdf.html', data_tosend)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Form%s.pdf' % (kwargs['id'])
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


def actformdetails(request, id):
    act = get_object_or_404(Form, pk=id)

    total = 0
    for a in act.goods.all():
        total += a.total_sum

    return render_to_pdf("forms/pdf.html", {
        "act": act,
        "total": total,
    })

def form_pdf_data(kwargs):
    data = Form.objects.get(id=kwargs['id'])
    total = 0
    data_tosend = vars(data)
    print(vars(data))

    # data_tosend['commissioners'] = User.objects.get()
    # print(vars(data))
    data_tosend['goods'] = Good.objects.filter(form=kwargs['id'])
    for temp in data_tosend['goods']:
        total += temp.total_sum
    data_tosend['total'] = total
    return data_tosend
