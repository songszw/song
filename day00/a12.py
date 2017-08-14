import time as t


class MyTimer():
    # 初始化
    def __init__(self):
        self.unit = ['年', '月', '日', '时', '分', '秒']
        self.begin = 0
        self.end = 0
        self.prompt = '未开始计时'

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # begin
    def start(self):
        self.begin = t.localtime()
        self.prompt='请先停止计时'
        print('开始计时')

    # stop
    def stop(self):
        if not self.begin:
            print('请先运行开始')
            return

        self.end = t.localtime()
        print('停止计时')
        self._calc()

    # 计算运行时间
    def _calc(self):
        self.prompt = '总共运行了'
        self.lasted = []
        for item in range(6):
            self.lasted.append(self.end[item] - self.begin[item])
            if self.lasted[item]:
                self.prompt += (str(self.lasted[item]) + self.unit[item])

    def __add__(self,other):
        prompt = '总共运行了'
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=(str(result[index])+self.unit[index])

        return prompt


