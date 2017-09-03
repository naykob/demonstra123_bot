import telepot, time, subprocess

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if  '/0' in command:#В кавычках команда которую мы будем писать в телеграмм. 
                            #Можно и слова и по русски но начинать нужно именно с косой палочки
            p = subprocess.Popen(cmd0, shell=True)#А тут собственно выполняется команда которую
                            #мы задали для переменной "cmd0"
            bot.sendMessage(chat_id, "Комп не уйдёт в спящий режим")#А это ответ бота в чат.

        if  '/1' in command:
            p = subprocess.Popen(cmd1, shell=True)
            bot.sendMessage(chat_id, "Комп уйдёт в спящий режим через одну минуту простоя")

        if  '/off pc' in command:
            p = subprocess.Popen(shut, shell=True)
            bot.sendMessage(chat_id, "Выключаю комп")

        if  '/p' in command:
            p = subprocess.Popen(soundpc, shell=True)
            bot.sendMessage(chat_id, "Звук на столе")

        if  '/t' in command:
            p = subprocess.Popen(soundtv, shell=True)
            bot.sendMessage(chat_id, "Звук на телике")


bot = telepot.Bot('434702831:AAFERN3wFizrjhGv4Hbnc6K0vdwjfUexX9Q')#Вместо иксов пишем ваш токен
cmd0 = 'Powercfg -setactive 6a935962-1964-4f2a-a937-95cd9b8ca616'
cmd1 = 'Powercfg -setactive 021d63d0-34a0-4824-8f5a-b83156cba872'
shut = 'shutdown -s'
soundpc = 'C:\SSD_v3.exe\SSD.exe 7777hidden'
soundtv = 'C:\SSD_v3.exe\SSD.exe 7771hidden'

bot.message_loop(handle)

while 1:
    time.sleep(20)