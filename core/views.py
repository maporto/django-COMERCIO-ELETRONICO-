# views.py 
from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
   return render(request, "index.html") 
   
def contato(request): 
   if request.method == "GET": 
      print ("CONTATO GET")
      return render(request, "contato.html") 
   else:
      print ("CONTATO POST")
      print ("Nome: ", request.POST.get("nome"), " - E-mail:", request.POST.get("email"), " - Telefone:", request.POST.get("telefone"), " - CPF:", request.POST.get("cpf"), " - Sexo:", request.POST.get("sexo"), " - Data Nascimento:", request.POST.get("dtnasc"))
      return render(request, "index.html")

def login(request): 
   print ("LOGIN")
   if request.method == "GET": 
      print ("LOGIN GET")
      return render(request, "login.html") 
   else:
      print ("LOGIN POST")
      if request.POST['senha'] == "teste123":
         print ("SENHA VALIDA")
         print ("Usuario: ", request.POST.get("email"), " entrou com sucesso!")
         return render(request, "index.html")
      else:  
         print ("SENHA INVALIDA")
         print ("Usuario: ", request.POST.get("email"), " digitou a senha errada!")
         return render(request, "login.html")
