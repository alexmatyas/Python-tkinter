from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Progressbar

class NextQuest(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app
        global x 
        if self.ans1.get() or self.ans2.get() or self.ans3.get() or self.ans4.get() :
            if self.ans1.get() and self.ans2.get() and self.ans3.get() :
                results +=1
                x.append(1)
            else :
                x.append(0)
            self.destroy()
            app = NextQuest1(window)
        else :
            messagebox.showinfo("Ответ", "Пожалуйста, выберите ответ на вопрос!")

    def check(self) :
        global app
        global x
        x.append(0)
        self.destroy()
        app = NextQuest1(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "Выберите структурные составляющие процессов социализации и инкультурации:", font = 16).place(x=80, y=30)
        self.ans1 = BooleanVar()
        Checkbutton(self, text = "1) Архетипическая (конструирование образа виртуальной личности)", font = 14, variable=self.ans1).place(x=90, y=110)
        self.ans2 = BooleanVar()
        Checkbutton(self, text = "2) Мотивационная (удовлетворение актуальных потребностей) ", font = 14, variable=self.ans2).place(x=90, y=160)
        self.ans3 = BooleanVar()
        Checkbutton(self, text = "3) Инструментальная (развитие компетенций)", font = 14, variable=self.ans3).place(x=90, y=210)
        self.ans4 = BooleanVar()
        Checkbutton(self, text = "4) Деструктивная (разрушение привычного мироощущения)", font = 14, variable=self.ans4).place(x=90, y=260)
        Button(self, text = "Ок", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=450, y=340, width=180, height=35)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="10").place(x=170, y=450)

class NextQuest1(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app
        global x
        ans = self.ans.get()
        if not ans == "None" :
            if ans == "1" :
                results +=1
                x.append(1)
            else :
                x.append(0)
            self.destroy()
            app = NextQuest2(window)
        else :
            messagebox.showinfo("Ответ", "Пожалуйста, выберите ответ на вопрос!")
            
    def check(self) :
        global app 
        global x
        x.append(0)
        self.destroy()
        app = NextQuest2(window)
    
    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label(self, text="Почему для исследования темы социально-сетевой инкультуризации и социализации интересно использовать опыт молодёжи (20-25 лет)?", font = 14, wraplength=700).place(x=60, y=30)
        self.ans = StringVar()
        self.ans.set(None)
        Radiobutton(self, text = "Потому что именно это поколение могло «зафиксировать» момент появления в их жизни Интернета и первых платформ социальных сетей.", font = 14, wraplength=600, variable=self.ans, value=1).place(x=80, y=115)
        Radiobutton(self, text = "Потому что молодёжь (студенты) - самая доступная категория людей для проведения исследований.", font = 14, wraplength=600, variable=self.ans, value=2).place(x=80, y=180)
        Radiobutton(self, text = "Потому что это единственные представители пользователей социальных сетей.", font = 14, variable=self.ans, value=3).place(x=80, y=245)
        Radiobutton(self, text = "Потому что для молодёжи нехарактерна успешная киберсоциализация.", font = 14, variable=self.ans, value=4).place(x=80, y=290)
        Button(self, text = "Ок", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=450, y=340, width=180, height=35)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="20").place(x=170, y=450)

class NextQuest2(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app
        global x
        ans = self.ans.get()
        if not ans == "None":
            if ans == "2" :
                results +=1
                x.append(1)
            else :
                x.append(0)
            self.destroy()
            app = NextQuest3(window)
        else :
            messagebox.showinfo("Ответ", "Пожалуйста, выберите ответ на вопрос!")
            
    def check(self) :
        global app
        global x
        x.append(0)
        self.destroy() 
        app = NextQuest3(window)
    
    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label(self, text="По результатам опроса, когда у респондентов преимущественно формировались навыки цифровой грамотности?", font = 14, wraplength=700).place(x=60, y=30)
        self.ans = StringVar()
        self.ans.set(None)
        Radiobutton(self, text = "В детском и подростковом возрасте, когда происходило непосредственное знакомство с социальными сетями.", font = 14, wraplength=600, variable=self.ans, value=1).place(x=80, y=115)
        Radiobutton(self, text = "Во взрослом возрасте, преимущественно благодаря чтению научной литературы и специальным дисциплинам в вузе.", font = 14, wraplength=600, variable=self.ans, value=2).place(x=80, y=180)
        Radiobutton(self, text = "Это врождённый компонент, на его формирование окружение и новая информация не оказывают большого влияния.", font = 14, wraplength=600, variable=self.ans, value=3).place(x=80, y=245)
        Button(self, text = "Ок", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=450, y=340, width=180, height=35)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="30").place(x=170, y=450)

