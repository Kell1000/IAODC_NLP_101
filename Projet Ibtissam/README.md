# Système d'Extraction de Texte PDF et Correction Grammaticale

## Table des matières
1. [Aperçu](#aperçu)
2. [Fonctionnalités principales](#fonctionnalités-principales)
3. [Architecture du système](#architecture-du-système)
4. [Technologies utilisées](#technologies-utilisées)
5. [Structure du projet](#structure-du-projet)
6. [Installation](#installation)
7. [Utilisation](#utilisation)
8. [Exemple de workflow](#exemple-de-workflow)
9. [Considérations de conception](#considérations-de-conception)
10. [Améliorations futures](#améliorations-futures)
11. [Auteur](#auteur)
12. [Licence](#licence)

---

## Aperçu
Ce projet implémente un pipeline complet de traitement automatique du langage naturel (NLP) qui extrait le texte à partir de documents PDF, le prétraite et applique une correction grammaticale automatique à l'aide d'un modèle de type transformer séquence-à-séquence.

Le système inclut également une interface interactive permettant la correction de texte en temps réel. Il est adapté au nettoyage de documents, à la normalisation linguistique et au traitement de grands volumes de texte.

---

## Fonctionnalités principales
- Extraction automatique de texte à partir de documents PDF multi-pages
- Prétraitement et segmentation des textes longs
- Correction grammaticale via un modèle préentraîné
- Reconstruction de documents complets corrigés
- Interface interactive pour la saisie utilisateur en temps réel
- Architecture modulaire et extensible

---

## Architecture du système

### 1. Traitement des documents
- Chargement et traitement de documents PDF
- Extraction du contenu textuel brut
- Prise en charge des documents multi-pages

### 2. Prétraitement du texte
- Découpage du texte en segments compatibles avec le modèle
- Normalisation et nettoyage du contenu
- Préparation des entrées pour l'inférence

### 3. Modèle de correction grammaticale
- Architecture transformer séquence-à-séquence
- Génération du texte corrigé avec décodage par beam search
- Agrégation des segments corrigés en documents complets

### 4. Interface utilisateur
- Interface interactive pour test et démonstration
- Saisie de texte par l'utilisateur
- Affichage du texte corrigé en temps réel

---

## Technologies utilisées

### Traitement du langage naturel
- Transformers
- Sentence Transformers
- PyTorch

### Traitement de documents
- PyPDF2

### Traitement vectoriel et données
- FAISS

### Interface applicative
- Gradio

### Environnement de développement
- Python 3
- Jupyter Notebook

---

## Structure du projet
project/
│
├── Projet_ibtissam.ipynb # Notebook principal
├── data/ # Jeux de données (PDF et TXT)
├── models/ # Modèles sauvegardés
└── README.md # Documentation du projet

---

## Installation

### 1. Cloner le dépôt
```bash
git clone <url-du-repository>
cd <dossier-du-projet>

---

## Installation

### 1. Cloner le dépôt
```bash
git clone <url-du-repository>
cd <dossier-du-projet>

2. Installer les dépendances

pip install PyPDF2 faiss-cpu sentence-transformers transformers torch gradio





