# Pre-requisites
1. Linux
2. Python 3.6

# Installation
Install requirements in virtual environment

1. Install virtualenv
    ```
    pip install virtualenv
    ```
2. Create virtualenv
    ```
    mkdir myvenv
    cd myvenv
    virtualenv myvenv
    ```

3. Activate `myvenv` venv
    ```
    source myvenv/bin/activate
    
    or 
    
    . myvenv/bin/activate
    ```

4. Install from requirements.pip
    ```
    pip install -r requirements.pip
    ```

# Code Execution
1. Change to 'src' directory
    ```
    cd battle-ship/src/
    ``` 
2. Run the application
    ```
    python battleship.py
    ``` 

    
# Testing
1. Test battleship.py module
    ```
    cd battle-ship/src/
    pytest test.py
    ``` 
