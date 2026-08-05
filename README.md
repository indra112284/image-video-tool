# Image & Video Tool using OpenCV

## Project Overview

The Image & Video Tool is a Python application developed using the OpenCV library. It allows users to analyze images and videos, display important information, perform image format conversions, perform color space conversions, and retrieve video properties through a simple menu-driven interface.

This project was developed as part of learning Computer Vision and OpenCV fundamentals.

---

## Features

### Image Processing

- Accepts an image path as input.
- Displays the selected image.
- Prints:
  - Image Resolution (Width × Height)
  - Image Format (JPEG, PNG, BMP, TIFF)
  - Aspect Ratio
  - Image Color Space (BGR)
- Supports Image Format Conversion:
  - JPEG
  - PNG
  - BMP
- Supports Color Space Conversion:
  - BGR to RGB
  - BGR to HSV
  - BGR to Grayscale
- Saves converted images in the **output** folder.

---

### Video Processing

- Accepts a video path as input.
- Displays the video.
- Prints:
  - Frames Per Second (FPS)
  - Video Codec Information

---

## Project Structure

```text
image_video_tool/
│
├── image_data/
│   └── sample.jpg
│
├── video_data/
│   └── sample.mp4
│
├── output/
│
├── image_tool.py
├── video_tool.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- OpenCV
- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/image-video-tool.git
```

Go to the project directory:

```bash
cd image-video-tool
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## How to Run

Run the application using:

```bash
python main.py
```

Select one of the options from the menu:

1. Image Tool
2. Video Tool
3. Exit

---

## Sample Image Path

```text
image_data/sample.jpg
```

## Sample Video Path

```text
video_data/sample.mp4
```

---

## Concepts Covered

- Digital Images
- Image Resolution
- Image Formats
- Aspect Ratio
- Color Spaces (BGR, RGB, HSV, Grayscale)
- Image Format Conversion
- Color Space Conversion
- Video Processing
- FPS
- Video Codec Information
- OpenCV Fundamentals

---

## Future Enhancements

- Add image resizing.
- Add image rotation.
- Display video resolution.
- Display video duration.
- Capture video frames.
- Save image and video information to a text file.

---

## Author

Developed as part of Computer Vision & OpenCV Fundamentals training using Python and OpenCV.