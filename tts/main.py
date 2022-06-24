from gtts import gTTS
import os 

text = input('text: ')
save = input('name of file: ')
lang = 'en'
obj = gTTS(text = text, lang = lang, slow=False)

saved_file = obj.save(f'{save}.mp3')
os.system(f'mpg321{saved_file}')
