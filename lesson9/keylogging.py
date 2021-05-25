from pynput import keyboard

# def on_press_1(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

def on_release_1(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        # on_press=on_press_1,
        on_release=on_release_1) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    # on_press=on_press_1,
    on_release=on_release_1)
listener.start()