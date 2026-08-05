import cv2


def video_tool():

    video_path = input("\nEnter video path: ")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    codec = int(cap.get(cv2.CAP_PROP_FOURCC))

    codec_name = ""

    for i in range(4):
        codec_name += chr((codec >> (8 * i)) & 0xFF)

    print("\n===== Video Information =====")
    print("FPS :", fps)
    print("Codec :", codec_name)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()