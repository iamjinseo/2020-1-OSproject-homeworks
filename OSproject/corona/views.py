from django.shortcuts import render
from django.http import HttpResponse
from .models import Country

def index(request):
    countries = Country.objects.all()
    # for country in countries :
    #     str+="<p>{}(은)는 위험도 {}인 국가입니다. 자세한 내용은 아래를 참고해주세요<br>".format(country.name, country.safety)
    #     str+="입국 가능 여부는 '{}' 상태입니다.<br>".format(country.entrance)
    #     str+="{}".format(country.information)+"</p>"
    context = {'countries':countries}
    return render(request, 'corona/index.html', context)
