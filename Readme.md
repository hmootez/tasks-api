
## Installation

Vous aurez besoin de python installé sur votre machine.


### Instructions d'installation et de configuration



Installation :

```sh
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Lancement :

```sh
uvicorn main:app --reload

```
l'application sera lancé automatiquement sur votre navigateur ou vous pouvez tapez l'url suivant:
```
 http://127.0.0.1:8000
```