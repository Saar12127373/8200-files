from pynput import keyboard

def on_press(key):
    try:
        print(f"key_down: {key.char}")
    except AttributeError:
        print(f"key_down: {key}")

def on_release(key):
    try:
        print(f"key_up: {key.char}")
    except AttributeError:
        print(f"key_up: {key}")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()