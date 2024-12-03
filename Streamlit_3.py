import  streamlit  as  st 
from streamlit_option_menu import option_menu
import  streamlit_authenticator  as  stauth
import os
import  yaml 
from  yaml.loader  import  SafeLoader

yaml_file_path = os.path.join("https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/", "to", "authentificate.yaml")  
with open(yaml_file_path, 'r') as file:
    config  =  yaml.load(file ,  Loader = SafeLoader )

# Pré-hachage de tous les mots de passe en texte brut une fois 
# stauth.Hasher.hash_passwords(config['credentials'])

st.write("Test me with PikaChou82 and WCS on password")
authenticator  =  stauth . Authenticate ( 
    config ['credentials'], 
    config ['cookie']['name'], 
    config ['cookie']['key'], 
    config ['cookie']['expiry_days'] 
)

authenticator.login()

if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(
    '<p style="font-family: Arial; color: darkblue; font-size: 20px;">'
    f'Bienvenue <strong>{st.session_state["name"]}</strong> !'
    '</p>',
    unsafe_allow_html=True
)

with st.sidebar:
        st.sidebar.write('<h1 style="color:darkblue; font-family:Arial; font-size:30px;">Menu de navigation</h1>', unsafe_allow_html=True)    
        selected = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"],
        icons=["house", "image"],
        menu_icon="cast"
    )

if selected == "Accueil" and st.session_state['authentication_status']:
    st.write(
    '<p style="font-family: Arial; color: black; font-size: 15px;">'
    "On est sur la page d'accueil. Pour l'instant, il y a peu de choses dessus si ce n'est quelques infos sur moi et pourquoi cette page :)"
    '</p>',
    unsafe_allow_html=True   
)
    st.write("")
    st.write("")
    st.image(f'https://raw.githubusercontent.com/PikaChou82/PikaChou82/refs/heads/main/Pascal.jpg', width=150)
    st.write("")
    st.write("")
    st.write(
    '<p style="font-family: Arial; color: black; font-size: 15px;">'
    "Bon j'ai 42 ans (bientôt 43...), maman de deux garçons géniaux, femme d'un mari génial... et bref ! ça va :)"
    '</p>',
    unsafe_allow_html=True   
)
    st.write("")
    st.write(
    '<p style="font-family: Arial; color: black; font-size: 15px;">'
    "Pourquoi cette page ? Bonne question... Après 20 au service de la finance et des actionnaires, j'ai sauté le pas de la reconversion et me voici en train de me former à la data !"
    '</p>',
    unsafe_allow_html=True   
)
    st.write(
    '<p style="font-family: Arial; color: black; font-size: 15px;">'
    "Quelle histoire hein ? Alors trois infos sur moi (y en a une de fausse, si tu trouves je t'offre un cadeau) : <br>"
    f"- <i class='fas fa-syringe'></i> Mon premier stage était à 10 ans dans un cabinet vétérinaire<br>"
    f"- <i class='fas fa-mountain'></i> Mon sport préféré est la varappe<br>"
    f"- <i class='fas fa-guitar'></i> J'ai fait partie d'un groupe de rock"
    '</p>',
    unsafe_allow_html=True
)
    st.write("**Ta réponse en commentaire de la validation de cette quête ;)**")
        
elif selected == "Photos" and st.session_state['authentication_status']:
    st.write(
    '<p style="font-family: Arial; color: black; font-size: 15px;">'
    "Voici quelques photos de mon voyage au Japon :)"
    '</p>',
    unsafe_allow_html=True   
)
    st.write("")
    st.write("")
    col1, col2, col3 = st.columns([5, 5,5])
    with col1:
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/1.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/2.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/3.jpg', width=150)
        
    with col2:
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/4.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/5.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/6.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/11.jpg', width=150)
    with col3:
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/7.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/8.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/9.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/12.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/13.jpg', width=150)
        st.image(f'https://raw.githubusercontent.com/PikaChou82/Advanced/refs/heads/main/Images/10.jpg', width=150)
    
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')


