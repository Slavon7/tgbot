import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('🇺🇦 Ukrainian')
	btn2 = types.KeyboardButton('🇺🇸 English')

	markup.add(btn1, btn2)
	p = open("media/startpic.jpg", "rb")
	send_mess = f"<b>Вітаю {message.from_user.first_name} </b>!\nНа кафедрі КІП\nКуди підем?"
	bot.send_photo(message.chat.id, p, caption=send_mess, reply_markup=markup, parse_mode="HTML")



@bot.message_handler(commands=['help'])
def help(message):
	markup = types.InlineKeyboardMarkup()

	bot.send_message(message.chat.id, "Change the language /language \n"
									  "Restart the bot /start", reply_markup=markup, parse_mode="HTML")

@bot.message_handler(commands=['language'])
def language(message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

		btn1 = types.KeyboardButton('🇺🇦 Ukrainian')
		btn2 = types.KeyboardButton('🇺🇸 English')

		markup.add(btn1, btn2)
		bot.send_message(message.chat.id, "Choose a language", reply_markup=markup, parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data in ['computers_system', 'engineer_mob', 'innovation_campus','computers_merezi','system_programming','spec_comp','application-form'])
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'computers_system':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Інженерія мобільних пристроїв та прикладне програмування",
												  callback_data='engineer_mob')
				btn2 = types.InlineKeyboardButton("Інноваційний кампус", callback_data='innovation_campus')
				markup.add(btn1,btn2)

				bot.send_message(call.message.chat.id, '<b>Комп’ютерні системи та системне програмування</b>\n\n'
													   '✅ <b>Розробка сучасного програмного забезпечення</b> комп’ютерних систем, '
														'систем інтелектуальної обробки інформації, '
														'забезпечення якості обслуговування комп’ютерних систем '
														'і мереж (DevOps); проектування системних програм, залучання '
														'до проектних та дослідних робіт у галузі робототехніки.\n\n'
													    '<b>Основні спеціальні навчальні дисципліни</b>\n\n'
													   	'🔍  Програмування \n'
														'🔍  Об’єктно-орієнтоване програмування\n'
														'🔍  Архітектура комп’ютерів\n'
														'🔍  Обробка сигналів та зображень\n'
														'🔍  Формальні мови, граматики і автомати\n'
														'🔍  Комп’ютерна схемотехніка\n'
														'🔍  Комп’ютерні системи\n'
														'🔍  Комп’ютерні мережі\n'
														'🔍  Технологія автоматизованого проєктування\n'
														'🔍  Архітектура операційних систем\n'
														'🔍  Алгоритми та структури даних\n'
														'🔍  Організація та проєктування баз даних\n'
														'🔍  Основи обчислювального інтелекту\n'
														'🔍  Проєктування мобільних застосунків\n'
														'🔍  Комп’ютерна графіка\n'
														'🔍  Інженерія комп’ютерних ігрових технологій\n'
														'🔍  Основи комп’ютерної математики\n'
														'🔍  Теорія систем та системного аналізу\n'
														'🔍  Програмування мікропроцесорів\n'
														'🔍  Реверсивне програмування\n'
														'🔍  Архітектура та програмування мікроконтролерів\n\n', reply_markup=markup, parse_mode="HTML")

			elif call.data == 'engineer_mob':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Комп’ютерні системи та системне програмування",
												  callback_data='computers_system')
				btn2 = types.InlineKeyboardButton("Інноваційний кампус", callback_data='innovation_campus')
				markup.add(btn1, btn2)

				bot.send_message(call.message.chat.id, '<b>Інженерія мобільних пристроїв та прикладне програмування</b>\n\n'
						'📱 Сучасні мобільні пристрої – це різного складу та '
						'рівня комп’ютери. Ви опануєте знаннями та навичками, '
						'що дозволять керувати мобільними пристроями та '
						'наповнювати їх новими властивостями в залежності '
						'від галузі застосування. Сучасні програмісти – фахівці '
						'найвищого рівня, які аналізують, розробляють широкий '
						'спектр програмного забезпечення (Front-end, Back-end, '
						'Web та ін.).\n\n'
						'<b>Основні спеціальні навчальні дисципліни</b>\n\n'
						'⌨ Програмування\n'
						'⌨ Об’єктно-орієнтоване програмування\n'
						'⌨ Архітектура комп’ютерів\n'
						'⌨ Обробка сигналів та зображень\n'
						'⌨ Формальні мови, граматики і автомати\n'
						'⌨ Комп’ютерна схемотехніка\n'
						'⌨ Комп’ютерні системи\n'
						'⌨ Комп’ютерні мережі\n'
						'⌨ Технологія автоматизованого проєктування\n'
						'⌨ Архітектура операційних систем\n'
						'⌨ Алгоритми та структури даних\n'
						'⌨ Організація та проєктування баз даних\n'
						'⌨ Основи обчислювального інтелекту\n'
						'⌨ Комп’ютерна графіка\n'
						'⌨ Інженерія комп’ютерних ігрових технологій\n'
						'⌨ Проєктування мобільних застосунків\n'
						'⌨ Інтегровані системи комп’ютерної математики\n'
						'⌨ Системний аналіз та аналітичні дослідження\n'
						'⌨ Структура та функціонування мікропроцесорів\n'
						'⌨ Проєктування серверних застосунків\n'
						'⌨ Вбудовані системи\n\n', reply_markup=markup, parse_mode="HTML")

			elif call.data == 'innovation_campus':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Комп’ютерні системи та системне програмування",
												  callback_data='computers_system')
				btn2 = types.InlineKeyboardButton("Інженерія мобільних пристроїв та прикладне програмування",
												  callback_data='engineer_mob')
				markup.add(btn1, btn2)

				bot.send_message(call.message.chat.id, '<b>Інноваційний кампус</b>\n\n'
						'🌐 Інноваційна освітня траєкторія, '
						'яка розроблена командою українських '
						'ІТ-фахівців у співпраці з викладачами кафедри '
						'КІП. Концепція програми – перехід від декларативної '
						'схеми навчання, основою якої є здобуття знань, до '
						'проектної схеми, спрямованої на набуття практичних '
						'навичок створення продуктів та систем.\n\n'
						'<b>Основні спеціальні навчальні дисципліни</b>\n\n'
						'💽  Програмування\n'
						'💽  Об’єктно-орієнтоване програмування\n'
						'💽  Архітектура комп’ютерів\n'
						'💽  Обробка сигналів та зображень\n'
						'💽  Формальні мови, граматики і автомати\n'
						'💽  Комп’ютерна схемотехніка\n'
						'💽  Комп’ютерні системи\n'
						'💽  Комп’ютерні мережі\n'
						'💽  Технологія автоматизованого проєктування\n'
						'💽  Архітектура операційних систем\n'
						'💽  Алгоритми та структури даних\n'
						'💽  Організація та проєктування баз даних\n'
						'💽  Основи обчислювального інтелекту\n'
						'💽  Комп’ютерна графіка\n'
						'💽  Інженерія комп’ютерних ігрових технологій \n'
						'💽  Проєктування мобільних застосунків\n'
						'💽  Основи комп’ютерного моделювання\n'
						'💽  Системний аналіз\n'
						'💽  Архітектура та програмування мікропроцесорів\n'
						'💽  Розробка мультисервісних застосунків\n'
						'💽  Архітектура та програмування вбудованих систем\n\n', reply_markup=markup, parse_mode="HTML")

			elif call.data == 'computers_merezi':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Системне програмування",
												  callback_data='system_programming')
				btn2 = types.InlineKeyboardButton("Спеціалізовані комп'ютерні системи", callback_data='spec_comp')
				markup.add(btn1, btn2)

				bot.send_message(call.message.chat.id, '<b>Розробка та дослідження сучасного програмного забезпечення</b>'
													   ' комп’ютерних систем, систем інтелектуальної обробки інформації та управління базами даних,'
													   ' систем автоматизованого проектування компонентів.Навчання в магістратурі дає глибокі '
													   'знання про процеси комп’ютерної інженерії, зокрема комп’ютерних систем та мереж, і '
													   'розширює сприйняття обраної спеціальності.\n\n'
													   '<b>Основні спеціальні навчальні дисципліни</b>\n\n'
													   '•  Сучасні технології безпечного програмування\n'
													   '•  Засоби та алгоритми прийняття рішень\n'
													   '•  Програмування для глобальних мереж\n'
													   '•  Основи нейрокомп’ютингу\n'
													   '•  Оптимізація процесів в мультисервісних системах та мережах\n'
													   '•  Апаратні засоби локальних та глобальних мереж\n'
													   '•  Проєктування мікроконтролерних пристроїв\n'
													   '•  Проєктування корпоративних мереж\n'
													   '•  Контроль та діагностика комп`ютерних систем\n'
													   '•  Застосування багатозначної логіки у комп`ютерних системах', reply_markup=markup, parse_mode="HTML")

			elif call.data == 'system_programming':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Комп’ютерні системи та мережі",
												  callback_data='computers_merezi')
				btn2 = types.InlineKeyboardButton("Спеціалізовані комп'ютерні системи", callback_data='spec_comp')
				markup.add(btn1, btn2)

				bot.send_message(call.message.chat.id, '<b>Системне програмування</b> є видом сучасного програмування. <b>Системні програмісти</b>'
													   ' – фахівці найвищого рівня, що дозволяє їм досліджувати, аналізувати '
													   'і розробляти широкий спектр програмного забезпечення '
													   '(Front-end, Back-end, WEB та ін.). Навчання в магістратурі '
													   'дає глибокі знання про процеси комп’ютерної інженерії, '
													   'зокрема системного програмування, і розширює сприйняття '
													   'обраної спеціальності.\n\n'
													   '<b>Основні спеціальні навчальні дисципліни</b>\n\n'
													   '•  Сучасні технології безпечного програмування\n'
													   '•  Засоби та алгоритми прийняття рішень\n'
													   '•  Програмування для глобальних мереж\n'
													   '•  Основи нейрокомп’ютингу\n'
													   '•  Оптимізація процесів в мультисервісних системах та мережах\n'
													   '•  Програмування для корпоративних мереж\n'
													   '•  Теорія побудови трансляторів\n'
													   '•  Machine learning\n'
													   '•  Проєктування програм  діагностики  комп`ютерних систем та мереж\n'
													   '•  Проєктування програмного забезпечення  мікроконтролерних пристроїв', reply_markup=markup, parse_mode="HTML")

			elif call.data == 'spec_comp':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Комп’ютерні системи та мережі",
												  callback_data='computers_merezi')
				btn2 = types.InlineKeyboardButton("Системне програмування", callback_data='system_programming')
				markup.add(btn1, btn2)

				bot.send_message(call.message.chat.id,'<b>Сучасні мобільні пристрої</b> – це різного складу '
													  'і рівня комп’ютери. Ви опануєте знання і навички, які '
													  'дозволять керувати мобільними пристроями і наповнювати їх '
													  'новими властивостями в залежності від області застосування. '
													  '<b>Створення відео ігор</b> – творчий і складний процес, що вимагає '
													  'такого рівня підготовки в програмуванні, алгоритмах, апаратному '
													  'забезпеченні і мережевих технологіях, який дозволить розробити '
													  'щось дуже унікальне і, можливо, популярне. '
													  '<b>Навчання в магістратурі</b> дає глибокі знання про процеси комп’ютерної інженерії, '
													  'зокрема про програмування мобільних пристроїв і комп’ютерних ігор, '
													  'і розширює сприйняття обраної спеціальності.\n\n'
													  '<b>Основні спеціальні навчальні дисципліни</b>\n\n'
													  '•  Сучасні технології безпечного програмування\n'
													  '•  Засоби та алгоритми прийняття рішень\n'
													  '•  Програмування для глобальних мереж\n'
													  '•  Основи нейрокомп’ютингу\n'
													  '•  Оптимізація процесів в мультисервісних системах та мережах\n'
													  '•  Програмне забезпечення корпоративних мереж\n'
													  '•  Моделювання та оптимізація контенту комп`ютерних ігор\n'
													  '•  Методи та засоби обробки сигналів та зображень\n'
													  '•  Проєктування комп`ютерних діагностичних систем\n'
													  '•  Спеціалізовані комп`ютерні системи', reply_markup=markup,parse_mode="HTML")

			elif call.data == 'application-form':


				doc1 = open("media/Форма_заяви_на_1_курс_ХПІ - бланк.pdf", "rb")
				bot.send_document(call.message.chat.id, doc1)
				doc2 = open("media/Заява_на_ ІУС_НТУ_ХПІ.docx", "rb")
				bot.send_document(call.message.chat.id, doc2)
				doc3 = open("media/Приклад_заяви_на_1_курс_ХПІ_на_друкованій_формі.pdf", "rb")
				bot.send_document(call.message.chat.id, doc3)
				photo1 = open("media/ЗаяваУснСпівБес.jpg", "rb")
				bot.send_photo(call.message.chat.id, photo1)

	except Exception as e:
		print(repr(e))

