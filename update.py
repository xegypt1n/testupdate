from pyautoupdate import updater

u = updater.Updater()
u.set_repository("https://github.com/xegypt1n/testupdate/tree/master") # Mettez votre nom d'utilisateur et le nom de votre dépôt
u.set_current_version("2.0")

# Vérifier les mises à jour
if u.check_for_update():
    # Télécharger et appliquer la mise à jour
    u.download_update()
    u.apply_update()
