import pyautogui, tkinter, threading
from keyboard import is_pressed
from random import choice
import sounddevice as sd
import soundfile as sf

data, samplerate = sf.read('success.mp3')

win = tkinter.Tk()
win.geometry('500x370')
win.resizable(False, False)
win.title('Microsoft Points Macro')

start_words = ['how to ', 'what is ', 'imagine if ', 'so what ', 'what does ', 'when is ', 'how does ', 'how come '
               , 'when does ', 'where does ', 'for what does ', 'is ', 'why is ']
middle_word = ['play ', 'fire ', 'eat ', 'fight ', 'draw ', 'fake ', 'slap ', 'drive ', 'safe-', 'try ', 'fry ', 'graph '
               , 'explain ', 'unfold ', 'commence ', 'interact ', 'fetch ', 'hope ']
end_words = ['the game', 'a gun', 'bees', 'football', 'defined', 'fail', 'food', 'eggs', 'foo', 'dread', 'deepwoken'
             , 'roblox tycoon', 'money laundering', 'CoD', 'shawarma', 'tactics', 'RTS']
decorations = ['?', '!', '.', '', '', '', '???']

move_to_pos = (140, 70)
tk_search_var = tkinter.IntVar(win, 1)
sleep_seconds = tkinter.IntVar(win, 5)
in_search = False
searching = False

def random_sentence_search(button):
    button.config(state="disabled", text="Working")
    for i in range(0, tk_search_var.get()):
        print(threading.current_thread().name)
        if is_pressed('q'):
            print("trying to break")
            break
        pyautogui.sleep(sleep_seconds.get()/2)
        pyautogui.moveTo(move_to_pos)
        sentence = (choice(start_words)
                    + choice(middle_word)
                    + choice(end_words)
                    + choice(decorations))

        pyautogui.sleep(1)
        pyautogui.click()
        pyautogui.typewrite(sentence)
        pyautogui.press('enter')
        pyautogui.sleep(sleep_seconds.get()/2)
    sd.play(data, samplerate)
    sd.wait()
    button.config(state="normal", text="Start Macro")

def set_search_pos(button):
    global move_to_pos, searching
    button.config(state="disabled", text="Q to select")
    searching = not searching
    while searching:
        if is_pressed('q'):
            move_to_pos = pyautogui.position()
            button.config(state="normal", text="Select Pos")
            searching = False
            break

canvas = tkinter.Canvas(win, width=500, height=400)
canvas.pack()

start_button = tkinter.Button(canvas, text='Start Macro',
                              command=lambda: threading.Thread(target=random_sentence_search,
                                                               daemon=True, args=(start_button,)).start())
start_button.grid(column=0, row=0, padx=10, pady=10)

canvas2 = tkinter.Canvas(canvas, width=500, height=300)
canvas2.grid(column=1, row=0, padx=0, pady=10)

search_num_scale = tkinter.Scale(canvas2, variable=tk_search_var, from_=1, to=40, orient="horizontal", name="search amount")
search_num_scale.grid(column=0, row=0, padx=0, pady=10)

sleep_secs_num_scale = tkinter.Scale(canvas2, variable=sleep_seconds, sliderlength=10, length=50,
                                     from_=10, to=1, orient="vertical", name="sleep amount")
sleep_secs_num_scale.grid(column=1, row=0, padx=0, pady=10)

select_pos_button = tkinter.Button(canvas, text='Select Pos',
                                   command=lambda: threading.Thread(target=set_search_pos,
                                                                    daemon=True, args=(select_pos_button,)).start())
select_pos_button.grid(column=0, row=1, padx=10, pady=10)

pos_button_text = tkinter.Label(canvas, bg="#fffffd", text=' put the mouse over the search bar\n'
                                ' (the one on the very top) and press q ',
                                borderwidth=2, relief='ridge')
pos_button_text.grid(column=1, row=1, padx=10, pady=10)

explanation_text = tkinter.Label(win, bg="#fffffd", text='explanation:\n'
                                                        'to use this, you must have edge open, then make sure to try '
                                                        'first with just one search, then increase the amount in the '
                                                        'slider, its best if you do in patches of 10.\n'
                                                        'the other slider is the seconds between searches '
                                                        'increase if your internet is slow.\n'
                                                        'if you need to stop the macro hold q till it stops',
                                 borderwidth=2, relief='ridge', wraplength=400, justify='left')
explanation_text.pack(padx=10, pady=10)
win.mainloop()