class NextQuest3(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app 
        global x
        if self.ans1.get() or self.ans2.get() or self.ans3.get() or self.ans4.get() :
            if self.ans4.get() :
                results +=1
                x.append(1)
            else :
                x.append(0)
            self.destroy()
            app = NextQuest4(window)
        else :
            messagebox.showinfo("Ответ", "Пожалуйста, выберите ответ на вопрос!")

    def check(self) :
        global app
        global x
        x.append(0)
        self.destroy()
        app = NextQuest4(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "К чему ведёт успешная социализация и инкультурация в социальных сетях?", font = 14).place(x=80, y=30)
        self.ans1 = BooleanVar()
        Checkbutton(self, text = "1) К овладению мультимедийными возможностями платформ.", font = 14, variable=self.ans1).place(x=90, y=110)
        self.ans2 = BooleanVar()
        Checkbutton(self, text = "2) К росту созидательной активности.", font = 14, variable=self.ans2).place(x=90, y=160)
        self.ans3 = BooleanVar()
        Checkbutton(self, text = "3) К умению использовать релевантные коммуникативным задачам субжанры.", font = 16, variable=self.ans3).place(x=90, y=210)
        self.ans4 = BooleanVar()
        Checkbutton(self, text = "4) Всё вышеперечисленное.", font = 14, variable=self.ans4).place(x=90, y=260)
        Button(self, text = "Ок", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=450, y=340, width=180, height=35)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="40").place(x=170, y=450)

class NextQuest4(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app 
        global x
        ans1 = self.ans1.get()
        ans2 = self.ans2.get()
        if ans1 and ans2 :
            if ans1 == "инкультурация" or ans1 == "Инкультурация" or ans1 == "ИНКУЛЬТУРАЦИЯ":
                results +=1
                x.append(1)
            else :
                x.append(0)
            if ans2 == "социализация" or ans2 == "Социализация" or ans2 == "СОЦИАЛИЗАЦИЯ":
                results +=1
                x.append(1)
            else :
                x.append(0)
            self.destroy()
            app = NextQuest5(window)
        else :
            messagebox.showinfo("Ответ", "Пожалуйста, введите ответ на вопрос!")

    def check(self) :
        global app
        global x
        x.append(0)
        x.append(0)
        self.destroy()
        app = NextQuest5(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "Процесс воспроизводства «культурного человека» и механизм поддержания культурных изменений - это ...", font = 14, wraplength=400).place(x=60, y=60)
        self.ans1 = StringVar()
        Entry (self, width=20, textvariable=self.ans1, font = 14).place(x=500, y=70, width=150, height=30)
        Label (self, text = "Приобщение к той или иной группе, осознание своей роли в этом сообществе, как поиск личностной идентичности  - это ...", font = 14, wraplength=400).place(x=60, y=160)
        self.ans2 = StringVar()
        Entry (self, width=20, textvariable=self.ans2, font = 14).place(x=500, y=170, width=150, height=30)
        Button(self, text = "Ок", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=450, y=340, width=180, height=35)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="50").place(x=170, y=450)

class NextQuest5(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app 
        global x
        ans1 = self.ans1.get()
        ans2 = self.ans2.get()
        if ans1 and ans2:
            if ans1 == "8-12 лет":
                results +=1
                x.append(1)
            else :
                x.append(0)
            if ans2 == "5. Всё вышеперечисленное":
                results +=1
                x.append(1)
            else :
                x.append(0)
            self.destroy()
            app = NextQuest6(window)
        else :
            messagebox.showinfo("Ответ", "Пожалуйста, выберите ответ на вопрос!")

    def check(self) :
        global app
        global x
        x.append(0)
        x.append(0)
        self.destroy()
        app = NextQuest6(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "В каком возрасте, согласно результатам исследования, создавался первый аккаунт в социальных сетях?", font = 14, wraplength=400).place(x=60, y=60)
        self.ans1 = StringVar()
        Combobox (self, textvariable=self.ans1, values = ("5-8 лет", "8-12 лет", "12-15 лет", "Единого варианта не было"), font = 14).place(x=500, y=70, width=200, height=30)
        Label (self, text = "Основные мотивы респондентов при создании аккаунта: ", font = 14).place(x=60, y=190)
        self.ans2 = StringVar()
        Combobox (self, textvariable=self.ans2, values = ("1. Нежелание быть «белой вороной», отрываться от коллектива", "2. Онлайн-игры со сверстниками", "3. Расширение круга знакомств", "4. Потребность узнать что-то новое", "5. Всё вышеперечисленное"), font = 14).place(x=60, y=240, width=500, height=30)
        Button(self, text = "Ок", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=450, y=340, width=180, height=35)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="60").place(x=170, y=450)

