import keyboard

def print_key(event):
    print(event.name)

keyboard.on_press(print_key)
keyboard.wait()
