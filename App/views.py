from django.shortcuts import render

def nome_da_função(request):
	return render(request, "pages/index.html")
def cadastro(request):
	return render(request,"pages/cadastro.html")