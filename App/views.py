from django.shortcuts import render

def nome_da_função(request):
	return render(request, "pages/home.html")

def cadastro(request):
	return render(request,"pages/cadastro.html")

def info(request,id):
	return render(request, "pages/info.html")#context={}

# def login(request):
# 	return render(request, "pages/login.html")