@bot.callback_query_handler(func=lambda call: call.data in ['abitutient_bakalavr', 'abiturient_uskorenik'])
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'abitutient_bakalavr':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Для вступників на 2-3, 1 скорочений курс Бакалавра на основі МС, МБ, ФМБ (після коледжу)", callback_data='abiturient_uskorenik')

				markup.add(btn1)

				bot.send_message(call.message.chat.id, '<b>Для вступників на Бакалавра на основі ПЗСО (після 11 класів)</b>\n\n'
						'<b>Реєстрація для складання НМТ</b>\n\n'
						'📌  додаткова сесія – з 10 до 20 червня\n'
						'📌  спеціальна сесія – з 1 до 7 вересня.(після реєстрації необхідно підтвердити участь та обрати населений пункт)\n\n'
						'<b>Складання НМТ</b>\n\n'
						'📚  Основна сесія НМТ – з 18 липня до 10 серпня\n'
						'📚  Додаткова сесія НМТ – з 16 до 20 серпня\n'
						'📚  Спеціальна сесія НМТ – з 12 до 16 вересня\n\n'
						'<b>Реєстрація електронних кабінетів вступника – з 1 липня</b>\n\n'
						'<b>Подання заяв для вступу – з 29 липня до:</b>\n'
						'✉  8 серпня – для осіб, які вступають на основі індивідуальної усної співбесіди, творчих конкурсів (які складатимуться з 9 до 16 серпня);\n'
						'✉  23 серпня – для осіб, які вступають за результатами національного мультипредметного тесту, а також творчих конкурсів, які були складені з 1 до 18 липня.\n\n'
						'<b>Оприлюднення рейтингових списків на бюджет – не пізніше 29 серпня</b>\n\n'
						'<b>Підтвердження бажання навчатись на бюджеті – 2 вересня до 18:00</b>\n\n'
						'<b>Зарахування</b>\n'
						'⏱  бюджет – 5 вересня\n'
						'⏱  контракт – визначають правилами прийому закладу, але не пізніше 30 вересня.\n '
						'Переведення на вакантні місця – до 19 вересня.', reply_markup=markup, parse_mode="HTML")



			elif call.data == 'abiturient_uskorenik':
				markup = types.InlineKeyboardMarkup(row_width=1)
				btn1 = types.InlineKeyboardButton("Для вступників на Бакалавра на основі ПЗСО (після 11 класів)",
												  callback_data='abitutient_bakalavr')
				markup.add(btn1)

				bot.send_message(call.message.chat.id, '<b>Для вступників на 2-3, 1 скорочений курс Бакалавра на основі МС, МБ, ФМБ (після коледжу)</b>\n\n'
													   '<b>Реєстрація для складання НМТ</b>\n\n'
						'💼  додаткова сесія – з 10 до 20 червня\n'
						'💼  спеціальна сесія – з 1 до 7 вересня.(після реєстрації необхідно підтвердити участь та обрати населений пункт)\n\n'
						'<b>Складання НМТ</b>\n\n'
						'🖊  Основна сесія НМТ – з 18 липня до 10 серпня.\n'
						'🖊  Додаткова сесія НМТ – з 16 до 20 серпня.\n'
						'🖊  Спеціальна сесія НМТ – з 12 до 16 вересня.\n\n'
						'<b>Реєстрація електронних кабінетів вступника – з 1 липня.</b>\n\n'
						'<b>Подання заяв для вступу – з 29 липня до:</b>\n'
						'⚖  8 серпня – для осіб, які вступають на основі індивідуальної усної співбесіди;\n'
						'⚖  23 серпня – для осіб, які вступають за результатами національного мультипредметного тесту.\n\n'
						'<b>Вступні випробування: індивідуальні усні співбесіди – з 9 до 16 серпня.</b>\n\n'
						'<b>Оприлюднення рейтингових списків на бюджет – не пізніше 02 вересня.</b>\n\n'
						'<b>Підтвердження бажання навчатись на бюджеті – 7 вересня до 18:00.</b>\n\n'
						'<b>Зарахування:</b>\n\n'
						'⏳  бюджет – 9 вересня.\n'
						'⏳  контракт – визначають правилами прийому закладу, але не пізніше 30 вересня.\n'
						'<b>Переведення на вакантні місця – до 21 вересня.</b>', reply_markup=markup, parse_mode="HTML")

	except Exception as e:
		print(repr(e))

