from django.shortcuts import render, redirect
from django.template import loader

# Create your views here.
from users.forms import RegistrationForm


def register(request):
    # template = loader.get_template('forms/formView.html')
    if request.method == "POST":
        registrationForm = RegistrationForm(request.POST)
        print(registrationForm.is_valid(), "AAAAAAAAAAAAAAAAAAAA")
        if registrationForm.is_valid():
            registrationForm.save()
            return redirect("users/login.html")
    else:
        registrationForm = RegistrationForm()

    return render(request, "users/registration.html", {
        "newForm": registrationForm
    })
    # return HttpResponse(template.render(context, request))
