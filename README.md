# IUT: Chaine CI/CD

@author Rxinui

## Atelier 0 : Hello World of CI/CD

### Pré-requis

Les technologies qui seront utilisées lors de cet atelier nécessitent :

Une installation de :

- [git](https://git-scm.com/downloads)

Un compte utilisateur sur :

- [Github (intégration)](https://github.com/login)
- [Docker Hub (repository)](https://hub.docker.com/)

### Introduction

Dans ce tutoriel, on va mettre en place **une chaîne CI/CD** en se basant sur l'atelier Docker de Sébastien Josset. Dans un premier temps, on s'intéressera à la partie intégration continue (CI) puis à la partie déploiment continu (CD).

#### Continuous Integration

Dans le cas de Docker, un schéma classique d'une chaine CI est :

1. **build**: créer une image Docker à partir d'un fichier de description (Dockerfile)
2. **test**: assurer que l'image Docker générée est fonctionnelle
3. **upload**: déposer l'image Docker dans un repository (Docker Hub dans notre cas) afin de le mettre à disposition de l'équipe 

Ces étapes, appellées **jobs**, doivent constituer une succession d'étapes d'intégration automatisées qui forme une chaine logique et successive (d'où le terme _chaine d'intégration continue_). Étant donnée qu'on parle d'automatisation, **il est nécessaire de définir l'évènement déclencheur de cette chaîne**. Par exemple :

- Évènement temporel: à une date précise ou périodique (tous les dimanches à 09:00)
- Évènement utilisateur: à chaque commit effectué sous le serveur git
- Autres évènements: un état final d'une autre chaine CI (dépendance entre chaines CI)

Le choix d'évènement est d'autant crucial que variable. Il dépend du besoin, de la méthodologie de travail voire de l'architecture et le coût d'un projet.

### GitHub Action : responsable de la chaine CI/CD

GitHub propose la création d'une chaine CI/CD avec sa solution maison nommée **GitHub Action**.
L'avantage de **GitHub Action** est qu'il s'applique sur les codes sources hébergés sur GitHub et offre au développeurs des modules de CI/CD appelées **Actions** disponible sur le [GitHub marketplace](https://github.com/marketplace?type=actions).

À la racine du projet, au sein d'un repo GitHub, un dossier `.github/workflows` doit être déclaré. Il contiendra la définition des chaînes CI/CD appelées **workflows**.
Chaque workflow correspond à un fichier YAML. Dans cet atelier, le fichier `.github/workflows/main.yml` représente un exemple de workflow appelé _main_. Veuillez vous en servir comme modèle afin de construire votre propre workflow.

GitHub Action utilise la syntaxe YAML (similaire au JSON) et suit les [propriétées énoncées dans la documentation officielle](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).

Dans cet atelier, on épargnera plusieurs concepts et termes de GitHub Action. Je vous incite donc à lire le [guide officiel](https://docs.github.com/en/actions/learn-github-actions).

1. **TOD0**: déclarer votre premier workflow appelé `docker.yaml`. Ajouter ce workflow a votre repository puis pousser vos changements sur github. Vérifier que votre workflow est présent, dans l'onglet _Actions_, sur le panel situé à votre gauche.

#### Code source

Le code source du projet se trouve dans le dossier `atelier`. On y retrouve :

- un fichier statique `atelier/index.html` qui affiche un simple `Hello World` dans une balise `<h1>`.
- un fichier de test `atelier/test.sh` qui vérifie que le contenue de la balise `<h1>` soit égale à la valeur stockée dans la variable shell `expected_result`.

Les objectifs de cet atelier sont :

- A. Construire une chaine CI/CD qui permet de build, tester et déployer.
- B. Mettre en avant l'exécution des étapes **tester** et **déployer**.
- C. Re-déclencher la chaine CI/CD à chaque nouveauté.


_That's all folks :)_
