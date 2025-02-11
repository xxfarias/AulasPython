import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
    print('Foi possivel acessar o site')
except:
    print('Não foi possivel acessar o site')
else:
    print('Tudo ok')
    print(site.read())