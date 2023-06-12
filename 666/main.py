#калькулятор
'''''def calc():
    print('qq')
    try:
        num1=int(input('Введите первое число: '))
        num2=int(input('Введите второе число: '))
        x=input('Знак: ')
    except ValueError:
        print('Вы ввели неверное значение')
    if x == "*":
        print(num1*num2)
    elif x == "/":
        print(num1/num2)
    elif x == "+":
        print(num1+num2)
    elif x == "-":
        print(num1-num2)
def calc():
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
        x = 0
    except ValueError:
        print('Вы ввели неверное значение')
    else:
        x = b**2 - 4*a*c
        print(x)
calc()'''''
from types import TracebackType

#обычная викторина
'''#questions = [\
#{'question': 'Когда вышел бойцовский клуб?', 'answers': ['2014', '1991', '1996', 'Нет правильного ответа'],
#'right_answer': 3},{'question': 'Как зовут актера, сыгравшего главного героя в фильме бойцовский клуб?',
#'answers': ['Эдвард', 'Гарри', 'Лео', 'Дима'],
#'right_answer': 1},{'question': 'Кого сыграл Брэд Питт в фильме бойцовский клуб?',
#'answers': ['Роберт Полсон,', 'Марта Сюарт', 'Тайлер Дерден', 'Нет правильного ответа'],
#'right_answer': 3}]

#points = 0
#for quest in questions:
#    answer_number = 0
#    for answer in quest['answers']:
#        answer_number += 1
#        print(answer_number,'.',answer)
#    user_answer = int(input('Ваш ответ:'))
#    if user_answer == quest.get('right_answer'):
#        points += 1
#        print('Верно')
#    else:
#        print('Не верно')
#    print('-'*50)
#print('Верных Ответов:', points)
#if quest.get ('right_answer') > 3:
#    print('Ты победил!')
#else:
#    quest.get ('right_answer') < 3
#    print('Ты проиграл')'''

# Игра графическая викторина
'''from tkinter import *
#создаем окошко
window = Tk()
window.geometry('600x400')
window.title('Самый сложный тест')
cur_fact=0 #хранинение номера текущего факта
points=0
def check():
    global points,cur_fact
    #хранение ответа пользователя
    answer=var.get()
    if bool(answer)==facts[cur_fact]['right']:
        points += 1
    if cur_fact < len(facts) - 1:
        cur_fact+=1
        fact['text']=facts[cur_fact]['text']
    else:
        points_label=Label(text='Вы набрали: ' + str(points) + 'очоков',font=('Arial', 30))
        points_label.place(width=600,height=200)
facts = [{'text': 'Человек паук убивал людей', 'right': 1},{'text': 'Морбиус герой', 'right': 1},\
         {'text': 'Железный человек был инвалидом', 'right': 1}]

#создание заголовка
label_title=Label(text='Тестирование по вселенной Марвел', font=('Arial', 24))
label_title.place(x=0,y=0,width=600,height=50)
#создание вопросов
fact=Message(text=facts[cur_fact]['text'], font=('Arial', 18), width=550)
fact.place(x=10, y = 70)
#добавление вариантов ответа
var=IntVar()
true=Radiobutton(text='Правда',variable=var, value=1)
true.place(x=10,y=120)
false=Radiobutton(text='Ложь',variable=var, value=0)
false.place(x=10,y=170)
#кнопка
butt=Button(text='Ответить',font=('Arial', 20),command=check)
butt.place(x=200,y=130)
#создание картинок
pic_happy=PhotoImage(file='happy.png')
label_happy=Label(image=pic_happy)
pic_sad=PhotoImage(file='sad.png')
label_sad=Label(image=pic_sad)

window.mainloop()'''

#Игра кликер
'''from tkinter import *
import random
window = Tk()
window.geometry('600x400')
window.title('Кликер')
points=0
def check():
    global points
    b.place(x=random.randint(0, 550),y=random.randint(0, 350))
    points += 1
    label['text'] = points
    if points >= 10:
        y['text'] = 'Ну пожалуйста('
def zxc():
    global points
    y.place(x=random.randint(0, 550), y=random.randint(0, 350))
    points += 1
    label['text'] = points
    if points >= 10:
        b['text'] = 'Ну пожалуйста('
b = Button(text='Жмякни на меня', command=check)
label = Label(text=points)
label.place(x=10, y=10)
b.place(x=200, y=300)
y = Button(text='Нажми на меня', command=zxc)
y.place(x=100, y=250)
l = Label(text=points)
label.place(x=10, y=10)
window.mainloop()'''

