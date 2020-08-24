from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import OpenUrls
from django.http import JsonResponse


def home(request):
    return render(request, "index.html")


def shortener(request):
    ur_name = request.POST.get('url', None)
    if ur_name is not None:
        if not OpenUrls.objects.filter(origin_url=ur_name).exists():
            add = OpenUrls.objects.create(origin_url=ur_name)
            add.save()
            data = {
                "Url": ur_name + "/" + get_object_or_404(OpenUrls, origin_url=ur_name).shorted_url,
                "Short": get_object_or_404(OpenUrls, origin_url=ur_name).shorted_url
            }
            return JsonResponse(data)
        else:
            data = {
                "Url": request.get_host() + "/" + get_object_or_404(OpenUrls, origin_url=ur_name).shorted_url,
                "Short": get_object_or_404(OpenUrls, origin_url=ur_name).shorted_url
            }
            return JsonResponse(data)
    return HttpResponse(ur_name)


def redirect(request, shortener, *args, **kwargs):
    exists = get_object_or_404(OpenUrls, shorted_url=shortener)
    exists.click += 1
    exists.save()
    return HttpResponseRedirect(exists.origin_url)


def ip(request):
    return HttpResponse(request.META['REMOTE_ADDR'] + " " + request.headers['User-Agent'])
