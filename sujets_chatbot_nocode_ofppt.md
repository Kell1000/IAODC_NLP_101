# Sujets de recherche & mini-projets — Chatbots No-Code/Low-Code
### Filière Développeur Chatbot — OFPPT, stagiaires 2ᵉ année

---

## Introduction

Les 17 sujets ci-dessous couvrent une progression pédagogique allant du chatbot No-Code simple (FAQ, scénarios) jusqu'à l'agent IA autonome et l'évaluation de chatbots. Chaque sujet est calibré pour être réalisé en **~2 mois** par un stagiaire débutant/intermédiaire, avec un **prototype fonctionnel** comme livrable central, et une voie d'évolution vers du code (Python/API) pour les stagiaires plus avancés.

---

## NIVEAU 1 — FONDAMENTAUX

### Sujet 1 — Chatbot d'accueil et d'orientation pour un centre de formation

1. **Problématique :** Les nouveaux stagiaires et visiteurs d'un centre de formation (type OFPPT) posent sans cesse les mêmes questions (horaires, filières, inscriptions, contacts) au personnel administratif, ce qui surcharge l'accueil.
2. **Question de recherche :** Un chatbot No-Code basé sur des intents/scénarios peut-il réduire significativement le nombre de questions répétitives adressées à l'accueil ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir et déployer un chatbot d'accueil basé sur des intents et des scénarios de dialogue.
4. **Objectifs spécifiques :**
   - Identifier les 15-20 questions les plus fréquentes (FAQ) par entretiens/observation.
   - Modéliser les intents et les flux de conversation.
   - Construire le chatbot sur une plateforme No-Code.
   - Intégrer le chatbot à un canal (site web ou WhatsApp).
   - Mesurer le taux de résolution automatique.
5. **Solution proposée :** Chatbot conversationnel à base d'intents/entités répondant aux questions fréquentes et orientant vers un humain si besoin (fallback).
6. **Plateforme recommandée :** **Voiceflow** (design visuel de scénarios, gestion des intents simple, adapté aux débutants) ou **Botpress** en alternative open-source.
7. **Technologies complémentaires :** Widget web embarqué, webhook simple, Google Sheets pour le stockage des FAQ.
8. **Architecture :** Utilisateur → Widget web/WhatsApp → Chatbot (Voiceflow) → Moteur d'intents → Base FAQ (Sheets) → Réponse ou transfert humain.
9. **Partie recherche :** Étudier les approches classiques de chatbots à base de règles/intents (NLU rule-based vs statistique), comparer 2-3 outils No-Code de ce type, identifier les limites (rigidité, absence de compréhension du langage libre).
10. **Expérimentation :** Tester le chatbot avec 15 utilisateurs réels (stagiaires) sur un scénario de questions variées, comparer formulations attendues vs réelles.
11. **Métriques :** taux de résolution automatique, taux de fallback, temps de réponse, satisfaction utilisateur (questionnaire).
12. **Livrables :** Cahier des charges, état de l'art, prototype Voiceflow, schéma d'architecture, rapport de tests, présentation, démo live.
13. **Difficulté :** 🟢 Facile
14. **Extensions possibles :** Ajouter un LLM pour gérer les formulations libres non couvertes par les intents (évolution vers Niveau 2).

### Sujet 2 — Chatbot de prise de rendez-vous pour un cabinet (médical, administratif)

1. **Problématique :** La prise de rendez-vous téléphonique dans les petites structures marocaines (cabinets médicaux, services administratifs) est chronophage et sujette aux erreurs de planning.
2. **Question de recherche :** Un chatbot No-Code connecté à un agenda peut-il automatiser efficacement la prise de rendez-vous sans erreurs de double-réservation ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir un chatbot transactionnel connecté à un calendrier.
4. **Objectifs spécifiques :**
   - Modéliser le parcours de réservation (créneaux, confirmation, annulation).
   - Connecter le chatbot à Google Calendar via API/webhook.
   - Gérer les cas d'erreur (créneau indisponible).
   - Envoyer une confirmation automatique (email/SMS).
   - Évaluer la fiabilité du système sur des scénarios réels.
5. **Solution proposée :** Chatbot avec formulaire conversationnel de prise de rendez-vous, vérification de disponibilité en temps réel et confirmation automatique.
6. **Plateforme recommandée :** **Voiceflow** + **Make** (pour la connexion à Google Calendar), adapté car il gère bien les logiques conditionnelles simples.
7. **Technologies complémentaires :** API Google Calendar, Make (automatisation), webhook, email transactionnel.
8. **Architecture :** Utilisateur → Chatbot (Voiceflow) → Webhook → Make → Google Calendar → Confirmation → Utilisateur.
9. **Partie recherche :** Comparer les approches de gestion de créneaux (slot-filling), étudier les chatbots transactionnels existants (Calendly-bot, etc.), critères d'évaluation de fiabilité.
10. **Expérimentation :** Simuler 20 réservations concurrentes/successives et vérifier l'absence de conflits.
11. **Métriques :** taux d'erreurs de réservation, temps moyen de complétion du parcours, taux d'abandon.
12. **Livrables :** Cahier des charges, état de l'art, prototype, architecture, jeu de tests, rapport, démo.
13. **Difficulté :** 🟢 Facile
14. **Extensions possibles :** Ajouter un rappel automatique par SMS/WhatsApp, puis un agent IA gérant les reprogrammations en langage libre.

### Sujet 3 — Chatbot de recommandation touristique locale (Maroc)

