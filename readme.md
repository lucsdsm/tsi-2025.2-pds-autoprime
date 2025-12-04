
**AutoPrime - Backend Django (proxy para API externa)**

- **Status:** Protótipo funcional
- **Stack:** Django 4.2, Python 3.11, Docker

**Visão Geral**
- Projeto Django que expõe endpoints HTTP para gerenciar carros. Todas as operações são proxied para uma API externa — não é usado banco de dados local para dados dos carros.

**Estrutura principal**
- `django/` : código do projeto Django
	- `autoprime/` : configurações do projeto (settings, urls, wsgi)
	- `api/` : app que contém as views/urls/templates que fazem proxy para a API externa

**Endpoints disponíveis (mapeados no Django)**
Todos usam `POST` e estão expostos na raiz do servidor Django (porta 8080 por padrão):

- `POST /getCarro` — body `modelo=BMW` → retorna JSON com `preco`
- `POST /saveCarro` — body `modelo=BMW,350000` → salva via API externa
- `POST /deleteCarro` — body `modelo=BMW` → deleta via API externa
- `POST /updateCarro` — body `modelo=BMW,375000` → atualiza via API externa
- `POST /listarCarros` — sem body → retorna lista de carros via API externa

As views do Django apenas repassam a requisição para a `API_BASE_URL` configurada e retornam a resposta ao cliente, com tratamento básico de erros e timeout (10s).

**Configuração da API externa**
- Variável de ambiente utilizada: `API_BASE_URL`
- Arquivo de exemplo: `django/.env.example`
- Arquivo de configuração local: `django/.env` (substitua `http://SEU_IP_AQUI:PORTA` pelo IP/porta real da API externa)

Exemplo:
```
API_BASE_URL=http://192.168.1.100:8080
```

**Como rodar (com Docker)**
1. Entre na pasta do Django:
```bash
cd django
```
2. Construa e suba o container:
```bash
docker-compose up --build
```
3. Acesse a interface de testes (template HTML simples):
- http://localhost:8080

**Dependências**
- Listadas em `django/requirements.txt` (Django e `requests`)

**Notas importantes**
- O projeto foi implementado como um proxy/gateway para a API externa — em nenhuma hipótese os dados dos carros são persistidos localmente.
- Os templates HTML em `django/api/templates/api/index.html` são básicos e servem apenas para testes manuais rápidos.
- O Django Admin está disponível em `/admin` (útil para gerenciar objetos do Django se necessário), mas não é usado para gerenciar os carros.
- CSRF foi desabilitado nas views que fazem proxy para facilitar testes via formulários e `curl`. Em produção isso deve ser revisado.

**Testes rápidos (curl)**
```bash
# Salvar
curl -X POST http://localhost:8080/saveCarro -d "modelo=BMW,350000"

# Consultar
curl -X POST http://localhost:8080/getCarro -d "modelo=BMW"

# Atualizar
curl -X POST http://localhost:8080/updateCarro -d "modelo=BMW,375000"

# Deletar
curl -X POST http://localhost:8080/deleteCarro -d "modelo=BMW"

# Listar todos
curl -X POST http://localhost:8080/listarCarros
```

**Onde editar se precisar**
- `django/autoprime/settings.py` — alterar `API_BASE_URL` padrão
- `django/api/views.py` — lógica que faz as requisições para a API externa
- `django/api/templates/api/index.html` — formulário HTML de testes

