import os
from subprocess import Popen, PIPE

from bottle import route, run, template, redirect

dir = '/mnt/miukki/music'
files = os.listdir(dir)

music_player = None

list_template = '''
<ul>
% for item in files:
    <li><a href='/play/{{item}}'>{{item}}</a></li>
% end
</ul>
'''

@route('/list')
def list():
    return template(list_template, files=files)


@route('/')
def index():
    return 'lets play music!!'


@route('/play/<filename>')
def play(filename):

    global music_player
    if music_player:
        music_player.kill()

    music_player = Popen(['omxplayer', os.path.join(dir, filename)], stdin=PIPE, stdout=PIPE)

    redirect('/list')

run(host='localhost', port=8080)
