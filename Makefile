extract-bot:
	pybabel extract --input-dirs=. -o app/bot/localization/locales/message.pot

init-bot:
	pybabel init -i app/bot/localization/locales/message.pot -d app/bot/localization/locales -l en
	pybabel init -i app/bot/localization/locales/message.pot -d app/bot/localization/locales -l uz

compile-bot:
	pybabel compile -d app/bot/localization/locales
	pybabel update -d app/bot/localization/locales -i app/bot/localization/locales/message.pot
	
update-bot:
	pybabel update -d app/bot/localization/locales -i app/bot/localization/locales/message.pot 

start-bot:
	python -m app.bot.main