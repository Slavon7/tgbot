import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('🌟 Кафедра КІП')
	btn2 = types.KeyboardButton('📈 Можливості для студентів')
	btn3 = types.KeyboardButton('📋 Умови вступу')
	btn4 = types.KeyboardButton('☎ Зв`язатися із кафедрою')

	markup.add(btn1, btn2, btn3, btn4)

	p = open("media/startpic.png", "rb")
	send_mess = f"<b>Вітаю {message.from_user.first_name} {message.from_user.last_name}</b>!\nНа кафедрі КІП\nКуди підем?"
	bot.send_photo(message.chat.id, p, caption=send_mess, reply_markup=markup, parse_mode="HTML")


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "⬅ назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('🌟 Кафедра КІП')
		btn2 = types.KeyboardButton('📈 Можливості для студентів')
		btn3 = types.KeyboardButton('📋 Умови вступу')
		btn4 = types.KeyboardButton('☎ Зв`язатися із кафедрою')

		markup.add(btn1, btn2, btn3, btn4)
		final_message = "🙂 Головна"

	elif get_message_bot == "☎ зв`язатися із кафедрою":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Завідувач кафедри</b>\n\nЗаковоротний Олександр Юрійович" \
						"\nКонтактний телефон: +38 (097) 967-32-71<b>\n\nНаше місцезнаходження</b>" \
						"\n\nвулиця Кирпичова, 2 (що була Фрунзе), Харків, Харківська область, " \
						"61002 вечерній корпус, к. 309, т. 70-76-165\n<b>Метро Пушкінська</b>"
		photo = open("media/way.png", "rb")
		bot.send_photo(message.chat.id, photo)

	elif get_message_bot == "🌟 кафедра кіп":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('👩‍🏫 Викладачі')
		btn2 = types.KeyboardButton('💫 Відмінності кафедри')
		btn3 = types.KeyboardButton('📖 Історія кафедри')
		btn4 = types.KeyboardButton('👨‍💻 Аудиторія кафедри')
		btn5 = types.KeyboardButton('👨‍🎓 Наші випускники')
		btn6 = types.KeyboardButton('👑 Елітарна школа')
		btn7 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)


		final_message = "<b>Кафедра КІП готує фахівців в області </b>\n\n 💻 Комп’ютерних систем і мереж " \
						"\n 💻 Програмного та апаратного забезпечення комп’ютерів\n 💻 Програмування " \
						"мобільних пристроїв і комп’ютерних ігор.\n\nНа кафедрі ведеться підготовка за " \
						"освітньо-професійними рівнями бакалавр і магістр за спеціальністю 123 " \
						"“Комп’ютерна інженерія”.\n\nНаша кафедра  співпрацює з провідними ІТ-компаніями Харкова. " \
						"Це дозволяє студентам кафедри проходити стажування та брати участь у програмах, " \
						"які проводять наші партнери.\n\nНаші випускники з успіхом працюють системними програмістами, " \
						"провідними програмістами, 1С-програмістами, системними аналітиками, " \
						"системними і мережевими адміністраторами, розробниками Web-додатків та Web-дизайнерами," \
						" адміністраторами баз даних, розробниками складних радіотехнічних пристроїв," \
						" а також пристроїв на базі мікроконтролерів, розробниками інформаційних систем," \
						" тестувальниками, фахівцями зв’язку, керівниками IT-відділів та відділів комп’ютерної безпеки," \
						" а також займають інші посади, що вимагають висококласного освіти в галузі інформаційних технологій.\n" \
						"<b>Докладніше на сайті кафедри: </b><a href='https://www.youtube.com/watch?v=GvHnXh_EbHA'>тут</a>"
		#markup = types.InlineKeyboardMarkup()
		#markup.add(types.InlineKeyboardButton("Сайт кафедри", url="https://web.kpi.kharkov.ua/cep/"))

	elif get_message_bot == "👩‍🏫 викладачі":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("👩‍🏫 Викладачі тут:", url="https://web.kpi.kharkov.ua/cep/vikladachi/"))
		final_message = "<b>Наші викладачі мають величезний досвід роботи та викладання</b>"

	elif get_message_bot == "💫 відмінності кафедри":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Більше INFO", url="http://web.kpi.kharkov.ua/cep/istoriya-rozvytku/"))
		final_message = "💥 Кафедра КІП має <b>60-річну історію</b> та є однією з <b>перших</b> 🥇 кафедр <b>України</b> 🇺🇦," \
						"яка готувала <b>фахівців з обчислювальної техніки та програмування</b>" \
						"\n\n💎 Заняття проводять досвідчені педагоги, серед яких <b>12 докторів наук 👩‍🔬👨‍🔬</b> та <b>23 PhD</b> 👨‍🏫👩‍🏫." \
						"Передбачено залучання до викладання <b>фахівців відомих ІТ-компаній</b> 👩‍💻👨‍💻." \
						"\n\n🌌 Заняття проводяться в <b>сучасних лабораторіях</b>, що були створені спільно з ІТ-компаніями <b>EPAM," \
						"NIX Solutions</b> та <b>GlobalLogic Ukraine</b>, які оснащені <b>сучасними технічними і програмними засобами</b>." \
						"\n\n<b>Випускники кафедри</b> працюють в <b>Україні</b> 🇺🇦 та <b>поза її межами</b> 🌎 на посадах:\n\n🐉 <b>архітектори програмного забезпечення</b> (Software Architect);" \
						"\n<b>🥷 розробники ПЗ</b> (Middle, Senior Developer);\n🧑<b>‍💻 керівники ІТ-підрозділів</b>;\n🦾 <b>адміністратори обчислювальної мережі</b> (Network administrator);" \
						"\n<b>👾 тестувальники</b> (QA Engineer);\n<b>👩‍💼 бізнес-аналітики</b> (Business Analyst);\n<b>👨‍💼 менеджери проектів</b> (Project Manager); "

	elif get_message_bot == "📖 історія кафедри":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Більше INFO", url="http://web.kpi.kharkov.ua/cep/istoriya-rozvytku/"))
		final_message = "📚 Кафедра “Обчислювальна техніка та програмування” (ОТП) була організована в <b>1961 році...</b>"

	elif get_message_bot == "👨‍💻 аудиторія кафедри":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Комп'ютерні лабораторії, cтейкхолдери та багато </b><a href='https://www.youtube.com/watch?v=GvHnXh_EbHA'><b>іншого</b></a>"

	elif get_message_bot == "👨‍🎓 наші випускники":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Випускники кафедри</b> працюють в <b>Україні</b> 🇺🇦 та <b>поза її межами</b> 🌎 на посадах:" \
						"\n\n🐉<b> архітектори програмного забезпечення</b> (Software Architect);" \
						"\n🥷 <b>розробники ПЗ</b> (Middle, Senior Developer);" \
						"\n🧑‍💻<b> керівники ІТ-підрозділів</b>;" \
						"\n🦾 <b>адміністратори обчислювальної мережі</b> (Network administrator);" \
						"\n👾 <b>тестувальники</b>(QA Engineer);" \
						"\n👩‍💼<b> бізнес-аналітики</b> (Business Analyst);" \
						"\n👨‍💼 <b>менеджери проектів</b> (Project Manager);"

	elif get_message_bot == "👑 елітарна школа":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Елітарна школа Політехнік", url="http://web.kpi.kharkov.ua/polytechnik/"))
		final_message = "<b>Про нас</b>\nЕлітарна школа <b>Політехнік</b> це " \
						"підготовчі курси при кафедрі Комп'ютерна інженерія " \
						"та програмування» «Комп'ютерні науки та інформаційні " \
						"технології» НТУ «ХПІ» для підготовки до зовнішнього " \
						"незалежного оцінювання з математики, фізики, української мови" \
						" та літератури, програмування та вступу до НТУ «ХПІ»." \
						" \n<b>Заняття проходять індивідуально або у групах в он-лайн " \
						"та оф-лайн режимах</b>"

	elif get_message_bot == "📈 можливості для студентів":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('📖 Проєктне навчання')
		btn2 = types.KeyboardButton('👩‍💻 Дуальна освіта')
		btn3 = types.KeyboardButton('💵 Працевлаштування')
		btn4 = types.KeyboardButton('⚒ Практика')
		btn5 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3, btn4, btn5)

		final_message = "<b>На кафедрі</b> навчаються щорічно більше ніж 8️⃣0️⃣0️⃣ студентів," \
						"що створює екосистему 🏞 для <b>стартапів 🚀, формування гуртків," \
						"груп за різними інтересами</b> 🗺 тощо. Щорічно," \
						"кращі студенти <b>представляють кафедру</b> у фахових олімпіадах з <b>системного програмування ⚙ ," \
						"робототехніки 🤖, адміністрування Linux 🐧, " \
						"кібербезпеки</b> 🛡, конкурсів <b>мобільних додатків 📱, " \
						"веб-застосунків</b> 🌐 та займають призові місця 🏆🥇🥈🥉!"

	elif get_message_bot == "📖 проєктне навчання":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Читати далі", url="https://google.com"))
		final_message = "інфо <a href='https://google.com'>Інфо</a>\nЩе Інфо"

	elif get_message_bot == "👩‍💻 дуальна освіта":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Читати далі", url="http://vstup.kpi.kharkov.ua/edprogram/suchasne-prohramuvannia-mobilni-prystroi-ta-komp-iuterni-ihry-innovatsiinyi-kampus-bakalavr/"))
		final_message = "<b>СУЧАСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ (БАКАЛАВР, “ІННОВАЦІЙНИЙ КАМПУС”)</b>" \
				"\n\n<b>Розробка сучасного</b> програмного забезпечення комп’ютерних систем " \
						"універсального та спеціального призначення, кіберфізичних систем," \
						" програмування мобільних пристроїв і комп’ютерних ігор, організація" \
						" функціонування відповідних програмно-технічних засобів та їх " \
						"автоматизованого тестування, дослідження у галузі робототехніки."

	elif get_message_bot == "💵 працевлаштування":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Читати далі", url="https://web.kpi.kharkov.ua/otp/uk/pratsevlashtuvannya/"))
		final_message = "<b>Працевлаштування</b>" \
						"\n\n<b>Наші партнери:</b>" \
						"\nEPAM\nNIX Solution\nGlobalLogic\nINSART\nSoftServe"

	elif get_message_bot == "⚒ практика":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Читати далі", url="https://google.com"))
		final_message = "інфо <a href='https://google.com'>Інфо</a>\nЩе Інфо"

	elif get_message_bot == "📋 умови вступу":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('⏱ Етапи вступної кампанії')
		btn2 = types.KeyboardButton('🔎 Кількість бюджетних та контрактних місць')
		btn3 = types.KeyboardButton('📝 Корисні посилання')
		btn4 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3, btn4)

		final_message = "<a href='http://web.kpi.kharkov.ua/cep/wp-content/uploads/sites/217/2022/05/Prezentatsiya_Vstupna_kampaniya_NTU_HPI_2022_Kafedra_KIP.pdf'>Вступна компанія <b>2022</b> </a>"

	elif get_message_bot == "🗳 вступ на бакалаврат на основі пзсо (після 11 класів)":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Посмотреть INFO", url="https://google.com"))
		final_message = "інфо <a href='https://google.com'>Інфо</a>\nЩе Інфо"

	elif get_message_bot == "⏱ етапи вступної кампанії":
		markup = types.InlineKeyboardMarkup()

		final_message = "<b>СТРОКИ ВСТУПУ НА БАКАЛАВРА У 2022 РОЦІ</b>" \
						"\n\n🇺🇦 Вступна кампанія складається з кількох етапів, кожен з яких має визначені строки." \
						"\n\n✅ З 01 липня – реєстрація е-кабінетів і завантаження документів." \
						"\n\n✅ З 29 липня – прийом заяв і документів від вступників." \
						"\n\n✅ 01-18 липня – проведення творчих конкурсів." \
						"\n\n✅ 09-16 серпня – проведення співбесід." \
						"\n\n✅ 17 серпня – оприлюднення рейтингових списків (бюджет)." \
						"\n\n✅ До 20 серпня – виконання вимог до зарахування." \
						"\n\n✅ 22 серпня – зарахування вступників (бюджет)." \
						"\n\n✅ До 30 вересня – зарахування вступників (контракт)."

	elif get_message_bot == "🔎 кількість бюджетних та контрактних місць":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Посмотреть INFO", url="https://google.com"))
		final_message = "інфо <a href='https://google.com'>Інфо</a>\nЩе Інфо"

	elif get_message_bot == "📝 корисні посилання":
		markup = types.InlineKeyboardMarkup()

		final_message = "<b>Корисні посилання:</b>\n\n<a href='https://web.kpi.kharkov.ua/cep/'><b>🌐 Веб-сайт кафедри</b></a>\n" \
						"\n<a href='https://t.me/khpi_otp'>☎ Telegram канал</a>" \
						"<a href='https://discord.gg/kZEzDV7'>🏆Discord-server </a>" \
						"\n<a href='https://cutt.ly/otp_ntukhpi_youtube'>📺 Youtube</a>" \
						"<a href='https://www.instagram.com/_.k.i.p._/'>👸 Instagram</a>" \
						"\n<a href='https://vm.tiktok.com/ZMLnv3dYD/'>🎶 Tik-Tok</a>" \
						"<a href='https://www.facebook.com/KafedraKIP/'>👵 Facebook</a>" \
						"\n\n<a href='https://cutt.ly/yHJQV84'>📕 Умови вступу</a>" \
						"\n\n<b>📞 Телефони для зв’язку:</b>\n +380979673271, +380675740497."

	elif get_message_bot == "слава україні":
		markup = types.InlineKeyboardMarkup()
		final_message = "Героям Слава 🇺🇦🇺🇦🇺🇦"
	elif get_message_bot == "dev":
		markup = types.InlineKeyboardMarkup()
		final_message = "Vyacheslav"

	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('🌟 Кафедра КІП')
		btn2 = types.KeyboardButton('📈 Можливості для студентів')
		btn3 = types.KeyboardButton('📋 Умови вступу')
		btn4 = types.KeyboardButton('☎ Зв`язатися із кафедрою')
		markup.add(btn1, btn2, btn3, btn4)
		final_message = "Так, так, так\nСтій, краще натисни на кнопку"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)