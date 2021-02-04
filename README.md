# Flask API template 🤯🤯🤯
This is a public repository with contents of Flask Web Development, here you will find examples applied in a Restful API, and a basic and flexible structure to start your Flask apps.
<br />
<h1>Steps to run this app 👇👇👇</h1>
<br />

1- Cloning repo
-----------------------------------

```
$ git clone https://github.com/josethz00/flask_api_template/edit/initial_template/
```

2- Enter in folder
-----------------------------------

```
$ cd server
```

3- Install the requirements
-----------------------------------

```
$ pip3 install -r requirements.txt
```

4- Start Flask server
-----------------------------------

```
$ python3 app.py
```

5- Start redis-server (if is not active)
-----------------------------------
```
$ redis-server --daemonize yes
```

6- Start celery worker (if your application needs)
-----------------------------------

```
$ celery -A tasks app.celery --loglevel=INFO
```
<br />
<div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/3otPoS81loriI9sO8o" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/filmeditor-will-ferrell-elf-3otPoS81loriI9sO8o">via GIPHY</a></p>
