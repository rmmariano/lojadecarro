

from datetime import datetime
from os import path as os_path

# Pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH=os_path.sep.join(os_path.abspath(__file__).split(os_path.sep)[:-2])

now = datetime.now()
s_now = str(now)

filename = 'saida_cron_cron.txt'
path = PROJECT_PATH+'/cron/'+filename
#path = '/docs/teste/'+filename

if not os_path.exists(path):
	arquivo = open(path, 'w')
	arquivo.write('Comecando em '+s_now+'\n')
	arquivo.close()
else:
	arquivo = open(path, 'r')
	texto = arquivo.readlines()
	texto.append(s_now+'\n') 
	arquivo = open(path, 'w')
	arquivo.writelines(texto)
	arquivo.close()