#дз словари1
'''violator_songs = {
    'lonewolf': 2.50,
    'Go slow': 3.10,
    'EVE': 2.10,
    'Cinderella': 2.40,
    'Demons and Monsters': 3.10,
    'Akihabara': 1.40,
    'Blame game': 2.40,
    'After dark': 3.30
}
x = 0
y = int(input('Сколько песен выбрать? '))
for i in range(y):
    song = input("Название "+str(i+1)+" песни: ")
    if song in violator_songs:
        x += violator_songs[song]
print('Общее время звучания: ', x, 'минуты')'''

#дз словари2
'''goods = {
    "Лампа": '12345',
    "Стол": '23456',
    "Диван": '34567',
    "Стул": '45678',
}
store = {
    '12345': [
            {'pieces': 27, 'price': 42},
    ],
    '23456': [
        {'pieces': 22, 'price': 510},
        {'pieces': 32, 'price': 520},
    ],
    '34567': [
        {'pieces': 2, 'price': 1200},
        {'pieces': 1, 'price': 1150},
    ],
    '45678': [
        {'pieces': 50, 'price': 100},
        {'pieces': 12, 'price': 95},
        {'pieces': 43, 'price': 97},
    ],
}

for i in goods:
    x = 0
    y = 0
    for j in store[goods[i]]:
        x += j['pieces'] * j['price']
        for t in store[goods[i]]:
            y += t['pieces']
print(i, '-', y, 'штук',  ":", x, 'рублей')'''

#типа вирус
'''from tkinter import*
window = Tk()
window.geometry('450x300')
#запрет на изменение параметров окна
window.resizable(width=False,height=False)
#задаем фон
window.config(bg='black')
#добавляем текст
text=Label(text='Ваш компьютер заражен', bg='black',fg= 'red', font= ('Arial', 18))
text.place(x=0,y=130,width=450,height=100)
#добавляем счетчик
count_text=Label(text='6', bg='black',fg= 'red', font= ('Arial', 18))
def on_close():
    if int(count_text['text']) > 0:
        count_text['text'] = int(count_text['text'])-1
        count_text.place(x=90,y=100,width=300, height=70)
        window.after(1000, on_close) #функция отложенного запуска (1000 милисек = 1 сек)
    else:
        width=window.winfo_screenwidth()
        height=window.winfo_screenheight()
        window.geometry(str(width)+'x'+str(height))
        photo=PhotoImage(file='BlindEarlyGiraffe-size_restricted.gif')
        label=Label(image=photo, bg='black')
        label.image=photo
        label.place(width=width,height=height)
        window.after(20000, exit)
window.protocol('WM_DELETE_WINDOW', on_close)

window.mainloop()'''

#парсинг
'''import requests
import random
from bs4 import BeautifulSoup
def get_fact ():
    response = requests.get('https://i-fakt.ru/').content # запрос по ссылке
    html = BeautifulSoup(response, 'lxml') #оформление красивого вывода
    fact = random.choice(html.find_all(class_='p-2 clearfix')) #список
    reference = fact.a.attrs    #словари
    href_fact = reference.get('href') #вытаскивание ссылки
    print(fact.text, href_fact)

def get_fest():
    response = requests.get('https://kudago.com/msk/festival/').content
    html = BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='post-title-link'))
    print(fest['href'])
    reference=fest['href']
    print(fest.text,reference)

def get_film ():
    response = requests.get('https://kudago.com/msk/kino/schedule-cinema/').content
    html = BeautifulSoup(response, 'lxml')
    film = random.choice(html.find_all(class_='post-title-link'))
    reference = film['href']
    print(film.text,reference)
get_film()'''

#дз вирус1
'''from tkinter import*
from tkinter import ttk
window = Tk()
window.geometry('750x400')
window.resizable(width=False,height=False)
window.config(bg='black')
text=Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!', bg='black',fg= 'red', font= ('Arial', 20))
text.place(x=140,y=40,width=450,height=100)
clicks=0
def zxc():
    global clicks
    y.place(x=285, y=150)
    clicks += 1
    if clicks == 1:
        y['text'] = 'Чтобы забрать выйгрыш необходимо внести 1000руб.'
        y.place(x=200, y=150)
y = Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!', command=zxc)
y.place(x=285, y=150)
def on_close(self, parent):
    super().on_close(parent)
window.protocol('WM_DELETE_WINDOW', on_close)
window.mainloop()'''

