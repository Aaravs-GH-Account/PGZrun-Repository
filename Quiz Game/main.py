import pgzrun
WIDTH=870
HEIGHT=650
TITLE='Quiz Game'

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)

answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)

answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)

score=0
time_left=10
is_game_over=False
question_file_name=r'c:\Users\kidsLogin\Desktop\Quiz Game\questions.txt'
marquee_message=''

answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count=0 #total number of questions
question_index=0 #current question

def draw():
    screen.clear()
    global marquee_message
    
    screen.fill('black')
    screen.draw.filled_rect(marquee_box,'black')
    screen.draw.filled_rect(question_box,'blue')
    screen.draw.filled_rect(timer_box,'red')
    screen.draw.filled_rect(skip_box,'green')

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,'yellow')

    marquee_message=f'Welcome to the Quiz Game. Q: {question_index} of {question_count}'
    screen.draw.textbox(marquee_message,marquee_box,color='white')
    screen.draw.textbox(str(time_left),timer_box,color='white')
    screen.draw.textbox('Skip',skip_box,color='white')
    screen.draw.textbox(question[0].strip(),question_box, color='black')
    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box, color='black')
        index=index+1

def move_marquee():
    marquee_box.x = marquee_box.x-2
    if marquee_box.right<0:
        marquee_box.left=WIDTH

def read_question_file():
    global question_count, questions
    q_file=open(question_file_name,'r')
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split('|')

def update():
    move_marquee()

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.colliepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index=index+1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score, question, questions, time_left
    score=score+1
    if questions:
        question=read_next_question()
        time_left=10
    else:
        game_over()





#question=['Question:','ans1','ans2','ans3','ans4','1']
read_question_file()
question=read_next_question()
pgzrun.go()
