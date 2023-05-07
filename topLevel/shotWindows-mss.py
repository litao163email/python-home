from mss import mss
with mss() as screenshot:
    screenshot.shot(output='scr.png')
