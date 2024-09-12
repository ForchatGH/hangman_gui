from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random

"""В игре реализованно:
1. Открытие стартового окна
2. Кнопки выбора категории
3. Непосредственно выбор категории и обработка событий соответствующих кнопок
4. После выбора категории окно очищается
5. Следующим шагом реализовать старт игры (стоит рассмотреть вариант, где для выбора категории
используется несколько кнопок, а для начала игры используется одна кнопка)
6. Реализовать отображеие статуса игры
7."""

word_animals = ['Собака', 'Козел', 'Лошадь', 'Свинья', 'Кролик', 'Трубкозуб', 'Альбатрос', 'Аллигатор', 'Альпака',
           'Амфибия', 'Анаконда', 'Удильщик', 'Муравей', 'Муравьед', 'Антилопа', 'Обезьяна', 'Жерех', 'Бабуин',
           'Барсук', 'Бандикут', 'Ракушка', 'Барракуда', 'Василиск', 'Пчела', 'Птица', 'Бизон', 'Кабан', 'Бонобо',
           'Бовид', 'Бабочка', 'Канюк', 'Верблюд', 'Водосвинка', 'Кардинал', 'Карибу', 'Гусеница', 'Сороконожка',
           'Моллюск', 'Хамелеон', 'Гепард', 'Синица', 'Курица', 'Шимпанзе', 'Шиншилла', 'Бурундук', 'Кобра',
           'Таракан', 'Треска', 'Кондор', 'Констриктор', 'Корова', 'Койот', 'Крикет', 'Крокодил', 'Ворона',
           'Кукушка', 'Цикада', 'Олень', 'Динго', 'Динозавр', 'Дельфин', 'Голубь', 'Стрекоза', 'Дракон', 'Червь',
           'Уховертка', 'Ехидна', 'Угорь', 'Цапля', 'Горностай', 'Сокол', 'Хорек', 'Зяблик', 'Светляк', 'Фламинго',
           'Блоха', 'Лягушка', 'Газель', 'Геккон', 'Песчанка', 'Гиббон', 'Жираф', 'Суслик', 'Горилла', 'Кузнечик',
           'Рябчик', 'Гуань', 'Гуанако', 'Цесарка', 'Чайка', 'Гуппи', 'Пикша', 'Палтус', 'Хомяк', 'Ястреб', 'Сельдь',
           'Бегемот', 'Анкилостома', 'Шершень', 'Журчалка', 'Колибри', 'Гиена', 'Игуана', 'Импала', 'Шакал', 'Ягуар',
           'Медуза', 'Кенгуру', 'Зимородок', 'Коала', 'Криль', 'Минога', 'Жаворонок', 'Пиявка', 'Лемминг', 'Лемур',
           'Леопард', 'Леопон', 'Лимпет', 'Ящерица', 'Саранча', 'Гагара', 'Скумбрия', 'Сорока', 'Ламантин', 'Мандрил',
           'Марлин', 'Мартышка', 'Сурок', 'Куница', 'Мастодонт', 'Медоуларк', 'Сурикат', 'Норка', 'Пескарь', 'Пересмешник',
           'Мангуст', 'Комар', 'Овцебык', 'Нарвал', 'Тритон', 'Соловей', 'Оцелот', 'Осьминог', 'Опоссум', 'Орангутанг',
           'Страус', 'Выдра', 'Панда', 'Пантера', 'Попугай', 'Куропатка', 'Павлин', 'Пеликан', 'Пингвин', 'Окунь', 'Фазан',
           'Пиранья', 'Планарий', 'Утконос', 'Дикобраз', 'Креветка', 'Примас', 'Тупик', 'Питон', 'Перепела', 'Крыса',
           'Ворон', 'Рептилия', 'Носорог', 'Грызун', 'Ладья', 'Петух', 'Аскариды', 'Парусник', 'Саламандра', 'Лосось',
           'Гребешок', 'Скорпион', 'Акула', 'Землеройка', 'Шелкопряд', 'Сцинк', 'Скунс', 'Слизняк', 'Корюшка', 'Улитка',
           'Бекас', 'Воробей', 'Колпица', 'Кальмар', 'Белка', 'Осетр', 'Ласточка', 'Лебедь', 'Такин', 'Тапир', 'Тарантул',
           'Долгопят', 'Термит', 'Крачка', 'Дрозд', 'Тиглон', 'Черепаха', 'Тукан', 'Форель', 'Тунец', 'Индюк', 'Тиранозавр',
           'Уриал', 'Викунья', 'Гадюка', 'Полевка', 'Валлаби', 'Ласка', 'Росомаха', 'Вомбат', 'Дятел', 'Крапивник', 'Зебра']

