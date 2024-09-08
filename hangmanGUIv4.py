from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random

word_animals = ['Cat']

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

tries = 6
lettersUsed = ' '

def cat(word_animals, word_food):
	global category
	if category == 1:
		word = random.choice(word_animals).lower()
		return word
	elif category == 2:
		word = random.choice(word_food).lower()
		return word
def clickAnimal():
	global category
	category = 1
	btnAnimal.destroy()
	btnFood.destroy()
	
	game()
def clickFood():
	global category
	category = 2
	btnAnimal.destroy()
	btnFood.destroy()
	
	game()
def retryGame():
	btnAnimal = tk.Button(window, text="animal", command=clickAnimal)
	btnFood = tk.Button(window, text="food", command=clickFood)

	btnAnimal.pack()
	btnFood.pack()
def getWord(word_list):
	word = random.choice(word_list).lower()
	return word
def game():
	"""Главный метод программы"""
	statusCanvas.place(x=290, y=125)
	def ent():
		global inputChar, tries
		inputChar = userEntry.get()
		gameLogic(word, wordGue)
	def hiddenWord(word):
		"""Скрытое слово"""
		wordGue = list()
		wordCompletion = '_' * len(word)
		for i in range(len(word)):
			wordGue.append(wordCompletion[i])
		return wordGue
	word = cat(word_animals, word_food)
	wordGue = hiddenWord(word)

	userEntry.pack()

	global btnEnter
	#Кнопка ввода
	btnEnter = tk.Button(window, text="Ввод", command=ent)
	btnEnter.pack()

	gueLabel = tk.Label(text=hiddenWord(word))
	gueLabel.pack()
	
	answerLabel = tk.Label(text=" ")
	answerLabel.pack()

	def clickYes():
		global windowGameOver, userEntry, btnEnter
		retryGame()
		userEntry.destroy()
		btnEnter.destroy()
		#gueLabel.destroy()
		#answerLabel.destroy()

		userEntry = tk.Entry(window)
		btnEnter = tk.Button(window, text="Ввод", command=ent)
		#gueLabel = tk.Label(window, text=" ")

		userEntry.pack()
		btnEnter.pack()

		windowGameOver.destroy()
	def clickNo():
		global windowGameOver
		windowGameOver.destroy()
		window.destroy()
	

	def gameLogic(word, wordGue):
		"""Логика игры"""
		global tries, lettersUsed, statusCanvas, window
		res = list()
		if res != word:
			if inputChar.isalpha() and len(inputChar) == 1:
				if (inputChar not in word) and (inputChar in lettersUsed):
					answerLabel.configure(text="Неверно!" + "\nСписок использованных букв\n" + lettersUsed)
					print("неверно 1")
				elif (inputChar not in word) and (inputChar not in lettersUsed):
					tries -= 1
					statusCanvas.destroy()

					statusCanvas = tk.Canvas(width=250, height=250)
					statusCanvas.place(x=290, y=125)
					image_p = PhotoImage(file="images/Death_" + str(tries) + ".png")
					statusCanvas.create_image(10, 10, anchor=NW, image=image_p)

					lettersUsed += inputChar
					answerLabel.configure(text="Неверно!2" + "\nСписок использованных букв:\n" + lettersUsed)
					print("неверно 2", tries)
					print(lettersUsed)
					print(wordGue)
					if tries == 0:
						print("вы проиграли")
						window.destroy()
					statusCanvas.mainloop()

					
				for i in range(len(word)):
					if inputChar == word[i]:
						wordGue.insert(i, inputChar)
						del wordGue[i+1]
						print("вы угадали букву")
						if (inputChar not in lettersUsed):
							lettersUsed += inputChar
						answerLabel.configure(text="Вы угадали букву!" + "\nСписок использованных букв:\n" + lettersUsed)
						gueLabel.configure(text=wordGue)

				res = ''.join(wordGue)
				print(res)
				if res == word:
					print("вы угадали слово")
					print(word)
					global windowGameOver
					windowGameOver = Tk()
					windowGameOver.title("game over")
					windowGameOver.geometry("250x200")

					gameOverLabel = tk.Label(windowGameOver, text="Поздравляем!\nВы угадали слово!\nЗагаданное слово: " + word + "\nПовторить игру?")
					gameOverLabel.pack()

					btnYes = tk.Button(windowGameOver, text="Yes", command=clickYes)
					btnYes.pack()

					btnNo = tk.Button(windowGameOver, text="No", command=clickNo)
					btnNo.pack()

					tries = 6
					word = cat(word_animals, word_food)
					wordGue = hiddenWord(word)
					lettersUsed = ' '
					res = list()

					print(tries)
					print(word)
					print(wordGue)
					print(lettersUsed)
					print(res)

					answerLabel.configure(text=" ")
					gueLabel.configure(text=wordGue)

					statusCanvas.destroy()

					statusCanvas = Canvas(width=250, height=250)
					#statusCanvas.place(x=290, y=125)
					image_p = PhotoImage(file="images/Death_" + str(tries) + ".png")
					statusCanvas.create_image(10, 10, anchor=NW, image=image_p)



	#


	



#Главное окно
window = Tk()
window.title("HangmanGUIv4_alpha")
window.geometry("800x600")

#Кнопки выбора категории слова
btnAnimal = tk.Button(window, text="animal", command=clickAnimal)
btnFood = tk.Button(window, text="food", command=clickFood)

#Кнопки взаимодействия с игрой
#Кнопка ввода
#---

#Поле ввода
userEntry = tk.Entry(window)

#Статус игры
statusCanvas = tk.Canvas(width=250, height=250)
#statusCanvas.place(x=290, y=125)
image_p = PhotoImage(file="images/Death_" + str(tries) + ".png")
statusCanvas.create_image(10, 10, anchor=NW, image=image_p)



#pack
#Кнопки
btnAnimal.pack()
btnFood.pack()

window.mainloop()