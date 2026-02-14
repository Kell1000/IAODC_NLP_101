# Manipulation des Transformers et Exploration des LLM

## Partie 1 : Questions Théoriques

### Question 1
Expliquez en vos propres mots ce qu'est un modèle Transformer et quelle innovation majeure il apporte par rapport aux architectures précédentes (RNN, LSTM).

### Question 2
Qu'est-ce que le mécanisme d'attention (attention mechanism) ? Pourquoi est-il crucial dans l'architecture Transformer ?

### Question 3
Définissez les termes suivants :
- **Token**
- **Embedding**
- **Context window**
- **Temperature**
- **Top-k sampling**

### Question 4
Quelle est la différence entre :
- Un modèle encoder-only (comme BERT)
- Un modèle decoder-only (comme GPT)
- Un modèle encoder-decoder (comme T5)

Donnez un exemple d'usage pour chacun.

### Question 5
Expliquez le processus de pré-entraînement et de fine-tuning d'un LLM. Pourquoi ces deux étapes sont-elles importantes ?

---

## Partie 2 : Manipulation Pratique avec Hugging Face

### Exercice 1 : Chargement et utilisation d'un modèle

Écrivez un script Python qui :
1. Charge le modèle `distilbert-base-uncased-finetuned-sst-2-english`
2. Analyse le sentiment des phrases suivantes :
   - "I love this movie, it's amazing!"
   - "This product is terrible and broken."
   - "The weather is okay today."
3. Affiche les résultats avec les scores de confiance

**Bibliothèques autorisées :** transformers, torch

### Exercice 2 : Génération de texte

Créez un script qui :
1. Charge le modèle `gpt2`
2. Génère du texte à partir du prompt : "Once upon a time in a magical forest,"
3. Expérimente avec différents paramètres :
   - `temperature` : 0.7, puis 1.5
   - `max_length` : 50, puis 100
   - `top_k` : 50
4. Compare et commente les résultats obtenus avec différentes températures

### Exercice 3 : Tokenization

Écrivez un code qui :
1. Charge le tokenizer de `bert-base-uncased`
2. Tokenise la phrase : "Transformers are revolutionizing natural language processing!"
3. Affiche :
   - Les tokens
   - Les IDs des tokens
   - Le texte décodé à partir des IDs
4. Expliquez ce qui se passe avec les mots composés ou inconnus

---

## Partie 3 : Exploration et Analyse

### Exercice 4 : Comparaison de modèles

Comparez les performances de deux modèles différents sur la même tâche de question-réponse :
- `distilbert-base-cased-distilled-squad`
- `bert-large-uncased-whole-word-masking-finetuned-squad`

**Contexte :** "The Eiffel Tower is located in Paris, France. It was completed in 1889 and stands 330 meters tall."

**Questions :**
1. "Where is the Eiffel Tower located?"
2. "When was it completed?"
3. "How tall is the Eiffel Tower?"

Analysez :
- La précision des réponses
- Le temps d'inférence
- Les scores de confiance

### Exercice 5 : Prompt Engineering

Pour la tâche de génération de texte, testez différents prompts pour obtenir :
1. Un poème sur l'intelligence artificielle
2. Une explication technique du machine learning
3. Une recette de cuisine

Documentez :
- Les prompts utilisés
- Les résultats obtenus
- Les ajustements nécessaires pour améliorer la sortie

---

## Partie 4 : Mini-Projet

### Projet : Classificateur de sentiment personnalisé

Créez une petite application qui :
1. Prend en entrée un texte de l'utilisateur
2. Utilise un modèle de votre choix pour analyser le sentiment
3. Affiche le résultat de manière conviviale
4. Permet de traiter plusieurs textes successivement

**Bonus:** Ajoutez une interface simple avec Gradio ou Streamlit

---

## Ressources autorisées

- Documentation officielle de Hugging Face : https://huggingface.co/docs
- Documentation PyTorch/TensorFlow
- Vos notes de cours

**⚠️ Important :** Le plagiat de code trouvé en ligne sans compréhension est sanctionné. Vous devez être capable d'expliquer chaque ligne de votre code.
