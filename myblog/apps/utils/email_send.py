# _*_ coding:utf-8 _*_
from random import Random

from users.models import EmailVerifyRecord

def random_str(rendomlength = 8):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    lenth = len(chars)
    random = Random
    for i in range(rendomlength):
        str+=chars[random.randint(0,length)]
    return str




def send_register_email(email,type=0):
    email_record = EmailVerifyRecord()
    rendom_str =Random()



def generate_random_str():
    pass
