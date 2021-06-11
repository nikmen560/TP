from src.Strings import errorEmptyInput, errorNoInt,errorWrongInput

class CoreUi:
	def headline(text):
		print(text)
		
	def userInput(text):
		while True:
			result = input(text)
			if not result:
				print(errorEmptyInput)
			else:
				return result
	
	def userInputInt(text):
		minUserInput = 0
		maxUserInput = 10000
		while True:
			result = input(text)
			if not result:
				print(errorEmptyInput)
				continue

			elif not result.isdigit():
				print(errorNoInt)
				continue
			
			elif not minUserInput < result < maxUserInput:
				print(errorWrongInput)
				continue

			else:
				return int(result) 
