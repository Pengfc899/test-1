"""
将华氏温度转换成摄氏温度
F = 1.8C + 32
"""

f = float(input('请输入华氏温度:100 '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1c摄氏度' % (f, c))