#дз ткинтер
'''from tkinter import *
import time
import random
window = Tk()
window.geometry('600x400')
window.config(bg='purple')
window.title('Кликер')
points=0
def check():
    global points,b
    b.place(x=random.randint(0, 550),y=random.randint(100, 350))
    points += 1
    label['text'] = points
    if points > 15:
        label_title['text']='Тебе лучше?'
    if points > 25:
        label_title['text'] = 'Ну все, пора за работу!'
    if points > 35:
        label_title['text'] = 'ХВАТИТ!'
    if points > 37:
        time.sleep(200000)
label_title = Label(text='Покликай немного и расслабься', bg='purple', font=('Arial', 24))
label_title.place(x=0, y=0, width=600, height=50)
b = Button(text='Жмякни на меня', command=check)
label = Label(text=points)
label.place(x=10, y=10)
b.place(x=200, y=300)
window.mainloop()'''

#Телеграмм бот
'''import telebot
import requests
import random
from bs4 import BeautifulSoup
token = "5610656983:AAGMWJLPG5ekYNQ4S3GJF4nHlHfG3NofSJ4"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = ' Привет! Я умею рассказывать стихи, знаю много интересных фактов  и могу присылать аниме картинки'
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Факт')
    button2 = telebot.types.KeyboardButton('Картинки из аниме')
    button3 = telebot.types.KeyboardButton('Стихотворение')
    button4 = telebot.types.KeyboardButton('Игры')
    keyboard.add(button1,button2,button3,button4)
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    send_poem_text = ' Муха села на варенье вот и все стихотворение... '
    bot.send_message(message.chat.id, send_poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url=telebot.types.InlineKeyboardButton('Перейти', url='https://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id, 'Больше стихов здесь: ', reply_markup=keyboard)

@bot.message_handler(commands=['facts'])
def get_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['animepictures'])
def send_animepictures(message):
    anipicture_numder=str(random.randint(1,10))
    anipicture_img = open('img/' + anipicture_numder + '.jpg', 'rb')
    bot.send_photo(message.chat.id, anipicture_img)

@bot.message_handler(commands=['game'])
def get_game(message):
    send_game_text = ' Какой жанр игр вы предпочитаете? '
    bot.send_message(message.chat.id, send_game_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)
    button_adventure = telebot.types.InlineKeyboardButton('Приключения', url='https://www.igromania.ru/games/pc/adventure/')
    keyboard.add(button_adventure)
    button_sport = telebot.types.InlineKeyboardButton('Спорт', url='https://www.igromania.ru/games/pc/sport/')
    keyboard.add(button_sport)
    button_horror = telebot.types.InlineKeyboardButton('Хоррор', url='https://www.igromania.ru/games/pc/horror/')
    keyboard.add(button_horror)
    bot.send_message(message.chat.id, 'Варианты: ', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip() == 'Факт':
        get_fact(message)
    elif message.text.strip() == 'Стихотворение':
        send_poem(message)
    elif message.text.strip() == 'Картинки из аниме':
        send_animepictures(message)
    elif message.text.strip() == 'Игры':
        get_game(message)
bot.polling()'''


#Рисование на окне
'''from tkinter import*

window = Tk()
window.geometry('800x600')
#Создание холста
canvas=Canvas(window, width=800, height=600,bg='white')

#размещение холста
canvas.pack()

#прямоугольник
canvas.create_polygon(10,260,60,200,110,260,fill='red', outline='')
canvas.create_rectangle(20,260,100,360,fill='black', outline='')
canvas.create_rectangle(200,200,50,180,fill='green', outline='')
window.mainloop()'''

#Работа с классом
'''from tkinter import*
window = Tk()
window.geometry('800x600')
canvas=Canvas(window, width=800, height=600,bg='white')
canvas.pack()
class House:
    def __init__(self,roof_color,wall_color):
        self.roof_color = roof_color
        self.wall_color = roof_color
        self.height=130
        self.width=140
        self.roof=None
        self.wall=None
    def build_house(self,x,y):
        h=self.height
        w=self.width
        self.roof=canvas.create_rectangle(x, y, x + w, y, x + w/2 , h-100, fill=self.roof_color)
        self.roof = canvas.create_polygon(x+20,y,x+120,y+100,fill=self.wall_color, outline='')
house_1=House('yellow', 'green')
house_1.build_house(20,50)
window.mainloop()'''

