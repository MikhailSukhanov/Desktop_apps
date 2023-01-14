from tkinter import *
from tkinter import filedialog as fd
import math

def remove_all():
	for widget in w_list:
		widget.grid_remove()

def is_num(s):
	ch = '-.1234567890'
	switch = True
	for i in s:
		if i not in ch:
			switch = False
			break
	return switch

def text_create():
	remove_all()
	txt.delete(1.0, END)
	txt.grid()

def text_open():
	filepath = fd.askopenfilename()
	if filepath != '':
		remove_all()
		txt.delete(1.0, END)
		txt.grid()
		f = open(filepath, encoding = 'utf-8')
		s = f.read()
		txt.insert(1.0, s)
		f.close()

def text_save():
	remove_all()
	txt.grid()
	filepath = fd.asksaveasfilename(filetypes = (('TXT file', '*.txt'), ('All files', '*.*')))
	if filepath != '':
		if filepath[-4:] != '.txt':
			filepath += '.txt'
		f = open(filepath, 'w')
		s = txt.get(1.0, END)
		f.write(s)
		f.close()

def get_time():
	remove_all()
	lab1.grid()
	ent1.grid()
	lab2.grid()
	ent2.grid()
	but1.grid()
	lab3.grid()

def get_time_calc():
	s1 = ent1.get()
	s2 = ent2.get()
	if is_num(s1) and is_num(s2):
		s1 = float(s1)
		s2 = float(s2)
		if s1 >= 1 and s2 >= 1 and s1 < 13 and s2 < 13:
			s = s1 - s2
			if s1 < s2:
				s += 12
			lab3['text'] = str(round(s, 2)) + ' часа(ов)'
		else:
			lab3['text'] = 'Числа должны быть в интервале [1; 13)'
	else:
		lab3['text'] = 'Должны быть введены числа в интервале [1; 13)'

def time_interval():
	remove_all()
	lab4.grid()
	ent3.grid()
	lab5.grid()
	ent4.grid()
	but2.grid()
	lab6.grid()

def time_interval_calc():
	s1 = ent3.get()
	s2 = ent4.get()
	if is_num(s1) and is_num(s2):
		s1 = float(s1)
		s2 = float(s2)
		if s1 >= 1 and s2 >= 1 and s1 < 13 and s2 < 13:
			s = s1 - s2
			if s1 < s2:
				s += 12
			lab6['text'] = 'Прошло ' + str(round(s, 2)) + ' часа(ов)'
		else:
			lab6['text'] = 'Числа должны быть в интервале [1; 13)'
	else:
		lab6['text'] = 'Должны быть введены числа в интервале [1; 13)'

def moments_method():
	remove_all()
	lab7.grid()
	ent5.grid()
	lab8.grid()
	ent6.grid()
	lab9.grid()
	ent7.grid()
	but3.grid()
	lab10.grid()
	lab11.grid()

def moments_method_calc():
	delta = ent5.get()
	phi = ent6.get()
	t = ent7.get()
	if is_num(delta) and is_num(phi) and is_num(t):
		delta = float(delta)
		phi = float(phi)
		t = float(t)
		ctgA = math.tan(delta) * math.cos(phi) / math.sin(t) - math.sin(phi) / math.tan(t)
		A = math.atan(1 / ctgA)
		lab10['text'] = 'ctgAc = ' + str(round(ctgA, 3))
		lab11['text'] = 'Ac = ' + str(round(A, 3)) + ' + πn, n∈Z'
	else:
		lab10['text'] = 'Должны быть введены числовые параметры (в радианах)'
		lab11['text'] = ''

def height_method():
	remove_all()
	lab12.grid()
	ent8.grid()
	lab13.grid()
	ent9.grid()
	lab14.grid()
	ent10.grid()
	but4.grid()
	lab15.grid()
	lab16.grid()

def height_method_calc():
	delta = ent8.get()
	phi = ent9.get()
	h = ent10.get()
	if is_num(delta) and is_num(phi) and is_num(h):
		delta = float(delta)
		phi = float(phi)
		h = float(h)
		cosA = math.sin(delta) / (math.cos(phi) * math.cos(h)) - math.tan(phi) * math.tan(h)
		if cosA < -1 or cosA > 1:
			lab15['text'] = 'cosAc > 1 или cosAc < -1'
			lab16['text'] = ''
		else:
			A = math.acos(cosA)
			lab15['text'] = 'cosAc = ' + str(round(cosA, 3))
			lab16['text'] = 'Ac = ' + '±' + str(round(A, 3)) + ' + 2πn, n∈Z'
	else:
		lab15['text'] = 'Должны быть введены числовые параметры (в радианах)'
		lab16['text'] = ''

