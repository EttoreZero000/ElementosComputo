import cv2
import mediapipe as mp
import math
import time
import subprocess
import webbrowser
# Inicializar MediaPipe Hands.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Capturar video desde la cámara.
cap = cv2.VideoCapture(0)

# Tiempo de actualización de la posición de los dedos en segundos.
tiempo_actualizacion = 0.5

# Tiempo de inicio del programa.
tiempo_inicio = time.time()

# Definir el gesto para abrir YouTube.
gesto = [[True, True, False, False, False],[True,True,True,True,True],[True,False,False,False,False]]

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        # Leer frame desde la cámara.
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar el video.")
            break

        # Verificar si es hora de actualizar la posición de los dedos.
        if time.time() - tiempo_inicio >= tiempo_actualizacion:
            # Convertir el frame a RGB.
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Realizar la detección de manos.
            results = hands.process(frame_rgb)

            # Lista para almacenar los resultados de la evaluación.
            dedos_estirados = []

            # Calcular la distancia entre la palma y la punta de cada dedo.
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    palm_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                    palm_x, palm_y, palm_z = palm_landmark.x, palm_landmark.y, palm_landmark.z

                    for finger_tip in [mp_hands.HandLandmark.THUMB_TIP, 
                                       mp_hands.HandLandmark.INDEX_FINGER_TIP, 
                                       mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                                       mp_hands.HandLandmark.RING_FINGER_TIP,
                                       mp_hands.HandLandmark.PINKY_TIP]:
                        tip_landmark = hand_landmarks.landmark[finger_tip]
                        tip_x, tip_y, tip_z = tip_landmark.x, tip_landmark.y, tip_landmark.z
                        
                        # Calcular la distancia euclidiana entre la palma y la punta del dedo.
                        distance = math.sqrt((palm_x - tip_x)**2 + (palm_y - tip_y)**2 + (palm_z - tip_z)**2)

                        # Evaluar si la distancia es mayor que 0.20 y agregar True o False a la lista.
                        dedos_estirados.append(distance > 0.20)

            # Verificar si el gesto coincide con el de YouTube.
            if dedos_estirados == gesto[0]:
                # Abrir YouTube.
                webbrowser.open("https://www.youtube.com")
            # Actualizar el tiempo de inicio para el próximo ciclo de actualización.
            tiempo_inicio = time.time()

            # Dibujar los puntos de referencia de los dedos en el frame.
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Mostrar el frame con los puntos de los dedos dibujados.
            cv2.imshow('Hand Tracking', frame)

        # Salir del bucle si se presiona la tecla 'q'.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberar recursos.
cap.release()
cv2.destroyAllWindows()