#Делаем простенькую игру
'''from tkinter import *
import random
window=Tk()
w=600
h=600

window.geometry(str(w)+'x'+str(h))
#создание холста
canvas=Canvas(window, width=w, height=h)
canvas.pack()
#создание фона для игры
bg_photo=PhotoImage(file='4_bg.png')
#создание рыцаря
class Knight:
    def __init__(self): #конструктор (метод инициализации)
        #координаты центра рыцаря
        self.x=70 #атрибуты
        self.y=h//2
        #скорость рыцаря
        self.v=0
        #изображение рыцаря
        self.photo=PhotoImage(file='4_knight.png')
    #движение вверх
    def up(self, event):
        self.v=-3
    #движение вниз
    def down(self, event):
        self.v=3
    #остановка
    def stop(self, event):
        self.v=0
#класс Дракон
class Dragon:
    def __init__(self):
        self.x=750
        self.y=random.randint(100, 500)
        self.v=random.randint(1, 3)
        self.photo=PhotoImage(file='4_dragon.png')
knight=Knight() #вызов конструктора класса - создание экземпляра класса рыцарь
#создание экземпляров дракончиков
dragons=[]
for i in range(3):
    dragons.append(Dragon())



def game():
    canvas.delete('all')
    canvas.create_image(w//2, h//2, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y+=knight.v
    current_dragon = 0  # счётчик драконов
    dragon_to_kill = -1  # дракон, которого нужно удалить (индекс)
    for dragon in dragons:
        dragon.x-=dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

        if ((dragon.x-knight.x)**2) + ((dragon.y - knight.y)**2) <= (96)**2: #условие столкновения
            dragon_to_kill=current_dragon
        current_dragon+=1
#Проигрыш
        if dragon.x<=0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text="You lose!", font="Verdana 42", fill='red')
            break
    if dragon_to_kill>=0:
        del dragons[dragon_to_kill]
    if len(dragons)==0:
        canvas.delete('all')
        canvas.create_text(w // 2, h // 2, text="You win!", font="Verdana 42", fill='red')
    window.after(5, game)

game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)

window.mainloop()'''

'''from tkinter import *
class Image(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Прямоугольники и треугольники")
        self.pack(fill=BOTH, expand=True)
        c = Canvas(self)
        c.create_line(10, 10, 100, 100, 150, 50, 10, 10, fill="#1f1", width=2)
        c.create_line(150, 10, 150, 100, 180, 200, 150, 10, fill="#2e2", width=2)
        c.create_line(250, 110, 350, 150, 280, 200, 250, 110,  fill="#2e2", width=2)
        c.create_rectangle(230, 10, 290, 60, outline="#f11", fill="#1f1", width=2)
        c.create_rectangle(20, 110, 90, 160, outline="#f11", fill="#1f1", width=2)
        c.pack(fill=BOTH, expand=True)
w = Tk()
f = Image()
w.geometry("400x250")
w.mainloop()'''


#API звездные войны
'''import requests

url = 'https://swapi.dev/api/'

response=requests.get(url).json()
print(response)

people_api=response.get('people') #ссылка на инфу о персонажах
planets_api=response.get('planets') #ссылка на инфу о планетах
starship_api=response.get('starships')#ссылка на инфу о короблях
print(people_api)

def check_people(api):
    for i in range(1,6):
        req_people=requests.get(f'{api}/{i}').json()
        massa=req_people['mass']
        print(massa)
check_people(people_api)

def check_planets(api):
    for i in range(1,6):
        req_planet=requests.get(f'{api}/{i}').json()
        diam = req_planet.get('diameter')
        print(diam)
check_planets(planets_api)

def starships(api):
    for i in range(1,6):
        req_starships=requests.get(f'{api}/{i}').json()
        speed=req_starships.get('max_atmosphering_speed')
        print(speed)
starships(starship_api)'''


