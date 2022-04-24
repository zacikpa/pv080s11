import yaml
import subprocess
import hashlib
import subprocess
import flask


def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=file)
    subprocess.call(command, shell=True)


def load_config(filename):
    # Load a configuration file into YAML
    stream = file.open(filename, "r")
    config = yaml.load(stream)


def fetch_website(urllib_version, url):
    # Import the requested version of urllib
    exec("import urllib% as urllib" % urllib_version, globals())
    # Fetch and print the requested URL
    http = urllib.PoolManager()
    r = http.request('GET', url)
    print(r.data)


def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")
