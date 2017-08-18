import pickle,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
__db_main = BASE_DIR+r'\data\main_dict'
__db_teacher = BASE_DIR+r'\data\teacher_dict'

class School(object):
    '''创建学校'''
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('学校名：[%s]\t 地址：[%s]'%(self.name,self.addr))

    def hire_teacher(self,dict,course,teacher,file):
        '''数据库添加讲师信息'''
        dict[self][course] = {'teacher':teacher}
        file_oper(file,'wb',dict)

    def create_course(self,dict,course,file):
        '''数据库添加课程资料'''
        dict[self][course]={}
        file_oper(file,'wb',dict)

    def create_grade(self,dict,teacher_dict,course,grade,teacher,file1,file2):
        '''数据库添加班级信息'''
        dict[self][course] = grade
        file_oper(file1,'wb',dict)
        teacher_dict[teacher] = {'grade':grade}
        file_oper(file2,'wb',teacher_dict)


class Course():
    '''创建课程'''
    def __init__(self,name,price,time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        '''查看课程信息'''
        print('[课程：%s] \t [价格：%s]\t[周期：%s个月]'%(self.name,self.price,self.time))


class Grade():
    '''创建班级'''
    def __init__(self,name,course,teacher):
        student = set([])
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = student

    def cat_grade(self):
        print('[班级：%s]\t [课程：%s]\t [讲师：%s]'%(self.name,self.course,self.teacher))

    def add_student(self,student_name,dict,teacher,file):
        self.student.add(student_name)
        dict[teacher] = {'grade':self}
        file_oper(file,'wb',dict)

class People()
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Teacher(People):
    def __init__(self,name,age,school,course,role = '讲师'):
        super(Teacher,self).__init__(name,age)
        self.school = school
        self.course = course
        self.role = role

    def cat_teacher(self):
        '''查看老师资料和课程'''
        print('课程:%s\t 讲师:%s'%(self.course,self.name))

def file_oper(file,mode,*args):
    '''数据库写入，读取操作'''
    if mode == 'wb':
        with open(file,mode) as f:
            dict = args[0]
            f.write(pickle.dumps(dict))
    if mode == 'rb':
        with open(file,mode) as f:
            dict = pickle.loads(f.read())
            return dict
def information(dict,mode,*args):
    '''通过匹配mode模式，打印相应的输出信息'''
    if args:
        dict_info,set_info={},args[0]
    else:
        dict_info,set_info={},set([])
    if dict:
        for key in dict:
            if mode == 'course':
                key.cat_course()
            if mode == 'main':
                key.cat_school()
            if mode == 'teacher' and key == 'teacher':
                dict[key].cat_teacher()
                set_info.add(dict[key].name)
            if mode == 'teacher_center':
                pass
            if type(key) != str:
                dict_info[key.name] = key
    return dict_info,set_info

def school_center():
    '''学校管理中心'''
    Flag = True
    while Flag:
        dict_main = file_oper(__db_main,'rb')
        res_dict = information(dict_main,'main')[0]
        school_name = input('\33[34;0m输入要选择的学校名\33[0m:').strip()
        if school_name in res_dict:
            school = res_dict[school_name]
            while Flag:
                print('欢迎进入%s 学校'% school_name)
                choice = options(list_school)






