import threading,time
def run(n):
  global num
  num+=1
  print(num)

num = 0
t_obj = []

for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.start()
    t_obj.append(t)
for t in t_obj:
    t.join()

print('-----------all threads has fished',threading.current_thread(),threading.active_count())
print(num)