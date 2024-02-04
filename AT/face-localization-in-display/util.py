import numpy as np
import matplotlib.pyplot as plt
import cv2

def show_msg(msg, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)  # White color in BGR
    font_thickness = 2
    text_position = (50, 100)  # (x, y) coordinates of the text
    
    cv2.putText(frame, msg, text_position, font, font_scale, font_color, font_thickness)

def show_arrow(direction, frame, center_y, center_x, frame_width, frame_height):
    
    arrow_size = 50
    arrow_color = (0, 255, 0)  # Cor da seta (verde)
    
    if (direction == 'left'):
        arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
        cv2.arrowedLine(arrow, (arrow_size-1, arrow_size//2), (0, arrow_size//2), arrow_color, 3)
        frame[center_y-arrow_size//2:center_y+arrow_size//2, 0:arrow_size] = arrow
        
    elif (direction == 'right'):
        arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
        cv2.arrowedLine(arrow, (0, arrow_size//2), (arrow_size-1, arrow_size//2), arrow_color, 3)
        frame[center_y-arrow_size//2:center_y+arrow_size//2, frame_width-arrow_size:frame_width] = arrow


    elif (direction == 'up'):
        arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
        cv2.arrowedLine(arrow, (arrow_size//2, arrow_size-1), (arrow_size//2, 0), arrow_color, 3)
        frame[0:arrow_size, center_x-arrow_size//2:center_x+arrow_size//2] = arrow
        
    elif (direction == 'bottom'):
        arrow = np.zeros((arrow_size, arrow_size, 3), dtype=np.uint8)
        cv2.arrowedLine(arrow, (arrow_size//2, 0), (arrow_size//2, arrow_size-1), arrow_color, 3)
        frame[frame_height-arrow_size:frame_height, center_x-arrow_size//2:center_x+arrow_size//2] = arrow
