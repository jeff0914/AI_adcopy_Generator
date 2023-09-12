# AI_adcopy_Gernerator
 
A Django project that deploys JWT, REST framework, and an AI advertising copy generator on Docker.

## Prerequisites

- Docker
- OpenAI API

## Installation to Start

1. Clone this repository
```bash
   git clone https://github.com/jeff0914/AI_adcopy_Gernerator.git
```
2. Navigate to the project directory
```bash
cd AI_adcopy_Gernerator
```
3. Put your OpenAI API KEY in .env 
" OPENAI_API_KEY=  "

4. Build the Docker image
```bash
docker-compose build
```
5. Run the Docker container
```bash
docker-compose up -d
```
6. Start the AI adcopy Gernerator
```bash
docker exec -it {web-container-name} bash

python  manage.py makemigrations app

python manage.py migrate
```
7. Click url And Gernerate It !
http://localhost:8000/

## Usage

[AI ad copy Generator](https://www.notion.so/AI-ad-copy-Generator-217fca2c1c4c4122a1e28b6694310060) 

[Create Account For Backend, Rest Framework For CRUD](https://www.notion.so/Django-Rest-Framework-For-CRUD-5ee026e45ea641698bfdd946505b5ca3?pvs=4)  


## License
MIT license