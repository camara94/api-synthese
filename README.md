# Création API REST en Python
Dans ce tuto, nous allons réaliser une API RESTFULL en qui va exploiter notre algorithme de synthèse automatique
que nous avons réalisé dans les tuto précédents.

## Installer Python
Si vous avez pas python, pouvez l'installer à travers ce [lien](https://www.python.org/downloads/).
Je vous recommande la version 3.x.x surtout.

Sous Windows, cliquez sur l'icône du menu Démarrer et tapez <code>**cmd**</code> dans la zone de recherche, puis appuyez sur <code>**Entrée**</code>.

Une fois votre ligne de commande ouverte, saisissez ces commandes :
<pre>
<code>
    python --version
    pip --version
</code>
</pre>

Si la sortie de ces commandes inclut un numéro de version, Python est installé et disponible à partir de la ligne de commande et vous pouvez passer à l'étape suivante.

## Installer flask
<pre>
<code>
    pip install flask --user
</code>
</pre>

## Créer un projet
Sous Windows, vous pouvez créer le dossier <code>**api**</code> avec ces commandes dans votre environnement de ligne de commande <code>**cmd**</code> :

<pre>
<code>
    md api
    cd api
</code>
</pre>

## Installer  flask-cors

<pre>
<code>
    pip install -U flask-cors
</code>
</pre>

Ensuite, ouvrez un éditeur de texte (tel que VSCODE ou Notepad++), créer un fichier <code>api.py</code> et entrez le code suivant :
## Importer les packages suivants
<pre>
<code>
    import flask
    from flask import request, jsonify
    from synthese import *
    from flask_cors import CORS, cross_origin
</code>
</pre>

## Créer un endpoint 
Cet endpoint, va me permettre de prendre l'URL d'un article retourner l'article et son résumé.

<pre>
<code>
@app.route('/api', methods=['GET'])
@cross_origin()
def api_url():
    # Check if an URL was provided as part of the URL.
    # If URL is provided, assign it to a variable.
    # If no URL is provided, display an error in the browser.
    if 'url' in request.args:
        url = str(request.args['url'])
        return synthese_automatique(url)
    else:
        return "Error: No id field provided. Please specify an url."
</code>
</pre>