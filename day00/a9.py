import time as t
class MyTimer():
    def __init__(self):
        self.prompt = '未开始计时'
        self.lasted = []
        self.start = 0
        self.stop = 0
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    #开始计时
    def start(self):
        self.start = t.localtime()
        print('计时开始...')

    #停止计时
    def stop(self):
        self.stop = t.localtime()
        print('计时结束！')
        self._calc()
        
    #内部方法计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            self.prompt+=str(self.lasted[index])

        print(self.prompt)

