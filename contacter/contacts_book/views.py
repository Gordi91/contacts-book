from django.shortcuts import render
from django.views import View


class Menu(View):
    def get(self, request):
        template_name = 'contacts_book/menu.html'
        return render(request, template_name)
