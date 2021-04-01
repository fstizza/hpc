from subprocess import run, call
import os

targets = {'o1': { 'comp': 'cc', 'evars' : [('PAPI_REPORT','1')], 'flags': ['-O1--march-native']}}

def correr(targetName):
  run('cd' + targetName + ' && ./tiny_md > res.out && cd ../')
  pass

def compilar(target):
  tn, cfg = target
  print("Compilando {0}".format(tn))
  print("Configuración")
  
  prefix = ''
  
  keys = cfg.keys()

  if('evars' in keys):
    for evar in cfg['evars']:
      prefix += '{0}={1} '.format(evar[0], evar[1])

  # if('comp' in keys):
  #   prefix += 'CC={0} '.format(cfg['comp'])
  
  if('flags' in keys):
    prefix += 'CFLAGS='
    for arg in cfg['flags']:
      prefix += arg + ' '

  print(prefix)
  
  if(os.path.isdir('./${0}'.format(tn))):
    run(['meson', 'setup', '--reconfigure'])  

  else:
    run(['{0} meson setup {1}'.format(prefix, tn)], shell= True, text= True)
  
  # return res.returncode == 0


def automatizar():
  for target in targets.items():
    if(not compilar(target)):
      print("Error")
      
    
    # if(not correr())


if __name__ == '__main__':
  automatizar()
  



    