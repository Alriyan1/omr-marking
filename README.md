
# OMR Marking System

An intelligent Optical Mark Recognition (OMR) system that automatically grades multiple-choice question papers using computer vision and image processing techniques. This system can detect marked answers, compare them with correct answers, and provide instant grading results.

## 🚀 Features

- **Automatic OMR Detection**: Identifies and processes OMR sheets from images
- **Real-time Processing**: Works with both static images and webcam feeds
- **Intelligent Grading**: Automatically compares student answers with correct answers
- **Visual Feedback**: Shows correct/incorrect answers with color coding
- **Score Calculation**: Provides percentage-based scoring
- **Multiple Formats**: Supports various image formats (JPG, PNG)
- **Perspective Correction**: Automatically corrects skewed or rotated images
- **Debug Visualization**: Shows processing steps for troubleshooting

## 📋 Prerequisites

- Python 3.7+
- OpenCV 4.5+
- NumPy
- Webcam (optional, for live processing)
- 2GB+ RAM recommended

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd OMR_Marking
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install opencv-python numpy
   ```

3. **Ensure you have the required files:**
   - `main.py` - Main application file
   - `utils.py` - Utility functions
   - Sample OMR images (1.jpg, 2.jpg, 3.jpg, etc.)

## 🚀 Usage

### Basic Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Configure parameters** in `main.py`:
   ```python
   path = '1.jpg'           # Image file path
   wImg = 700               # Image width
   hImg = 700               # Image height
   Question = 5             # Number of questions
   Choice = 5               # Number of choices per question
   ans = [1,2,0,1,4]       # Correct answers (0-indexed)
   webcamfeed = False       # Use webcam (True) or image file (False)
   ```

3. **Press 's' key** to stop the application

### Configuration Options

#### Image Processing
- **Image Size**: Adjust `wImg` and `hImg` for different paper sizes
- **Question Count**: Set `Question` to match your OMR sheet
- **Choice Count**: Set `Choice` for multiple choice options
- **Answer Key**: Update `ans` array with correct answers

#### Webcam Mode
- Set `webcamfeed = True` for live processing
- Adjust webcam settings in the code if needed

## 🏗️ Project Structure

```
OMR_Marking/
├── main.py                 # Main application file
├── utils.py                # Utility functions
├── 1.jpg                  # Sample OMR sheet 1
├── 2.jpg                  # Sample OMR sheet 2
├── 3.jpg                  # Sample OMR sheet 3
├── MCQPaper.jpg           # Sample MCQ paper
├── FinalResult.jpg        # Sample result
└── README.md              # This file
```

## 🔧 Technical Details

### Processing Pipeline

1. **Image Preprocessing**
   - Image resizing to standard dimensions
   - Grayscale conversion
   - Gaussian blur for noise reduction
   - Canny edge detection

2. **Contour Detection**
   - External contour identification
   - Rectangle detection for OMR boundaries
   - Corner point extraction

3. **Perspective Transformation**
   - Homography matrix calculation
   - Image warping for alignment
   - Grade section isolation

4. **Answer Detection**
   - Grid-based answer box splitting
   - Pixel counting for mark detection
   - Threshold-based answer validation

5. **Grading & Visualization**
   - Answer comparison with correct key
   - Score calculation
   - Result overlay on original image

### Key Functions

#### `rectContour(contours)`
- Filters contours to find rectangular shapes
- Sorts by area to identify main OMR and grade sections

#### `getCornerPoints(cont)`
- Extracts corner points from contours
- Uses polygon approximation for accuracy

#### `reorder(myPoints)`
- Reorders corner points for consistent processing
- Ensures proper perspective transformation

#### `splitBoxes(img)`
- Divides thresholded image into answer grids
- Creates 5x5 matrix for question-answer mapping

#### `showAnswer(img, myIndex, grading, ans, questions, choices)`
- Visualizes grading results
- Shows correct/incorrect answers with colors

## 📊 OMR Sheet Requirements

### Format Specifications
- **Grid Layout**: 5x5 matrix (5 questions × 5 choices)
- **Marking**: Darkened circles or filled bubbles
- **Paper**: White background with clear boundaries
- **Contrast**: High contrast between marks and background

### Answer Encoding
- **Indexing**: 0-based indexing (0=A, 1=B, 2=C, 3=D, 4=E)
- **Format**: Python list `[1,2,0,1,4]`
- **Example**: `[1,2,0,1,4]` means B, C, A, B, E

## 🎯 Use Cases

### Educational Institutions
- **Exam Grading**: Quick assessment of multiple-choice tests
- **Quiz Evaluation**: Instant feedback for classroom activities
- **Practice Tests**: Automated scoring for practice materials

### Business Applications
- **Survey Processing**: Customer feedback form analysis
- **Voting Systems**: Ballot counting and verification
- **Quality Control**: Inspection checklist processing

### Research & Development
- **Data Collection**: Research survey processing
- **A/B Testing**: Response analysis and comparison
- **Market Research**: Customer preference evaluation

## 🐛 Troubleshooting

### Common Issues

1. **No Contours Detected**
   - Check image quality and contrast
   - Ensure proper lighting conditions
   - Verify image format compatibility

2. **Incorrect Answer Detection**
   - Adjust threshold values in the code
   - Check mark darkness and consistency
   - Verify grid alignment

3. **Perspective Issues**
   - Ensure camera is perpendicular to paper
   - Check for paper wrinkles or folds
   - Adjust image preprocessing parameters

### Performance Tips

- **Image Quality**: Use high-resolution, well-lit images
- **Marking**: Ensure dark, consistent marks
- **Paper Condition**: Avoid creases and shadows
- **Camera Angle**: Maintain perpendicular alignment

## 🔧 Customization

### Adding More Questions
```python
Question = 10  # Increase question count
Choice = 4     # Adjust choice count
ans = [1,2,0,1,4,3,2,1,0,2]  # Extend answer key
```

### Different Grid Sizes
```python
# Modify splitBoxes function for custom grid
def splitBoxes(img, rows, cols):
    rows = np.vsplit(img, rows)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, cols)
        for box in cols:
            boxes.append(box)
    return boxes
```

### Custom Threshold Values
```python
# Adjust in main.py
imgThresh = cv2.threshold(imgWrapGray, 150, 255, cv2.THRESH_BINARY_INV)[1]
```

## 🌟 Advanced Features

### Real-time Processing
- Webcam integration for live OMR processing
- Instant feedback and grading
- Batch processing capabilities

### Multiple Answer Types
- Single choice questions
- Multiple choice questions
- True/False questions
- Numerical responses

### Export Functionality
- Save graded results as images
- Export scores to CSV/Excel
- Generate detailed reports

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- **OpenCV** for computer vision capabilities
- **NumPy** for numerical operations
- **Computer Vision Community** for algorithms and techniques

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the code comments for implementation details

## 🔮 Future Enhancements

- [ ] Machine learning-based answer detection
- [ ] Support for different OMR formats
- [ ] Cloud-based processing
- [ ] Mobile application
- [ ] API endpoint for integration
- [ ] Advanced analytics and reporting
- [ ] Multi-language support
- [ ] Batch processing interface

---

**Happy OMR Processing! 📝✅**
