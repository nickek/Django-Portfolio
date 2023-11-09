from django.shortcuts import redirect
from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse, response
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile(request):

    template = loader.get_template('user_profile/profile.html')
    return HttpResponse(template.render({}, request))
