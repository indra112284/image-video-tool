import cv2
import os


def image_tool():

    # Get image path
    image_path = input("\nEnter image path: ").strip()

    # Check file exists
    if not os.path.exists(image_path):
        print("Error: File does not exist!")
        return

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read image!")
        return

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
    # Output Folder
    # -----------------------------
    os.makedirs("output", exist_ok=True)

    # -----------------------------
    # Format Conversion
    # -----------------------------
    print("\nConvert Image Format")
    print("1. JPEG")
    print("2. PNG")
    print("3. BMP")
    print("4. Skip")

    choice = input("Enter choice: ")

    if choice == "1":

        cv2.imwrite("output/converted.jpg", image)
        print("JPEG Saved Successfully")

    elif choice == "2":

        cv2.imwrite("output/converted.png", image)
        print("PNG Saved Successfully")

    elif choice == "3":

        cv2.imwrite("output/converted.bmp", image)
        print("BMP Saved Successfully")

    else:

        print("Format conversion skipped.")

    # -----------------------------
    # Color Conversion
    # -----------------------------
    print("\nColor Space Conversion")
    print("1. RGB")
    print("2. HSV")
    print("3. Grayscale")
    print("4. Skip")

    color_choice = input("Enter choice: ")

    display_image = image.copy()
    window_name = "Original Image"

    if color_choice == "1":

        display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        cv2.imwrite("output/rgb_image.jpg", display_image)

        window_name = "RGB Image"

        print("RGB Image Saved Successfully")

    elif color_choice == "2":

        display_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        cv2.imwrite("output/hsv_image.jpg", display_image)

        window_name = "HSV Image"

        print("HSV Image Saved Successfully")

    elif color_choice == "3":

        display_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("output/gray_image.jpg", display_image)

        window_name = "Grayscale Image"

        print("Grayscale Image Saved Successfully")

    else:

        print("Color conversion skipped.")

    # -----------------------------
    # Resize only for display
    # -----------------------------
    h, w = display_image.shape[:2]

    if w > 1000:

        scale = 1000 / w

        new_w = int(w * scale)

        new_h = int(h * scale)

        display_image = cv2.resize(display_image, (new_w, new_h))

    # -----------------------------
    # Display Image
    # -----------------------------
    cv2.imshow(window_name, display_image)

    print("\nPress any key inside the image window to continue...")

    cv2.waitKey(0)

    cv2.destroyAllWindows()