# Jeu : deviner le nombre

# Nombre secret
nombre_secret = 35

print("🎯 Bienvenue dans le jeu ! Devine le nombre secret entre 1 et 100.")

# Boucle infinie jusqu'à ce que l'utilisateur trouve
while True:
    # Demande à l'utilisateur
    essai = int(input("👉 Entre ton nombre : "))

    # Vérifie si c'est correct
    if essai == nombre_secret:
        print("✅ Bravo ! Tu as trouvé le bon nombre 🎉")
        break
    elif essai < nombre_secret:
        print("📉 Trop petit ! Essaie un nombre plus grand.")
    else:
        print("📈 Trop grand ! Essaie un nombre plus petit.")
