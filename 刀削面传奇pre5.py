#库导入
import random as ra
import time as ti
import tkinter as tk

root = tk.Tk()
root.title('更新速览')
root.geometry("300x200")
label1 = tk.Label(root, text = "pre_5")
label2 = tk.Label(root, text = "更新速览")
label3 = tk.Label(root, text = "1增加性别")
label4 = tk.Label(root, text = "2.优化GUI")
label5 = tk.Label(root, text = "————————————————————————")
label6 = tk.Label(root, text = "关闭该窗口以开食游戏")
label7 = tk.Label(root,text = "GH工作室官网来啦！")
label8 = tk.Label(root,text = "https://wlgzs.my.canvasite.cn/gh-studio")
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
label8.pack()
root.mainloop()
yj = 0
x = 1
print('该游戏由GH工作室出品')
print('微硬出品，必属精品')
print('——————————————————————————————')
print('蒙古海军司令五星上将詹姆斯下士说：“没有什么不是一碗刀削面解决不了的。”')
print('刀削面传奇')
print('奇妙至极')
print('——————————————————————————————')
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
  st = ra.randint(3,9)
  ti.sleep(st)
  mf = ra.randint(1,2)
  if mf == 1:
    xb = ('他')
  else:
    xb = ('她')
  print('一位顾客来到！')
  y = ra.randint(0,2)
  if y == 0:
    print(xb,'要一份加卤蛋的面')
    pl = 1
    jc = 0
  else:
    if y == 1:
      print(xb,'要一份加香菜的面')
      pl = 2
      jc = 0
    else:
      print(xb,'要一份加卤蛋和香菜的面')
      pl = 12
      pl2 = 21
      jc = 1
  print('添加香菜输入1，添加卤蛋输入2')
  a = int(input())
  if jc == 0:
    if a == pl:
      print('顾客满意地享用刀削面去了，业绩+1')
      yj += 1
  elif a == pl or a == pl2:
    print('顾客满意地享用刀削面去了，业绩+1')
    yj += 1
  else:
    print('顾客不满意,业绩-1')
    yj -= 1
  print('——————————————————————————————')