word_food = ['Абрикос', 'Авокадо', 'Амарант', 'Ананас', 'Анчоус', 'Апельсин', 'Арахис', 'Арбуз', 'Аспартам', 'Базилик', 'Баклажан', 'Бамия', 'Банан',
        'Батат', 'Вишня', 'Индейка', 'Грейпфрут', 'Ботва', 'Броколли', 'Брюква', 'Капуста', 'Бузина', 'Булка', 'Булгур', 'Ваниль', 'Васаби',
        'Ветчина', 'Вигна', 'Виноград', 'Водка', 'Пшеница', 'Бургер', 'Говядина', 'Глютен', 'Голубика', 'Горбуша', 'Горох', 'Горчица', 'Гранат',
        'Гречка', 'Груша', 'Гуава', 'Джекфрукт', 'Дуриан', 'Ежевика', 'Жвачка', 'Жеруха', 'Зефир', 'Зубатка', 'Имбирь', 'Инжир', 'Йогурт', 'Кабачок',
        'Какао', 'Кальмар', 'Камбала', 'Карамель', 'Кардамон', 'Картофель', 'Каштан', 'Кервель', 'Кетчуп', 'Кешью', 'Кивано', 'Кефир', 'Кинза', 'Киноа',
        'Кипрей', 'Клементин', 'Клубника', 'Клюква', 'Кокос', 'Колбаса', 'Кольраби', 'Конфета', 'Кориандр', 'Корица', 'Крахмал', 'Креветка', 'Крекер',
        'Крендель', 'Крыжовник', 'Кукуруза', 'Курага', 'Лаваш', 'Лапша', 'Лебеда', 'Лепешка', 'Лобстер', 'Лонган', 'Майонез', 'Манго', 'Майоран', 'Малина',
        'Мангостин', 'Мандарин', 'Маниок', 'Манка', 'Маракуйя', 'Маргарин', 'Мармелад', 'Маслина', 'Масло', 'Мидия', 'Миндаль', 'Молоко', 'Сгущенка',
        'Мороженое', 'Нектарин', 'Наранхилья', 'Овсянка', 'Огурец', 'Окунь', 'Оливка', 'Опунция', 'Орегано', 'Осьминог', 'Отруби', 'Пажитник', 'Папайя',
        'Паприка', 'Патиссон', 'Перец', 'Перловка', 'Персик', 'Петрушка', 'Печенье', 'Пивас', 'Плантан', 'Помадка', 'Помело', 'Помидор', 'Попкорн', 'Ревень',
        'Редиска', 'Ряженка', 'Розмарин', 'Салат', 'Салями', 'Саподилла', 'Сардина', 'Сахар', 'Свекла', 'Сельдерей', 'Сметана', 'Слива', 'Сосиска', 'Спаржа',
        'Сухарь', 'Тамаринд', 'Творог', 'Темпее', 'Томат', 'Тортилья', 'Укроп', 'Уксус', 'Устрица', 'Фасоль', 'Фенхель', 'Фейхоа', 'Фисташка', 'Фруктоза',
        'Фундук', 'Халва', 'Хлебцы', 'Хотдог', 'Хурма', 'Цикорий', 'Чабер', 'Чернослив', 'Чечевица', 'Чеснок', 'Чизбургер', 'Чизкейк', 'Чипсы', 'Шампиньон',
        'Шафран', 'Шоколад', 'Шпинат', 'Щавель', 'Щербет', 'Эстрагон', 'Энергетик', 'Юкола', 'Яблоко']

def hiddenWord(word):
	wordGue = list()
	wordCompletion = '_' * len(word)
	for i in range(len(word)):
		wordGue.append(wordCompletion[i])
	return wordGue

def getWord(word_animals, word_food):
	if choiceCategory() == 'animal':
		word = random.choice(word_animals).lower()
		return word
	elif choiceCategory() == 'food':
		word = random.choice(word_food).lower()
		return word

def choiceCategory():
	global category
	if category == 1:
		return 'animal'
	elif category == 2:
		return 'food'

def startWindow():
	"""Window choice category"""
	def clearStartWindow():
		"""Clear start window"""
		helloLabel.destroy()
		categoryLabel.destroy()
		btnAnimal.destroy()
		btnFood.destroy()
	def animalClick():
		global category, word, wordGue
		category = 1
		choiceCategory()
		word = getWord(word_animals, word_food)
		wordGue = hiddenWord(word)
		clearStartWindow()
		gameWindow()
	def foodClick():
		global category, word, wordGue
		category = 2
		choiceCategory()
		word = getWord(word_animals, word_food)
		wordGue = hiddenWord(word)
		clearStartWindow()
		gameWindow()

	helloLabel = tk.Label(window, text="Hello gamer!", font=("Arial", 15))
	helloLabel.pack()
	
	categoryLabel = tk.Label(window, text="Выберите категорию", font=("Arial", 15))
	categoryLabel.pack()
	
	btnAnimal = tk.Button(window, text="animal", command=animalClick)
	btnAnimal.place(x=300, y=75)
	
	btnFood = tk.Button(window, text="food", command=foodClick)
	btnFood.place(x=375, y=75)

