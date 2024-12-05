import streamlit as st
import pandas as pd

# Charger les données des comptes depuis un fichier CSV
accounts = pd.DataFrame({
    "name": ["alice", "bob", "root"],
    "password": ["pass123", "1234", "password"],
    "email": ["alice@example.com", "bob@example.com", "root@example.com"],
    "failed_login_attempts": [0, 0, 0],
    "logged_in": [False, False, False],
    "role": ["user", "admin", "superadmin"]
})


# Fonction pour vérifier les informations d'identification
def authenticate(username, password):
    user = accounts[accounts["name"] == username]
    if not user.empty and user.iloc[0]["password"] == password:
        return user.iloc[0]
    return None

# Page d'authentification
if "authenticated_user" not in st.session_state:
    st.session_state["authenticated_user"] = None

if st.session_state["authenticated_user"] is None:
    st.title("Page d'authentification")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        user = authenticate(username, password)
        if user is not None:
            st.session_state["authenticated_user"] = user
            st.success(f"Bienvenue, {user['name']} !")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
else:
    user = st.session_state["authenticated_user"]

    # Interface principale après authentification
    st.sidebar.title("Menu")
    st.sidebar.write(f"Bienvenue, {user['name']} !")
    menu = st.sidebar.radio("Naviguer", ["Accueil", "Album de photos", "Déconnexion"])

    if menu == "Déconnexion":
        st.session_state["authenticated_user"] = None
        st.experimental_rerun()

    if menu == "Accueil":
        st.title("Bienvenue sur la page d'accueil")
        st.write("Vous êtes connecté !")

    if menu == "Album de photos":
        st.title("Album de photos")
        st.write("Voici l'album de votre animal préféré !")

        # Disposer les images en 3 colonnes
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://static.streamlit.io/examples/cat.jpg", caption="Photo 1")
        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/800px-June_odd-eyed-cat.jpg", caption="Photo 2")
        with col3:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/VAN_CAT.png/800px-VAN_CAT.png", caption="Photo 3")
