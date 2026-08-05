import cv2
import os


def image_tool():

    # Get image path
    image_path = input("\nEnter image path: ").strip()

    # Check whether file exists
    if not os.path.exists(image_path):
        print("Error: File does not exist!")
        return

    # Read image
    image = cv2.imread(image_path)

    # Check image loaded successfully
    if image is None:
        print("Error: Unable to read image!")
        return

    # -----------------------------
    # Display Original Image
    # -----------------------------
    cv2.imshow("Original Image", image)

    # -----------------------------
    # Image Information
    # -----------------------------
    height, width = image.shape[:2]

    print("\n========== Image Information ==========")
    print(f"Resolution : {width} x {height}")

    extension = os.path.splitext(image_path)[1].lower()

    formats = {
        ".jpg": "JPEG",
        ".jpeg": "JPEG",
        ".png": "PNG",
        ".bmp": "BMP",
        ".tiff": "TIFF"
    }

    print("Image Format :", formats.get(extension, "Unknown"))

    aspect_ratio = width / height
    print(f"Aspect Ratio : {aspect_ratio:.2f}")

    print("Color Space : BGR")

    # -----------------------------
    # Create Output Folder
    # -----------------------------
    os.makedirs("output", exist_ok=True)

    # -----------------------------
    # Image Format Conversion
    # -----------------------------
    print("\nConvert Image Format")
    print("1. JPEG")
    print("2. PNG")
    print("3. BMP")
    print("4. Skip")

    choice = input("Enter choice: ")

    if choice == "1":

        success = cv2.imwrite("output/converted.jpg", image)
        print("Saved :", success)

    elif choice == "2":

        success = cv2.imwrite("output/converted.png", image)
        print("Saved :", success)

    elif choice == "3":

        success = cv2.imwrite("output/converted.bmp", image)
        print("Saved :", success)

    else:

        print("Format conversion skipped.")

    # -----------------------------
    # Color Space Conversion
    # -----------------------------
    print("\nColor Space Conversion")

    print("1. RGB")
    print("2. HSV")
    print("3. Grayscale")
    print("4. Skip")

    color_choice = input("Enter choice: ")

    if color_choice == "1":

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        success = cv2.imwrite("output/rgb_image.jpg", rgb)

        print("RGB Saved :", success)

        cv2.imshow("RGB Image", rgb)

    elif color_choice == "2":

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        success = cv2.imwrite("output/hsv_image.jpg", hsv)

        print("HSV Saved :", success)

        cv2.imshow("HSV Image", hsv)

    elif color_choice == "3":

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        success = cv2.imwrite("output/gray_image.jpg", gray)

        print("Gray Saved :", success)

        cv2.imshow("Gray Image", gray)

    else:

        print("Color conversion skipped.")

    # -----------------------------
    # Close OpenCV Windows
    # -----------------------------
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    return