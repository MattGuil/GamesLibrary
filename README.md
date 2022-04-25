# Démarrage backend

## Creation de l'environnement virtuel python (1 seule fois)
```sh
conda create --name=matt1 python
conda activate matt1
pip install flask
pip install flask_cors
```

## Démarrage (start.bash)
```sh
#!/bin/bash
source /opt/miniconda3/bin/activate matt1
export FLASK_APP=main
export FLASK_ENV=development
nohup flask run --host=0.0.0.0 > main.log 2>&1 &
```

> ## Autres scripts (pour linux)
> - *stop.bash* (arrête le serveur)
> - *status.bash* (montre les processus du serveur)
> - *log.bash* (montre le contenu de mail.log)
