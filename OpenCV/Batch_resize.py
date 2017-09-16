import cv2
import glob

images = glob.glob("*.jpg")  # search for anything with the passed string

for image in images:

    img = cv2.imread(image,0)

    rezize_images = cv2.resize(img,(100,100)) # resize all images to 100 by 100

    cv2.imshow("resize",rezize_images)

    cv2.waitKey(2000)

    cv2.destroyAllWindows()

    cv2.imwrite("all_images_rezized"+image,rezize_images)
