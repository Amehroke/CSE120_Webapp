import streamlit as st


# Insert containers separated into tabs:
tab1, tab2 = st.sidebar.tabs(["Image", "Defects"])
tab1.write("Please Enter Silicon Wafer Dimensions")

# You can also use "with" notation:
with tab1:
    # Wafer Width
    w = st.number_input("Wafer Width")
    rndw = st.checkbox('Randomize', key='rndw_key')

    # Wafer Height
    h = st.number_input("Wafer Height")
    rndh = st.checkbox('Randomize', key='rndh_key')

    # Vertical Line Thickness
    vt = st.number_input("Verical Line Thickness")
    rndvt = st.checkbox('Randomize', key='rndvt_key')

    # Horizontal Line Thickness
    ht = st.number_input("Horizontal Line Thickness")
    rndht = st.checkbox('Randomize', key='rndht_key')

    # Width of Grid
    wg = st.number_input("Width of Grid")
    rndwg = st.checkbox('Randomize', key='rndwg_key')

    # Height of Grid
    hg = st.number_input("Height of Grid")
    rndhg = st.checkbox('Randomize', key='rndhg_key')
    

with tab2:
    st.write("Please Enter Defects")
    #spot defects
    spot = st.number_input("Number of Spot Defects")
    rndSp = st.checkbox('Randomize', key='rndSp_key')
    
    #Scratch defects
    scratch = st.number_input("Number of Scratch Defects")
    rndSc = st.checkbox('Randomize', key='rndSc_key')
    
    #Cloudy defects
    cloudy = st.number_input("Number of Cloudy Defects")
    rndCl = st.checkbox('Randomize', key='rndCl_key')
    
    #Radial defects
    radial = st.number_input("Number of Radial Defects")
    rndRd = st.checkbox('Randomize', key='rndRd_key')
    
    submit_button1 = st.button('Submit', key='submit_button1')
    



# Create columns within the container
col1, col2,= st.columns([1, 1])

# Place images into the columns
with col1:
    st.image('./Image/Screenshot 2023-10-19 at 10.13.39 PM.png')
    st.write("Caption for Image 1")
    
with col2:
    st.write("Details for image 1")
    
col3, col4,= st.columns([1, 1])

with col3:
    st.image('./Image/Screenshot 2023-10-19 at 10.13.39 PM.png')
    st.write("Caption for Image 2")

with col4:
    st.image('./Image/Screenshot 2023-10-19 at 10.13.39 PM.png')