class NextQuest6(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app 
        global x
        ans1 = self.ans1.get()
        ans2 = self.ans2.get()
        if ans1 == "1":
            results +=1
            x.append(1)
        else :
            x.append(0)
        if ans2 == "43":
            results +=1
            x.append(1)
        else :
            x.append(0)
        self.destroy()
        app = NextQuest7(window)
        
    def check(self) :
        global app
        global x
        x.append(0)
        x.append(0)
        self.destroy()
        app = NextQuest7(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "Труды каких исследователей оказали влияние на авторов монографии?", font = 14).place(x=80, y=30)
        Label (self, text = "1) Г. Дженкинса, Л.О. Пазиной и С.С. Зубаревой, Д. Миллера", font = 14).place(x=90, y=80)
        Label (self, text = "2) З. Фрейда, Ф. Ницше, Л. Толстого", font = 14).place(x=90, y=130)
        Label (self, text = "3) А. П. Глухова, М. Н. Бычковой, И. В. Гужовой", font = 14).place(x=90, y=180)
        self.ans1 = StringVar()
        Spinbox(self, from_=1, to=3, width=5, textvariable=self.ans1, font = 14).place(x=600, y=130, width=40, height=35)
        Label (self, text = "Приблизительно какой процент составили респонденты, заводившие свой первый аккаунт «из чистого любопытства»?", font = 14, wraplength=400).place(x=80, y=230)
        self.ans2 = StringVar()
        Spinbox(self, values=(10, 25, 43, 90), width=5, textvariable=self.ans2, font = 14).place(x=600, y=240, width=40, height=35)
        Button(self, text = "Ок", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=450, y=340, width=180, height=35)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="70").place(x=170, y=450)

class NextQuest7(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app 
        global x
        results +=1
        x.append(1)
        self.destroy()
        app = NextQuest8(window)
        
    def checkNotOK(self) :
        global app
        global x
        x.append(0)
        self.destroy()
        app = NextQuest8(window)

    def check(self) :
        global app
        global x
        x.append(0)
        self.destroy()
        app = NextQuest8(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "Нужно ли родителям проявлять реальный интерес к своим детям, их занятиям и творческим порывам в культуре социальных сетей для формирования совместной «культуры участия»?", font = 14, wraplength=500).place(x=140, y=80)
        Button(self, text = "Да", bg="green", fg="white", font = 14, command = self.checkOK).place(x=200, y=200)
        Button(self, text = "Нет", bg="green", fg="white", font = 14, command = self.checkNotOK).place(x=530, y=200)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="80").place(x=170, y=450)

