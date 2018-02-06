# _*_ coding:utf-8 _*_

import re

line = 'bobby123'

regex_str = '^.*3$'

if re.match(regex_str,line):
    print('yes')
else:
    print('no')