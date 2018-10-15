import os
import configparser as cg
import shutil

def init():
    global config
    config = cg.ConfigParser()
    config.read('config.ini')
    print(config['Folder']['Project'])
    return config

def move(file, fro, to, to2):
    shutil.copy(fro + file, to)
    shutil.copy(fro + file, to2)
    print(file + ' updated')

def check(file, fro):
    if os.path.getmtime(fro + file) > os.path.getmtime(config['Folder']['CTM'] +"/"+file) or os.path.exists(config['Folder']['CTM'] +"/"+file) == False:
        return True
    else:
        return False

def main():
    init()
    print(os.listdir(config['Folder']['Project']))

    for x in os.listdir(config['Folder']['Project']):
        if  os.path.isdir(config['Folder']['Project']+"/"+x):

            print('In directory: '+x)

            for y in os.listdir(config['Folder']['Project']+"/"+x):


                if y.endswith('.txm'):
                    if check(y, config['Folder']['Project'] + "/" + x + "/"):
                        move(y, config['Folder']['Project'] + "/" + x + "/", config['Folder']['CTM'],
                         config['Folder']['Auto'])
    input('Press Enter to continue...')

main()