def moments_height_method():
	remove_all()
	lab17.grid()
	ent11.grid()
	lab18.grid()
	ent12.grid()
	lab19.grid()
	ent13.grid()
	but5.grid()
	lab20.grid()
	lab21.grid()

def moments_height_method_calc():
	t = ent11.get()
	delta = ent12.get()
	h = ent13.get()
	if is_num(t) and is_num(delta) and is_num(h):
		t = float(t)
		delta = float(delta)
		h = float(h)
		sinA = math.sin(t) * math.cos(delta) / math.cos(h)
		if sinA < -1 or sinA > 1:
			lab20['text'] = 'sinAc > 1 или sinAc < -1'
			lab21['text'] = ''
		else:
			A = math.asin(sinA)
			lab20['text'] = 'sinAc = ' + str(round(sinA, 3))
			lab21['text'] = 'Ac = ' + str(round(A, 3)) + ' + 2πk, π - ' + str(round(A, 3)) + ' + 2πn,  k,n∈Z'
	else:
		lab20['text'] = 'Должны быть введены числовые параметры (в радианах)'
		lab21['text'] = ''

def star_height():
	remove_all()
	lab22.grid()
	ent14.grid()
	lab23.grid()
	ent15.grid()
	lab24.grid()
	ent16.grid()
	but6.grid()
	lab25.grid()
	lab26.grid()

def star_height_calc():
	phi = ent14.get()
	delta = ent15.get()
	t = ent16.get()
	if is_num(phi) and is_num(delta) and is_num(t):
		phi = float(phi)
		delta = float(delta)
		t = float(t)
		sinhc = math.sin(phi) * math.sin(delta) + math.cos(phi) * math.cos(delta) * math.cos(t)
		if sinhc < -1 or sinhc > 1:
			lab25['text'] = 'sinhc > 1 или sinhc < -1'
			lab26['text'] = ''
		else:
			hc = math.asin(sinhc)
			lab25['text'] = 'sinhc = ' + str(round(sinhc, 3))
			lab26['text'] = 'hc = ' + str(round(hc, 3)) + ' + 2πk, π - ' + str(round(hc, 3)) + ' + 2πn,  k,n∈Z'
	else:
		lab25['text'] = 'Должны быть введены числовые параметры (в радианах)'
		lab26['text'] = ''

def vessel_coordinates():
	remove_all()
	lab27.grid()
	ent17.grid()
	lab28.grid()
	ent18.grid()
	lab29.grid()
	ent19.grid()
	lab30.grid()
	ent20.grid()
	lab31.grid()
	ent21.grid()
	lab32.grid()
	ent22.grid()
	but7.grid()
	lab33.grid()
	lab34.grid()

def vessel_coordinates_calc():
	A1 = ent17.get()
	n1 = ent18.get()
	A2 = ent19.get()
	n2 = ent20.get()
	phi_c = ent21.get()
	l_c = ent22.get()
	if is_num(A1) and is_num(n1) and is_num(A2) and is_num(phi_c) and is_num(l_c):
		A1 = float(A1)
		n1 = float(n1)
		A2 = float(A2)
		n2 = float(n2)
		phi_c = float(phi_c)
		l_c = float(l_c)
		if A1 != A2:
			d_phi = (n1 * math.sin(A2) - n2 * math.sin(A1)) / math.sin(A2 - A1)
			d_lambda = (n2 * math.cos(A1) - n1 * math.cos(A2)) / (math.sin(A2 - A1) * math.cos(phi_c))
			phi = (phi_c + d_phi) * 180 / math.pi
			lambda_ = (l_c + d_lambda) * 180 / math.pi
			if phi > 90 or phi < -90:
				phi %= 90
			if lambda_ > 180 or lambda_ < -180:
				lambda_ %= 180
			lab33['text'] = 'φ = ' + str(round(phi, 4)) + '°'
			lab34['text'] = 'λ = ' + str(round(lambda_, 4)) + '°'
		else:
			lab33['text'] = 'A1 = A2'
			lab34['text'] = ''
	else:
		lab33['text'] = 'Должны быть введены числовые параметры (в радианах)'
		lab34['text'] = ''

