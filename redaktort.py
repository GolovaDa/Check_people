from detector import detect_people
import cv2



image=r"C:\Users\danil\people_counter_learning\examples\photo_2026-11-20_22-27-30.jpg"

image1=cv2.imread(image)
if image1 is None:
    print("Нету фото")
else:
    boxes=detect_people(image1)
    cv2.putText(image1, f"Количество людей: {len(boxes)}",(70,100),
    cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,0),2)
    for box in boxes:
        x1, y1, x2, y2 = box
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        cv2.rectangle(image1,(x1,y1),(x2,y2),(0,255,0),10)
    cv2.imshow("Result", image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    