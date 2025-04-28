📦 Tools

Tools  is a versatile Python library designed for media processing and geometric calculations. It provides tools for image conversion and basic operations with geometric shapes. 
Features 

    Media Conversion:  
        Convert images to JPG format.
        Extensible modules for future support of audio, video, and text processing.
         

    Geometric Calculations:  
        Calculate the area of a circle by radius.
        Calculate the area of a triangle by its three sides.
        Check if a triangle is right-angled.
        Calculate the perimeter of a rectangle.
         
     
Option 1: Install via pip (from GitHub)

You can install the library directly from the GitHub repository using pip: 
```bash
pip install git+https://github.com/MrRuzal/tools.git
```

Option 2: Clone and Install Locally 

Alternatively, you can clone the repository and install it locally:
```bash
# Step 1: Clone the repository
git clone https://github.com/MrRuzal/tools.git

# Step 2: Navigate to the project directory
cd tools

# Step 3: Install the library
pip install .
```

Option 3: Install in Editable Mode (for developers) 

If you plan to modify the library or contribute to its development, install it in editable mode: 
```bash
pip install -e .
```

### Usage 

Media Conversion 
Convert Images to JPG 

Use the convert_image_to_jpg function to convert images to the JPG format: 
```python
from converter.images.convert_image_to_jpg import convert_image_to_jpg

# Convert an image to JPG
convert_image_to_jpg('path/to/input.png', 'path/to/output.jpg')
```

Geometric Calculations 
Working with Circles 

Calculate the area of a circle using the Circle class: 
```python
from geometry.circle import Circle

# Create a circle with radius 5
circle = Circle(radius=5)

# Calculate the area of the circle
print(circle.area())  # Output: 78.53981633974483
```

Working with Triangles 

Calculate the area of a triangle and check if it's a right-angled triangle using the Triangle class: 
```python
from geometry.triangle import Triangle

# Create a triangle with sides 3, 4, and 5
triangle = Triangle(a=3, b=4, c=5)

# Calculate the area of the triangle
print(triangle.area())  # Output: 6.0

# Check if the triangle is right-angled
print(triangle.is_right_triangle())  # Output: True
```

Working with Rectangles 

Calculate the area and perimeter of a rectangle using the Rectangle class: 
```python
from geometry.rectangle import Rectangle

# Create a rectangle with width 4 and height 6
rectangle = Rectangle(width=4, height=6)

# Calculate the area of the rectangle
print(rectangle.area())  # Output: 24.0

# Calculate the perimeter of the rectangle
print(rectangle.perimeter())  # Output: 20.0
```

Requirements 

    Python 3.8 or higher.
    Dependencies:
        Pillow==9.3.0 (for image processing).
         
Install all dependencies using: 
```bash
pip install -r requirements.txt
```


### Example Workflow 

Step 1: Install the Library 
```bash
pip install git+https://github.com/MrRuzal/tools.git
```

Step 2: Use the Library
```python
from geometry.circle import Circle
from geometry.triangle import Triangle

# Circle example
circle = Circle(radius=7)
print(f"Circle Area: {circle.area()}")

# Triangle example
triangle = Triangle(a=6, b=8, c=10)
print(f"Triangle Area: {triangle.area()}")
print(f"Is Right-Angled: {triangle.is_right_triangle()}")
```