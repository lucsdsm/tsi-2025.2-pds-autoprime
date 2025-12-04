from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
import json


def index(request):
    """Página inicial com formulários para testar os endpoints"""
    return render(request, 'carros/index.html')


@csrf_exempt
def get_carro(request):
    """Endpoint: getCarro - Retorna o preço de um carro pelo modelo via API externa"""
    if request.method == 'POST':
        try:
            modelo = request.POST.get('modelo', '').strip()
            
            if not modelo:
                return JsonResponse({'erro': 'Modelo não informado'}, status=400)
            
            # Faz requisição para a API externa
            api_url = f"{settings.API_BASE_URL}/getCarro"
            response = requests.post(api_url, data={'modelo': modelo}, timeout=10)
            
            if response.status_code == 200:
                return JsonResponse(response.json())
            else:
                return JsonResponse(response.json() if response.content else {'erro': 'Erro na API'}, 
                                  status=response.status_code)
                
        except requests.exceptions.RequestException as e:
            return JsonResponse({'erro': f'Erro ao conectar com a API: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


@csrf_exempt
def save_carro(request):
    """Endpoint: saveCarro - Salva um novo carro via API externa"""
    if request.method == 'POST':
        try:
            data = request.POST.get('modelo', '')
            
            if ',' not in data:
                return JsonResponse({'erro': 'Formato inválido. Use: modelo,preço'}, status=400)
            
            # Faz requisição para a API externa
            api_url = f"{settings.API_BASE_URL}/saveCarro"
            response = requests.post(api_url, data={'modelo': data}, timeout=10)
            
            if response.status_code == 200:
                return HttpResponse(status=200)
            else:
                return JsonResponse(response.json() if response.content else {'erro': 'Erro na API'}, 
                                  status=response.status_code)
            
        except requests.exceptions.RequestException as e:
            return JsonResponse({'erro': f'Erro ao conectar com a API: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


@csrf_exempt
def delete_carro(request):
    """Endpoint: deleteCarro - Deleta um carro via API externa"""
    if request.method == 'POST':
        try:
            modelo = request.POST.get('modelo', '').strip()
            
            if not modelo:
                return JsonResponse({'erro': 'Modelo não informado'}, status=400)
            
            # Faz requisição para a API externa
            api_url = f"{settings.API_BASE_URL}/deleteCarro"
            response = requests.post(api_url, data={'modelo': modelo}, timeout=10)
            
            if response.status_code == 200:
                return HttpResponse(status=200)
            else:
                return JsonResponse(response.json() if response.content else {'erro': 'Erro na API'}, 
                                  status=response.status_code)
                
        except requests.exceptions.RequestException as e:
            return JsonResponse({'erro': f'Erro ao conectar com a API: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


@csrf_exempt
def update_carro(request):
    """Endpoint: updateCarro - Atualiza o preço de um carro via API externa"""
    if request.method == 'POST':
        try:
            data = request.POST.get('modelo', '')
            
            if ',' not in data:
                return JsonResponse({'erro': 'Formato inválido. Use: modelo,preço'}, status=400)
            
            # Faz requisição para a API externa
            api_url = f"{settings.API_BASE_URL}/updateCarro"
            response = requests.post(api_url, data={'modelo': data}, timeout=10)
            
            if response.status_code == 200:
                return HttpResponse(status=200)
            else:
                return JsonResponse(response.json() if response.content else {'erro': 'Erro na API'}, 
                                  status=response.status_code)
                
        except requests.exceptions.RequestException as e:
            return JsonResponse({'erro': f'Erro ao conectar com a API: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


@csrf_exempt
def listar_carros(request):
    """Endpoint: listarCarros - Lista todos os carros via API externa"""
    if request.method == 'POST':
        try:
            # Faz requisição para a API externa
            api_url = f"{settings.API_BASE_URL}/listarCarros"
            response = requests.post(api_url, timeout=10)
            
            if response.status_code == 200:
                return JsonResponse(response.json())
            else:
                return JsonResponse(response.json() if response.content else {'erro': 'Erro na API'}, 
                                  status=response.status_code)
                
        except requests.exceptions.RequestException as e:
            return JsonResponse({'erro': f'Erro ao conectar com a API: {str(e)}'}, status=500)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)
