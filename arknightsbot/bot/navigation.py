from arknightsbot.detection.image_rec import *
from arknightsbot.ldplayer.client import (
    scroll,
    restart_AK
)

def get_to_main_menu_after_startup():
    print("Trying to get to main menu after starting")
    click_image("initial_start_button.png", delay=10)
    click_image("login_start_button.png", delay=10)
    while check_if_on_main_menu() is False:
        sleep(15)


def return_to_main_menu():
    sleep(3)
    if check_if_on_main_menu() is False:
        if locate_image_on_screen("home_button.png", max_tries=0) is not None:
            print("Trying to return to main menu")
            click_image("home_button.png")
            click_image("home_tab_button.png", delay=1)
        else:
            print("Failed to return to main menu, restarting Arknights")
            restart_AK()
            get_to_main_menu_after_startup()


def open_terminal():
    print("Trying to open terminal")
    click_image("terminal_button.png")


def open_main_theme_menu():
    print("Trying to open main theme menu")
    if check_if_on_main_menu():
        open_terminal()
        click_image("main_theme_button.png", delay=1)
    # I'm fairly certain there is not a single menu without the home button
    else:
        return_to_main_menu()
        open_main_theme_menu()


def go_to_act(act_number):
    act_to_clicks = {
        0: [(65, 136), (65, 136)],
        1: [(65, 136)],
        2: []
    }
    open_main_theme_menu()
    clicks = act_to_clicks[act_number]
    print(f"Going to act {act_number}")
    for click in clicks:
        click_on_location(click, delay=1)
    click_on_location((957, 360), delay=1)


def go_to_episode(episode_number):
    episode_to_clicks = {
        0: 3,
        1: 2,
        2: 1,
        3: 0,
        4: 4,
        5: 3,
        6: 2,
        7: 1,
        8: 0,
        9: 1,
        10: 0
    }
    clicks = episode_to_clicks[episode_number]
    act = episode_number // 4
    go_to_act(act)
    if clicks == 0:
        print(f"Already in episode {episode_number}")
    else:
        print(f"Going to episode {episode_number}")
    for i in range(clicks):
        click_on_location((982, 663), delay=1)

    print("Scrolling to beginning of episode")
    for i in range(10):
        scroll("left")


# def go_to_stage(stage_number):

# #Checks
#
def check_if_on_main_menu():
    print("Checking if on main menu")
    if locate_image_on_screen("terminal_button.png", max_tries=0) is not None:
        print("Is on main menu")
        return True
    else:
        print("Is not on main menu")
        return False
