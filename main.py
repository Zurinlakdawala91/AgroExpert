import streamlit as st


from streamlit_option_menu import option_menu

import home, crop_recommendation

st.set_page_config(
    page_title="AgroExpert",
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run():
        with st.sidebar:
            main = option_menu(
                menu_title='AgroExpert 🌱',
                options=['Home','Crop Recommendation'],
                icons=['house-fill','sheaf-of-rice'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},})
            

        if main=='Home':
            home.main()
        if main=='Crop Recommendation':
            crop_recommendation.main()
    run()
            