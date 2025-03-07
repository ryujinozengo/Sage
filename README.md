# Sage-Virtual-Assistant

Meet Sage, your AI-powered personal assistant. Stay organized with scheduling, reminders, and notifications. Get news, weather, and traffic updates. Enjoy personalized movie and song recommendations. Order food effortlessly. Experience a stress-free, productive day with Sage.


# Images
![Sage (1)](https://github.com/ryujinozengo/Sage-Virtual-Assistant/assets/131596281/21d852e1-35fc-4ac8-afa8-bfd7f32733be)
![Sage (2)](https://github.com/ryujinozengo/Sage-Virtual-Assistant/assets/131596281/315dd98b-7027-44f6-87eb-ceb820c9dcf5)



# High DPI
> Qt Widgets is an old technology and does not have a good support for high DPI settings, making these images look distorted when your system has DPI applied above 100%.
You can minimize this problem using a workaround by applying this code below in "main.py" just below the import of the Qt modules.
```python
# ADJUST QT FONT DPI FOR HIGHT SCALE
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96"
```

# Running
> Inside your preferred terminal run the commands below depending on your system, remembering before installing Python 3.9> and PySide6 "pip install PySide6".
> ## **Windows**:
```console
python main.py
```
> ## **MacOS and Linux**:
```console
python3 main.py
```
# Compiling
> ## **Windows**:
```console
python setup.py build
```

# Project Files And Folders
> **main.py**: application initialization file.

> **main.ui**: Qt Designer project.

> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. Use version 6 >

> **setup.py**: cx-Freeze setup to compile your application (configured for Windows).

> **themes/**: add here your themes (.qss).

> **modules/**: module for running GUI.

> **modules/app_funtions.py**: add your application's functions here.
Up
> **modules/app_settings.py**: global variables to configure user interface.

> **modules/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **modules/ui_functions.py**: add here only functions related to the user interface / GUI.

> **modules/ui_main.py**: file related to the user interface exported by Qt Designer. You can compile it manually using the command: ```pyside6-uic main.ui> ui_main.py ```.
After expoting in .py and change the line "import resources_rc" to "from. Resoucers_rc import *" to use as a module.

> **images/**: put all your images and icons here before converting to Python (resources_re.py) ```pyside6-rcc resources.qrc -o resources_rc.py```.




