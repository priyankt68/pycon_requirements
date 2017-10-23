import subprocess

LATEST_DATA_URL = 'https://github.com/pythonindia/inpycon2017/blob/master/data/api/tracks.json'


if __name__ == '__main':

    subprocess.call(['wget', '-P', '/data', LATEST_DATA_URL])


