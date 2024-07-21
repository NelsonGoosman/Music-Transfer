import colorama
from pynput import keyboard
from pynput.keyboard import Key
colorama.just_fix_windows_console()
import os




class UI_Loop:
    idx = 0
    playlists = None
    def __init__(self, playlists):
        self.playlists = playlists
        self.show_interface()
        with keyboard.Listener(on_release=self.on_key_release) as listener:
            listener.join()

    def show_interface(self):
        for i in range(len(self.playlists)):
            if i == self.idx: 
                print("> " +  colorama.Fore.GREEN + self.playlists[i])
            else:
                print("  " + colorama.Fore.WHITE + self.playlists[i])

    def on_key_release(self, key):
        if key == Key.up:
            self.increase_idx()
        elif key == Key.down:
            self.decrease_idx()
        elif key == Key.esc:
            exit()
        os.system('cls')
        self.show_interface()

    def increase_idx(self):
        if self.idx < len(self.playlists):
            self.idx += 1

    def decrease_idx(self):
        if self.idx > 0:
            self.idx -= 1