def calculator():
	def clear():
		global var, var_w
		ent.delete(0, END)
		var = 0
		var_w = ''
		lab['text'] = ''

	def sin():
		global var
		if is_num(ent.get()):
			s = math.sin(float(ent.get()))
			lab['text'] = str(round(s, 3))
			ent.delete(0, END)
		else:
			lab['text'] = 'Введите число'
			ent.delete(0, END)

	def cos():
		global var
		if is_num(ent.get()):
			s = math.cos(float(ent.get()))
			lab['text'] = str(round(s, 3))
			ent.delete(0, END)
		else:
			lab['text'] = 'Введите число'
			ent.delete(0, END)

	def button(but):
		global var, var_w
		if is_num(ent.get()):
			var = float(ent.get())
			ent.delete(0, END)
			var_w = but
		else:
			ent.delete(0, END)
			lab['text'] = 'Введите число'

	def calculate():
		global var, var_w
		if is_num(ent.get()):
			match var_w:
				case 'plus':
					var += float(ent.get())
				case 'minus':
					var -= float(ent.get())
				case 'exponent':
					var **= float(ent.get())
				case 'multiply':
					var *= float(ent.get())
				case 'divide':
					var /= float(ent.get())
			if var == int(var):
				lab['text'] = str(int(var))
			else:
				lab['text'] = str(round(var, 3))
		else:
			lab['text'] = 'Введите число'
		ent.delete(0, END)
		var = 0
		var_w = ''

	a = Toplevel()
	a.geometry('158x158')
	a.resizable(False, False)

	var = 0
	var_w = ''

	ent = Entry(a, width = 23)
	ent.grid(row = 0, column = 0, columnspan = 3, pady = [10, 7], padx = 6, sticky = W)
	but1 = Button(a, text = 'C', width = 5, command = clear)
	but1.grid(row = 1, column = 0, pady = 1, padx = [5, 1])
	but2 = Button(a, text = '+', width = 5, command = lambda f = 'plus': button(f))
	but2.grid(row = 1, column = 1, pady = 1, padx = 1)
	but3 = Button(a, text = '-', width = 5, command = lambda f = 'minus': button(f))
	but3.grid(row = 1, column = 2, pady = 1, padx = 1)
	but4 = Button(a, text = 'x^y', width = 5, command = lambda f = 'exponent': button(f))
	but4.grid(row = 2, column = 0, pady = 1, padx = [5, 1])
	but5 = Button(a, text = '*', width = 5, command = lambda f = 'multiply': button(f))
	but5.grid(row = 2, column = 1, pady = 1, padx = 1)
	but6 = Button(a, text = '/', width = 5, command = lambda f = 'divide': button(f))
	but6.grid(row = 2, column = 2, pady = 1, padx = 1)
	but7 = Button(a, text = 'sin(x)', width = 5, command = sin)
	but7.grid(row = 3, column = 0, pady = 1, padx = [5, 1])
	but8 = Button(a, text = 'cos(x)', width = 5, command = cos)
	but8.grid(row = 3, column = 1, pady = 1, padx = 1)
	but9 = Button(a, text = '=', width = 5, command = calculate)
	but9.grid(row = 3, column = 2, pady = 1, padx = 1)
	lab = Label(a, text = '')
	lab.grid(row = 4, column = 0, columnspan = 3, pady = 7, padx = 5)

def dictionary():
	remove_all()
	ent23.grid()
	but8.grid()
	txt1.grid()

def dictionary_find():
	k = ent23.get().lower()
	txt1.delete(1.0, END)
	if k in terms.keys():
		txt1.insert(1.0, terms.get(k))
	elif k != '':
		txt1.insert(1.0, 'Термин не найден')

root = Tk()
root.title('Навигация')
root.geometry('453x335')

menu = Menu(root)
root.configure(menu = menu)

file_menu = Menu(menu, tearoff = 0)
file_menu.add_command(label = 'Создать', command = text_create)
file_menu.add_command(label = 'Открыть', command = text_open)
file_menu.add_command(label = 'Сохранить', command = text_save)
file_menu.add_separator()
file_menu.add_command(label = 'Выход', command = lambda: root.destroy())

time_menu = Menu(menu, tearoff = 0)
time_menu.add_command(label = 'Который час?', command = get_time)
time_menu.add_command(label = 'Сколько времени прошло?', command = time_interval)

azimuth_menu = Menu(menu, tearoff = 0)
azimuth_menu.add_command(label = 'Метод моментов', command = moments_method)
azimuth_menu.add_command(label = 'Метод высот', command = height_method)
azimuth_menu.add_command(label = 'Метод высот и моментов', command = moments_height_method)

