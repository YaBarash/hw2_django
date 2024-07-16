import json

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = {'Name': name, 'Number': phone, 'Message': message}
        with open('data.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file)
    return render(request, 'contacts.html')
