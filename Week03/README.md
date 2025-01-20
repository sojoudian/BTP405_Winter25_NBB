### How to create a Virual Environemtn

#### For mac users
```bash
python3 -m venv env && source env/bin/activate
```

#### For Windows users
```bash
python3 -m venv env && source env/Scripts/activate
```

#### Intall mypy
After the virtual environment activated:
```bash
pip install mypy
#mypy addres/of/the/pythonfile
mypy Week03/Lecture/05.py
```