#API центробанка
'''import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = 'http://www.cbr.ru/scripts/XML_daily.asp?'

today=datetime.today()
today=today.strftime('%d/%m/%Y')
print(today)
dict_today={'date_req':today}

#date = f'date_req={today}'
#response=requests.get(url+date)
response=requests.get(url, params=dict_today)
xml=BeautifulSoup(response.content,'lxml')
print(xml)

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text
print(getCourse('R01235'),'рублей за один доллар')
print(getCourse('R01239'),'рублей за один евро')
print(getCourse('R01020A'),'рублей за один Азербайджанский манат')
print(getCourse('R01090B'),'рублей за Белорусский рубль')'''

#Голосовой помощник
'''import random
from pygame import mixer
from gtts import gTTS
import time
my_file=open('some_text.txt','w')
my_file.write('стрей даун')
my_file.close()

my_file=open('some_text.txt','r')
my_string=my_file.read()
my_file.close()

mixer.init()
tts=gTTS(text=my_string, lang='ru')
tts.save('music.mp3')

mixer.music.load('music.mp3')
mixer.music.play()
time.sleep(5)'''

'''import speech_recognition as sr
r=sr.Recognizer() #распознавтель
with sr.Microphone(device_index=1) as source:
    print('Скажи что-нибудь...')
    audio=r.listen(source)
speech=r.recognize_google(audio,language='ru_RU')
print('Вы сказали:',speech)
hello=['Привет', 'Здрасте','Ку','Здарова']
film=['Бойцовский клуб','Остров проклятых','Американский психопат','Драйв']
if speech == 'Привет':
    print(random.choice(hello))
elif speech == 'фильм':
    print(random.choice(film))'''




'''class tank:
    def __init__(self, model, armor,min_damage,max_damage,health):
        self.model=model
        self.armor=armor
        self.damage=random.randint(min_damage, max_damage)
        self.health = health
    def print_info(self):
        print(f'{self.model} имеет любую броню {self.armor} при мм {self.health} при единицах здоровья и уроне {self.damage} в единиц')
    def health_down(self, enemy_damage):
        self.health=enemy_damage
        print(f'{self.model}Броня пробита')
    def shot(self, enemy):
        if enemy.health <=0:
            print(f'Экипаж танка {enemy.model} уничтожен')
        else:
            enemy.health_down(enemy.damage)
            print(f'Точное попадание в цель, у противника{enemy.model} осталось {enemy.health} здоровья ')

tank1=tank('T-34', 90, 20, 30, 100)
tank2=tank('T-90',120, 10, 50, 150)
tank1.print_info()
tank2.print_info()'''

'''from tkinter import*
import time
import random

window =Tk()
window.title('Пинг-понг')
window.resizable(False,False)
canvas=Canvas(window, width=500, height=400)
canvas.pack()

class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.oval=canvas.create_oval(200,200,215,215,fill=color)
        dir = [-3,-1,-2,0,1,2,3]
        self.x= randomchoice
        self.x=0
        self.y=-1
    def draw(self):
        self.canvas.move(self.oval,self.x,self.y)
        pos=self.canvas.coords(self.oval)
        if pos[0]<=0:
            self.x=2
        if pos[2]>=500:
            self.x=-1
        if pos[1]<=0:


ball=Ball(canvas,'red')

while True:
    ball.draw()
    window.update()
    time.sleep(0.01)'''


#вк бот
'''import vk_api
from course import *
token='vk1.a.Pc4-xQB-VNFHb503SFdIJMwK3uiYcI3luY0HJ9o2pTrRAKfquzvBfGzmaIxFkGyowK66puTh6XKtZUl3P_\
hwXixrsr2XluSiRjCNKC-AAkE0nZ9s5NV3ZQ_v_\
eKsGcPWDUMBM_J3Uuj5Xa8_vCHmhJBVdeSb3mDDumhZ4ffdNEBkAySSXluVWKLyRfXH3mf1pvFGsJZa7vJTpgDkoc2-kQ'
vk=vk_api.VkApi(token=token) #создание экземпляра класса VkApi

vk._auth_token()
messages = vk.method('messages.getConversations', {'offset': 0, 'count': 20, 'filter': 'unanswered'})

while True:
    messages=vk.method('messages.getConversations', {'offset':0,'count':20, 'filter':'unanswered'})
    print(messages)
    if messages['count']>=1:
        user_id=messages['items'][0]['last_message']['from_id']
        message_text=messages['items'][0]['last_message']['text']
        message_id=messages['items'][0]['last_message']['id']
        if message_text.lower()=='курс':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': getCourse('R01235')})
        else:
            vk.method('messages.send', {'peer_id':user_id, 'random_id':message_id, 'message':message_text})'''


