import pyautogui

def autoClick(seconds):
	if seconds == -1:
		seconds = 28800
	for i in range(seconds * 2):
		pyautogui.click(219, 436, 100, .005)
		pos = pyautogui.position()
		if pos[0] != 219 or pos[1] != 436:
			break

# autoClick(int(input("How long? (secs): ")))
autoClick(-1)
