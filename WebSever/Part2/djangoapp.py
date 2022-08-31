import sys
sys.path.insert(0, './helloword')
from helloword import wsgi


app = wsgi.application