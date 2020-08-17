# NaversAPI
NaversAPI é uma api escrita em python com framework django para criação de navers e projetos.

# Requisitos
- python 3
- django
- django rest framework

# Instalação
primeiro crie uma pasta onde preferir e clone o projeto:
```
git clone https://github.com/ArondevIta/navers.git
```
após clonar o projeto vamos instalar os requisitos, rode o seguinte comando:
``` 
pip install -r requirements.txt
```
este comando irá instalar os requisitos necéssarios para rodar o projeto.

Após instalar os requirements.txt iremos rodar as migrations para criar a base de dados, rode o seguinte comando:
```
python manage.py makemigrations
```
e agora
```
python manage.py migrate
```
Após instalar as migrations aconselho criar um super usuario para visualizar o admin:
```
python manage.py createsuperuser
```
agora vamos iniciar nosso projeto:
```
python manage.py runserver
```

# Como usar
Aconselho usar o POSTMAN ou INSOMNIA para testar as rotas 
## rotas
as rotas disponiveis são: 

### conta 
- accounts/ => cria um usúario
- login/ => loga na aplicação e retorna o token para navegar
### navers
- GET navers/index/ => retornar lista de navers para um usuario caso ele tenha navers cadastrado
- GET navers/<id>/show/ => retorna um naver especifico caso ele esteja ligado ao usúario que fez a requisição
- POST navers/ => cria um naver ligado ao usuario que fez a requisição
- PUT navers/<id>/ => atualiza os dados do naver caso ele exista e esteja ligado ao usúario que fez a requisição
- DELETE navers/<id>/ => deleta um naver caso ele exista e esteja ligado ao usúario que fez a requisição
### projects
- GET projects/index/ => retornar lista de projetos para um usuario caso ele tenha projetos cadastrado
- GET projects/<id>/show/ => retorna um projeto especifico caso ele exista e esteja ligado ao usúario que fez a requisição
- POST projects/ => cria um projeto ligado ao usuario que fez a requisição
- PUT projects/<id>/ => atualiza os dados do projeto caso ele exista e esteja ligado ao usúario que fez a requisição
- DELETE projects/<id>/ => deleta um projeto caso ele exista e esteja ligado ao usúario que fez a requisição
# Documentação
Para ter mais detalhes das rotas pode ser consultada a documentação disponível no link abaixo:
https://documenter.getpostman.com/view/9953840/T1LQhmRA

Obrigado!
