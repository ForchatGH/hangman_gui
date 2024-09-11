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

word_animals = ['Cat']

word_food = ['Apple']

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
		clearStartWindow()

	helloLabel = tk.Label(window, text="Hello gamer!")
	helloLabel.pack()
	
	categoryLabel = tk.Label(window, text="Выберите категорию")
	categoryLabel.pack()
	
	btnAnimal = tk.Button(window, text="animal", command=animalClick)
	btnAnimal.pack()
	
	btnFood = tk.Button(window, text="food", command=foodClick)
	btnFood.pack()


	
def gameWindow():
	"""Window game"""
	global tries, lettersUsed, wordResult
	tries = 6
	lettersUsed = ' '
	wordResult = list()

	global statusCanvas
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
						print("you lose")
						closeGameWindow()



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
				#print(wordResult)
				if wordResult == word:
					print("you won")
					closeGameWindow()
		statusCanvas.mainloop()
	def closeGameWindow():
		statusCanvas.destroy()
		window.destroy()


	userEntry = tk.Entry(window)
	userEntry.bind("<KeyPress-Return>", click)
	userEntry.bind("<KeyRelease-Return>", lambda event: userEntry.delete(0, tk.END))

	answerLabel = tk.Label(window, text=" ")
	gueLabel = tk.Label(window, text=" ")
	#btnEnter = tk.Button(window, text="enter", command=ent)

	userEntry.pack()
	answerLabel.pack()
	gueLabel.pack()
	#btnEnter.pack()

	statusCanvas.mainloop()



#Главное окно
window = Tk()
window.title("HangmanGUIv5_alpha")
window.geometry("800x600")

startWindow()

window.mainloop()