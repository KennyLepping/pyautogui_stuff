import keyboard
import pyautogui

def main():
    while True:
        # Listen for CTRL+\ key combination
        if keyboard.is_pressed('ctrl+\\'):
            print('Detected ctrl+\\')
            # Press CTRL+E
            pyautogui.hotkey('ctrl', 'e')
            # Sleep to avoid repeated keypresses
            keyboard.wait('ctrl')
        # Exit the loop when the user presses 'q'
        if keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
