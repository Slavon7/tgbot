import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('🌟 Кафедра КІП')
	btn2 = types.KeyboardButton('📈 Можливості для студентів')
	btn3 = types.KeyboardButton('📋 Вступнику')
	btn4 = types.KeyboardButton('🎉 День відкритих дверей')
	btn5 = types.KeyboardButton('📖 Освітні програми')
	btn6 = types.KeyboardButton('☎ Зв`язатися із кафедрою')

	markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

	p = open("media/startpic.png", "rb")
	send_mess = f"<b>Вітаю {message.from_user.first_name} {message.from_user.last_name}</b>!\nНа кафедрі КІП\nКуди підем?"
	bot.send_photo(message.chat.id, p, caption=send_mess, reply_markup=markup, parse_mode="HTML")


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "⬅ назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🌟 Кафедра КІП')
		btn2 = types.KeyboardButton('📈 Можливості для студентів')
		btn3 = types.KeyboardButton('📋 Вступнику')
		btn4 = types.KeyboardButton('🎉 День відкритих дверей')
		btn5 = types.KeyboardButton('📖 Освітні програми')
		btn6 = types.KeyboardButton('☎ Контакти')

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		final_message = "<b>❗️ Шановні старшокласники та абітурієнти❗️</b>⠀" \
						"\n\nКафедра <b>Комп'ютерної інженерії та програмування</b> (КІП) <b>Національного технічного університету " \
						"Харківський політехнічний інститут (НТУ ХПІ 🏛)</b> готує фахівців 12 галузі знань <b>Інформаційні технології</b> за спеціальністю <b>123 Комп'ютерна інженерія</b>"

	elif get_message_bot == "☎ контакти":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Завідувач кафедри</b>\n\nЗаковоротний Олександр Юрійович" \
						"\nКонтактний телефон: +38 (097) 967-32-71<b>\n\nНаше місцезнаходження</b>" \
						"\n\nвулиця Кирпичова, 2 (що була Фрунзе), Харків, Харківська область, " \
						"61002 вечерній корпус, к. 309, т. 70-76-165\n<b>Метро Пушкінська</b>"
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
		btn7 = types.KeyboardButton("⬅ Назад")

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
						" програмістами, 1С-програмістами, системними аналітиками," \
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
		markup.add(types.InlineKeyboardButton("👩‍🏫 Викладачі тут:", url="https://web.kpi.kharkov.ua/cep/vikladachi/"))
		final_message = "<b>Наші викладачі мають величезний досвід роботи та викладання</b>"

	elif get_message_bot == "💫 конкурентні переваги навчання на кафедрі":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Більше INFO", url="http://web.kpi.kharkov.ua/cep/istoriya-rozvytku/"))
		final_message = "Участь в проекті <b>«Innovation Campus»;</b> використання в освіті методології практичного " \
						"навчання на базі створеної на кафедрі експериментальної лабораторії <b>«NоvаLab»;</b> " \
						"можливість вибору індивідуальної освітньої траєкторії; проходження здобувачами " \
						"вищої освіти навчальної практики та дипломного проектування у провідних ІТ-компаніях " \
						"України; викладання окремих дисциплін англійською мовою; участь в міжнародних олімпіадах " \
						"з робототехніки і системного програмування;  можливість долучатись до програм міжнародної " \
						"академічної мобільності та отримання паралельно магістерських дипломів українського та  " \
						"іноземного зразків."

	elif get_message_bot == "📖 історія кафедри":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Більше INFO", url="http://web.kpi.kharkov.ua/cep/istoriya-rozvytku/"))
		final_message = "📚 Наша кафедра була організована в 1961 році як кафедра " \
						"“Математичні та лічильно-вирішальні прилади та пристрої” (МЛВПП)," \
						" потім вона носила назву “Електронні обчислювальні машини”, після " \
						"цього знайшла своє третє ім’я – Обчислювальна техніка та програмування." \
						" З 2021 року кафедра пройшла ребрендінг та наразі має назву Комп'ютерна інженерія та програмування <b>(КІП)</b>"

	elif get_message_bot == "👨‍💻 аудиторії кафедри":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Комп'ютерні лабораторії, cтейкхолдери та багато </b><a href='https://www.youtube.com/watch?v=GvHnXh_EbHA'><b>іншого</b></a>" \
						"<a href='https://youtu.be/7pgKzwBN9-o'><b>\nВідео 3D аудиторій</b></a>" \


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


	elif get_message_bot == "🖥 інноваційний кампус":

		markup = types.InlineKeyboardMarkup()
		final_message = "☝️Інноваційний кампус НТУ «ХПІ»!☝️\nНавчайся та роби реальні проекти!\nСтуденти нашої " \
						"кафедри мають можливість навчатися та розробляти реальні проекти, " \
						"взявши участь у програмі \nІнноваційний кампус НТУ «ХПІ». \nЦе — перший проект в Україні на базі державного вишу, " \
						"який об’єднає IT-навчання, школу підприємництва та коворкінг." \
						"<a href='Подробиці тут: http://campus.kpi.kharkov.ua/'>Подробиці тут</a> "

	elif get_message_bot == "📈 можливості для студентів":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍💻 Дуальна освіта')
		btn2 = types.KeyboardButton('💵 Можливості працевлаштування')
		btn3 = types.KeyboardButton('👩‍💻 Розробки наших студентів')
		btn4 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3, btn4)

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
		markup.add(types.InlineKeyboardButton("Читати далі", url="https://web.kpi.kharkov.ua/otp/uk/pratsevlashtuvannya/"))
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
		final_message = "<a href='https://web.kpi.kharkov.ua/cep/2022/06/13/virtualna-3d-ekskursiya-po-navchalnym-laboratoriyam-kafedry-kip/'>⭐️Віртуальна 3D-екскурсія по навчальних лабораторіях кафедри КІП\n\n</a>" \
						"<a href='https://web.kpi.kharkov.ua/cep/2022/06/13/vizualizatsiya-navchalnogo-korpusu-u-1/'>⭐️Візуалізація навчального корпусу У-1\n\n</a>" \
						"<a href='https://web.kpi.kharkov.ua/cep/2022/06/12/komp-yuterna-gra-student-history/'>⭐️Комп’ютерна гра «Student History» про життя студента\n\n</a>" \
						"<a href='https://web.kpi.kharkov.ua/cep/2022/06/12/1940/'>⭐️AR-ігри «Card AR»  та «Maze AR»\n\n</a>"

	elif get_message_bot == "📋 вступнику":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('⏱ Етапи вступної кампанії')
		btn2 = types.KeyboardButton('🔎 Кількість бюджетних та контрактних місць')
		btn3 = types.KeyboardButton('📝 Корисні посилання')
		btn4 = types.KeyboardButton('🎓 Магістратура')
		btn5 = types.KeyboardButton('👑 Елітарна школа')
		btn6 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		bot.send_message(message.chat.id,"Мотиваційні листи \nОбов’язкові для вступу!!!\n\nМотиваційний лист – викладена вступником " \
						"письмово у довільній формі інформація про його особисту зацікавленість у вступі" \
						" на певнуосвітню програму (спеціальність,заклад освіти) та відповідні очікування, досягнення " \
						"у навчанні та інших видах діяльності, власні сильні та слабкі сторони, до якого у разі необхідності" \
						" вступником може бути додано (у тому числі в електронній формі) матеріали, що підтверджують викладену " \
						"в лист інформацію.\n\n <b>Трохи зачекайте...</b>", reply_markup=markup, parse_mode="HTML")

		send_mess1 = "Презентація"
		send_mess2 = "Мотиваційний лист"
		doc1 = open("media/Prezentatsiya_KIP.pdf", "rb")
		bot.send_document(message.chat.id, doc1, caption=send_mess1, reply_markup=markup, parse_mode="HTML")
		doc2 = open("media/motivationpaper.docx", "rb")
		bot.send_document(message.chat.id, doc2, caption=send_mess2, reply_markup=markup, parse_mode="HTML")
		doc3 = open("media/examplemotivationpaper.docx", "rb")
		bot.send_document(message.chat.id, doc3)
		final_message = "Приклад заповнення мотиваційних листів"

	elif get_message_bot == "⏱ етапи вступної кампанії":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/vstupnakompania.png", "rb")
		bot.send_photo(message.chat.id, photo)
		final_message = "Етапи вступної компанії"

	elif get_message_bot == "🔎 кількість бюджетних та контрактних місць":
		markup = types.InlineKeyboardMarkup()

		p = open("media/countbudgeting.png", "rb")
		bot.send_photo(message.chat.id, p)
		p2 = open("media/countbudgeting2.png", "rb")
		bot.send_photo(message.chat.id, p2)
		p.close()
		p2.close()
		final_message = "Кількість бюджетних місць та контрактних місць"

	elif get_message_bot == "📝 корисні посилання":
		markup = types.InlineKeyboardMarkup()
		final_message = "<b>Корисні посилання:</b>\n\n<a href='http://vstup.kpi.kharkov.ua/korisni-posilannya-dlya-abituriientiv/'><b>Абітурієнтам</b></a>" \
						"\n<a href='https://web.kpi.kharkov.ua/cep/'><b>🌐 Веб-сайт кафедри</b></a>\n" \
						"<a href='https://t.me/CEP_123CE'><b>⌨ Телеграм чат для абітурієнтів</b></a>\n" \
						"\n<a href='https://t.me/khpi_otp'>☎ Telegram канал</a>" \
						"<a href='https://discord.gg/kZEzDV7'>🏆Discord-server </a>" \
						"\n<a href='https://cutt.ly/otp_ntukhpi_youtube'>📺 Youtube</a>" \
						"<a href='https://www.instagram.com/_.k.i.p._/'>👸 Instagram</a>" \
						"\n<a href='https://vm.tiktok.com/ZMLnv3dYD/'>🎶 Tik-Tok</a>" \
						"<a href='https://www.facebook.com/KafedraKIP/'>👵 Facebook</a>" \
						"\n\n<a href='https://cutt.ly/yHJQV84'>📕 Умови вступу</a>" \
						"\n\n<b>📞 Телефони для зв’язку:</b>\n +380979673271, +380675740497."

	elif get_message_bot == "🎓 магістратура":
		markup = types.InlineKeyboardMarkup()
		photo = open("media/vstupdomagistraruri.png", "rb")
		photo2 = open("media/formularozrahunku.png", "rb")
		photo3 = open("media/drugavisosvita.png", "rb")
		bot.send_photo(message.chat.id, photo)
		bot.send_photo(message.chat.id, photo2)
		bot.send_photo(message.chat.id, photo3)
		final_message = "Вступ до Магістратури"

	elif get_message_bot == "👑 елітарна школа":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Елітарна школа Політехнік", url="http://web.kpi.kharkov.ua/polytechnik/uk/"))
		final_message = "<b>Про нас</b>\n\nЕлітарна школа <b>Політехнік</b> це " \
						"підготовчі курси при кафедрі Комп'ютерна інженерія " \
						"та програмування» НТУ «ХПІ» для підготовки до зовнішнього " \
						"незалежного оцінювання з математики, фізики, української мови" \
						" та літератури, програмування та вступу до НТУ «ХПІ»." \
						" \n\n<b>Заняття проходять індивідуально або у групах в он-лайн " \
						"та оф-лайн режимах</b>"

	elif get_message_bot == "📖 освітні програми":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		btn1 = types.KeyboardButton('🎮 СУЧАСНЕ ПРОГРАМУВАННЯ, МОБІЛЬНІ ПРИСТРОЇ ТА КОМП’ЮТЕРНІ ІГРИ «ІННОВАЦІЙНИЙ КАМПУС»')
		btn2 = types.KeyboardButton('🧩 ПРИКЛАДНА КОМП’ЮТЕРНА ІНЖЕНЕРІЯ')
		btn3 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3)

		final_message = "Перелік освітніх програм"

	elif get_message_bot == "🎮 сучасне програмування, мобільні пристрої та комп’ютерні ігри «інноваційний кампус»":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍💼 Спеціалізації для бакалаврів')
		btn2 = types.KeyboardButton('👨‍🎓 Спеціалізації для магістрів')
		btn3 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3)

		final_message = "🎮 Сучасне програмування, мобільні пристрої та комп’ютерні ігри «інноваційний кампус»"

	elif get_message_bot == "👩‍💼 спеціалізації для бакалаврів":
		markup = types.InlineKeyboardMarkup()
		final_message = "🌐 Комп'ютерні системи та системне програмування.\n" \
						"📲 Інженерія мобільних пристроїв та прикладне програмування.\n" \
						"💡 Інноваційний кампус.\n\n" \
						"Більш детально за посиланням: <a href='http://vstup.kpi.kharkov.ua/edprogram/suchasne-prohramuvannia-mobilni-prystroi-ta-komp-iuterni-ihry-innovatsiinyi-kampus-bakalavr/'>Клац</a>"

	elif get_message_bot == "👨‍🎓 спеціалізації для магістрів":
		markup = types.InlineKeyboardMarkup()
		final_message = "🌐 Комп’ютерні системи та мережі.\n" \
						"⚙ Системне програмування.\n" \
						"📱 Програмування мобільних пристроїв і комп’ютерних ігор.\n\n" \
						"Більш детально за посиланням: <a href='http://vstup.kpi.kharkov.ua/edprogram/suchasne-prohramuvannia-mobilni-prystroi-ta-komp-iuterni-ihry-innovatsiinyi-kampus-magistr/ '>Клац</a>"

	elif get_message_bot == "🧩 прикладна комп’ютерна інженерія":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('👩‍🎓 Спеціалізації для бакалаврів')
		btn2 = types.KeyboardButton('🧑‍💼 Спеціалізації для магістрів')
		btn3 = types.KeyboardButton("⬅ Назад")

		markup.add(btn1, btn2, btn3)

		final_message = "🧩 Прикладна комп’ютерна інженерія"

	elif get_message_bot == "👩‍🎓 спеціалізації для бакалаврів":
		markup = types.InlineKeyboardMarkup()
		final_message = "Більш детально за посиланням для бакалаврів:\n" \
						"<a href='http://vstup.kpi.kharkov.ua/edprogram/prykladna-komp-iuterna-inzheneriia-bakalavr/ '>Клац</a>"

	elif get_message_bot == "🧑‍💼 спеціалізації для магістрів":
		markup = types.InlineKeyboardMarkup()
		final_message = "Більш детально за посиланням для магістрів:\n" \
						"<a href='http://vstup.kpi.kharkov.ua/edprogram/prykladna-komp-iuterna-inzheneriia-magistr/'>Клац</a>"

	elif get_message_bot == "слава україні":
		markup = types.InlineKeyboardMarkup()
		final_message = "Героям Слава 🇺🇦🇺🇦🇺🇦"
	elif get_message_bot == "dev":
		markup = types.InlineKeyboardMarkup()
		final_message = "Vyacheslav"

	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🌟 Кафедра КІП')
		btn2 = types.KeyboardButton('📈 Можливості для студентів')
		btn3 = types.KeyboardButton('📋 Вступнику')
		btn4 = types.KeyboardButton('🎉 День відкритих дверей')
		btn5 = types.KeyboardButton('📖 Освітні програми')
		btn6 = types.KeyboardButton('☎ Контакти')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "Так, так, так\nСтій, краще натисни на кнопку"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)