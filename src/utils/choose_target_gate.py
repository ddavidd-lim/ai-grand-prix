def find_target_gate(img, model, conf=0.15):
    """
    Finds a single gate that is the closest to the drone.
    
    Parameters
    img: the image path of what the drone sees
    model: the loaded model that's being used to find bounding boxes (e.g. YOLO('models/n6.pt'))
    conf: the confidence level threshold for valid bounding boxes

    Returns a tuple of coordinates for the top left and bottom right corner of the chosen bounding box
    """
    results = model(img, conf=conf)
    boxes = results[0].boxes
    
    if len(boxes) < 1:
        return None
    
    closest, closest_area = None, 0
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
        area = abs(x2 - x1) * abs(y2 - y1)
        if area > closest_area:
            closest, closest_area = (x1, y1, x2, y2), area
    
    return closest
    