class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []


    def enroll(self,stu_obj):
        print('为学员 %s 办理注册手续'%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print('雇佣新员工: %s'%staff_obj.name)
        self.staffs.append(staff_obj)
class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


    def tell(self):
        pass


class Students(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Students,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade


    def tell(self):
        print('''
        ------info of teacher:%s------
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print('%s has paid tuition for $%s'% (self.name,amount))


class Teachers(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teachers,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ------info of teacher:%s------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def Teach(self):
        print('%s is teaching course[%s]'%(self.name,self.course))

school = School('一中','山西省朔州市朔城区🐐街')
t1 = Teachers('瓢',40,'男',5000,'地理')
t2 = Teachers('喵喵',35,'女',3500,'英语')
s1 = Students('蔡胖胖',25,'男','stu001','332')
s2 = Students('王爱',25,'女','stu002','332')
t1.tell()
t1.Teach()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)
school.staffs[0].Teach()
for stu in school.students:
    stu.pay_tuition(5000)