def clearGameWindow():
	global answerLabel, gueLabel, userEntry, statusCanvas, windowRetry
	answerLabel.destroy()
	gueLabel.destroy()
	userEntry.destroy()
	statusCanvas.destroy()
	windowRetry.destroy()

def clickYes():
	clearGameWindow()
	startWindow()

def clickNo():
	windowRetry.destroy()
	window.destroy()

def retryGameWindow():
	global windowRetry
	windowRetry = Toplevel()
	windowRetry.title("game over")
	windowRetry.geometry("260x200")

	btnYes = tk.Button(windowRetry, text="Yes", command=clickYes)
	btnNo = tk.Button(windowRetry, text="No", command=clickNo)

	btnYes.pack()
	btnNo.pack()

def gameWindow():
	"""Window game"""
	global tries, lettersUsed, wordResult
	tries = 6
	lettersUsed = ' '
	wordResult = list()

	global answerLabel, gueLabel, userEntry, statusCanvas
	statusCanvas = tk.Canvas(window, width=250, height=250)
	statusCanvas.place(x=290, y=125)
	image_p = PhotoImage(file="images/Death_" + str(tries) + ".png")
	statusCanvas.create_image(10, 10, anchor=NW, image=image_p)

	def click(event):
		ent()

	def ent():
		global tries, lettersUsed, statusCanvas, wordResult, wordGue
		inputChar = userEntry.get()
		if wordResult != word:
			if inputChar.isalpha() and len(inputChar) == 1:
				if (inputChar not in word) and (inputChar in lettersUsed):
					answerLabel.configure(text="Неверно!" + "\nСписок использованных букв\n" +
										  lettersUsed)
				elif (inputChar not in word) and (inputChar not in lettersUsed):
					tries -= 1
					statusCanvas.destroy()

					statusCanvas = tk.Canvas(window, width=250, height=250)
					statusCanvas.place(x=290, y=125)
					image_p = PhotoImage(file="images/Death_" + str(tries) + ".png")
					statusCanvas.create_image(10, 10, anchor=NW, image=image_p)

					lettersUsed += inputChar
					answerLabel.configure(text="Неверно!" + "\nСписок использованных букв\n" +
										  lettersUsed)
					if tries == 0:
						"""Если игра окончена предложить пользователю выбор закрыть игру/продолжить игру(отобразить окно).
						Если вользователь выбрал 'закрыть игру', то закрыть окно.
						Если пользователь выбрал 'продолжить игру', то
						1. Закрыть окно выбора
						2. Очистить окно gameWindow()
						3. Вызвать функцию startWindow()"""
						userEntry['state'] = tk.DISABLED
						retryGameWindow()
				for i in range(len(word)):
					if inputChar == word[i]:
						wordGue.insert(i, inputChar)
						del wordGue[i+1]
						if (inputChar not in lettersUsed):
							lettersUsed += inputChar
						answerLabel.configure(text="Вы угадали букву!" + "\nСписок использованных букв\n" +
											  lettersUsed)
						gueLabel.configure(text=wordGue)
				wordResult = ''.join(wordGue)
				if wordResult == word:
					userEntry['state'] = tk.DISABLED
					retryGameWindow()
		statusCanvas.mainloop()
	def closeGameWindow():
		statusCanvas.destroy()
		window.destroy()

	userEntry = tk.Entry(window)
	userEntry.bind("<KeyPress-Return>", click)
	userEntry.bind("<KeyRelease-Return>", lambda event: userEntry.delete(0, tk.END))

	answerLabel = tk.Label(window, text="Введите букву", font=("Arial", 15))
	gueLabel = tk.Label(window, text=wordGue, anchor=CENTER, font=("Arial", 15))
	#btnEnter = tk.Button(window, text="enter", command=ent)

	userEntry.place(x=345, y=425)
	answerLabel.pack(side=TOP)
	gueLabel.place(x=355, y=75)
	#btnEnter.pack()

	statusCanvas.mainloop()

#Главное окно
window = Tk()
window.title("HangmanGUIv5_alpha")
window.geometry("800x600")

startWindow()

window.mainloop()