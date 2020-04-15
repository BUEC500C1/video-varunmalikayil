#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/flaskapp')
import tweepy
from flaskapp import app as application