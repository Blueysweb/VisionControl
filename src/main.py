from camera import open_camera
from hand_tracker import HandTracker

def main():
    hand_tracker = HandTracker()
    open_camera(hand_tracker)
    
if __name__ == "__main__":
    main()