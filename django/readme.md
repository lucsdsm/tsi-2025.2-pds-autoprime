# AutoPrime Backend - Django

Backend do sistema AutoPrime para gerenciamento de carros.

## Endpoints Disponíveis

Todos os endpoints usam método POST:

- `POST /getCarro` - Consultar preço de um carro
  - Body: `modelo=BMW`
  - Response: `{"preco": "350000.00"}`

- `POST /saveCarro` - Salvar novo carro
  - Body: `modelo=BMW,350000`
  - Response: status 200

- `POST /deleteCarro` - Deletar carro
  - Body: `modelo=BMW`
  - Response: status 200

- `POST /updateCarro` - Atualizar preço do carro
  - Body: `modelo=BMW,375000`
  - Response: status 200

- `POST /listarCarros` - Listar todos os carros
  - Body: (vazio)
  - Response: `{"carros": [{"modelo": "BMW", "preco": "350000.00"}]}`

## Como Rodar

1. Entre na pasta django:
```bash
cd django
```

2. Suba os containers:
```bash
docker-compose up --build
```

3. Acesse no navegador:
- Interface de testes: http://localhost:8080
- Admin Django: http://localhost:8080/admin

## Estrutura do Banco

Tabela `carros`:
- id (auto)
- modelo (varchar, único)
- preco (decimal)

## Notas

- Porta: 8080
- CSRF desabilitado nos endpoints da API
- Templates HTML sem CSS para testes rápidos
