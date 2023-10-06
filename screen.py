import pyautogui
import cv2
import numpy as np

# Captura de pantalla de la región de la ventana específica
def capture_window_region(window_position, window_size):
    screenshot = pyautogui.screenshot(region=(window_position[0], window_position[1], window_size[0], window_size[1]))
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Definir la posición y el tamaño de la ventana específica
window_position = (1550, 35)  # Cambia estas coordenadas según la ubicación de la ventana
window_size = (190, 900)      # Cambia el tamaño según el tamaño de la ventana

while True:
    # Capturar la región de la ventana
    window_image = capture_window_region(window_position, window_size)

    # Mostrar la captura de pantalla en una ventana emergente
    cv2.imshow('Ventana Específica', window_image)

    # Esperar 1 segundo y detectar la tecla 'q' para salir del bucle
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

# Cerrar todas las ventanas de OpenCV
cv2.destroyAllWindows()