@bot.message_handler(content_types=['text'])
def mess(message, btn1=None):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "🇺🇸 change language":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🇺🇦 Ukrainian')
		btn2 = types.KeyboardButton('🇺🇸 English')

		markup.add(btn1, btn2)

		final_message = "Choose language"

	elif get_message_bot == "🇺🇦 change language":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🇺🇦 Ukrainian')
		btn2 = types.KeyboardButton('🇺🇸 English')

		markup.add(btn1, btn2)

		final_message = "Choose language"

	elif get_message_bot == "🇺🇦 ukrainian":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🌟 Кафедра КІП')
		btn2 = types.KeyboardButton('📈 Можливості для студентів')
		btn3 = types.KeyboardButton('📋 Вступнику')
		btn4 = types.KeyboardButton('🎉 День відкритих дверей')
		btn5 = types.KeyboardButton('☎ Зв`язатися із кафедрою')
		btn6 = types.KeyboardButton('🇺🇸 Change language')

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "Обрана мова: Українська"


	elif get_message_bot == "⬅ на початок":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🌟 Кафедра КІП')
		btn2 = types.KeyboardButton('📈 Можливості для студентів')
		btn3 = types.KeyboardButton('📋 Вступнику')
		btn4 = types.KeyboardButton('🎉 День відкритих дверей')
		btn5 = types.KeyboardButton('☎ Контакти')
		btn6 = types.KeyboardButton('🇺🇸 Change language')

		markup.add(btn1, btn2, btn3, btn4,btn5,btn6)
		photo = open("media/startpic.jpg","rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>❗️ Шановні старшокласники та абітурієнти❗️</b>⠀" \
						"\n\nКафедра <b>Комп'ютерної інженерії та програмування</b> (КІП) <b>Національного технічного університету " \
						"Харківський політехнічний інститут (НТУ ХПІ 🏛)</b> готує фахівців 12 галузі знань <b>Інформаційні технології</b> за спеціальністю <b>123 Комп'ютерна інженерія</b>"

	elif get_message_bot == "⬅ назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍💼 Бакалаврат')
		btn2 = types.KeyboardButton('🎓 Магістратура')
		btn3 = types.KeyboardButton('📝 Корисні посилання')
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, btn3, btn4)

		photo = open("../../Desktop/telegram_bot/media/dipplomniroboti.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>Комп’ютерна інженерія  (Computer Engineering)</b> – це напрям, який об’єднує в собі частини електротехніки, комп’ютерних наук та програмної інженерії, що необхідні для проектування та розроблення комп’ютерних систем. "

	elif get_message_bot == "⬅ hазад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

		btn1 = types.KeyboardButton('📖 Конкурсні пропозиції')
		btn2 = types.KeyboardButton('⏱ Етапи вступної компанії')
		btn3 = types.KeyboardButton('🧮 Розрахунок конкурсного бaлу')
		btn4 = types.KeyboardButton('🔎 Кількість місць')
		btn5 = types.KeyboardButton("⬅ Назад")
		btn6 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "<b>Важливі посилання\n\n</b>" \
						"<a href='http://vstup.kpi.kharkov.ua/wp-content/uploads/2022/05/kn-vstup-na-osnovi-pzso-dorozhna-karta-vstupnoi-kampanii-2022-roku-v-ntu-khpi.pdf'>📫  Інструкція по вступу на 1 курс бакалаврату на основі ПЗСО (після 11 класів)\n\n</a>" \
						"<a href='http://vstup.kpi.kharkov.ua/wp-content/uploads/2022/05/kn-vstup-na-osnovi-ms-mb-fmb-dorozhna-karta-vstupnoi-kampanii-2022-roku-v-ntu-khpi.pdf'>📫  Інструкція по вступу на 2-3 та 1 скорочений курс бакалаврату на основі МС, МБ, ФМБ (після коледжу)\n\n</a>" \
						"<a href='http://vstup.kpi.kharkov.ua/korisni-posilannya-dlya-abituriientiv/litsenziinyi-obsiag-ta-vartist-navchannia/'>📫  Вартість навчання та кількість ліцензійних місць\n\n</a>" \
						"<a href='http://vstup.kpi.kharkov.ua/maksymalni-obsiagy-derzhavnogo-zamovlennia-na-1-kurs-bakalavratu/'>📫  Максимальні обсяги державного замовлення\n\n</a>" \
						"<a href='http://vstup.kpi.kharkov.ua/admission/admission_rules/'>📫  Правила прийому до НТУ “ХПІ”\n\n</a>"

	elif get_message_bot == "⬅ нaзад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		btn1 = types.KeyboardButton('🎮 СУЧАСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ (ІННОВАЦІЙНИЙ КАМПУС)')
		btn2 = types.KeyboardButton('🧩 ПРИКЛАДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ')
		btn3 = types.KeyboardButton("⬅ Hазад")  # Бакалаврат тут h
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, btn3, btn4)

		final_message = "Перелік освітніх програм"

	elif get_message_bot == "⬅ hазaд":  ########## magistratura nazad
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('📖 Кoнкурсні пропозиції')  # 📖 КOнкурсні пропозиції - o = ENG
		btn2 = types.KeyboardButton('⏱ Етапи вступнoї компанії')  # ⏱ Етапи вступнOї компанії - o = ENG
		btn3 = types.KeyboardButton('🧮 Розрахунок конкурсного балу')  # 🧮 РOзрахунок конкурсного балу - o = ENG
		btn4 = types.KeyboardButton('🔎 Кiлькість місць')  # i - eng
		btn5 = types.KeyboardButton('📄 Мoтиваційний лист')  # 📄 МOтиваційні листи - o = ENG
		btn6 = types.KeyboardButton("⬅ Назад")  # ⬅ НазAд = eng
		btn7 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

		final_message = "<b>Важливі посилання</b>\n\n" \
						"<a href='http://vstup.kpi.kharkov.ua/wp-content/uploads/2022/05/kn-vstup-na-osnovi-bakalavra-spetsialista-magistra-dorozhna-karta-vstupnoi-kampanii-2022-roku-v-ntu-khpi.pdf'>🎯  Інструкція по вступу до магістратури</a>\n\n " \
						"<a href='http://vstup.kpi.kharkov.ua/korisni-posilannya-dlya-abituriientiv/litsenziinyi-obsiag-ta-vartist-navchannia/'>🎯  Ліцензійний обсяг та вартість навчання</a>" \
						"<a href='http://vstup.kpi.kharkov.ua/admission/admission_rules/'>🎯  Правила прийому до НТУ “ХПІ”</a>"

	elif get_message_bot == "☎ контакти":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Завідувач кафедри</b>\n\nЗаковоротний Олександр Юрійович" \
						"\nКонтактний телефон: +38 (097) 967-32-71<b>\n\nНаше місцезнаходження</b>" \
						"\n\nвулиця Кирпичова, 2 (що була Фрунзе), Харків, Харківська область, " \
						"61002 вечерній корпус, к. 309, т. 70-76-165\n<b>Метро Пушкінська</b>\n\n" \
						"<b>Залишились ще питання?</b>\n" \
						"Запитайте їх тут : https://t.me/CEP_123CE"

		photo = open("media/way.png", "rb")
		bot.send_photo(message.chat.id, photo)

	elif get_message_bot == "🎉 день відкритих дверей":
		markup = types.InlineKeyboardMarkup()
		final_message = "Онлайн-зустріч колективу кафедри комп'ютерної інженерії та програмування з абітурієнтами, які бажають вступити на спеціальність 123 Комп'ютерна інженерія" \
						"<a href='https://youtu.be/Lbj_wUomn4Y'> </a>"

	elif get_message_bot == "🌟 кафедра кіп":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍🏫 Викладачі')
		btn2 = types.KeyboardButton('💫 Конкурентні переваги навчання на кафедрі')
		btn3 = types.KeyboardButton('📖 Історія кафедри')
		btn4 = types.KeyboardButton('👨‍💻 Аудиторії кафедри')
		btn5 = types.KeyboardButton('👨‍🎓 Наші випускники')
		btn6 = types.KeyboardButton('🖥 Інноваційний кампус')
		btn7 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

		final_message = "<b>Кафедра КІП готує фахівців в області</b>\n " \
						"\n💻 Комп’ютерних систем і мереж " \
						"\n💻 Програмного та апаратного забезпечення комп’ютерів" \
						"\n💻 Програмування мобільних пристроїв і комп’ютерних ігор." \
						"\n💻 Web-дизайну та Internet-програмування" \
						"\n\nНа кафедрі ведеться підготовка за освітньо-професійними рівнями " \
						"бакалавр і магістр за спеціальністю 123 “Комп’ютерна інженерія”." \
						"\n\nНаша кафедра  співпрацює з провідними ІТ-компаніями Харкова. " \
						"Це дозволяє студентам кафедри проходити стажування та брати участь" \
						" у програмах, які проводять наші партнери." \
						"\n\nНаші випускники з" \
						" успіхом працюють системними програмістами, провідними" \
						" програмістами, системними аналітиками," \
						" системними і мережевими адміністраторами, розробниками" \
						" Web-додатків та Web-дизайнерами, адміністраторами баз даних," \
						" розробниками складних радіотехнічних пристроїв, а також" \
						" пристроїв на базі мікроконтролерів, розробниками інформаційних" \
						" систем, тестувальниками, фахівцями зв’язку, керівниками" \
						" IT-відділів та відділів комп’ютерної безпеки, а також" \
						" займають інші посади, що вимагають висококласного освіти" \
						" в галузі інформаційних технологій.Докладніше на сайті кафедри:" \
						" <a href='https://www.youtube.com/watch?v=GvHnXh_EbHA'>тут</a>"


	elif get_message_bot == "👩‍🏫 викладачі":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("👩‍🏫 Резюме викладачів", url="https://web.kpi.kharkov.ua/cep/vikladachi/"))

		photo = open("media/teachers.png", "rb")
		bot.send_photo(message.chat.id, photo)
		final_message = "<b>✏ На кафедрі <b>«Комп’ютерна інженерія та програмування»</b> працюють 12 докторів наук " \
						"та 23 кандидата наук (PhD).\n" \
						"🧑‍🏫 Наші викладачі мають величезний досвід роботи та викладання.</b>"

	elif get_message_bot == "💫 конкурентні переваги навчання на кафедрі":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Більше INFO", url="http://web.kpi.kharkov.ua/cep/kafedra-sogodni/"))
		photo = open("media/mozlivostiprazevlashtuvania.png","rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "✅ Участь в проекті «Innovation Campus»\n" \
						"✅ Використання в освіті методології практичного навчання на базі створеної на кафедрі експериментальної лабораторії «NоvаLab»\n" \
						"✅ Можливість вибору індивідуальної освітньої траєкторії\n" \
						"✅ Проходження здобувачами вищої освіти навчальної практики та дипломного проектування у провідних ІТ-компаніях України\n" \
						"✅ Викладання дисциплін англійською мовою\n" \
						"✅ Участь в міжнародних олімпіадах з робототехніки і системного програмування\n" \
						"✅ Можливість долучатись до програм міжнародної академічної мобільності та отримання паралельно " \
						"магістерських дипломів українського та  іноземного зразків\n" \
						"✅Участь у Всеукраїнських та міжнародних конкурсах студентських наукових праць в ІТ галузі " \
						"під керівництвом кваліфікованих керівників"

	elif get_message_bot == "📖 історія кафедри":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/kolaz.png","rb")
		bot.send_photo(message.chat.id, photo)
		markup.add(types.InlineKeyboardButton("Більше INFO", url="http://web.kpi.kharkov.ua/cep/istoriya-rozvytku/"))
		final_message = "📚 Наша кафедра була організована в 1961 році як кафедра " \
						"“Математичні та лічильно-вирішальні прилади та пристрої”.\n" \
						"📺Потім вона носила назву “Електронні обчислювальні машини”, після " \
						"цього знайшла своє третє ім’я – <b>“Обчислювальна техніка та програмування“</b>\n" \
						"🎉 З 2021 року кафедра пройшла ребрендінг, та наразі має назву <b>Комп'ютерна інженерія та програмування (КІП)</b>"

	elif get_message_bot == "👨‍💻 аудиторії кафедри":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/photo_lab.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>Комп'ютерні лабораторії, cтейкхолдери та багато </b><a href='https://www.youtube.com/watch?v=GvHnXh_EbHA'><b>іншого</b></a>" \
						"<a href='https://www.youtube.com/watch?v=ZzA20qnbNiY&list=PLD1uBTwvx9NgsjFS2sS774iUW3hDrEUeX&index=1'><b>\nВідео 3D аудиторій</b></a>" \


	elif get_message_bot == "👨‍🎓 наші випускники":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/prezedentNIX.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>Випускники кафедри</b> працюють в <b>Україні</b> 🇺🇦 та <b>поза її межами</b> 🌎 на посадах:" \
						"\n\n🐉<b> архітектори програмного забезпечення</b> (Software Architect);" \
						"\n🥷 <b>розробники ПЗ</b> (Middle, Senior Developer);" \
						"\n🧑‍💻<b> керівники ІТ-підрозділів</b>;" \
						"\n🦾 <b>адміністратори обчислювальної мережі</b> (Network administrator);" \
						"\n👾 <b>тестувальники</b>(QA Engineer);" \
						"\n👩‍💼<b> бізнес-аналітики</b> (Business Analyst);" \
						"\n👨‍💼 <b>менеджери проектів</b> (Project Manager);"


	elif get_message_bot == "🖥 інноваційний кампус":

		markup = types.InlineKeyboardMarkup()
		final_message = "☝️Інноваційний кампус НТУ «ХПІ»!☝️\nНавчайся та роби реальні проекти!\nСтуденти нашої " \
						"кафедри мають можливість навчатися та розробляти реальні проекти, " \
						"взявши участь у програмі \nІнноваційний кампус НТУ «ХПІ». \nЦе — перший проект в Україні на базі державного вишу, " \
						"який об’єднає IT-навчання, школу підприємництва та коворкінг." \
						"<a href='https://www.youtube.com/watch?v=PYb6F9G-7EM&t=12s'>Про Кампус</a> "

	elif get_message_bot == "📈 можливості для студентів":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍💻 Дуальна освіта')
		btn2 = types.KeyboardButton('💵 Можливості працевлаштування')
		btn3 = types.KeyboardButton('👩‍💻 Розробки наших студентів')
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, btn3, btn4)

		photo = open("media/nashipartner.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>На кафедрі</b> навчаються щорічно більше ніж 8️⃣0️⃣0️⃣ студентів," \
						"що створює екосистему 🏞 для <b>стартапів 🚀, формування гуртків," \
						"груп за різними інтересами</b> 🗺 тощо. Щорічно," \
						"кращі студенти <b>представляють кафедру</b> у фахових олімпіадах з <b>системного програмування ⚙ ," \
						"робототехніки 🤖, адміністрування Linux 🐧, " \
						"кібербезпеки</b> 🛡, конкурсів <b>мобільних додатків 📱, " \
						"веб-застосунків</b> 🌐 та займають призові місця 🏆🥇🥈🥉!"

	elif get_message_bot == "👩‍💻 дуальна освіта":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Читати далі", url="http://vstup.kpi.kharkov.ua/edprogram/suchasne-prohramuvannia-mobilni-prystroi-ta-komp-iuterni-ihry-innovatsiinyi-kampus-bakalavr/"))
		final_message = "Можливість долучатись до програм міжнародної академічної мобільності та отримання паралельно магістерських дипломів українського та  іноземного зразків."

	elif get_message_bot == "💵 можливості працевлаштування":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Читати далі", url="https://web.kpi.kharkov.ua/cep/"))
		final_message = "<b>Випускники кафедри</b> працюють в <b>Україні</b> 🇺🇦 <b>та поза її межами</b> 🌎 на посадах:" \
						"\n\n<b>🐉 архітектори програмного забезпечення</b> (Software Architect);" \
						"\n🥷 <b>розробники ПЗ</b> (Middle, Senior Developer);" \
						"\n🧑‍💻 <b>керівники ІТ-підрозділів;</b>" \
						"\n🦾 <b>адміністратори обчислювальної мережі</b> (Network administrator);" \
						"\n👾 <b>тестувальники</b> (QA Engineer);" \
						"\n👩‍💼 <b>бізнес-аналітики</b> (Business Analyst);" \
						"\n👨‍💼 <b>менеджери проектів</b> (Project Manager);"

	elif get_message_bot == "👩‍💻 розробки наших студентів":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/rozrobki.png", "rb")
		bot.send_photo(message.chat.id, photo)
		final_message = "<a href='https://web.kpi.kharkov.ua/cep/2022/06/13/virtualna-3d-ekskursiya-po-navchalnym-laboratoriyam-kafedry-kip/'>⭐️Віртуальна 3D-екскурсія по навчальних лабораторіях кафедри КІП\n\n</a>" \
						"<a href='https://web.kpi.kharkov.ua/cep/2022/06/13/vizualizatsiya-navchalnogo-korpusu-u-1/'>⭐️Візуалізація навчального корпусу У-1\n\n</a>" \
						"<a href='https://web.kpi.kharkov.ua/cep/2022/06/12/komp-yuterna-gra-student-history/'>⭐️Комп’ютерна гра «Student History» про життя студента\n\n</a>" \
						"<a href='https://web.kpi.kharkov.ua/cep/2022/06/12/1940/'>⭐️AR-ігри «Card AR»  та «Maze AR»\n\n</a>"

	elif get_message_bot == "📋 вступнику":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍💼 Бакалаврат')
		btn2 = types.KeyboardButton('🎓 Магістратура')
		btn3 = types.KeyboardButton('📝 Корисні посилання')
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, btn3, btn4)

		photo = open("../../Desktop/telegram_bot/media/dipplomniroboti.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>Комп’ютерна інженерія  (Computer Engineering)</b> – це напрям, який об’єднує в собі частини електротехніки, комп’ютерних наук та програмної інженерії, що необхідні для проектування та розроблення комп’ютерних систем. "

	elif get_message_bot == "📄 мотиваційний лист":
		markup = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id,"Мотиваційні листи \n"
										 "<b>Обов’язкові для вступу!!!</b>\n\n"
										 "<b>Мотиваційний лист</b> – викладена вступником "
										 "письмово у довільній формі інформація про його особисту зацікавленість у вступі"
										 " на певну освітню програму (спеціальність,заклад освіти) та відповідні очікування, досягнення "
										 "у навчанні та інших видах діяльності, власні сильні та слабкі сторони, до якого у разі необхідності"
										 " вступником може бути додано (у тому числі в електронній формі) матеріали, що підтверджують викладену "
										 "в лист інформацію.\n\n", reply_markup=markup, parse_mode="HTML")

		doc = open("media/Приклад_заповнення_мотиваційного_листа_Вступ_на_БАКАЛАВРАТ.docx", "rb")
		bot.send_document(message.chat.id, doc)

		final_message = "🔖 Координати для надсилання <b>Мотиваційних Листів</b>\n\n" \
						"Шановні абітурієнти кафедри\n" \
						"<b>🖥 Комп’ютерної інженерії та програмування!</b>\n\n" \
						"Разом з тим, що ви обов’язково маєте надати до приймальної " \
						"комісії мотиваційні листи з іншими документами для вступу в " \
						"НТУ 'ХПІ', висловлюємо до вас прохання також обов’язково " \
						"надіслати ці листи за такою адресою: zhilin_ussr@ukr.net\n" \
						"У разі виникнення будь-яких питань щодо вступу до навчання на " \
						"нашій кафедрі (Комп’ютерної інженерії та програмування) необхідно " \
						"телефонувати особисто доценту кафедри\n\n" \
						"<b>👨‍🏫 Жиліну Володимиру Анатолійовичу:</b> \n" \
						"067-5740497\n\n" \
						"<b>⏱ Чекаємо на вас у якості студентів нашої кафедри!</b>"

	elif get_message_bot == "🔎 кількість місць":
		markup = types.InlineKeyboardMarkup()

		doc = open("media/bakalavr.pdf", "rb")
		bot.send_document(message.chat.id, doc)
		doc.close()
		final_message = "Кількість  місць"

	elif get_message_bot == "📝 корисні посилання":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Корисні посилання:</b>\n\n" \
						"<a href='https://t.me/CEP_123CE'><b>⌨ Телеграм чат для абітурієнтів</b></a>" \
						"\n<a href='http://vstup.kpi.kharkov.ua/korisni-posilannya-dlya-abituriientiv/'><b>🧑‍💼 Сайт ЦПК НТУ 'ХПІ'</b></a>" \
						"\n<a href='https://web.kpi.kharkov.ua/cep/'><b>🌐 Веб-сайт кафедри</b></a>\n" \
						"\n<a href='https://t.me/khpi_otp'>☎ Telegram канал</a>" \
						"<a href='https://discord.gg/kZEzDV7'>🏆Discord-server </a>" \
						"\n<a href='https://cutt.ly/otp_ntukhpi_youtube'>📺 Youtube</a>" \
						"<a href='https://www.instagram.com/_.k.i.p._/'>👸 Instagram</a>" \
						"\n<a href='https://vm.tiktok.com/ZMLnv3dYD/'>🎶 Tik-Tok</a>" \
						"<a href='https://www.facebook.com/KafedraKIP/'>👵 Facebook</a>" \
						"\n\n<a href='https://cutt.ly/yHJQV84'>📕 Умови вступу</a>" \
						"\n\n<b>📞 Телефони для зв’язку:</b>\n +380979673271, +380675740497."

	elif get_message_bot == "🎓 магістратура":
		markup = types.ReplyKeyboardMarkup()
		btn1 = types.KeyboardButton(
			'🎮 СУЧAСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ')  # 🎮 СУЧaСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ «ІННОВАЦІЙНИЙ КАМПУС» - a = eng
		btn2 = types.KeyboardButton(
			'🧩 ПРИКЛAДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ')  # 🧩 ПРИКЛaДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ - a = eng
		btn3 = types.KeyboardButton("⬅ Назад")
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, row_width=1)
		markup.add(btn3, btn4, row_width=2)

		final_message = "Магістратура"

	elif get_message_bot == "📖 кoнкурсні пропозиції":
		markup = types.ReplyKeyboardMarkup()
		btn1 = types.KeyboardButton('🎮 СУЧAСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ') # 🎮 СУЧaСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ «ІННОВАЦІЙНИЙ КАМПУС» - a = eng
		btn2 = types.KeyboardButton('🧩 ПРИКЛAДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ') # 🧩 ПРИКЛaДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ - a = eng
		btn3 = types.KeyboardButton("⬅ Hазaд")  # Бакалаврат тут h and A
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, row_width=1)
		markup.add(btn3, btn4, row_width=2)

		final_message = "Магістратура"

	elif get_message_bot == "🔎 кiлькість місць":
		markup = types.InlineKeyboardMarkup()

		doc = open("media/magistr.pdf", "rb")
		bot.send_document(message.chat.id, doc)
		doc.close()
		final_message = "Кількість  місць"

		markup.add(btn1)
		final_message = "<b>Щоб подати заяву на вступ за квотою-2, треба</b>\n\n" \
						"1. Скачати, роздрукувати та заповнити заяву на вступ.\n " \
						"2. Сфотографувати її і за можливістю завірити електронним " \
						"цифровим підписом.  \n3. Сфотографувати або відсканувати документи " \
						"(паспорт/свідоцтво про народження, реєстрацію місця проживання, ідентифікаційний " \
						"номер платника податків, документ про середню освіту та додаток до нього), прикріпити  " \
						"фотокартку розміром не більш ніж 1мб.  \n4. Якщо ви бажаєте замість НМТ пройти індивідуальну " \
						"усну співбесіду - роздрукувати, заповнити та сфотографувати відповідну заяву.  \n5. Прикріпити " \
						"усе зазначене вище + мотиваційний лист до електронного листа, в якості теми вказати власні ПІБ.  " \
						"\n6. Відправити лист на пошту vstup.cs@khpi.edu.ua та бути на зв'язку - вам повідомлять про дату " \
						"та час індивідуальної усної співбесіди.  Також ви можете прийти з зазначеними вище документами " \
						"до нашої стаціонарної приймальної комісії за адресою вул. Кирпичова, 2, корпус У-2."

	elif get_message_bot == "🎮 сучaсне програмування, мобільні пристрої та комп’ютерні ігри":
		markup = types.InlineKeyboardMarkup(row_width=1)
		btn1 = types.InlineKeyboardButton("Комп’ютерні системи та мережі", callback_data='computers_merezi')
		btn2 = types.InlineKeyboardButton("Системне програмування", callback_data='system_programming')
		btn3 = types.InlineKeyboardButton("Спеціалізовані комп'ютерні системи", callback_data='spec_comp')

		markup.add(btn1, btn2, btn3)
		final_message = "<b>КОНКУРСНА ПРОПОЗИЦІЯ</b>\n\n" \
						"🎮 СУЧАСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ\n\n" \
						"<b>Розробка сучасного програмного забезпечення</b>\n " \
						"комп’ютерних систем універсального та спеціального призначення, кіберфізичних систем, програмування " \
						"мобільних пристроїв і комп’ютерних ігор, організація функціонування відповідних " \
						"програмно-технічних засобів та їх автоматизованого тестування, дослідження у галузі робототехніки.\n\n" \
						"<b>Конкурсна пропозиція має три освітні траєкторії (спеціалізації)</b>\n" \
						"💡 Комп’ютерні системи та мережі\n" \
						"💡 Системне програмування\n" \
						"💡 Спеціалізовані комп’ютерні системи"

	elif get_message_bot == "🧩 приклaдна комп’ютерна інженерія":
		markup = types.InlineKeyboardMarkup()

		final_message = "<b>Web-дизайн та Internet-програмування</b>\n\n" \
						"Web-дизайн та Internet-програмування є видом сучасного програмування. " \
						"Випускники спеціалізації – фахівці найвищого рівня, що дозволяє їм досліджувати, " \
						"аналізувати і розробляти широкий спектр web-контенту та програмного забезпечення " \
						"для мережі Internet. Навчання в магістратурі дає глибокі знання про процеси " \
						"комп’ютерної інженерії, зокрема web-дизайну, і розширює сприйняття обраної спеціальності.\n\n" \
						"<b>Основні спеціальні навчальні дисципліни</b>\n" \
						"•  Сучасні цифрові технології у Індустрії 4.0\n" \
						"•  Основи наукових досліджень\n" \
						"•  Технології автоматизації інфрастуктури\n" \
						"•  Програмування для глобальних мереж\n" \
						"•  Розробка прикладних internet-застосунків\n" \
						"•  Сучасні технології безпечного програмування\n" \
						"•  Засоби та алгоритми прийняття рішень\n" \
						"•  Основи пошукової оптимізації (SEO)\n" \
						"•  Програмування для корпоративних мереж\n" \
						"•  Основи нейрокомп'ютингу\n" \
						"•  Оптимізація процесів в мультисервісних системах та мережах"


	elif get_message_bot == "🧮 poзрахунок конкурсного балу":  # 📖 РOзрахунок конкурсного балу - o = ENG
		markup = types.InlineKeyboardMarkup()
		doc = open("media/kn_vstup_na_osnovi_bakalavra_spetsialista_magistra_dorozhna_karta.pdf", "rb")
		bot.send_document(message.chat.id, doc)
		final_message = "<b>Конкурсний бал (КБ)</b> = П1, де П1 – оцінка фахового іспиту (у разі конкурсного відбору " \
						"за результатами фахового іспиту на бюджет/контракт) або при вступі тільки на контракт без фахового " \
						"іспиту, а лише за Мотиваційним листом (за рішенням вступника)"

	elif get_message_bot == "⏱ етапи вступнoї компанії":  # ⏱ Етапи вступнOї компанії - o = ENG
		markup = types.InlineKeyboardMarkup()

		final_message = "<b>Реєстрація електронних кабінетів – з 1 серпня</b>\n\n" \
						"<b>Подання заяв для вступу розпочинається 16 серпня та завершується</b>\n" \
						"⏱  23 серпня – для осіб, які вступають на основі індивідуальної усної співбесіди замість МТНК.\n" \
						"⏱  15 вересня – для осіб, які вступають на основі результатів МТНК або тільки фахового іспиту в закладі освіти.\n\n" \
						"<b>Вступні випробування</b>\n" \
						"⌛  фахові іспити – з 17 серпня до 16 вересня.\n" \
						"⌛  індивідуальні усні співбесіди з іноземної мови (для спеціальних умов вступу та другої вищої освіти) – з 25 серпня до 31 серпня.\n\n" \
						"<b>Оприлюднення рейтингових списків на бюджет – не пізніше 20 вересня.</b>\n\n" \
						"<b>Підтвердження бажання навчатись на бюджеті – до 18:00 24 вересня.</b>\n\n" \
						"<b>Зарахування</b>\n" \
						"🗞  бюджет – 25 вересня\n" \
						"🗞  контракт – визначається правилами прийому закладу, але не пізніше 30 листопада.\n\n" \
						"<b>Переведення на вакантні місця – до 10 жовтня</b>"

	elif get_message_bot == "🧮 розрахунок конкурсного балу": # 📖 РOзрахунок конкурсного балу - o = ENG
		markup = types.InlineKeyboardMarkup()
		doc = open("media/kn_vstup_na_osnovi_bakalavra_spetsialista_magistra_dorozhna_karta.pdf", "rb")
		bot.send_document(message.chat.id, doc)
		final_message = "<b>Конкурсний бал (КБ)</b> = П1, де П1 – оцінка фахового іспиту (у разі конкурсного відбору " \
						"за результатами фахового іспиту на бюджет/контракт) або при вступі тільки на контракт без фахового " \
						"іспиту, а лише за Мотиваційним листом (за рішенням вступника)"

	elif get_message_bot == "📖 кoнкурсні пропозиції": # 📖 КOнкурсні пропозиції - o = ENG
		markup = types.InlineKeyboardMarkup()

		final_message = "<b>Про нас</b>"


	elif get_message_bot == "📄 мoтиваційний лист": # 📄 МOтиваційні листи - o = ENG
		markup = types.InlineKeyboardMarkup()
		doc = open("media/Приклад_заповнення_мотиваційного_листа_Вступ_до_МАГІСТРАТУРИ.docx", "rb")
		bot.send_document(message.chat.id, doc)
		photo = open("media/zhilin_ussr@ukr.net.png", "rb")
		bot.send_photo(message.chat.id, photo)
		final_message = "<b>📄 Мoтиваційний лист</b>"

	elif get_message_bot == "✉ зразок заяви (друга вища)":  # ✉ зразок заяви(друга вища)
		markup = types.InlineKeyboardMarkup()
		doc = open("media/zayava5kurs.doc", "rb")
		bot.send_document(message.chat.id, doc)
		final_message = "<b>✉ Зразок заяви (друга вища)</b>"

	elif get_message_bot == "👑 елітарна школа":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/elitarnaschool.png", "rb")
		bot.send_photo(message.chat.id, photo)
		markup.add(types.InlineKeyboardButton("Елітарна школа Політехнік", url="http://web.kpi.kharkov.ua/polytechnik/uk/"))
		final_message = "Елітарна школа <b>Політехнік</b> це " \
						"підготовчі курси при кафедрі Комп'ютерна інженерія " \
						"та програмування» НТУ «ХПІ» для підготовки до зовнішнього " \
						"незалежного оцінювання з математики, фізики, української мови" \
						" та літератури, програмування та вступу до НТУ «ХПІ»." \
						" \n\n<b>Заняття проходять індивідуально або у групах в он-лайн " \
						"та оф-лайн режимах</b>"

	elif get_message_bot == "📖 конкурсні пропозиції":
		markup = types.ReplyKeyboardMarkup()
		btn1 = types.KeyboardButton('🎮 СУЧАСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ (ІННОВАЦІЙНИЙ КАМПУС)')
		btn2 = types.KeyboardButton('🧩 ПРИКЛАДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ')
		btn3 = types.KeyboardButton("⬅ Hазад")  # Бакалаврат тут h
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, row_width=1)
		markup.add(btn3, btn4, row_width=2)


		final_message = "Перелік освітніх програм"

	elif get_message_bot == "🎮 сучасне програмування, мобільні пристрої та комп’ютерні ігри (інноваційний кампус)":
		markup = types.InlineKeyboardMarkup(row_width=1)
		btn1 = types.InlineKeyboardButton("Комп’ютерні системи та системне програмування", callback_data='computers_system')
		btn2 = types.InlineKeyboardButton("Інженерія мобільних пристроїв та прикладне програмування", callback_data='engineer_mob')
		btn3 = types.InlineKeyboardButton("Інноваційний кампус", callback_data='innovation_campus')

		markup.add(btn1, btn2, btn3)

		final_message = "<b>КОНКУРСНА ПРОПОЗИЦІЯ</b>\n\n" \
						"🎮 «СУЧАСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ (ІННОВАЦІЙНИЙ КАМПУС)»\n\n" \
						"<b>Розробка сучасного програмного забезпечення</b>\n " \
						"комп’ютерних систем універсального та спеціального призначення, кіберфізичних систем, програмування " \
						"мобільних пристроїв і комп’ютерних ігор, організація функціонування відповідних " \
						"програмно-технічних засобів та їх автоматизованого тестування, дослідження у галузі робототехніки.\n\n" \
						"<b>Конкурсна пропозиція має три освітні траєкторії (спеціалізації)</b>\n" \
						"💡 Комп’ютерні системи та системне програмування\n" \
						"💡 Інженерія мобільних пристроїв та прикладне програмування\n" \
						"💡 Інноваційний кампус"


	elif get_message_bot == "👨‍🎓 магістратура":
		markup = types.InlineKeyboardMarkup()
		final_message = "🖥 Комп’ютерні системи та мережі.\n" \
						"🖥 Системне програмування.\n" \
						"🖥 Програмування мобільних пристроїв і комп’ютерних ігор.\n\n" \
						"Більш детально за посиланням: <a href='http://vstup.kpi.kharkov.ua/edprogram/suchasne-prohramuvannia-mobilni-prystroi-ta-komp-iuterni-ihry-innovatsiinyi-kampus-magistr/ '>Клац</a>"

	elif get_message_bot == "👩‍💼 бакалаврат":
		markup = types.ReplyKeyboardMarkup()
		btn1 = types.KeyboardButton(
			'🎮 СУЧАСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ (ІННОВАЦІЙНИЙ КАМПУС)')
		btn2 = types.KeyboardButton('🧩 ПРИКЛАДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ')
		btn3 = types.KeyboardButton("⬅ Назад")
		btn4 = types.KeyboardButton("⬅ На початок")

		markup.add(btn1, btn2, row_width=1)
		markup.add(btn3, btn4, row_width=2)

		final_message = "<b>Кафедра веде підготовку магістрів за двома освітніми програмами (див. конкурсні пропозиції):</b>\n\n" \
						"🎮 Сучасне програмування, мобільні пристрої та комп’ютерні ігри (Інноваційний кампус)\n" \
						"🧩 Прикладна комп’ютерна інженерія\n\n" \
						"<b>Наші студенти</b> – найкращі учасники науко-дослідної роботи та переможці конкурсів стартапів освітньо-стипендіальних програм."


	elif get_message_bot == "⏱ етапи вступної компанії":
		markup = types.InlineKeyboardMarkup(row_width=1)
		btn1 = types.InlineKeyboardButton("Для вступників після 11 класів", callback_data='abitutient_bakalavr')
		btn2 = types.InlineKeyboardButton("Для вступників на 2-3, 1 скорочений курс після коледжу",
										  callback_data='abiturient_uskorenik')
		markup.add(btn1, btn2)

		final_message = "<b>👇 Оберіть варіант вступу</b> (натисніть відповідну кнопку)\n" \
						"Якщо у вас залишилися питання, Ви можете задати їх у " \
						"<a href='https://t.me/CEP_123CE'>телеграм чаті</a>\n\n"

	elif get_message_bot == "для вступників на бакалавра на основі пзсо (після 11 класів)":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Реєстрація для складання НМТ</b>\n\n" \
						"📌  додаткова сесія – з 10 до 20 червня\n" \
						"📌  спеціальна сесія – з 1 до 7 вересня.(після реєстрації необхідно підтвердити участь та обрати населений пункт)\n\n" \
						"<b>Складання НМТ</b>\n\n" \
						"📚  Основна сесія НМТ – з 18 липня до 10 серпня\n" \
						"📚  Додаткова сесія НМТ – з 16 до 20 серпня\n" \
						"📚  Спеціальна сесія НМТ – з 12 до 16 вересня\n\n" \
						"<b>Реєстрація електронних кабінетів вступника – з 1 липня</b>\n\n" \
						"<b>Подання заяв для вступу – з 29 липня до:</b>\n" \
						"✉  8 серпня – для осіб, які вступають на основі індивідуальної усної співбесіди, творчих конкурсів (які складатимуться з 9 до 16 серпня);\n" \
						"✉  23 серпня – для осіб, які вступають за результатами національного мультипредметного тесту, а також творчих конкурсів, які були складені з 1 до 18 липня.\n\n" \
						"<b>Оприлюднення рейтингових списків на бюджет – не пізніше 29 серпня</b>\n\n" \
						"<b>Підтвердження бажання навчатись на бюджеті – 2 вересня до 18:00</b>\n\n" \
						"<b>Зарахування</b>\n" \
						"⏱  бюджет – 5 вересня\n" \
						"⏱  контракт – визначають правилами прийому закладу, але не пізніше 30 вересня.\n" \
						"Переведення на вакантні місця – до 19 вересня."

	elif get_message_bot == "для вступників на 2-3, 1 скорочений курс бакалавра на основі мс, мб, фмб (після коледжу)":
		markup = types.InlineKeyboardMarkup()

		final_message = "<b>Реєстрація для складання НМТ</b>\n\n" \
						"💼  додаткова сесія – з 10 до 20 червня\n" \
						"💼  спеціальна сесія – з 1 до 7 вересня.(після реєстрації необхідно підтвердити участь та обрати населений пункт)\n\n" \
						"<b>Складання НМТ</b>\n\n" \
						"🖊  Основна сесія НМТ – з 18 липня до 10 серпня.\n" \
						"🖊  Додаткова сесія НМТ – з 16 до 20 серпня.\n" \
						"🖊  Спеціальна сесія НМТ – з 12 до 16 вересня.\n\n" \
						"<b>Реєстрація електронних кабінетів вступника – з 1 липня.</b>\n\n" \
						"<b>Подання заяв для вступу – з 29 липня до:</b>\n" \
						"⚖  8 серпня – для осіб, які вступають на основі індивідуальної усної співбесіди;\n" \
						"⚖  23 серпня – для осіб, які вступають за результатами національного мультипредметного тесту.\n\n" \
						"<b>Вступні випробування: індивідуальні усні співбесіди – з 9 до 16 серпня.</b>\n\n" \
						"<b>Оприлюднення рейтингових списків на бюджет – не пізніше 02 вересня.</b>\n\n" \
						"<b>Підтвердження бажання навчатись на бюджеті – 7 вересня до 18:00.</b>\n\n" \
						"<b>Зарахування:</b>\n\n" \
						"⏳  бюджет – 9 вересня.\n" \
						"⏳  контракт – визначають правилами прийому закладу, але не пізніше 30 вересня.\n" \
						"<b>Переведення на вакантні місця – до 21 вересня.</b>"


	elif get_message_bot == "🧮 розрахунок конкурсного бaлу":
		markup = types.InlineKeyboardMarkup()
		final_message = "🇺🇦 ПРО РОЗРАХУНОК КОНКУРСНОГО БАЛА (БАКАЛАВР) для спеціальності " \
						"123 Комп'ютерна інженерія\n\nКонкурсний бал – це оцінка вступника, " \
						" якої входять результати вступних випробувань та інші показники.\n\n " \
						"Конкурсний бал вступника бакалавра обчислюється за результатами НМТ " \
						"з української мови (перший предмет), математики (другий) та історії " \
						"України (третій), або балів ЗНО 2019–2021 років з трьох предметів.\n\n" \
						"⚡️Формула розрахунку конкурсного бала бакалавра\n\n" \
						"✅ЗА РЕЗУЛЬТАТАМИ НМТКОНКУРСНИЙ БАЛ (КБ) = К1 × П1 + К2 × П2 + К3 × П3  \n\n" \
						"🔸🔹П1, П2, П3 – оцінки з першого, другого та третього предметів за шкалою 100-200 балів;\n\n" \
						"🔸🔹К1, К2, К3 – вагові коефіцієнти, що визначені для кожної спеціальності;\n" \
						"Для спеціальності 123 \n" \
						"К1=0,3 (Українська мова)  \n" \
						"К2=0,5 (Математика)  \n" \
						"К3=0,2 (Історія України)" \
						"✅ЗА РЕЗУЛЬТАТАМИ ЗНО \n" \
						"КОНКУРСНИЙ БАЛ (КБ) =( К1 × П1 + К2 × П2 + К3 × П3 ) / 0,9\n\n" \
						"🔸🔹П1, П2, П3 – оцінки з першого, другого та третього предметів за шкалою 100-200 балів;\n\n" \
						"🔸🔹К1, К2, К3 – вагові коефіцієнти, що визначені для кожної спеціальності;\n" \
						"Для спеціальності 123\n" \
						"К1=0,2 (Українська мова) \n" \
						"К2=0,5 (Математика) \n" \
						"К3=0,2 (третій предмет, третій предмет, що залежить від року здачі ЗНО)\n" \
						"Третій предмет:\n" \
						"2021 - будь-який предмет\n" \
						"2020 - іноземна мова або фізика (при вступу на контракт також може бути врахований бал з історії України)\n" \
						"2019 - іноземна мова або фізика\n\n" \
						"📌 Остаточно конкурсний бал множиться на регіональний (РК) та галузевий (ГК) коефіцієнти шляхом його множення на їх добуток."

	elif get_message_bot == "🧩 прикладна комп’ютерна інженерія":
		markup = types.InlineKeyboardMarkup()

		final_message = "🎨 <b>Web-дизайн та Internet-програмування🎨</b>\n" \
						"Спеціалізація поєднує три складові освіти\n\n" \
						"🎯 фундаментальна, що базується на кращих традиціях університетської освіти\n" \
						"🎯 професійна підготовка за фахом, яка формує корисні техніко-технологічні знання та вміння (комп’ютерна графіка, інформатика, програмування та ін.)\n" \
						"🎯 професійна підготовка за спеціалізацією, що надає методи та засоби проектування сайтів та веб-додатків, проектування інтерфейсів, " \
						"розробку креативної концепції сайту, створення дизайну сайту, створення макетів сторінок, " \
						"створення мультимедіа-об’єктів, програмування (розробка функціональних інструментів) або інтеграція у систему " \
						"управління вмістом (CMS), оптимізація та розміщення матеріалів сайту, тестування та обслуговування сайту, публікація " \
						"проекту на хостингу та  ін.\n\n" \
						"<b>Основні спеціальні навчальні дисципліни</b>\n\n" \
						"💻  Програмування\n" \
						"💻  Системне програмування\n" \
						"💻  Розробка та застосування баз даних\n" \
						"💻  Системне програмне забезпечення\n" \
						"💻  Управління IT-проектами\n" \
						"💻  Архітектура комп’ютерів\n" \
						"💻  Засоби захисту інформації\n" \
						"💻  Системи штучного інтелекту\n" \
						"💻  Проектування мобільних застосунків\n" \
						"💻  Обробка сигналів та зображень\n" \
						"💻  Алгоритми та структури даних\n" \
						"💻  Організація та проектування баз даних\n" \
						"💻  Об’єктно-орієнтоване програмування\n" \
						"💻  Комп’ютерна графіка\n" \
						"💻  Internet-програмування\n" \
						"💻  Web-технології\n" \
						"💻  Інтелектуальний аналіз даних\n" \
						"💻  Проектування серверних застосунків\n" \
						"💻  Тестування програмного забезпечення\n" \
						"💻  Інтерфейс користувача\n" \
						"💻  Створення та обробка контенту\n\n" \

	elif get_message_bot == "🇺🇸 english":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🌟 KIP Department')
		btn2 = types.KeyboardButton('📈 Opportunities for students')
		btn3 = types.KeyboardButton('📋 To the entrant')
		btn4 = types.KeyboardButton('☎ Contact the department')
		btn5 = types.KeyboardButton('🇺🇦 Change language')

		markup.add(btn1, btn2, btn3, btn4, btn5)

		photo = open("media/startpic_eng.jpg", "rb")
		bot.send_photo(message.chat.id, photo)
		final_message = "❗️ Dear Future Students ❗ \n\n️⠀" \
						"The Department of Computer Engineering and " \
						"Programming (CEP) of the National Technical " \
						"University 'Kharkiv Polytechnic Institute' (NTU KhPI 🏛) " \
						"trains specialists of the 12th field of knowledge " \
						"'Information Technology', the specialty 123 'Computer Engineering' "

	elif get_message_bot == "🌟 kip department":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍🏫 Teachers')
		btn2 = types.KeyboardButton('💫 Competitive advantages of studying at the department')
		btn3 = types.KeyboardButton('📖 History of the department')
		btn4 = types.KeyboardButton('👨‍💻 Auditoriums of the department')
		btn5 = types.KeyboardButton('👨‍🎓 Our graduates')
		btn6 = types.KeyboardButton('🖥 Innovative campus')
		btn7 = types.KeyboardButton("⬅ To the beginning")

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

		final_message = "<b>The KIP department trains specialists in the region</b>\n " \
						"\n💻 Computer systems and networks " \
						"\n💻 Computer software and hardware" \
						"\n💻 Programming of mobile devices and computer games." \
						"\n💻 Web design and Internet programming" \
						"\n\nThe department conducts training according to educational and professional levels " \
						"Bachelor's and Master's degree in specialty 123 'Computer Engineering'." \
						"\n\nOur department cooperates with the leading IT companies of Kharkiv. " \
						"This allows students of the department to undergo internships and participate" \
						" in programs conducted by our partners." \
						"\n\nOur graduates from" \
						"successfully work as system programmers, leading" \
						" by programmers, 1C programmers, system analysts," \
						"system and network administrators, developers" \
						" Web-applications and Web-designers, database administrators," \
						" developers of complex radio technical devices, as well as" \
						"microcontroller-based devices by information developers" \
						"systems, testers, communication specialists, managers" \
						" IT departments and computer security departments, as well as" \
						"occupy other positions that require a high-class education" \
						" in the field of information technologies. More details on the website of the department:" \
						" <a href='https://www.youtube.com/watch?v=GvHnXh_EbHA'>here</a>"

	elif get_message_bot == "📈 opportunities for students":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍💻 Dual educationа')
		btn2 = types.KeyboardButton('💵 Employment opportunities')
		btn3 = types.KeyboardButton('👩‍💻 Developments of our students')
		btn4 = types.KeyboardButton("⬅ To the beginning")

		markup.add(btn1, btn2, btn3, btn4)

		photo = open("media/nashipartner.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>More than </b> 8️⃣0️⃣0️⃣ students study annually at the department," \
						"which creates an ecosystem 🏞 for <b>startups 🚀, formation of circles," \
						"groups with different interests</b> 🗺 etc. Annually," \
						"the best students <b>represent the department</b> in professional Olympiads in <b>system programming ⚙ ," \
						"robotics 🤖, Linux administration 🐧, " \
						"cyber security</b> 🛡, competitions <b>mobile applications 📱, " \
						"web applications</b> 🌐 and take the prize places 🏆🥇🥈🥉!"

	elif get_message_bot == "📋 to the entrant":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍💼 Bachelor`s degree')
		btn2 = types.KeyboardButton('🎓 Magistracy')
		btn3 = types.KeyboardButton('📝 Useful links')
		btn4 = types.KeyboardButton("⬅ To the beginning")

		markup.add(btn1, btn2, btn3, btn4)

		photo = open("../../Desktop/telegram_bot/media/dipplomniroboti.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>Комп’ютерна інженерія  (Computer Engineering)</b> – це напрям, який об’єднує в собі частини електротехніки, комп’ютерних наук та програмної інженерії, що необхідні для проектування та розроблення комп’ютерних систем. "

	elif get_message_bot == "☎ contact the department":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Head of the department</b>\n\nZakovorotny Oleksandr Yuriyovych" \
						"\nContact phone: +38 (097) 967-32-71<b>\n\nOur location</b>" \
						"\n\nKirpychova Street, 2 (formerly Frunze), Kharkiv, Kharkiv region, " \
						"61002 evening building, k. 309, t. 70-76-165\n<b>Pushkinskaya Metro</b>\n\n" \
						"<b>Any questions left?</b>\n" \
						"Ask them here : https://t.me/CEP_123CE"

	elif get_message_bot == "👩‍🏫 teachers":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("👩‍🏫 Teacher CVs", url="https://web.kpi.kharkov.ua/cep/vikladachi/"))

		photo = open("media/teachers.png", "rb")
		bot.send_photo(message.chat.id, photo)
		final_message = "<b>✏️ The Department of Computer Engineering and Programming has 11 Doctors of Science and 23 PhDs.</b>\n" \
						"<b>🧑‍🏫 Our teachers have vast experience in work and teaching.</b>"


	elif get_message_bot == "📖 history of the department":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/kolaz.png", "rb")
		bot.send_photo(message.chat.id, photo)
		markup.add(types.InlineKeyboardButton("More information", url="http://web.kpi.kharkov.ua/cep/istoriya-rozvytku/"))
		final_message = "📚 Our department was organized in 1961 as the Department of Mathematical and Calculating Instruments and Devices."\
						"📺Then it was called 'Electronic computers', after which it found its third name - 'Computer Engineering and Programming'"

	elif get_message_bot == "👨‍💻 auditoriums of the department":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/photo_lab.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>Computer labs, stakeholders and more </b><a href='https://www.youtube.com/watch?v=GvHnXh_EbHA'><b>іншого</b></a>" \
						"<a href='https://www.youtube.com/watch?v=ZzA20qnbNiY&list=PLD1uBTwvx9NgsjFS2sS774iUW3hDrEUeX&index=1'><b>\nVideo of 3D classrooms</b></a>"

	elif get_message_bot == "👨‍🎓 our graduates":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/GRADUATES_eng.png", "rb")
		bot.send_photo(message.chat.id, photo)

		final_message = "<b>Graduates of the department</b> work in <b>Ukraine</b> 🇺🇦 and <b>outside its borders</b> 🌎 in positions:" \
						"\n\n🐉<b> software architects</b> (Software Architect);" \
						"\n🥷 <b>software developers</b> (Middle, Senior Developer);" \
						"\n🧑‍💻<b> heads of IT departments</b>;" \
						"\n🦾 <b>computer network administrators</b> (Network administrator);" \
						"\n👾 <b>testers</b>(QA Engineer);" \
						"\n👩‍💼<b> business analysts</b> (Business Analyst);" \
						"\n👨‍💼 <b>project managers</b> (Project Manager);"

	elif get_message_bot == "🖥 innovative campus":

		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Feedback about the campus of a 4th year student of the department of CEP\n " \
						"AyubaAyoub El-Haddadi</b> (КН-919i.е)\n My stay on campus was a good experience for me, I have gained and boosted my skills in this field, " \
						"introduced and learned many useful things that I am working with currently." \
						"We had a full stack development training, developed many projects with (HTML, CSS, JS, React and PHP Laravel)." \
						" Projects that i have on my personal portfolio and GitHub (Uevent, Chronos, ...)\n\n" \
						"Portfolio - <a href='https://aelhaddadi.com'>https://aelhaddadi.com</a> \n" \
						"Github - <a href='https://github.com/Elh-Ayoub'>https://github.com/Elh-Ayoub</a> "

	elif get_message_bot == "⬅ to the beginning":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🌟 KIP Department')
		btn2 = types.KeyboardButton('📈 Opportunities for students')
		btn3 = types.KeyboardButton('📋 To the entrant')
		btn4 = types.KeyboardButton('☎ Contact the department')
		btn5 = types.KeyboardButton('🇺🇦 Change language')

		markup.add(btn1, btn2, btn3, btn4, btn5)

		photo = open("media/startpic_eng.jpg", "rb")
		bot.send_photo(message.chat.id, photo)
		final_message = "❗️ Dear Future Students ❗ \n\n️⠀" \
						"The Department of Computer Engineering and " \
						"Programming (CEP) of the National Technical " \
						"University 'Kharkiv Polytechnic Institute' (NTU KhPI 🏛) " \
						"trains specialists of the 12th field of knowledge " \
						"'Information Technology', the specialty 123 'Computer Engineering' "



	elif get_message_bot == "слава україні":
		markup = types.InlineKeyboardMarkup()
		final_message = "Героям Слава 🇺🇦🇺🇦🇺🇦"
	elif get_message_bot == "dev":
		markup = types.InlineKeyboardMarkup()
		final_message = "Vyacheslav KN-920E -> KN-920A"

	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🌟 Кафедра КІП')
		btn2 = types.KeyboardButton('📈 Можливості для студентів')
		btn3 = types.KeyboardButton('📋 Вступнику')
		btn4 = types.KeyboardButton('🎉 День відкритих дверей')
		btn5 = types.KeyboardButton('☎ Контакти')
		btn6 = types.KeyboardButton('🇺🇸 Change language')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "Так, так, так\nСтій, краще натисни на кнопку"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)