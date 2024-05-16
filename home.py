import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def main():
    
    
    # ---- LOAD ASSETS ----
    lottie_coding = load_lottieurl("https://lottie.host/4c5442ce-2152-4f42-947e-880c68a0dc10/EZUmNlsm1v.json")
    

    st.title(
    """AgroExpert"""
            )
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        
        with left_column:
            
            st.write("##")
            st.write(
                """
                In our project, we're dedicated to empowering farmers, gardeners, and agricultural enthusiasts with expert knowledge and resources to cultivate thriving crops and sustainable practices. Whether you're a seasoned farmer looking to optimize your yields or a novice gardener eager to learn the ropes, you've come to the right place.

                Our mission is simple: to be your trusted partner in navigating the complexities of agriculture, offering insights, guidance, and practical solutions tailored to your needs. Through our comprehensive articles, hands-on advice, and personalized consultations, we're here to support you every step of the way on your agricultural journey.

                Explore our site to discover a wealth of information, from crop cultivation techniques to pest management strategies, market insights, and beyond. Join us in cultivating a greener, more prosperous future for agriculture.
                """
            )
            
        with right_column:
            st_lottie(lottie_coding, height=500, key="coding",width="300")


    
if __name__ == "__main__":
    main()
