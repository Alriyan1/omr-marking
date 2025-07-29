# 🚦 Traffic Sign Detection System

A real-time traffic sign detection system using computer vision and deep learning. This project can detect and classify 43 different types of traffic signs from live camera feed or images.

## 📋 Table of Contents

- [Features](#-features)
- [Supported Traffic Signs](#-supported-traffic-signs)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Information](#-model-information)
- [Dataset](#-dataset)
- [Technical Details](#-technical-details)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

## ✨ Features

- **Real-time Detection**: Live camera feed processing
- **High Accuracy**: Pre-trained deep learning model
- **43 Traffic Sign Classes**: Comprehensive coverage of common traffic signs
- **Confidence Scoring**: Probability display for predictions
- **Image Preprocessing**: Automatic grayscale conversion and histogram equalization
- **Easy to Use**: Simple Python script with minimal setup

## 🛑 Supported Traffic Signs

The system can detect 43 different traffic signs including:

### Speed Limits
- Speed limit (20km/h, 30km/h, 50km/h, 60km/h, 70km/h, 80km/h, 100km/h, 120km/h)
- End of speed limit (80km/h)
- End of all speed and passing limits

### Prohibitions
- No passing
- No passing for vehicles over 3.5 metric tons
- No vehicles
- Vehicles over 3.5 metric tons prohibited
- No entry
- End of no passing
- End of no passing by vehicles over 3.5 metric tons

### Priority & Right of Way
- Right-of-way at the next intersection
- Priority road
- Yield
- Stop

### Warnings
- General caution
- Dangerous curve to the left/right
- Double curve
- Bumpy road
- Slippery road
- Road narrows on the right
- Road work
- Traffic signals
- Pedestrians
- Children crossing
- Bicycles crossing
- Beware of ice/snow
- Wild animals crossing

### Directional
- Turn right/left ahead
- Ahead only
- Go straight or right/left
- Keep right/left
- Roundabout mandatory

## 📁 Project Structure

```
trafficsigndetection/
├── trafficSign.py          # Main application script
├── main.ipynb              # Jupyter notebook for training/analysis
├── model_trained.p         # Pre-trained model (pickle format)
├── labels.csv              # Traffic sign class labels
├── myData/                 # Training dataset
│   ├── 0/                  # Speed limit 20km/h images
│   ├── 1/                  # Speed limit 30km/h images
│   ├── 2/                  # Speed limit 50km/h images
│   └── ...                 # (43 folders total)
└── README.md               # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.7+
- Webcam (for real-time detection)
- Sufficient lighting for better detection accuracy

### Required Packages

```bash
pip install opencv-python
pip install numpy
pip install tensorflow
pip install keras
```

### Quick Setup

1. **Clone or download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd trafficsigndetection
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Create requirements.txt if not present)*

## 🎯 Usage

### Real-time Detection

Run the main script to start real-time traffic sign detection:

```bash
python trafficSign.py
```

**Controls:**
- **ESC key**: Exit the application
- **Webcam**: Point at traffic signs for detection

### Expected Output

The application will display:
- **Original Image**: Live camera feed with detection overlay
- **Class**: Detected traffic sign class (number + name)
- **Probability**: Confidence percentage (only shown if > 90%)

### Customization

You can modify these parameters in `trafficSign.py`:

```python
frameWidth = 640      # Camera resolution width
frameHeight = 480     # Camera resolution height
brightness = 180      # Camera brightness
threshold = 0.90      # Confidence threshold (90%)
```

## 🤖 Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 32x32 grayscale images
- **Output**: 43-class classification
- **Format**: Pickle (.p) file
- **Training**: Custom dataset with 43 traffic sign classes

### Model Performance

- **Accuracy**: High accuracy on trained dataset
- **Speed**: Real-time processing capable
- **Robustness**: Handles various lighting conditions

## 📊 Dataset

The training dataset (`myData/`) contains:
- **43 folders** (one per traffic sign class)
- **Thousands of images** per class
- **Varied conditions**: Different lighting, angles, backgrounds
- **Format**: PNG images, 32x32 pixels

### Dataset Statistics

- **Total Classes**: 43
- **Total Images**: ~50,000+ images
- **Image Size**: 32x32 pixels
- **Format**: Grayscale

## 🔧 Technical Details

### Image Preprocessing Pipeline

1. **Resize**: Convert to 32x32 pixels
2. **Grayscale**: Convert to single channel
3. **Histogram Equalization**: Enhance contrast
4. **Normalization**: Scale pixel values to [0,1]
5. **Reshape**: Prepare for model input (1,32,32,1)

### Model Architecture

```python
# Simplified architecture overview
Input: (32, 32, 1) grayscale image
↓
Convolutional layers
↓
Pooling layers
↓
Dense layers
↓
Output: 43-class probabilities
```

### Key Functions

- `preprocess(img)`: Complete image preprocessing
- `getClassName(classNo)`: Convert class number to readable name
- `grayscale(img)`: Convert to grayscale
- `equalize(img)`: Apply histogram equalization

## 🛠️ Troubleshooting

### Common Issues

**1. Camera not working**
```bash
# Check camera permissions
# Ensure no other application is using the camera
```

**2. Model loading error**
```bash
# Verify model_trained.p exists in the directory
# Check file permissions
```

**3. Low detection accuracy**
- Ensure good lighting conditions
- Hold traffic sign images clearly in camera view
- Check if camera is focused properly

**4. Import errors**
```bash
# Install missing packages
pip install opencv-python numpy tensorflow keras
```

**5. Performance issues**
- Reduce camera resolution in the script
- Close other applications using camera
- Ensure sufficient system resources

### Performance Tips

- **Good Lighting**: Ensure adequate lighting for better detection
- **Stable Camera**: Keep camera steady for accurate results
- **Clear Signs**: Use clear, unobstructed traffic sign images
- **Optimal Distance**: Maintain appropriate distance from camera

## 🤝 Contributing

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### Areas for Improvement

- [ ] Add support for more traffic sign types
- [ ] Implement video file processing
- [ ] Add model retraining capabilities
- [ ] Improve detection accuracy
- [ ] Add GUI interface
- [ ] Support for multiple camera inputs

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Traffic sign dataset contributors
- OpenCV community
- TensorFlow/Keras developers
- Computer vision research community

---

## 🎮 Interactive Demo

Try these traffic signs with your camera:

1. **Speed Limit Signs**: Hold up printed speed limit signs
2. **Stop Signs**: Use a red octagonal stop sign
3. **Yield Signs**: Show triangular yield signs
4. **Warning Signs**: Display various warning symbols

**Pro Tip**: Print traffic sign images and hold them in front of the camera for testing!

---

*Made with ❤️ for computer vision enthusiasts* 
