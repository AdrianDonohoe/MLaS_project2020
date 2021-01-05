# Machine Learning and Statistics Project 2020
***
## Wind Power Modelling

This repository contains my submission for the Machine Learning and Statistics Project 2020.

The submission is a jupyter notebook which investigates the dataset and models the data, a flask web application which publishes the model and allows the user to make predictions using a html frontend.

The repository contains the following files :

1. Dockerfile. Used to build a docker image to run the flask application in a docker container.

2. A jupyter notebook, for investigation and model analysis.

3. model_server.py , a python flask application.

4. powerproduction.txt, a text file containing the dataset

5. A README (this file)

6. requirements.txt, used to build the python environment

    ```bash
    pip install -r requirements.txt
    ```
7. wind_power_weigths,wind_power.h5 . Model save files. These are loaded by the flask application.

8. static files served by the flask application, including the html frontend, which uses JavaScript/AJAX to request prediction from server.


## Linux
```bash
export FLASK_APP=model_server.py
python3 -m flask run
```

# Windows
```bash
set FLASK_APP=model_server.py
python -m flask run
```

```bash
docker build . -t mlas-model-image
docker run --name mlas-model-container -d -p 5000:5000 mlas-model-image
```

