# hotels



## Краткое описание 
Проект бронирование отелей c библиотекой fastapi изучение курса - https://artemshumeiko.zenclass.ru/public/products 

## 1 Настройка проекта

1. Создать и активировать виртуальное окружение

```angular2html
python3 -m venv .venv
source .venv/bin/activate
```
2.  Установить библиотеку fastapi

```angular2html
pip install fastapi[all]
```

3. Зафиксировать все библиотеки requirements.txt

```angular2html
python -m pip freeze > requirements.txt
```
## 2 Команды для запуска проекта на локальном компьютере

1. Запуск проекта на локальном компьютере тремя способами
   
#### 1 способ, флаг --reload не обязательный
```angular2html
uvicorn main:app --reload
```
#### 2 способ
```angular2html
fastapi dev main.py
```
#### 3 способ если на
```angular2html
python main.py
```
#### Remark: Данный вид запуска применяется при разворачивании проекта на сервере
## 3 Установка и настройка docker в локальном компьютере для линукса - https://docs.docker.com/engine/install/ubuntu/

1. Set up Docker's apt repository.

```angular2html
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. Install the Docker packages.

```angular2html
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the Docker Engine installation is successful by running the hello-world image.

```angular2html
sudo docker run hello-world
```

4. Для запуска docker без sudo необходимо сделать:

```angular2html
sudo usermod -aG docker $USER
```

5. /home/d/.docker - В директории на локальном компьютере удалить папку
6. Выполнить reboot

## 3.1 Запуск проекта в Docker
1. Перейти в директорию проекта на локальном компьютере через терминал пример:
   <img alt="Пример" height="100" src="![img.png](img.png)" title="Пример" width="100"/>
2. Собрать образ контейнера
```angular2html
docker build -t fastapi .
```
3. Проверить добавление образа
```angular2html
docker images
```
4. Запустить проект внутри контейнера
```angular2html
docker run -it fastapi bash
```
5. Команды, чтобы удалить контейнер и образ
```angular2html
docker rm <id_container>
docker rmi <id_images>
```

## 4 Дополнительная информация по проекту

1. Доступ к swagger документации - http://127.0.0.1:8000/docs#/

