from celery import Celery
import urllib.request
import os

BASE_DIR = '/home/lucka/Videos'

app = Celery(
    'app'
    , backend = 'rpc://'
    , broker = 'pyamqp://guest@localhost')

@app.task
def download(url, filename) :
    """
    Download a page and save it to the BASEDIR directory
      url: the url to download
      filename: the filename used to save the url in BASEDIR
    """
    response = urllib.request.urlopen(url)
    data = response.read()
    with open(BASE_DIR+"/"+filename,'wb') as file:
        file.write(data)
    file.close()

@app.task
def list() :
    """ Return an array of all downloaded files """
    return os.listdir(BASE_DIR)