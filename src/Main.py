from src.Customer import Customer
from src.Price import Price
from src.Product import Product
from src.File import File

from src.Strings import *

defaultData = [
	[
		Customer('Ковалев', 'Никита', 'г. Смолевичи', 0),
        Customer('Иванов', 'Илья', 'г. Минск', 1),
        Customer('Козлов', 'Василий', 'г. Жодино', 2) 
	],
	[ 
        Product('Рыба', 0),
        Product('Мясо', 1),
        Product('Хлеб', 2),
		Product('Сыр', 3),
        Product('Молоко', 4),
        Product('Конфеты', 5),
		Product('Бытовая химия', 6),
        Product('Вода', 7),
        Product('Алкоголь', 8)
    ],
	[
		Price(5, 0, 0, '01.05.2021', 0),
		Price(2, 1, 1, '02.05.2021', 1),
		Price(3, 2, 2, '03.05.2021', 2),
		Price(4,3, 3, '04.05.2021', 3),
		Price(1,4,4, '05.05.2021', 4),
		Price(6,5,5, '06.05.2021', 5),
		Price(3,6,6, '07.05.2021', 6),
		Price(1,7,7, '08.05.2021', 7),
		Price(2,8,8, '09.05.2021', 8)
	]

]


