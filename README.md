# Machine Learning and Statistics Project 2020

## Wind Power Modelling

This repository contains my submission for the Machine Learning and Statistics Project 2020.

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

