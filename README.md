## What

This repository is useful is creating requirements.txt file for each workshop and directory.

It does following 2 things.
1. File to create folders as per workshops and talks.
2. For each talk/workshop, there exists a requirements.txt. Each of this requirement is written as talk_id_requirements.txt within each of the folders file.

### Creating requirements.txt for each of the talk and workshop

Following commands will create ```requirements``` folder. 

```
cd pycon_requirements
python src/structure.py
```

Running the previous script would have created requirements folder as well.

```
pycon_requirements
        |
        |_ data
        |_ src
        |_ requirements
```

Update one of the requirements.txt file.

Add following to requirements/workshops/Effectively_Debugging_Deep_Neural_Networks/requirements.txt
```
scikit-learn
tensorflow
keras
pandas
```

Run fetch packages for a workshop. Use fetch_requirements.py to do this.

```
python src/fetch_requirements.py
```

This command will create a lib folder in ```requirements/workshops/Effectively_Debugging_Deep_Neural_Networks```.

### Installing packages
```
pip install --find-links=requirements/workshops/Effectively_Debugging_Deep_Neural_Networks/lib/ -r requirements/workshops/Effectively_Debugging_Deep_Neural_Networks/requirements.txt
```

### Testing installation of packages

Fire up python interpreter
```
python
>>> import tensorflow
>>> import sklearn
```