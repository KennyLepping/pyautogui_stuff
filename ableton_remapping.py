import keyboard
import pyautogui

def main():
    while True:
        # Listen for CTRL+\ key combination
        if keyboard.is_pressed('ctrl+\\'):
            print('Detected ctrl+\\')
            # Press CTRL+E
            pyautogui.hotkey('ctrl', 'e')
            print('Pressed CTRL+E')
        if keyboard.is_pressed('shift+\\'):
            print('Detected shift+\\')
            # Press SHIFT+TAB
            pyautogui.hotkey('shift', 'tab')
            print('Pressed SHIFT+TAB')
        if keyboard.is_pressed('ctrl', '/'):
            print('Detected ctrl+/')
            # Press SHIFT+TAB
            pyautogui.hotkey('ctrl', 'z')
            print('Pressed CTRL+Z')
        # Exit the loop when the user presses 'q'
        if keyboard.is_pressed('ctrl+q'):
            break

if __name__ == "__main__":
    main()
