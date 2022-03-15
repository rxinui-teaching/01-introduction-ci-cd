# IUT: Chaine CI/CD

@author Rxinui

## Atelier 0 : Hello World of CI/CD

### Pré-requis

Les technologies qui seront utilisées lors de cet atelier nécessitent :

Une installation de :
- [git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org/downloads/)

Un compte utilisateur sur :
- [Github (intégration)](https://github.com/login)
- [Deta.sh (déploiement)](https://web.deta.sh/)
### Exercice

Dans ce tutoriel, on va mettre en place une chaîne CI/CD simplistique avec pour seul intéret **la découverte des outils** et la mise en oeuvre des étapes CI/CD classique.

Une chaîne de CI/CD classique possède à minima deux étapes :
1. Build : la construction / compilation / packaging du code
2. Deploy : la publication du code au sein d'un environment 
#### GitHub Action : responsable de la chaine CI/CD

GitHub propose la création d'une chaine CI/CD avec sa solution maison nommée **GitHub Action**. 
L'avantage de **GitHub Action** est qu'il s'applique sur les codes sources hébergés sur GitHub.
