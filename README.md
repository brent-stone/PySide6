# PySide6
PySide6 Examples

vertical and horizontal policies.
```python
sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
MainWindow.setSizePolicy(sizePolicy)
```
![Policies](https://github.com/brent-stone/PySide6/images/Horizontal_Vertical_Policies.PNG?raw=true)