menu.add_cascade(label = 'Файл', menu = file_menu)
menu.add_cascade(label = 'Время', menu = time_menu)
menu.add_cascade(label = 'Азимут светила', menu = azimuth_menu)
menu.add_command(label = 'Высота светила', command = star_height)
menu.add_command(label = 'Координаты судна', command = vessel_coordinates)
menu.add_command(label = 'Калькулятор', command = calculator)
menu.add_command(label = 'Словарь', command = dictionary)

txt = Text(width = 55, height = 19, wrap = WORD)
txt.grid(padx = 4, pady = 2)

lab1 = Label(text = 'Положение стрелки Большой Медведицы для полуночи данного дня:')
lab1.grid(row = 0, sticky = W, padx = 3, pady = [5, 3])
ent1 = Entry(width = 30)
ent1.grid(row = 1, sticky = W, padx = 5, pady = [3, 6])
lab2 = Label(text = 'Текущее положение стрелки Большой Медведицы:')
lab2.grid(row = 2, sticky = W, padx = 3, pady = [5, 3])
ent2 = Entry(width = 30)
ent2.grid(row = 3, sticky = W, padx = 5, pady = [3, 6])
but1 = Button(text = 'Рассчитать время', width = 16, command = get_time_calc)
but1.grid(row = 4, sticky = W, padx = 5, pady = [7, 3])
lab3 = Label(text = '')
lab3.grid(row = 5, sticky = W, padx = 3, pady = 5)

lab4 = Label(text = 'Положение стрелки Большой Медведицы вначале:')
lab4.grid(row = 0, sticky = W, padx = 3, pady = [5, 3])
ent3 = Entry(width = 30)
ent3.grid(row = 1, sticky = W, padx = 5, pady = [3, 6])
lab5 = Label(text = 'Текущее положение стрелки Большой Медведицы:')
lab5.grid(row = 2, sticky = W, padx = 3, pady = [5, 3])
ent4 = Entry(width = 30)
ent4.grid(row = 3, sticky = W, padx = 5, pady = [3, 6])
but2 = Button(text = 'Рассчитать время', width = 16, command = time_interval_calc)
but2.grid(row = 4, sticky = W, padx = 5, pady = [7, 3])
lab6 = Label(text = '')
lab6.grid(row = 5, sticky = W, padx = 3, pady = 5)

lab7 = Label(text = 'Параметр δ:')
lab7.grid(row = 0, sticky = W, padx = 3, pady = [5, 3])
ent5 = Entry(width = 30)
ent5.grid(row = 1, sticky = W, padx = 5, pady = [3, 6])
lab8 = Label(text = 'Параметр φс:')
lab8.grid(row = 2, sticky = W, padx = 3, pady = [5, 3])
ent6 = Entry(width = 30)
ent6.grid(row = 3, sticky = W, padx = 5, pady = [3, 6])
lab9 = Label(text = 'Параметр tM:')
lab9.grid(row = 4, sticky = W, padx = 3, pady = [5, 3])
ent7 = Entry(width = 30)
ent7.grid(row = 5, sticky = W, padx = 5, pady = [3, 6])
but3 = Button(text = 'Расчёт', width = 8, command = moments_method_calc)
but3.grid(row = 6, sticky = W, padx = 5, pady = [7, 3])
lab10 = Label(text = '')
lab10.grid(row = 7, sticky = W, padx = 3, pady = [5, 2])
lab11 = Label(text = '')
lab11.grid(row = 8, sticky = W, padx = 3, pady = 2)

lab12 = Label(text = 'Параметр δ:')
lab12.grid(row = 0, sticky = W, padx = 3, pady = [5, 3])
ent8 = Entry(width = 30)
ent8.grid(row = 1, sticky = W, padx = 5, pady = [3, 6])
lab13 = Label(text = 'Параметр φс:')
lab13.grid(row = 2, sticky = W, padx = 3, pady = [5, 3])
ent9 = Entry(width = 30)
ent9.grid(row = 3, sticky = W, padx = 5, pady = [3, 6])
lab14 = Label(text = 'Параметр h:')
lab14.grid(row = 4, sticky = W, padx = 3, pady = [5, 3])
ent10 = Entry(width = 30)
ent10.grid(row = 5, sticky = W, padx = 5, pady = [3, 6])
but4 = Button(text = 'Расчёт', width = 8, command = height_method_calc)
but4.grid(row = 6, sticky = W, padx = 5, pady = [7, 3])
lab15 = Label(text = '')
lab15.grid(row = 7, sticky = W, padx = 3, pady = [5, 2])
lab16 = Label(text = '')
lab16.grid(row = 8, sticky = W, padx = 3, pady = 2)

