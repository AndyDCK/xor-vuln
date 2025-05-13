# Crypto XOR - Authentification vulnérable

Ce projet simule une application Flask avec un système de **chiffrement maison cassable** basé sur **XOR + base64**, comme on peut en rencontrer en CTF.
L'objectif est de comprendre comment casser un chiffrement faible et forger un token admin pour obtenir un flag.

---

## Stack

- Python 3.11
- Flask
- Chiffrement par **XOR**
- Encodage en **base64**
- Interface web
- Dockerisé pour tests isolés

---

## Fonctionnement

- L'utilisateur saisit un **nom** (ex : `guest`)
- Le serveur chifre `user:<nom>` avec un XOR + une clé faible
- Il encode le tout en base64 -> **token**
- Ce token peut ensuite être soumis à `/` :
    - Si le token déchiffré contient `"admin" -> FLAG`

---

## Lancer l'application

```bash
docker build -t flask-xor-vuln .
docker run -p 8080:80 flask-xor-vuln
```

L'application est accessible ici : `http://localhost:8080`
