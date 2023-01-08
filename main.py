from speechkit import Session, SpeechSynthesis
import pyaudio

newlines = []
authdata = []
filename = input("Enter dataset lines file: ") #здесь вводится имя файла, из которого будут читаться строки
startingIndex = int(input("Enter initial file index: ")) #здесь поставьте первый абсолютный индекс в табличке
#в папке с этим кодом оставьте файл dataset.txt, в котором построчно перечислены строки для озвучки
with open(filename, 'r',encoding="utf-8-sig") as file:
    for line in file:
        newlines.append(line.replace('\t', '').strip()) #заполняем список строк для озвучки

with open("yandexCloud.txt", 'r',encoding="utf-8-sig") as file:
    for line in file:
        authdata.append(line.split("=")[1].strip()) #получаем секретные данные для использования со SpeechKit API

oauth_token = authdata[0]
catalog_id = authdata[1]

session = Session.from_yandex_passport_oauth_token(oauth_token, catalog_id)
synthesizeAudio = SpeechSynthesis(session)
for index, string in enumerate(newlines):
    absIndex = startingIndex+index
    synthesizeAudio.synthesize(
        #здесь вставляйте свой путь до папки, куда будут сгружаться файлы
        #в конце дописать {absIndex}.wav
        format(f'C:\\Users\\Vladislav\\PycharmProjects\\yandex_SpeechKitUsage\\output\\{absIndex}.wav'), text=string,
        voice='filipp', sampleRateHertz='16000',
    )