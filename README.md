### What

This repository is useful is creating requirements.txt file for each workshop and directory.

It does following stuff.
1. File to create folders as per workshops and talks.
2. For each talk/workshop, there exists a requirements.txt.
3. Using ```src/fetch_requirements.py```, we can download packages as well deps locally. It uses ```pip download``` for it.
4. This can further be used to installed locally downloaded packages using ```pip install --find-links```.

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

Update one of the requirements.txt file. Let's take "Effectively_Debugging_Deep_Neural_Networks" as
an example.

Add following to ```requirements/workshops/Effectively_Debugging_Deep_Neural_Networks/requirements.txt```
```
scikit-learn
tensorflow
keras
pandas
```

Run following command to fetch packages for workshop. fetch_requirements.py should be able to do this for you.

```
python src/fetch_requirements.py
```

This command will create a lib folder in ```requirements/workshops/Effectively_Debugging_Deep_Neural_Networks```.

### Installing packages
```
pip install --find-links=requirements/workshops/Effectively_Debugging_Deep_Neural_Networks/lib/ -r requirements/workshops/Effectively_Debugging_Deep_Neural_Networks/requirements.txt
```

### Testing installation of packages

Fire up python interpreter to test whether packages have been installed or not.
```
➜  pycon_requirements git:(master) ✗ python
Python 2.7.13 (default, Apr  4 2017, 08:46:44)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow
>>> import tensorflow
>>> import sklearn
```

Since we're able to successfully import ```tensorflow```, we can be sure that we've 
correctly installed the package.

## TODO
- A setup script which creates a ```virtualenv``` and then test package imports.