class NextQuest8(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app
        global x 
        results +=1
        x.append(1)
        self.destroy()
        app = NextQuest9(window)
        
    def checkNotOK(self) :
        global app
        global x
        x.append(0)
        self.destroy()
        app = NextQuest9(window)

    def check(self) :
        global app
        global x
        x.append(0)
        self.destroy()
        app = NextQuest9(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "Становятся ли различия в мотивах, практиках использования социальных медиа и профилях цифровых компетенций причиной межпоколенческого цифрового разрыва?", font = 14, wraplength=500).place(x=140, y=80)
        Button(self, text = "Да", bg="green", fg="white", font = 14, command = self.checkOK).place(x=200, y=200)
        Button(self, text = "Нет", bg="green", fg="white", font = 14, command = self.checkNotOK).place(x=530, y=200)
        Button(self, text = "Пропустить вопрос", font = 14, command = self.check, bg="#B0E0E6").place(x=80, y=340, width=180, height=35)
        Progressbar (self, length=400, value="90").place(x=170, y=450)

class NextQuest9(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()
    
    def checkOK(self) :
        global results
        global app 
        global x
        ans1 = self.ans1.get()
        ans2 = self.ans2.get()
        if ans1 == 70:
            results +=1
            x.append(1)
        else :
            x.append(0)
        if ans2 == 3 :
            results +=1
            x.append(1)
        else :
            x.append(0)
        self.destroy()
        app = AllResults(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        Label (self, text = "Установите значение на шкале, соответствующее проценту респондентов, ответивших «Навыки фильтрации и проверки информации в сетях» на вопрос о ключевых цифровых компетенциях (из Таблицы 1).", font = 14, wraplength=700).place(x=50, y=30)
        self.ans1 = IntVar()
        Scale (self, orient="horizontal", resolution=10, from_=0, to=100, variable=self.ans1, font = 14).place(x=280, y=120, width=180)
        Label (self, text = "Что НЕ входит в модель социально-сетевой цифровой грамотности?", font = 14).place(x=80, y=180)
        Label (self, text = "1. Лингвистическая грамотность", font = 14).place(x=90, y=230)
        Label (self, text = "2. Грамотность безопасности", font = 14).place(x=90, y=260)
        Label (self, text = "3. Грамотность ответственности", font = 14).place(x=90, y=290)
        Label (self, text = "4. Грамотность самопрезентации", font = 14).place(x=90, y=320)
        self.ans2 = IntVar()
        Scale (self, orient="vertical", resolution=1, from_=1, to=4, variable=self.ans2, font = 14).place(x=500, y=230, height=110)
        Button (self, text = "Получить результаты", font = 14, command = self.checkOK, bg="#B0E0E6").place(x=290, y=370, width=180, height=35)
        Progressbar (self, length=400, value="100").place(x=170, y=450)

class AllResults(Frame) :
    def __init__(self, fr) :
        super().__init__(fr)
        self.place(relwidth=1, relheight=1)
        self.quest()

    def txtWrite(self) :
        self.txt = open("e:/Downloads/Programm/Results.txt", "w+", encoding='utf-8')
        self.txt.write("Ваши результаты: " + str(results) + " из 14")
        self.txt.write('\n')
        for i in range(len(x)):
            if x[i] == 0 :
                self.txt.write("\n" + '%3s'%(str(i+1)) + ". " + "Неверно")
            else :
                self.txt.write("\n" + '%3s'%(str(i+1)) + ". " + "Верно")
        self.txt.write('\n')
        self.txt.close()
        messagebox.showinfo("Запись", "Результаты успешно записаны!")


    def goBack(self) :
        global app
        self.destroy()
        app = NextQuest(window)

    def quest(self) :
        Label(self, image = bgImage).place(relwidth=1, relheight=1)
        global results
        Label (self, text="Ваши результаты: {0} из 14".format(results), font = 14).place(x=80, y=70)
        for i in range(len(x)) :
            if i < 7 :
                Label (self, text="№: {0} ".format(i+1), font = 14).place(x=80+70*i, y=160, width=70)
                if x[i] == 0 :
                    Label (self, text="Неверно", font = 14).place(x=80+70*i, y=190, width=70)
                else :
                    Label (self, text="Верно", font = 14).place(x=80+70*i, y=190, width=70)
            else :
                Label (self, text="№: {0} ".format(i+1), font = 14).place(x=80+70*(i-7), y=260, width=70)
                if x[i] == 0 :
                    Label (self, text="Неверно", font = 14).place(x=80+70*(i-7), y=290, width=70)
                else :
                    Label (self, text="Верно", font = 14).place(x=80+70*(i-7), y=290, width=70)
        Button(self, text = "Записать результаты\nв файл", font = 14, command = self.txtWrite, bg="#B0E0E6").place(x=80, y=355, width=170, height=60)
        Button(self, text = "В начало", font = 14, command = self.goBack, bg="#B0E0E6").place(x=520, y=370, width=100, height=35)

results = 0
x = []
window = Tk()
window.title("Вопросы к курсовой")
window.geometry("750x500")
window.resizable(False, False)
bgImage = PhotoImage(file="bg.png")
lbl_img = Label(window, image = bgImage).place(relwidth=1, relheight=1)
app = NextQuest(window)

window.mainloop()