import matplotlib.pyplot as plt
import matplotlib.axis 
import numpy as np

# Данные
group = ['Новости', 'Чат', 'Продажа', 'Фак. А', 'Фак. Е', 'Фак. И', 'Фак. О', 'Фак. Р']
message = [100, 10, 23, 7, 35, 28, 74, 125]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)


fig_line = plt.figure(figsize=(10, 10))
fig_circular = plt.figure(figsize=(10, 10))
fig_table = plt.figure(figsize=(10, 10))

# График-линия
ax1 = fig_line.add_subplot(111)
ax1.plot(group, message)

# График-круг
ax2 = fig_circular.add_subplot(111)
ax2.pie(message, labels = group, autopct='%1.1f%%', explode = explode, wedgeprops={'lw':1,'edgecolor':'k'}, 
       pctdistance = 1.1,labeldistance = 1.15,rotatelabels=True)
ax2.axis('equal')

# График-столб
ax3 = fig_table.add_subplot(111)
ax3.bar(group, message)
#ax3.xlabel('Группы', fontsize=17, fontstyle='normal')
plt.show()

