class GestureStabilizer:
    def __init__(self, history_length=5):
        self.history = []
        self.history_length = history_length
        
    def update(self, gesture):
        self.history.append(gesture)
        if len(self.history) > self.history_length:
            self.history.pop(0)
        if len(set(self.history)) == 1:
            return self.history[0]
        else:
            return "UNKNOWN"
        
def is_finger_extended(landmarks, tip_id, mid_id):
    tip = landmarks.landmark[tip_id]
    mid = landmarks.landmark[mid_id]
    
    if tip.y < mid.y:
        return True
    else:
        return False
    
    
def is_open_palm(landmarks):
    if is_finger_extended(landmarks, 4, 3) and \
       is_finger_extended(landmarks, 8, 6) and \
       is_finger_extended(landmarks, 12, 10) and \
       is_finger_extended(landmarks, 16, 14) and \
       is_finger_extended(landmarks, 20, 18):
        return True
    else:
        return False
    
    
def is_peace_sign(landmarks):
    if is_finger_extended(landmarks, 8, 6) and\
    is_finger_extended(landmarks, 12, 10) and \
    not is_finger_extended(landmarks, 16, 14) and \
    not is_finger_extended(landmarks, 20, 18):
        return True
    else:
        return False
    
def recognize_gesture(landmarks):
    if is_open_palm(landmarks):
        return "OPEN_PALM"
    if not is_finger_extended(landmarks, 8, 6) and \
       not is_finger_extended(landmarks, 12, 10) and \
       not is_finger_extended(landmarks, 16, 14) and \
       not is_finger_extended(landmarks, 20, 18):
       return "FIST"
    if is_peace_sign(landmarks):
        return "PEACE"
   
   
    return "UNKNOWN"