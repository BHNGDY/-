import random
import time

print('刀削面传奇')
print('pre-1')
print('——————————————————————————————')
print('更新速览')
print('——————————————————————————————')
print('pre-1/2025-1-29')
print('——————————————————————————————')
print('1.添加：游玩界面')
print('2.添加：业绩')
print('3.画大饼：配料选择')
print('——————————————————————————————')
yj = 0
x = 1
for x in range (2):
  print('刀削面')
  print('哦刀削面')
input('ENTER开始新的一天')
pc = ("刀削面","卤蛋","面","香菜",)
fs = 0
sc = 0
th = 0
fo = 0
print('——————————————————————————————')
while x == 1:
  print("您有",pc[0],fs,"碗")
  print("您有",pc[1],sc,"个")
  print("您有",pc[2],th,"份")
  print("您有",pc[3],fo,"份")
  print('业绩：',yj)
  print('——————————————————————————————')
  print('等待顾客中···')
  print('——————————————————————————————')
  st = random.randint(3,9)
  time.sleep(st)
  print('一位顾客来到！')
  y = random.randint(0,2)
  if y == 0:
    print('他/她要一份加卤蛋的面')
  else:
    if y == 1:
      print('他/她要一份加香菜的面')
    else:
      print('他/她要一份加卤蛋和香菜的面')
  anj = random.randint(0,8)
  print(anj)
  print('请在键盘上按下上面的数字上菜')
  a = int(input())
  if  anj <= a and anj >= a:
    print('顾客满意地享用刀削面去了，业绩+1')
    yj += 1
  else:
    print('顾客不满意,业绩-1')
    yj -= 1
  print('——————————————————————————————')
