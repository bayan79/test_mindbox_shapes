## Package for calculating shapes area
For now supports followed shapes:
- circle
- triangle

## install
```bash
pip install dist/shape_area-0.1.0-py3-none-any.whl
```

## test
Before running tests you must install the package.
```bash
python -m unittest discover tests
```

## basic usage
```python
from shape_area import Circle

print(Circle(10).calc_square())
>> 314.1592653589793
```