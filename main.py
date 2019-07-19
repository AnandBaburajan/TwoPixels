# USAGE
# python main.py -i vid.mp4 -o result.mp4

from LSBSteg import*
import numpy as np
import argparse
import cv2

def vid_test():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Input video file")
    ap.add_argument("-o", "--output", required=True, help="Output video file")
    args = vars(ap.parse_args())

    cap = cv2.VideoCapture(args["input"])

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(args["output"],fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

                cap.release()
                out.release()
                cv2.destroyAllWindows()

def main():
    steg = LSBSteg(cv2.imread("img.png"))
    img_encoded = steg.encode_text("11_byte_ID_")
    cv2.imwrite("en_img.png", img_encoded)

    im = cv2.imread("img.png")
    steg = LSBSteg(im)
    print("Video ID:",steg.decode_text())

if __name__=="__main__":
    main()