1. **Problématique :** Les touristes et visiteurs manquent d'un outil interactif simple pour obtenir des recommandations personnalisées (restaurants, lieux, activités) dans une ville marocaine.
2. **Question de recherche :** Un chatbot à scénarios avec filtres (budget, type d'activité) fournit-il des recommandations jugées pertinentes par les utilisateurs ?
3. **Objectif général :** Le stagiaire doit être capable de construire un chatbot de recommandation basé sur des règles de filtrage.
4. **Objectifs spécifiques :**
   - Constituer une base de données de lieux/activités (ex : Casablanca, Marrakech).
   - Concevoir un arbre de questions (préférences utilisateur).
   - Implémenter la logique de recommandation.
   - Intégrer des cartes/liens (Google Maps).
   - Évaluer la pertinence perçue des recommandations.
5. **Solution proposée :** Chatbot conversationnel questionnant l'utilisateur sur ses préférences puis proposant une liste filtrée de recommandations avec liens.
6. **Plateforme recommandée :** **Botpress** (flexibilité des flux conditionnels, hébergement possible en self-host, gratuit).
7. **Technologies complémentaires :** Google Sheets/Airtable (base de données), Google Maps API (liens), widget web.
8. **Architecture :** Utilisateur → Chatbot (Botpress) → Logique de filtrage → Base de données (Airtable) → Réponse enrichie (liens/cartes).
9. **Partie recherche :** Étudier les systèmes de recommandation basés règles vs collaboratifs, comparer avec des chatbots touristiques existants, limites du filtrage par règles.
10. **Expérimentation :** Faire tester le chatbot par 10-15 utilisateurs avec profils différents et comparer aux recommandations qu'un humain aurait données.
11. **Métriques :** pertinence perçue (note /5), taux de clics sur les recommandations, temps de réponse.
12. **Livrables :** Cahier des charges, état de l'art, prototype, base de données, rapport de tests, démo.
13. **Difficulté :** 🟢 Facile
14. **Extensions possibles :** Remplacer le filtrage par règles par un LLM + RAG sur des avis/descriptions de lieux (évolution Niveau 3).

---

## NIVEAU 2 — IA GÉNÉRATIVE

### Sujet 4 — Assistant conversationnel personnel avec mémoire de contexte

1. **Problématique :** Les chatbots à base d'intents échouent dès que l'utilisateur formule une demande de façon inattendue, et ne se souviennent pas du contexte de la conversation.
2. **Question de recherche :** Dans quelle mesure l'intégration d'un LLM améliore-t-elle la compréhension du langage libre et la cohérence conversationnelle par rapport à un chatbot à intents ?
3. **Objectif général :** Le stagiaire doit être capable d'intégrer un LLM à un chatbot No-Code pour gérer la conversation libre et la mémoire à court terme.
4. **Objectifs spécifiques :**
   - Comparer un flux à intents et un flux basé LLM sur les mêmes cas d'usage.
   - Configurer un prompt système adapté au cas d'usage choisi.
   - Gérer la mémoire conversationnelle (historique des échanges).
   - Connecter le chatbot à une API LLM.
   - Évaluer la qualité et la cohérence des réponses.
5. **Solution proposée :** Assistant conversationnel généraliste (ex : assistant d'étude pour stagiaires) utilisant un LLM avec gestion d'historique.
6. **Plateforme recommandée :** **Dify** (interface No-Code dédiée aux applications LLM, gestion native du prompt et de la mémoire) ou **Flowise** en alternative Low-Code.
7. **Technologies complémentaires :** API LLM (OpenAI, Mistral, ou modèle open-source via Groq/OpenRouter), prompt engineering, gestion de sessions.
8. **Architecture :** Utilisateur → Interface chat (Dify) → Gestion mémoire → LLM (API) → Réponse contextualisée.
9. **Partie recherche :** État de l'art sur les LLM conversationnels, techniques de gestion de mémoire (fenêtre glissante, résumé), comparaison de 2-3 LLM accessibles via API, critères de qualité de réponse (cohérence, pertinence, ton).
10. **Expérimentation :** Comparer, sur 20 questions identiques, les réponses du chatbot à intents (Sujet 1) et de l'assistant LLM ; faire évaluer par un panel de 10 utilisateurs.
11. **Métriques :** pertinence des réponses (note humaine), taux de réponses hors-sujet, cohérence sur conversation multi-tours, coût par conversation (tokens).
12. **Livrables :** Cahier des charges, état de l'art comparatif, prototype Dify, jeu de prompts, rapport d'évaluation, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ajouter du RAG pour ancrer les réponses sur des documents spécifiques (Niveau 3).

### Sujet 5 — Générateur de réponses personnalisées pour un service client

1. **Problématique :** Les agents de service client passent beaucoup de temps à rédiger des réponses similaires (réclamations, retours produit) sans que celles-ci soient toujours homogènes en ton.
2. **Question de recherche :** Un LLM guidé par des templates de prompt peut-il générer des réponses de service client jugées professionnelles et adaptées au contexte marocain ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir un chatbot générateur de réponses professionnelles à partir d'un LLM paramétré.
4. **Objectifs spécifiques :**
   - Collecter des exemples réels de réclamations et réponses.
   - Concevoir des templates de prompt par catégorie de demande.
   - Intégrer le LLM avec contrôle du ton (formel, empathique).
   - Mettre en place un mécanisme de validation humaine avant envoi.
   - Évaluer la qualité perçue des réponses générées.
5. **Solution proposée :** Chatbot interne (outil d'aide à la rédaction) qui génère une proposition de réponse à une réclamation client, validée ou modifiée par un agent.
6. **Plateforme recommandée :** **Dify** (gestion de prompts structurés et variables) — adapté pour un usage orienté génération de texte contrôlée.
7. **Technologies complémentaires :** API LLM, prompt templates, interface de validation (formulaire).
8. **Architecture :** Agent → Interface (Dify) → Sélection catégorie → LLM (prompt template) → Proposition de réponse → Validation agent → Envoi.
9. **Partie recherche :** Étudier le prompt engineering pour la génération contrôlée, comparer différentes stratégies de templates, limites des LLM en génération de texte professionnel (biais, hallucination de faits).
10. **Expérimentation :** Générer des réponses pour 20 réclamations types et les faire noter par des agents/formateurs par rapport à des réponses rédigées manuellement.
11. **Métriques :** taux de réponses jugées "utilisables sans modification", temps de rédaction gagné, taux de correction nécessaire, satisfaction des évaluateurs.
12. **Livrables :** Cahier des charges, état de l'art, banque de prompts, prototype, rapport d'évaluation, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ajouter un module RAG sur l'historique des réclamations similaires déjà traitées.

### Sujet 6 — Chatbot pédagogique de révision pour stagiaires OFPPT

1. **Problématique :** Les stagiaires manquent d'outils interactifs pour réviser un module de cours en dehors des heures de formation.
2. **Question de recherche :** Un chatbot basé sur un LLM peut-il générer des questions de révision adaptées à un module de cours et améliorer l'engagement des stagiaires ?
3. **Objectif général :** Le stagiaire doit être capable de développer un chatbot pédagogique capable de générer des quiz et d'expliquer des notions de cours.
4. **Objectifs spécifiques :**
   - Structurer le contenu d'un module de cours en base de connaissance.
   - Concevoir des prompts de génération de questions/réponses.
   - Implémenter un mode "quiz" et un mode "explication libre".
   - Suivre la progression de l'apprenant (score).
   - Évaluer l'impact perçu sur la révision.
5. **Solution proposée :** Chatbot pédagogique interactif proposant quiz auto-générés et explications à la demande sur un module choisi (ex : Python, réseaux, bases de données).
6. **Plateforme recommandée :** **Flowise** (Low-Code, bonne flexibilité pour orchestrer prompts + logique de score).
7. **Technologies complémentaires :** API LLM, base de connaissance (fichiers de cours), stockage de scores (Google Sheets/Airtable).
8. **Architecture :** Stagiaire → Chatbot (Flowise) → Générateur de quiz (LLM) → Base de cours → Suivi de score → Restitution.
9. **Partie recherche :** État de l'art des tuteurs intelligents (Intelligent Tutoring Systems) simplifiés, comparaison d'outils de génération de quiz par IA, critères pédagogiques d'évaluation.
10. **Expérimentation :** Faire utiliser le chatbot par un groupe de stagiaires pendant 2 semaines de révision et comparer les résultats à un groupe témoin sur un mini-test.
11. **Métriques :** taux de bonnes réponses au quiz final, temps d'engagement, taux d'hallucination dans les explications, satisfaction stagiaires.
12. **Livrables :** Cahier des charges, état de l'art, prototype, base de contenu structurée, rapport d'expérimentation, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ancrer les réponses sur les supports de cours réels via RAG pour réduire les hallucinations (Niveau 3).

---

## NIVEAU 3 — RAG (Retrieval-Augmented Generation)

### Sujet 7 — Chatbot RAG sur le règlement intérieur et les procédures OFPPT

1. **Problématique :** Les stagiaires et formateurs consultent difficilement les règlements et procédures administratives (absences, stages, examens) dispersés dans plusieurs documents PDF.
2. **Question de recherche :** Un chatbot RAG interrogeant directement les documents officiels réduit-il le temps de recherche d'information par rapport à une recherche manuelle ?
3. **Objectif général :** Le stagiaire doit être capable de construire un chatbot RAG capable de répondre à partir de documents internes.
4. **Objectifs spécifiques :**
   - Collecter et nettoyer les documents de référence (règlement, guides).
   - Découper les documents (chunking) et générer les embeddings.
   - Mettre en place une base vectorielle et un pipeline de recherche.
   - Connecter le pipeline à un LLM pour générer des réponses sourcées.
   - Évaluer la précision et le taux d'hallucination.
5. **Solution proposée :** Chatbot documentaire répondant aux questions administratives avec citation du document source.
6. **Plateforme recommandée :** **Dify** (module RAG intégré prêt à l'emploi, upload direct de documents, adapté aux débutants en RAG).
7. **Technologies complémentaires :** Base vectorielle (intégrée à Dify ou Chroma/Weaviate), embeddings, chunking, LLM.
8. **Architecture :** Utilisateur → Chatbot (Dify) → Recherche vectorielle → Documents (règlement) → LLM → Réponse sourcée.
9. **Partie recherche :** État de l'art du RAG (principe, avantages vs fine-tuning), comparaison des stratégies de chunking, critères d'évaluation de la pertinence documentaire (recall, precision), limites du RAG (contexte tronqué, documents mal structurés).
10. **Expérimentation :** Constituer 20 questions types et vérifier si le chatbot cite la bonne source et donne une réponse correcte, comparer avec/sans RAG.
11. **Métriques :** précision des réponses, taux d'hallucination, taux de citation correcte de la source, temps de réponse.
12. **Livrables :** Cahier des charges, état de l'art, base documentaire indexée, prototype, jeu de questions-tests, rapport, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Étendre à plusieurs filières/centres avec gestion des permissions d'accès aux documents.

### Sujet 8 — Assistant RAG de support technique sur une documentation logicielle

1. **Problématique :** Les débutants en développement passent beaucoup de temps à chercher dans une documentation technique (ex : documentation d'un framework) l'information précise dont ils ont besoin.
2. **Question de recherche :** Un assistant RAG sur une documentation technique améliore-t-il la rapidité et la justesse de résolution des problèmes par rapport à une recherche classique (Ctrl+F, moteur de recherche) ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir un assistant RAG spécialisé sur une documentation technique.
4. **Objectifs spécifiques :**
   - Choisir une documentation technique cible (ex : une librairie Python, un framework).
   - Préparer et indexer le corpus documentaire.
   - Optimiser la stratégie de récupération (top-k, reranking simple).
   - Intégrer des exemples de code dans les réponses.
   - Évaluer la justesse technique des réponses.
5. **Solution proposée :** Chatbot d'aide au développement répondant avec extraits de documentation et exemples de code.
6. **Plateforme recommandée :** **Langflow** (Low-Code, orienté développeurs, bon contrôle du pipeline RAG et export vers du code Python).
7. **Technologies complémentaires :** Base vectorielle (Chroma/FAISS), embeddings, LLM, éventuellement API GitHub pour récupérer la doc.
8. **Architecture :** Développeur → Chatbot (Langflow) → Recherche vectorielle → Documentation indexée → LLM → Réponse + extrait de code.
9. **Partie recherche :** Comparer les approches de recherche documentaire technique (recherche par mots-clés vs sémantique), étudier les techniques de chunking adaptées au code, critères d'évaluation technique (exactitude du code, exécutabilité).
10. **Expérimentation :** Soumettre 15 questions techniques réelles et vérifier l'exactitude/exécutabilité des réponses proposées.
11. **Métriques :** taux d'exactitude technique, taux d'hallucination de fonctions inexistantes, temps de résolution, satisfaction utilisateur.
12. **Livrables :** Cahier des charges, état de l'art, corpus indexé, prototype Langflow, jeu de tests techniques, rapport, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ajouter un agent capable d'exécuter le code proposé dans un sandbox (évolution vers Niveau 5).

### Sujet 9 — Chatbot RAG d'information administrative marocaine (CNSS, impôts, état civil)

1. **Problématique :** Les citoyens marocains ont des difficultés à trouver rapidement des informations fiables sur les démarches administratives courantes, dispersées sur plusieurs sites officiels.
2. **Question de recherche :** Un chatbot RAG basé sur des documents officiels marocains peut-il fournir des réponses fiables et sourcées sur des démarches administratives courantes ?
3. **Objectif général :** Le stagiaire doit être capable de développer un chatbot RAG contextualisé sur des procédures administratives locales.
4. **Objectifs spécifiques :**
   - Collecter des documents officiels (guides CNSS, impôts, état civil).
   - Construire la base de connaissance et l'indexation vectorielle.
   - Concevoir un prompt garantissant la citation des sources et la prudence en cas d'incertitude.
   - Développer une interface conversationnelle simple.
   - Évaluer la fiabilité des réponses face à des cas réels.
5. **Solution proposée :** Chatbot d'information administrative citant systématiquement sa source et invitant à vérifier auprès de l'organisme concerné en cas de doute.
6. **Plateforme recommandée :** **Flowise** (bon contrôle du prompt de garde-fou et de la logique de citation).
7. **Technologies complémentaires :** Base vectorielle, embeddings, LLM, documents PDF officiels.
8. **Architecture :** Citoyen → Chatbot (Flowise) → Recherche vectorielle → Documents officiels → LLM → Réponse sourcée + avertissement.
9. **Partie recherche :** État de l'art des chatbots administratifs/gouvernementaux, enjeux de fiabilité et de responsabilité de l'information, critères d'évaluation (exactitude, prudence, traçabilité).
10. **Expérimentation :** Tester 20 questions administratives réelles et vérifier la conformité des réponses avec les textes officiels.
11. **Métriques :** taux d'exactitude, taux de réponses avec source citée, taux de refus prudent en cas d'ambiguïté, satisfaction utilisateur.
12. **Livrables :** Cahier des charges, état de l'art, base documentaire, prototype, rapport de conformité, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ajouter la mise à jour automatique de la base documentaire via scraping/API officielle.

---

## NIVEAU 4 — AUTOMATISATION

### Sujet 10 — Chatbot de commande WhatsApp pour petit commerce marocain

1. **Problématique :** Les petits commerçants marocains reçoivent leurs commandes par WhatsApp de façon manuelle, sans suivi structuré ni automatisation du traitement.
2. **Question de recherche :** L'automatisation d'un flux de commande via chatbot WhatsApp + n8n réduit-elle les erreurs et le temps de traitement des commandes ?
3. **Objectif général :** Le stagiaire doit être capable de mettre en place un chatbot transactionnel automatisé sur WhatsApp.
4. **Objectifs spécifiques :**
   - Modéliser le parcours de commande (catalogue, panier, confirmation).
   - Connecter le chatbot à l'API WhatsApp Business.
   - Automatiser l'enregistrement des commandes (n8n → Google Sheets/base de données).
   - Automatiser la notification au commerçant.
   - Évaluer la fiabilité et le gain de temps.
5. **Solution proposée :** Chatbot WhatsApp permettant de consulter un catalogue, passer commande, et transmettre automatiquement la commande au commerçant.
6. **Plateforme recommandée :** **n8n** (orchestration des automatisations et intégration WhatsApp/Sheets) associé à **Botpress** pour le dialogue.
7. **Technologies complémentaires :** API WhatsApp Business (ou Twilio), n8n, Google Sheets/Airtable, webhook.
8. **Architecture :** Client → WhatsApp → Chatbot (Botpress) → Webhook → n8n → Base de données commandes → Notification commerçant.
9. **Partie recherche :** État de l'art des chatbots e-commerce conversationnels, comparaison des outils d'automatisation (n8n vs Make vs Zapier), critères d'évaluation d'un flux transactionnel.
10. **Expérimentation :** Simuler 30 commandes avec différents scénarios (rupture de stock, annulation) et mesurer les erreurs.
11. **Métriques :** taux d'erreurs de commande, temps moyen de traitement, taux de complétion du parcours, satisfaction du commerçant.
12. **Livrables :** Cahier des charges, état de l'art, prototype, workflow n8n documenté, rapport de tests, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ajouter un module de paiement en ligne et un agent IA de recommandation de produits.

### Sujet 11 — Chatbot RH pour la gestion des demandes de congé

1. **Problématique :** La gestion des demandes de congé dans une PME est souvent faite par email/papier, ce qui complique le suivi et la validation.
2. **Question de recherche :** Un chatbot RH automatisé peut-il fiabiliser et accélérer le processus de demande et de validation de congés ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir un chatbot RH intégré à un workflow d'automatisation de validation.
4. **Objectifs spécifiques :**
   - Modéliser le processus de demande de congé (solde, dates, motif).
   - Automatiser la vérification du solde de congés disponible.
   - Automatiser l'envoi de la demande au responsable pour validation.
   - Notifier automatiquement le résultat à l'employé.
   - Évaluer le gain de temps par rapport au processus manuel.
5. **Solution proposée :** Chatbot RH permettant de soumettre une demande de congé, avec workflow de validation automatisé.
6. **Plateforme recommandée :** **Make** (bonne intégration avec Google Workspace/Outlook pour les emails et calendriers).
7. **Technologies complémentaires :** Google Sheets (base RH), Make, Gmail/Outlook API, chatbot (Voiceflow/Botpress).
8. **Architecture :** Employé → Chatbot → Vérification solde (Sheets) → Make → Email de validation au responsable → Retour → Notification employé.
9. **Partie recherche :** État de l'art des chatbots RH, comparaison des outils d'automatisation de workflow d'entreprise, critères d'évaluation (fiabilité, traçabilité, sécurité des données RH).
10. **Expérimentation :** Simuler 15 demandes de congé avec cas variés (solde insuffisant, chevauchement) et vérifier la robustesse du workflow.
11. **Métriques :** taux d'erreurs de traitement, temps moyen de validation, taux de notifications correctement délivrées, satisfaction utilisateur.
12. **Livrables :** Cahier des charges, état de l'art, prototype, workflow Make documenté, rapport de tests, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Étendre à d'autres processus RH (notes de frais, attestations) et ajouter un agent IA répondant aux questions RH générales via RAG.

### Sujet 12 — Chatbot de support technique avec création automatique de tickets

1. **Problématique :** Les demandes de support technique arrivent de façon non structurée (email, chat) et sont difficiles à prioriser et suivre.
2. **Question de recherche :** L'automatisation de la création et de la catégorisation de tickets à partir d'un chatbot améliore-t-elle le temps de prise en charge ?
3. **Objectif général :** Le stagiaire doit être capable de développer un chatbot de support connecté à un système de gestion de tickets automatisé.
4. **Objectifs spécifiques :**
   - Modéliser les catégories de problèmes techniques courants.
   - Concevoir le dialogue de qualification du problème.
   - Automatiser la création du ticket (Trello/Notion/Google Sheets) via n8n.
   - Automatiser la notification à l'équipe technique (Slack/email).
   - Évaluer la qualité de la catégorisation automatique.
5. **Solution proposée :** Chatbot qui qualifie un incident technique puis crée et route automatiquement un ticket vers l'équipe compétente.
6. **Plateforme recommandée :** **n8n** (flexibilité de connexion à de nombreux outils : Trello, Slack, email) avec **Voiceflow** pour le dialogue.
7. **Technologies complémentaires :** n8n, API Trello/Notion, Slack API, webhook.
8. **Architecture :** Utilisateur → Chatbot (Voiceflow) → Qualification du problème → Webhook → n8n → Création ticket (Trello) → Notification Slack.
9. **Partie recherche :** État de l'art des systèmes de ticketing automatisé et de la classification de demandes, comparaison d'outils d'automatisation, critères d'évaluation (précision de catégorisation, délai de prise en charge).
10. **Expérimentation :** Tester 20 scénarios d'incidents variés et vérifier la justesse de la catégorisation et du routage.
11. **Métriques :** taux de catégorisation correcte, temps de création du ticket, taux de notification réussie, satisfaction équipe support.
12. **Livrables :** Cahier des charges, état de l'art, prototype, workflow n8n, rapport de tests, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ajouter un LLM pour proposer une première solution avant escalade humaine (évolution vers agent, Niveau 5).

---

## NIVEAU 5 — AGENTIC AI

### Sujet 13 — Agent IA multi-outils de recherche et réservation (voyage)

1. **Problématique :** Organiser un voyage nécessite de consulter plusieurs sources (météo, vols, hôtels) séparément, ce qui est chronophage.
2. **Question de recherche :** Un agent IA capable d'orchestrer plusieurs outils (recherche, météo, réservation simulée) peut-il fournir une assistance de planification plus efficace qu'un chatbot classique ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir un agent IA orchestrant plusieurs outils/APIs de façon autonome.
4. **Objectifs spécifiques :**
   - Définir les outils que l'agent peut utiliser (météo, recherche web, base d'hôtels).
   - Configurer la logique de sélection d'outil par l'agent (function calling).
   - Gérer l'enchaînement de plusieurs étapes (planification multi-tours).
   - Présenter un résultat consolidé à l'utilisateur.
   - Évaluer la pertinence et la fiabilité des plans proposés.
5. **Solution proposée :** Agent conversationnel de planification de voyage qui interroge automatiquement plusieurs outils avant de proposer un itinéraire.
6. **Plateforme recommandée :** **Flowise** ou **Langflow** (support natif des agents avec outils/function calling en Low-Code).
7. **Technologies complémentaires :** API météo, API de recherche (SerpAPI ou équivalent), base d'hôtels (Airtable), LLM avec function calling.
8. **Architecture :** Utilisateur → Agent (Flowise) → Sélection d'outils → Appels API (météo, recherche, hôtels) → Synthèse LLM → Réponse consolidée.
9. **Partie recherche :** État de l'art des agents IA (ReAct, function calling), comparaison agent vs chatbot classique, critères d'évaluation de la fiabilité d'un agent multi-étapes (taux de succès de tâche, boucles infinies).
10. **Expérimentation :** Soumettre 15 demandes de planification variées et vérifier la cohérence et l'exactitude des informations combinées.
11. **Métriques :** taux de réussite de la tâche complète, nombre d'appels d'outils par requête, temps de réponse, taux d'erreurs d'orchestration.
12. **Livrables :** Cahier des charges, état de l'art, prototype agent, documentation des outils, rapport d'expérimentation, démo.
13. **Difficulté :** 🔴 Avancé
14. **Extensions possibles :** Ajouter un module de mémoire long terme des préférences utilisateur et une vraie API de réservation.

### Sujet 14 — Agent IA de veille technologique automatisée

1. **Problématique :** Les stagiaires et formateurs manquent de temps pour suivre l'actualité technologique pertinente à leur domaine (IA, chatbots, No-Code).
2. **Question de recherche :** Un agent IA automatisant la collecte, le résumé et la diffusion d'actualités techniques permet-il un gain de temps significatif par rapport à une veille manuelle ?
3. **Objectif général :** Le stagiaire doit être capable de développer un agent autonome de veille technologique programmée.
4. **Objectifs spécifiques :**
   - Définir les sources de veille (flux RSS, sites spécialisés).
   - Automatiser la collecte périodique des contenus.
   - Utiliser un LLM pour résumer et filtrer les contenus pertinents.
   - Automatiser la diffusion (email/Slack/Notion) du résumé.
   - Évaluer la pertinence des contenus sélectionnés.
5. **Solution proposée :** Agent qui collecte quotidiennement des actualités tech, les résume via LLM, et envoie une synthèse automatique.
6. **Plateforme recommandée :** **n8n** (déclenchement programmé/cron, agrégation de flux RSS, orchestration complète) avec appel LLM intégré.
7. **Technologies complémentaires :** n8n, flux RSS, API LLM, Notion/Slack/email pour la diffusion.
8. **Architecture :** Déclencheur (cron) → n8n → Collecte RSS → LLM (résumé/filtrage) → Diffusion (email/Slack) → Utilisateur final.
9. **Partie recherche :** État de l'art des agents de veille automatisée, techniques de résumé automatique (summarization), critères d'évaluation de la pertinence d'un résumé (couverture, fidélité).
10. **Expérimentation :** Comparer sur 2 semaines les résumés automatiques à une veille manuelle réalisée par le stagiaire.
11. **Métriques :** taux de pertinence des articles sélectionnés, fidélité du résumé (absence de déformation), régularité de la diffusion, temps gagné.
12. **Livrables :** Cahier des charges, état de l'art, workflow n8n documenté, prototype, rapport comparatif, démo.
13. **Difficulté :** 🟡 Intermédiaire / 🔴 Avancé selon le nombre de sources
14. **Extensions possibles :** Ajouter un chatbot permettant d'interroger la base d'articles collectés (RAG sur la veille).

### Sujet 15 — Agent IA autonome de recherche documentaire et synthèse multi-sources

1. **Problématique :** Rédiger une synthèse sur un sujet technique nécessite de croiser plusieurs documents/sources, tâche longue et sujette aux oublis.
2. **Question de recherche :** Un agent capable de décomposer une question complexe en sous-tâches de recherche produit-il des synthèses plus complètes qu'une recherche RAG simple ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir un agent de recherche capable de décomposer une tâche complexe en sous-étapes.
4. **Objectifs spécifiques :**
   - Définir un jeu de documents/sources multi-format.
   - Configurer un agent capable de planifier ses recherches (décomposition de tâche).
   - Orchestrer plusieurs appels de recherche (RAG + web) avant synthèse.
   - Structurer la réponse finale avec sources citées.
   - Évaluer la complétude et l'exactitude de la synthèse.
5. **Solution proposée :** Agent de recherche qui, face à une question complexe, planifie plusieurs sous-recherches puis produit une synthèse structurée sourcée.
6. **Plateforme recommandée :** **Langflow** (contrôle fin de l'orchestration agent + RAG, bon compromis Low-Code/code).
7. **Technologies complémentaires :** Base vectorielle, API de recherche web, LLM avec planification, function calling.
8. **Architecture :** Utilisateur → Agent (Langflow) → Planification des sous-tâches → RAG/Web → Agrégation → LLM (synthèse) → Réponse sourcée.
9. **Partie recherche :** État de l'art des agents de recherche (RAG agentique, planification de tâches), comparaison agent vs RAG simple, critères d'évaluation (complétude, exactitude, redondance).
10. **Expérimentation :** Soumettre 10 questions complexes multi-facettes et comparer les synthèses de l'agent à celles d'un RAG simple (Sujet 7/8).
11. **Métriques :** taux de complétude (couverture des sous-aspects attendus), taux d'exactitude, temps de traitement, coût en appels LLM.
12. **Livrables :** Cahier des charges, état de l'art, prototype agent, jeu de questions-tests, rapport comparatif, démo.
13. **Difficulté :** 🔴 Avancé
14. **Extensions possibles :** Ajouter un module de vérification croisée des faits (fact-checking) entre les sources.

---

## NIVEAU 6 — ÉVALUATION

### Sujet 16 — Système d'évaluation automatique de chatbots (benchmark)

1. **Problématique :** Les stagiaires et formateurs n'ont pas d'outil simple pour comparer objectivement plusieurs chatbots ou versions d'un même chatbot.
2. **Question de recherche :** Peut-on concevoir un protocole d'évaluation automatisé et reproductible permettant de comparer objectivement plusieurs chatbots sur un même jeu de questions ?
3. **Objectif général :** Le stagiaire doit être capable de concevoir un système d'évaluation automatisée de chatbots basé sur un jeu de test standardisé.
4. **Objectifs spécifiques :**
   - Construire un jeu de questions-réponses de référence (gold standard).
   - Automatiser l'envoi des questions à un ou plusieurs chatbots via API/webhook.
   - Utiliser un LLM "juge" pour scorer automatiquement les réponses.
   - Générer un rapport comparatif automatique.
   - Valider la fiabilité du LLM-juge par comparaison avec une évaluation humaine.
5. **Solution proposée :** Outil automatisé qui teste un ou plusieurs chatbots sur un jeu de questions et produit un score de qualité par critère.
6. **Plateforme recommandée :** **n8n** (orchestration des appels API vers les chatbots testés + LLM juge) associé à Google Sheets pour le reporting.
7. **Technologies complémentaires :** API des chatbots à tester, LLM juge, n8n, Google Sheets/Data Studio pour la visualisation.
8. **Architecture :** Jeu de questions → n8n → Appel chatbot testé → Réponse → LLM juge (scoring) → Stockage résultats → Tableau de bord.
9. **Partie recherche :** État de l'art de l'évaluation des chatbots/LLM (LLM-as-a-judge, métriques automatiques vs humaines), limites du LLM-juge (biais), critères d'évaluation standards (pertinence, exactitude, hallucination).
10. **Expérimentation :** Évaluer 2-3 chatbots développés dans d'autres sujets (ex : Sujets 1, 4, 7) sur un même jeu de 20 questions et comparer au jugement humain.
11. **Métriques :** corrélation score LLM-juge / score humain, précision, taux d'hallucination détecté, temps d'évaluation automatisée vs manuelle.
12. **Livrables :** Cahier des charges, état de l'art, jeu de test de référence, workflow d'évaluation n8n, rapport comparatif, démo.
13. **Difficulté :** 🔴 Avancé
14. **Extensions possibles :** Étendre le benchmark à l'évaluation continue en production (évolution vers le Sujet 17).

### Sujet 17 — Dashboard de monitoring des performances d'un chatbot en production

1. **Problématique :** Une fois déployé, un chatbot n'est généralement pas suivi dans le temps, ce qui empêche de détecter une dégradation de ses performances ou des questions mal traitées.
2. **Question de recherche :** Un tableau de bord de monitoring automatisé permet-il de détecter plus rapidement les problèmes de performance d'un chatbot en production ?
3. **Objectif général :** Le stagiaire doit être capable de mettre en place un système de monitoring continu des performances d'un chatbot.
4. **Objectifs spécifiques :**
   - Définir les indicateurs clés à suivre (fallback, satisfaction, temps de réponse).
   - Automatiser la collecte des logs de conversation.
   - Construire un tableau de bord de visualisation.
   - Mettre en place des alertes en cas de dégradation.
   - Évaluer l'utilité du dashboard pour l'amélioration continue.
5. **Solution proposée :** Dashboard connecté à un chatbot existant (ex : Sujet 1 ou 7) affichant en continu ses indicateurs de performance et alertant en cas d'anomalie.
6. **Plateforme recommandée :** **Make** (collecte automatisée des logs) + Google Data Studio/Looker Studio pour la visualisation.
7. **Technologies complémentaires :** Webhook de logs, Make, Google Sheets, Looker Studio, alertes email/Slack.
8. **Architecture :** Chatbot en production → Logs (webhook) → Make → Google Sheets → Looker Studio (dashboard) → Alertes.
9. **Partie recherche :** État de l'art du monitoring de chatbots/LLM en production (observabilité IA), indicateurs standards utilisés dans l'industrie, comparaison d'outils de dashboarding.
10. **Expérimentation :** Suivre pendant 2-3 semaines un chatbot réel (issu d'un autre sujet) et analyser l'évolution des indicateurs et la pertinence des alertes déclenchées.
11. **Métriques :** taux de fallback dans le temps, temps de réponse moyen, taux d'alertes pertinentes (vrais positifs), satisfaction utilisateur dans le temps.
12. **Livrables :** Cahier des charges, état de l'art, workflow Make, dashboard Looker Studio, rapport d'analyse, démo.
13. **Difficulté :** 🟡 Intermédiaire
14. **Extensions possibles :** Ajouter une boucle de réentraînement/amélioration semi-automatique du chatbot basée sur les questions en échec détectées.

---

## Classement par niveau

| Niveau | Thème | Sujets |
|---|---|---|
| 1 — Fondamentaux | Intents, scénarios, FAQ, UX conversationnelle | 1, 2, 3 |
| 2 — IA générative | LLM, prompting, mémoire conversationnelle | 4, 5, 6 |
| 3 — RAG | Documents, embeddings, base vectorielle | 7, 8, 9 |
| 4 — Automatisation | n8n, Make, APIs, webhooks | 10, 11, 12 |
| 5 — Agentic AI | Agents, outils, orchestration | 13, 14, 15 |
| 6 — Évaluation | Benchmark, hallucinations, monitoring | 16, 17 |

---

## Comparaison des plateformes

| Plateforme | No-Code | Low-Code | LLM | RAG | Agents | API | Automatisation | Difficulté | Cas d'usage typique |
|---|---|---|---|---|---|---|---|---|---|
| **Botpress** | ✅ | ✅ | ⚠️ (via intégration) | ⚠️ (via plugin) | ⚠️ limité | ✅ | ⚠️ | Facile | Chatbots à intents, self-hosted, FAQ/orientation |
| **Voiceflow** | ✅ | ⚠️ limité | ✅ (blocs IA) | ⚠️ basique | ❌ | ✅ | ⚠️ via intégrations | Facile | Chatbots transactionnels (RDV, commandes) |
| **Dify** | ✅ | ✅ | ✅ natif | ✅ natif (upload docs) | ✅ basique | ✅ | ⚠️ | Intermédiaire | Assistants LLM, RAG documentaire rapide |
| **Flowise** | ⚠️ | ✅ | ✅ natif | ✅ natif | ✅ (agents/outils) | ✅ | ⚠️ | Intermédiaire | RAG avancé, agents, prototypage LLM visuel |
| **Langflow** | ⚠️ | ✅ | ✅ natif | ✅ natif | ✅ (agents/outils) | ✅ | ⚠️ | Intermédiaire/Avancé | RAG technique, agents, export vers code |
| **n8n** | ⚠️ | ✅ | ✅ (nœud LLM) | ⚠️ via intégration | ✅ (AI Agent node) | ✅ | ✅ natif | Intermédiaire | Automatisation de bout en bout, intégrations multiples |
| **Make** | ✅ | ⚠️ | ✅ (module IA) | ❌ | ⚠️ limité | ✅ | ✅ natif | Facile/Intermédiaire | Automatisation métier (RH, ventes, notifications) |
| **Microsoft Copilot Studio** | ✅ | ⚠️ | ✅ natif | ✅ natif | ✅ | ✅ | ✅ (Power Automate) | Intermédiaire | Chatbots d'entreprise intégrés à l'écosystème Microsoft |
| **Google Dialogflow** | ✅ | ⚠️ | ⚠️ (via intégration Gemini) | ⚠️ limité | ❌ | ✅ | ⚠️ | Facile/Intermédiaire | Chatbots vocaux/textuels classiques, intents |

**Points forts / limites (synthèse) :**
- **Botpress / Voiceflow :** excellents pour démarrer (Niveau 1-2), très visuels, mais limités dès qu'il faut du RAG avancé ou des agents complexes.
- **Dify :** meilleur point d'entrée pour le RAG et les assistants LLM sans écrire de code — idéal Niveaux 2-3.
- **Flowise / Langflow :** les plus adaptés aux stagiaires visant une évolution vers le code (Python/LangChain sous-jacent) — idéal Niveaux 3-5.
- **n8n / Make :** indispensables dès qu'il faut connecter le chatbot à des systèmes externes (agenda, tickets, WhatsApp) — cœur du Niveau 4.
- **Copilot Studio / Dialogflow :** pertinents dans un contexte d'entreprise déjà équipée Microsoft/Google, mais moins flexibles pour l'expérimentation libre en formation.

---

## Sélection finale — 5 sujets recommandés pour l'OFPPT 2ᵉ année

Critères retenus : faisabilité en 2 mois, intérêt pédagogique, difficulté raisonnable, disponibilité des outils, potentiel de démonstration, valeur professionnelle, évolutivité vers l'IA générative/Agentic AI.

**1. Sujet 1 — Chatbot d'accueil et d'orientation pour un centre de formation**
Problématique → surcharge de l'accueil par des questions répétitives · Question de recherche → un chatbot à intents réduit-il les sollicitations répétitives ? · Solution → chatbot FAQ avec fallback humain · Plateforme → Voiceflow · Architecture → Utilisateur → Widget → Chatbot → Base FAQ → Réponse/transfert · Expérimentation → test avec 15 utilisateurs réels · Métriques → taux de résolution automatique, satisfaction · Livrables → cahier des charges, prototype, rapport, démo.

**2. Sujet 4 — Assistant conversationnel personnel avec mémoire de contexte**
Problématique → rigidité des chatbots à intents face au langage libre · Question de recherche → un LLM améliore-t-il la compréhension et la cohérence conversationnelle ? · Solution → assistant LLM avec gestion d'historique · Plateforme → Dify · Architecture → Utilisateur → Interface chat → Mémoire → LLM → Réponse · Expérimentation → comparaison intents vs LLM sur 20 questions · Métriques → pertinence, cohérence, coût · Livrables → état de l'art, prototype, rapport comparatif, démo.

**3. Sujet 7 — Chatbot RAG sur le règlement intérieur et les procédures OFPPT**
Problématique → difficulté à retrouver l'information dans les documents administratifs · Question de recherche → le RAG réduit-il le temps de recherche d'information ? · Solution → chatbot documentaire sourcé · Plateforme → Dify · Architecture → Utilisateur → Chatbot → Recherche vectorielle → Documents → LLM → Réponse sourcée · Expérimentation → 20 questions-tests avec/sans RAG · Métriques → précision, taux d'hallucination, citation correcte · Livrables → base documentaire indexée, prototype, rapport, démo.

**4. Sujet 10 — Chatbot de commande WhatsApp pour petit commerce marocain**
Problématique → gestion manuelle et non structurée des commandes WhatsApp · Question de recherche → l'automatisation réduit-elle les erreurs et le temps de traitement ? · Solution → chatbot transactionnel + automatisation n8n · Plateforme → n8n + Botpress · Architecture → Client → WhatsApp → Chatbot → Webhook → n8n → Base de données → Notification · Expérimentation → simulation de 30 commandes · Métriques → taux d'erreurs, temps de traitement, satisfaction · Livrables → workflow n8n documenté, prototype, rapport, démo.

**5. Sujet 13 — Agent IA multi-outils de recherche et réservation (voyage)**
Problématique → dispersion des sources lors de la planification d'un voyage · Question de recherche → un agent orchestrant plusieurs outils est-il plus efficace qu'un chatbot classique ? · Solution → agent de planification multi-étapes · Plateforme → Flowise · Architecture → Utilisateur → Agent → Sélection d'outils → APIs (météo, recherche, hôtels) → Synthèse LLM → Réponse · Expérimentation → 15 demandes de planification variées · Métriques → taux de réussite de tâche, nombre d'appels d'outils, fiabilité · Livrables → prototype agent, documentation des outils, rapport, démo.

Cette sélection couvre une **progression pédagogique complète** (fondamentaux → IA générative → RAG → automatisation → agents), tout en restant réalisable par un stagiaire de 2ᵉ année en ~2 mois avec des outils No-Code/Low-Code accessibles gratuitement ou en version d'essai.
