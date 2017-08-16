import configparser
conf = configparser.ConfigParser()
conf.read('example.ini')
# print(conf.sections())
# print(conf.defaults())
print(conf['bitbucket.org']['User'])