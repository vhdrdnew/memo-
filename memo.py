from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question("Яблуко", 'apple', "pineapple", "strawberry", "blueberry")
q2 = Question("2 + 2", '5', "44", "4", "5000")
q3 = Question("Столиця Чина", 'Пекин', "тайланд", "токио", "київ")
q4 = Question("Хот створив ядерку", 'Опенгаймер', "Xiaomi", "Poco", "Samsung")

questions = [q1, q2, q3, q4]
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def new_question():
    global curent_question
    curent_question = choice(questions)
    lb_Question.setText(curent_question.question)
    shuffle(radio_buttons)
    radio_buttons[0].setText(curent_question.answer)
    radio_buttons[1].setText(curent_question.wrong_answer1)
    radio_buttons[2].setText(curent_question.wrong_answer2)
    radio_buttons[3].setText(curent_question.wrong_answer3)
    
new_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_Correct.text():
                curent_question.got_right()
                lb_Resultat.setText('Вірно!')
                break
    else:
        lb_Resultat.setText('Не вірно!')
        curent_question.got_wrong()

def click_ok():
    if btn_OK.text() == 'Відповісти':
        check()
        rbtn_1.hide()
        rbtn_2.hide()
        rbtn_3.hide()
        rbtn_4.hide()

        btn_OK.setText('Наступне запитання')
    else:
        rbtn_1.show()
        rbtn_2.show()
        rbtn_3.show()
        rbtn_4.show()

        btn_OK.setText('Відповісти')

btn_OK.clicked.connect(click_ok) 

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)



def menu_generation():
    menu.show()
    window.hide()

btn_Menu.clicked.connect(menu_generation)

def menu_back():
    menu.hide()
    window.show()

btn_back.clicked.connect(menu_back)

window.show()
app.exec_()