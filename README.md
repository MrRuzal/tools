📦 Tools

Tools — это универсальная библиотека для работы с медиафайлами и геометрическими вычислениями.
Включает конвертацию изображений и базовые операции с геометрическими фигурами.

Установка

Установить библиотеку можно через pip:

```python
pip install git+https://github.com/MrRuzal/tools.git
```

Либо после клонирования репозитория:
```python
git clone https://github.com/MrRuzal/tools.git
cd tools
pip install .
```

Структура библиотеки

    converter/ — инструменты для конвертации медиа:

        images/ — конвертация изображений в формат JPG.

        audio/, video/, text/ — подготовленные модули для дальнейшего расширения.

    geometry/ — вычисление площадей фигур и проверка свойств:

        Площадь круга по радиусу.

        Площадь треугольника по трём сторонам.

        Проверка, является ли треугольник прямоугольным.


Примеры использования
Конвертация изображений
`
from converter.images.convert_image_to_jpg import convert_image_to_jpg

convert_image_to_jpg('path/to/input.png', 'path/to/output.jpg')
`

Работа с геометрией
`
from geometry.shapes import Circle, Triangle

# Работа с кругом
circle = Circle(radius=5)
print(circle.area())  # Выведет площадь круга

# Работа с треугольником
triangle = Triangle(3, 4, 5)
print(triangle.area())           # Выведет площадь треугольника
print(triangle.is_right_angled()) # Проверит, прямоугольный ли треугольник
`

Требования

    Python 3.8 и выше

    Pillow==9.3.0 (для работы с изображениями)

Автор: Ruzal
