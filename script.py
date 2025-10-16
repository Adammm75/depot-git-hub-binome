# 🎮 Jeu : Deviner le nombre mystère 🎯

# Nombre secret
NOMBRE_SECRET = 35

print("======================================")
print("🔢  Bienvenue dans le jeu de devinettes !")
print("🎯  Ton objectif : trouver le nombre secret entre 1 et 100.")
print("======================================\n")

# Boucle jusqu'à ce que l'utilisateur devine
while True:
    try:
        # 🧠 Demande à l'utilisateur
        essai = int(input("👉 Entre ton nombre : "))

        # ✅ Vérifie si c'est correct
        if essai == NOMBRE_SECRET:
            print("\n🎉 Bravo ! Tu as trouvé le bon nombre ✅")
            print("🏆 Félicitations, mission accomplie !")
            break
        elif essai < NOMBRE_SECRET:
            print("📉 Trop petit ! 💡 Essaie un nombre plus GRAND.\n")
        else:
            print("📈 Trop grand ! 💡 Essaie un nombre plus PETIT.\n")

    except ValueError:
        print("⚠️ Entrée invalide ! Merci d’entrer un nombre entier.\n")
