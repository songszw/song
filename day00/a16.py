class Countlist:
    def __init__(self,*args):
        self.value = [x for x in args]
        self.count = {}.fromkeys(range(len(self.value)),0)

    def __len__(self):
        return len(self.value)
    def __getitem__(self, item):
        self.count[item]+=1
        return self.value[item]
