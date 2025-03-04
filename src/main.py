import flet as ft
import random 
# from CountdownTimer import Countdown

global page_global, instructions_label, score_lbl, display_lbl, user_entry_box, colors_row 
# Flet widgets placeholders -- initially, they are set to None
# None is a place holder -- it means "nothing is in the box"
instructions_label = score_lbl = display_lbl = user_entry_box = colors_row = None

global game_started, right_answer, score, my_countdown
# Variables to Run the Game
game_started = False
right_answer = ""
score = 0
colors_list = ["Red", "Blue", "Yellow", "Pink", "Green", "Black", "Orange", "White", "Purple", "Brown"]


def make_widgets():
    global instructions_label, score_lbl, display_lbl, user_entry_box, colors_row

    instructions_label = ft.Text(
        value="Type the word color NOT the word text!", 
        size=20, 
        color= ft.ColorScheme.primary_container
    )

    # create a score label
    
    
    display_lbl = ft.Text("", size=20, weight= ft.FontWeight.BOLD)

    # create the user_entry_box
    



    # Add the available colors
    colors_row = ft.Row(
        spacing=10, 
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    color_displays = []
    # make a little container for each color and add it to color displays
    
    colors_row.controls = color_displays

def reset_the_game(event):
    global page_global, game_started, my_countdown, colors_row

def ask_play_again():
    global page_global


def add_widgets_to_page():
    global page_global, instructions_label, score_lbl,display_lbl, user_entry_box, colors_row

    page_global.add(instructions_label)
    # add the score_lbl to the page here
    
    page_global.add(display_lbl)
    # add the user_entry_box to the page here
    
    page_global.add(colors_row)

def check_answer(event):
    global user_entry_box, score
    print("checking the answer")
    

    

def show_next_color():
    global page_global, right_answer, my_countdown
    print("showing next color")




def run_on_enter(event):
    print("The game should start")


def main(page: ft.Page):
    global page_global
    page_global = page
    page.title = "ColorGame"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    make_widgets()
    add_widgets_to_page()
    page.on_keyboard_event = run_on_enter
    page.update()


ft.app(main)
