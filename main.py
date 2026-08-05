from image_tool import image_tool
from video_tool import video_tool


def main():

    while True:

        print("\n========== Image & Video Tool ==========")

        print("1. Image Tool")
        print("2. Video Tool")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            image_tool()

        elif choice == "2":
            video_tool()

        elif choice == "3":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()