lab17 = Label(text = 'Параметр tM:')
lab17.grid(row = 0, sticky = W, padx = 3, pady = [5, 3])
ent11 = Entry(width = 30)
ent11.grid(row = 1, sticky = W, padx = 5, pady = [3, 6])
lab18 = Label(text = 'Параметр δ:')
lab18.grid(row = 2, sticky = W, padx = 3, pady = [5, 3])
ent12 = Entry(width = 30)
ent12.grid(row = 3, sticky = W, padx = 5, pady = [3, 6])
lab19 = Label(text = 'Параметр hс:')
lab19.grid(row = 4, sticky = W, padx = 3, pady = [5, 3])
ent13 = Entry(width = 30)
ent13.grid(row = 5, sticky = W, padx = 5, pady = [3, 6])
but5 = Button(text = 'Расчёт', width = 8, command = moments_height_method_calc)
but5.grid(row = 6, sticky = W, padx = 5, pady = [7, 3])
lab20 = Label(text = '')
lab20.grid(row = 7, sticky = W, padx = 3, pady = [5, 2])
lab21 = Label(text = '')
lab21.grid(row = 8, sticky = W, padx = 3, pady = 2)

lab22 = Label(text = 'Параметр φс:')
lab22.grid(row = 0, sticky = W, padx = 3, pady = [5, 3])
ent14 = Entry(width = 30)
ent14.grid(row = 1, sticky = W, padx = 5, pady = [3, 6])
lab23 = Label(text = 'Параметр δ:')
lab23.grid(row = 2, sticky = W, padx = 3, pady = [5, 3])
ent15 = Entry(width = 30)
ent15.grid(row = 3, sticky = W, padx = 5, pady = [3, 6])
lab24 = Label(text = 'Параметр tM:')
lab24.grid(row = 4, sticky = W, padx = 3, pady = [5, 3])
ent16 = Entry(width = 30)
ent16.grid(row = 5, sticky = W, padx = 5, pady = [3, 6])
but6 = Button(text = 'Расчёт', width = 8, command = star_height_calc)
but6.grid(row = 6, sticky = W, padx = 5, pady = [7, 3])
lab25 = Label(text = '')
lab25.grid(row = 7, sticky = W, padx = 3, pady = [5, 2])
lab26 = Label(text = '')
lab26.grid(row = 8, sticky = W, padx = 3, pady = 2)

lab27 = Label(text = 'Параметр A1:')
lab27.grid(row = 0, column = 0, sticky = W, padx = [3, 8], pady = [5, 3])
ent17 = Entry(width = 30)
ent17.grid(row = 1, column = 0, sticky = W, padx = [5, 8], pady = [3, 6])
lab28 = Label(text = 'Параметр n1:')
lab28.grid(row = 0, column = 1, sticky = W, padx = 3, pady = [5, 3])
ent18 = Entry(width = 30)
ent18.grid(row = 1, column = 1, sticky = W, padx = 5, pady = [3, 6])
lab29 = Label(text = 'Параметр A2:')
lab29.grid(row = 2, column = 0, sticky = W, padx = [3, 8], pady = [5, 3])
ent19 = Entry(width = 30)
ent19.grid(row = 3, column = 0, sticky = W, padx = [5, 8], pady = [3, 6])
lab30 = Label(text = 'Параметр n2:')
lab30.grid(row = 2, column = 1, sticky = W, padx = 3, pady = [5, 3])
ent20 = Entry(width = 30)
ent20.grid(row = 3, column = 1, sticky = W, padx = 5, pady = [3, 6])
lab31 = Label(text = 'Параметр φс:')
lab31.grid(row = 4, column = 0, sticky = W, padx = [3, 8], pady = [5, 3])
ent21 = Entry(width = 30)
ent21.grid(row = 5, column = 0, sticky = W, padx = [5, 8], pady = [3, 6])
lab32 = Label(text = 'Параметр λс:')
lab32.grid(row = 4, column = 1, sticky = W, padx = 3, pady = [5, 3])
ent22 = Entry(width = 30)
ent22.grid(row = 5, column = 1, sticky = W, padx = 5, pady = [3, 6])
but7 = Button(text = 'Расчёт', width = 8, command = vessel_coordinates_calc)
but7.grid(row = 12, sticky = W, padx = 5, pady = [7, 3])
lab33 = Label(text = '')
lab33.grid(row = 13, column = 0, columnspan = 2, sticky = W, padx = 3, pady = [5, 2])
lab34 = Label(text = '')
lab34.grid(row = 14, column = 0, columnspan = 2, sticky = W, padx = 3, pady = 2)

