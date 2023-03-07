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

Dans le cas de Docker, un schéma classique d'une chaine CI consiste à :

1. **build**: créer une image Docker à partir d'un fichier de description (Dockerfile)
2. **test**: tester le fonctionnement de l'image Docker 
3. **upload**: déposer l'image Docker dans un repository (Docker Hub dans notre cas) afin de le mettre à disposition de l'équipe 

Ces étapes sont exécutées au sein d'un environnement virtuel, appellé **job**, basé sur un _GitHub Runner_ (comprendre, un serveur éligible à GitHub Actions, fournit par github.com). Les successions des étapes automatisées forment une chaine logique et successive (d'où le terme _chaine d'intégration continue_). Étant donné qu'on parle d'automatisation, **il est nécessaire de définir l'évènement déclencheur de cette chaîne**. Par exemple :

- Évènement temporel: à une date précise ou périodique (tous les dimanches à 09:00)
- Évènement utilisateur: à chaque commit effectué sous le serveur git
- Autres évènements: un état final d'une autre chaine CI (dépendance entre chaines CI)

Le choix d'évènement est d'autant crucial que variable. Il dépend du besoin, de la méthodologie de travail voire de l'architecture et le coût d'un projet.

Pour synthétiser, il est important de définir dans l'ordre suivant:
1. Un **évènement déclencheur**
2. Un ou plusieurs **jobs**
3. Une ou plusieurs **étapes** qui seront exécutées au sein d'un **job**


### GitHub Action : responsable de la chaine CI/CD

GitHub propose la création d'une chaine CI/CD avec sa solution maison nommée **GitHub Action**.
L'avantage de **GitHub Action** est qu'il s'applique sur les codes sources hébergés sur GitHub et offre au développeurs des modules de CI/CD appelées **Actions** disponible sur le [GitHub marketplace](https://github.com/marketplace?type=actions).

À la racine du projet, au sein d'un repo GitHub, un dossier `.github/workflows` doit être déclaré. Il contiendra la définition des chaînes CI/CD appelées **workflows**.
Chaque workflow correspond à un fichier YAML. Dans cet atelier, le fichier `.github/workflows/main.yml` représente un exemple de workflow appelé _main_. Veuillez vous en servir comme modèle afin de construire votre propre workflow dans votre propre repository GitHub.

GitHub Action utilise la syntaxe YAML (similaire au JSON) et suit les [propriétées énoncées dans la documentation officielle](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).

Dans cet atelier, on épargnera plusieurs concepts et termes de GitHub Action. Je vous incite donc à lire le [guide officiel](https://docs.github.com/en/actions/learn-github-actions).

1. **TODO**: déclarer votre premier workflow appelé `docker.yaml`. Ajouter ce workflow a votre repository puis pousser vos changements sur github. Vérifier que votre workflow est présent, dans l'onglet _Actions_, sur le panel situé à votre gauche.

### Une chaine CI sur un Dockerfile

Cette chaîne va se baser sur le [schéma classique](#continuous-integration) décrit au-dessus.

Tout d'abord, nous définissons l'évènement déclencheur de notre chaine CI. Il faut s'interroger sur **quand** souhaitons-nous que notre chaine s'exécute.

2. **TODO**: Définir (git) `push` comme évènement déclencheur de notre chaine.

Á présent, on peut s'occuper de la définition des étapes à exécuter. Pour se faire, un **job** doit être défini auquel un ensemble d'étapes seront attribués sous sa sections `steps: ` qui contiendra une liste d'actions à réaliser. Ces actions représentent soit des commandes Shell/Unix, soit des appels à modules appelés `actions` qui se trouvent sur le [GitHub Marketplace](https://github.com/marketplace?category=&query=&type=actions&verification=). 

3. **TODO**: Définir le premier **job** nommé `build-test-upload`. Configurer ce job pour qu'il tourne sous Linux.

Ce **job** devra contenir les étapes qui vont permettre de construire l'image Docker à partir du Dockerfile, tester l'image créée et téléverser cette image au sein d'un repository Docker. 

4. **TODO**: Dans la section `steps: `, écrire la première étape qui va build l'image Docker. _NOTE: on se contentera ici d'exécuter la commande Shell qui permet la construction d'une image Docker._

Avant de continuer sur la définition d'étapes, testons le bon fonctionnement de notre chaine CI. Ajouter les nouveaux changements apportés au projet à l'aide d'un `git add .` depuis la racine du projet. Créer un nouveau commit avec un message explicit en faisant `git commit -am "<message du commit>"`. 

5. **TODO**: Déclencher pour la première fois votre chaine CI en utilisant l'évènement déclencheur.

Vérifier que sur github.com dans l'onglet _Actions_ de votre projet, que votre chaine CI est en cours d'exécution ou terminée. Si succès, veuillez continuer l'atelier. Sinon, debugger les éventuelles erreurs (_ne pas hésiter à demander de l'aide sur le serveur discord_).

6. **TODO**: Rajouter une nouvelle étape, qui servira à tester l'image construire en démarrant un _container_ docker basé sur cette image. Puis, vérifier que le serveur nginx soit bien accessible via son protocole HTTP(S).

7. **TODO**: Enregistrer les changements apportés à l'aide des commandes `git` vues précédemments puis déclencher de nouveau votre chaine CI. Vérifier sur github.com que tout soit en ordre.

Si échec, veuillez debugger avant de continuer.

8. **TODO**: Rajouter l´étape **upload** qui permet de déposer votre image docker au sein d'un repository docker, ici votre espace Docker Hub personnel.

9. **TODO**: Enregistrer les changements apportés à l'aide des commandes `git` vues précédemments puis déclencher de nouveau votre chaine CI. Vérifier sur github.com que tout soit en ordre.

Si toutes les étapes fonctionnent correctement, votre chaine CI est terminée. À présent, à chaque fois que votre répertoire GitHub connaitra des changements, GitHub Actions se chargera de tester la validité de votre projet en déclenchant votre chaine CI. Ainsi, si vous introduisez un bug (ou une faute de syntaxe), votre chaine CI vous remontera qu'une erreur est survenue. Cette chaine CI est donc utile car :
- Elle automatise la partie fonctionnelle qui est: build, test et upload au sein d'un repertoire public.
- Elle sert de métric / filtre contre les erreurs introduites par un développeur. Très utile lorsque le projet est maintenu par une équipe de développeurs.

### Une chaine CI sur un docker-compose

_That's all folks :)_
