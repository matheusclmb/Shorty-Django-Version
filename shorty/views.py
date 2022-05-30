from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets
from utils.shorty.form import ShortenerForm

from shorty.models import Shortener
from shorty.serializers import ShortenerSerializer, StatsSerializer


# Create your views here.
def home(request):
    template = "shorty/pages/index.html"

    context = {}

    context["form"] = ShortenerForm()

    if request.method == "GET":
        return render(request, template, context)

    elif request.method == "POST":
        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri("/") + shortened_object.shortcode

            long_url = shortened_object.url

            context["new_url"] = new_url
            context["long_url"] = long_url

            return render(request, template, context)

        context["errors"] = used_form.errors

        return render(request, "shorty/pages/index.html")


def redirect_url_view(request, shortened_path):

    try:
        shortener = Shortener.objects.get(shortcode=shortened_path)

        shortener.redirectCount += 1

        shortener.save()

        return HttpResponseRedirect(shortener.url)

    except:
        raise Http404("Sorry this link does not exist")


class ShortenerViewSet(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer
    lookup_field = "shortcode"


class StatsViewSet(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = StatsSerializer
    lookup_field = "shortcode"
