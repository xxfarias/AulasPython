# pip install pyautogui
import pyautogui
import time
# Aguarde alguns segundos antes de inciar
# Para dar tempo de mover o mouse para o local desejado
time.sleep(5)
# Obtenha as coordendas do mouse (opcional)
x, y = pyautogui.position()
print(f"Coordenadas atuais do mouse: x={x}, y={y}")
# Defina as coordenadas do local onde você deseja clicar
target_x, target_y = 311, 30
# Mova o mouse para as coordenadas desejadas
pyautogui.moveTo(target_x, target_y)
# Simule um clique do mouse
pyautogui.click()
# Alternativamente, você pode usar o método
# Abaixo para clicar nas coordenadas diretamente