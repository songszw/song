import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'ServerAliveInterval':'45',
    'Compression':'yes',
    'CompressionLevel':'9'
}
config['bitbucket.org']={}
config['bitbucket.org']['User'] = 'hg'
config['bitbucket.server.com']={}
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
config['DEFAULT']['ForwardXll'] = 'yes'

with open('example.ini','w') as configfile:
    config.write(configfile)