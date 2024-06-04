import pyautogui
import time
time.sleep(2)
def click_center():
    # Obtiene las coordenadas del centro de la pantalla
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    # Hace clic en el centro de la pantalla
    pyautogui.click(center_x, center_y)

# Bucle infinito que hace clic en el centro de la pantalla cada segundo
while True:
    click_center()
    time.sleep(0)