#проект на мильон
'''from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import sqlite3

# функция обработки сообщений от пользователя
def reply(update, context):
    # получаем текст сообщения от пользователя
    message = update.message.text
    # создаем подключение к базе данных
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    # выполняем запрос к базе данных
    c.execute("SELECT answer FROM responses WHERE question LIKE ?", ('%'+message+'%',))
    # получаем ответ из базы данных
    response = c.fetchone()[0]
    # отправляем ответ пользователю
    update.message.reply_text(response)
    # закрываем соединение с базой данных
    conn.close()

# создаем объект Updater и передаем ему токен бота
updater = Updater('TOKEN')

# создаем диспетчер для обработки входящих сообщений
dispatcher = updater.dispatcher

# создаем обработчик для текстовых сообщений от пользователя
text_handler = MessageHandler(filters.text, reply)

# добавляем обработчик в диспетчер
dispatcher.add_handler(text_handler)

# запускаем бота
updater.start_polling()'''

'''from time import time
class Timer:
    def __init__(self):
        print('Инициализация')
        self.start=None

    def __enter__(self):
        print('Вход в КМ')
        self.start=time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb: TracebackType):
        t=time()-self.start
        print(f'Выход: время работы кода: {t} сек')

        if exc_type is TypeError:
            print('Ошибочка')
            return True

    def __str__(self):
        return 'Я таймер'

with Timer() as t1:
    my_list=[x for x in range(1,100)]
    my_list-='s'
    print(t1)'''

'''class Year:
    def __init__(self, days, season):
        self.__days=days
        self.__season = season
    def get_days(self):
        return self.__days
    def get_season(self):
        return self.__season
    def set_days(self, days):
        if days==365 or days == 366:
            self.__days=days
            raise Exception('Некорректное значение')
    def set_season(self, season):
        self.__season=season
year=Year(365, 'зима')
print(year.get_days())
year.set_season('весна')
print(year.get_season())
#пробуем поменять значение без сеттера: не получается
year.__season='зима'
print(year.get_season())
#year.set_days(364)


class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def name (self):
        return self.__name

    @name.setter  # сеттер
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

person=Person('Иван', 30)
print(person.name)
person.name='Ваня'
print(person.name)'''

'''import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from course import getCourse
from wiki import get_wiki_article

token = "vk1.a.Pc4-xQB-VNFHb503SFdIJMwK3uiYcI3luY0HJ9o2pTrRAKfquzvBfGzmaIxFkGyowK66puTh6XKtZUl3P_hwXixrsr2XluSiRjCNKC\
-AAkE0nZ9s5NV3ZQ_v_eKsGcPWDUMBM_J3Uuj5Xa8_vCHmhJBVdeSb3mDDumhZ4ffdNEBkAySSXluVWKLyRfXH3mf1pvFGsJZa7vJTpgDkoc2-kQ"

vk_session=vk_api.VkApi(token=token)
#vk._auth_token()

vk=vk_session.get_api()
longpoll=VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type== VkEventType.MESSAGE_NEW and event.to_me:
        msg=event.text.lower()
        user_id=event.user_id
        random_id=random.randint(1, 10**10)
        print(f'{msg}, {user_id}')
        if msg == '-к':
            responce = f'{getCourse("R01235")} рублей за 1 доллар\n{getCourse("R01239")} за 1 евро'
            vk.messages.send(user_id=user_id, random_id=random_id, message=responce)
        else:
            vk.messages.send(user_id=user_id, random_id=random_id, message=get_wiki_article(msg))'''

'''def strcounter(stroka):
    for sym in stroka:
        counter=0
        for sub_sym in stroka:
            if sub_sym == sym:
                counter+=1
        print(sym,counter)
strcounter('ansdgasf')'''

'''def strcounter(stroka):
    for sym in set(stroka):
        counter=0
        for sub_sym in stroka:
            if sub_sym == sym:
                counter+=1
        print(sym,counter)
strcounter('ansdgasf')
print(set('ansdsf'))'''

def strcounter(stroka):
    syms_counter={}
    for sym in stroka:
        syms_counter[sym]=syms_counter.get(sym,0)+1

    print(syms_counter)




strcounter('ansdgasf')