ent23 = Entry(width = 53)
ent23.grid(row = 0, column = 0, padx = [5, 1], sticky = W)
but8 = Button(text = 'Найти', width = 15, command = dictionary_find)
but8.grid(row = 0, column = 1, pady = 4, sticky = W)
txt1 = Text(width = 55, height = 17, wrap = WORD)
txt1.grid(row = 1, column = 0, columnspan = 2, padx = 4)
terms = {}
terms['высотная линия'] = 'Линией положения называется касательная, \
проведенная к изолинии вблизи счислимого места и замещающая собой изолинию.'
terms['азимут светила'] = 'Азимут светила - угол, образуемый плоскостью меридиана с вертикальной плоскостью, \
проходящей через это светило, и измеряемый дугой горизонта, которая содержится между этими двумя плоскостями.'
terms['пеленг'] = 'Пеленг - направление от наблюдателя на какой-либо объект, определяемое вертикальной плоскостью \
истинного (истинный пеленг), магнитного (магнитный пеленг) или компасного (компасный пеленг) меридиана и вертикальной \
плоскостью, проходящей через место наблюдателя и наблюдаемый объект.'
terms['счислимое место судна'] = 'Место судна, координаты которого получены графическим или аналитическим путем.'
terms['секстан'] = 'Секстан - инструмент, предназначенный для измерений высот небесных светил над видимым горизонтом, а также \
вертикальных и горизонтальных углов между ориентирами вручную, с целью определить координаты места наблюдателя.'
terms['метод обсерваций'] = 'Метод обсерваций основан на обработке навигационных параметров, измеренных с помощью \
технических средств судовождения относительно навигационных ориентиров.'
terms['метод счисления'] = 'Метод счисления основан на учете перемещения судна относительно точки \
с известными координатами.'
terms['астронавигационный параметр'] = 'Астронавигационный параметр - физическая величина, зависящая от географического \
места судна, его перемещения и положения небесного светила на небосводе, измеряемая определенным техническим \
средством навигации.'
terms['астронавигационная изолиния'] = 'Астронавигационная изолиния - линия на земной поверхности, каждая точка \
которой соответствует одному и тому же значению астронавигационного параметра.'
terms['круг равных высот'] = 'Круг равных высот - геометрическое место точек на земной поверхности относительно \
которых данное светило в некий фиксированный момент времени располагается на одной и той же высоте над горизонтом.'
terms['параллактический треугольник'] = 'Параллактический треугольник - сферический треугольник на небесной сфере, \
вершинами которого являются полюс (P), зенит (Z), и какое-либо выбранное светило (X).'
terms['мае'] = 'Морской астрономический ежегодник - астрономический календарь, содержащий в себе таблицы координат \
светил и позволяющий выбирать нужную для решения астрономической задачи координату того или другого светила для любого \
нужного момента.'
terms['часовой угол'] = 'Часовой угол - двугранный угол между плоскостями небесного меридиана и круга склонений, одна \
из экваториальных координат в астрономии. Обычно отсчитывается в часовой мере в обе стороны от южной части небесного \
меридиана (от 0 до +12 ч к западу и до -12 ч к востоку).'
terms['склонение светила'] = 'Склонение светила - угол между направлением на светило и плоскостью истинного горизонта \
(одна из координат в горизонтальной системе небесных координат, измеряется в градусах от плоскости наблюдателя: к \
северу – положительное склонение, к югу – отрицательное склонение).'
terms['астрономическая рефракция'] = 'Астрономическая рефракция - преломление света в атмосфере Земли или другой \
планеты, приводящее к различию между видимым и истинным направлениями на небесное тело.'
terms['суточный параллакс'] = 'Суточный параллакс - угол с вершиной в центре небесного светила и со сторонами, \
направленными к центру Земли и к точке наблюдения на земной поверхности; имеет заметную величину лишь для тел \
Солнечной системы. Суточный параллакс зависит от зенитного расстояния светила и меняется с суточным периодом.'

w_list = root.winfo_children()
remove_all()

root.mainloop()
