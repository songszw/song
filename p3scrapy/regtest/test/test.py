# _*_ coding:utf-8 _*_

import re

line = 'xxx出生于2011年1月3号'
line = 'xxx出生于2011年1月'
line = 'xxx出生于2011/1/3'
line = 'xxx出生于2011-1-3'
line = 'xxx出生于2011-1'
line = 'xxx出生于2011/01/03'
line = 'xxx出生于2011-01-03'

regex_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"
macth_obj = re.match(regex_str,line)
if macth_obj:
    print(macth_obj.group(1))
