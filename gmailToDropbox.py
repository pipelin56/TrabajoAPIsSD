from flask import Flask
from flask import render_template
from flask import request
from gmail import Gmail
import gmail
import os
import zipfile
import shutil
import datetime
import dropbox
app = Flask(__name__.split('.')[0])

contA = 0
archivo = ''
def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            #print 'zipping %s as %s' % (os.path.join(dirname, filename),arcname)
            zf.write(absname, arcname)
    zf.close()

@app.route("/success",methods=['POST'])
def sube():
	global contA
	global archivo
	token = request.form['tokenkey']
	app_key = '5g0781coh89ty89'
	app_secret = 'a77tewdx1s0cpa6'

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	authorize_url = flow.start()

	access_token, user_id = flow.finish(token)

	client = dropbox.client.DropboxClient(access_token)
	file = open(archivo+'.zip')
	response = client.put_file('Seguridad/'+archivo+'.zip',file)
	return render_template('success.html',n=contA)

@app.route("/dropbox",methods=['POST'])
def empaqueta():
	global contA
	global archivo
	contA=0
	username = request.form['email']
	password = request.form['pass']
	filtro = request.form['filtroH']
	print(username)
	print(password)
	g = gmail.login(username, password)
	print g.logged_in
	if filtro=='1':
		messages = g.inbox().mail()
	else:
		if filtro=='2':
			messages = g.inbox().mail(read=True)
		else:
			messages = g.inbox().mail(unread=True)
	if not os.path.exists('adjuntos'):
		os.makedirs('adjuntos')
	for mensaje in messages:
		mensaje.fetch()
		fecha = mensaje.sent_at.strftime("%d %m %Y %H:%M:%S")
		directory = 'adjuntos/'+mensaje.subject+' '+fecha
		if mensaje.attachments:
			if not os.path.exists(directory):
				os.makedirs(directory)
		for adjunto in mensaje.attachments:
			adjunto.save(directory +'/'+adjunto.name)
			contA = contA +1;
	archivo = "copia "+datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	zip('adjuntos/',archivo)
	shutil.rmtree('adjuntos')
	return render_template('dropbox.html')

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()