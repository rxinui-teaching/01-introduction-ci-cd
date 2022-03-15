# IUT: Chaine CI/CD

@author Rxinui

## Introduction

La chaine CI/CD est une méthode - très en vogue dans le DevOps - qui consiste à délivrer continuellement un produit de manière automatisé.
On parle de :
1. **Continuous Integration** : automatiser l'imbrication de nouvelles fonctionnalités sur celles existantes.
2. **Continuous Deployment** : automatiser la publication du produit.
3. **Continuous Delivery** (hors-tuto) : automatiser la publication du produit jusqu'à un certain niveau. Le produit ne sera jamais déployé au stade final (ie. accès par l'utilisateur) sans vérification par un humain (ie. administrateur du produit). Cette intervention est requise lorsque la publication finale demande des décisions critiques et complexes. N.B: très utilisé dans le monde de l'entreprise par rapport au *Continuous Deployment*.

Articles détaillées:
- [What is CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
- [Vidéo de Cookie connecté](https://www.youtube.com/watch?v=ws1qGuFMYlc)

## Atelier

L'atelier illustre la mise en place une chaine CI/CD simple à l'aide d'outils gratuit et utilisé dans le monde de l'entreprise / projet personnel.

### Pré-requis

Les technologies qui seront utilisées lors de cet atelier nécessite:

Une installation de :
- [git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/engine/install/#supported-platforms)

Un compte utilisateur de :
- [Github (intégration)](https://github.com/login)
- [Deta.sh (déploiement)](https://web.deta.sh/)
- [Docker Hub (build)](https://hub.docker.com/)

Une fois les pré-requis complétés, lancer la commande suivante afin de cloner le projet :

```bash
git clone 
```

### Tutoriel: Hello world 

### Debutant: Single Page Web with dynamic post

### Intermédiaire: Docker service with frontend / backend

### Entreprise: microservice