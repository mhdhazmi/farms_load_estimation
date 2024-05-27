import streamlit as st
import pandas as pd
import random
import pydeck as pdk
import options

# Function to fill in random values
def random_fill():
    random_text = "Random text " + str(random.randint(1, 100))
    random_long_text = "This is a longer piece of random text " + str(random.randint(1, 100))
    random_number = random.randint(0, 100)
    random_main_type = random.choice(options.main_type_values)
    random_multi_select = random.sample(["Option A", "Option B", "Option C"], k=2)
    random_dynamic_input = "Option 1,Option 2,Option 3"
    return random_text, random_long_text, random_number, random_main_type, random_multi_select, random_dynamic_input

# Main function
def main():
    st.set_page_config(layout="wide")

    # Display logo at the top
    st.image("MOE_logo.png", width=150)

    # Navigation state
    if 'page' not in st.session_state:
        st.session_state.page = 0

    if st.session_state.page == 0:
        page_1()
    elif st.session_state.page == 1:
        page_2()
    elif st.session_state.page == 2:
        page_3()

def page_1():
    st.title("Farms Electrical Load Estimation")

    st.header("File Uploader")
    st.subheader("Make sure all the fields are filled correctly in your excel sheet.")
    uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
    if uploaded_file is not None:
        st.write("File uploaded successfully")
        # Handle file processing based on file type
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            st.write(df)
        elif uploaded_file.type == "text/plain":
            st.text(uploaded_file.read().decode("utf-8"))

    st.header("Farm Information (HASAR)")

    random_fill_button = st.button("Fill Form with Typical Values")

    if random_fill_button:
        random_text, random_long_text, random_number, random_main_type, random_multi_select, random_dynamic_input = random_fill()
    else:
        random_text = random_long_text = random_dynamic_input = ""
        random_number = 2
        random_main_type = "Category 1"
        random_multi_select = []

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        farm_id = st.text_input("Enter your farm id", value=random_text)
        main_type = st.selectbox(
            "Select the main type of your farm",
            options.main_type_values,
            index=options.main_type_values.index(random_main_type) if random_main_type in options.main_type_values else 0
        )
        area = st.number_input(
            "What is the area of your farm in m^2",
            min_value=0.0,
            max_value=100.0,
            value=float(random_number),
            step=0.00001,
        )
        plantations = st.number_input(
            "How many plantations are in your farm?",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )

    with col2:
        owner_name = st.text_input("Enter the farm owner name", value=random_text)
        region = st.selectbox(
            "Select the region",
            options.region_values,
        )
        activities = st.number_input(
            "How many activities are in your farm?",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )
        plantations_type = st.selectbox(
            "Select the type of plantations",
            options.plantations_type_values,
        )

    with col3:
        national_id = st.number_input(
            "Enter the farm owner national ID",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )
        x_coordinate = st.number_input(
            "Enter the longitude of your farm",
            min_value=0.0,
            max_value=100.0,
            value=float(random_number),
            step=0.00001,
        )

        trees = st.number_input(
            "How many trees are in your farm?",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )

    with col4:
        phone_number = st.number_input(
            "Enter the farm owner phone number",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )
        y_coordinate = st.number_input(
            "Enter the latitude of your farm",
            min_value=0.0,
            max_value=100.0,
            value=float(random_number),
            step=0.00001,
        )

        protected_houses = st.number_input(
            "How many protected houses are in your farm?",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )

    st.header("Farms Equipment Information (Visits)")
    show_extra_fields = st.checkbox("Do you have information about Electrical and Mechanical equipment in the farm?")

    if show_extra_fields:
        st.subheader("Additional Input Fields")
       
        extra_field1 = st.number_input(
            "How many sprinklers are in your farm?",
            min_value=0,
            max_value=5,
            value=random_number,
            step=1,
        )
        extra_field2 = st.number_input(
            "How many Mechanical Heads are in your farm?",
            min_value=0,
            max_value=10,
            value=random_number,
            step=1,
        )
        extra_field3 = st.number_input(
            "How many Electrical Heads are in your farm?",
            min_value=0,
            max_value=10,
            value=random_number,
            step=1,
        )
        
        
        extra_field5 = st.number_input(
            "How many Pumps are in your farm?",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )
        
        extra_field6 = st.number_input(
            "How many Submersible Pumps are in your farm?",
            min_value=0,
            max_value=100,
            value=random_number,
            step=1,
        )

    col1, col2 = st.columns(2)
    with col2:
        if st.button("Next Step"):
            st.session_state.farm_id = farm_id
            st.session_state.main_type = main_type
            st.session_state.area = area
            st.session_state.plantations = plantations
            st.session_state.owner_name = owner_name
            st.session_state.region = region
            st.session_state.activities = activities
            st.session_state.national_id = national_id
            st.session_state.x_coordinate = x_coordinate
            st.session_state.trees = trees
            st.session_state.phone_number = phone_number
            st.session_state.y_coordinate = y_coordinate
            st.session_state.protected_houses = protected_houses
            if show_extra_fields:
                st.session_state.extra_field1 = extra_field1
                st.session_state.extra_field2 = extra_field2
                st.session_state.extra_field3 = extra_field3
            st.session_state.page = 1
            st.experimental_rerun()

def page_2():
    st.title("Additional Information")

    st.header("Wells Information")
    num_wells = st.session_state.get('plantations', 0)
    if num_wells > 0:
        for i in range(num_wells):
            st.write(f"### Well {i+1}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.selectbox(f"Status of Well {i+1}", ["Active", "Abandoned"], key=f"well_status_{i}")
                st.selectbox(f"Type of Well Irrigation  {i+1}", options.irrigation_type_values, key=f"well_type_{i}")
            with col2:
                st.text_input(f"Location of Well {i+1}", key=f"well_location_{i}")
            with col3:
                st.selectbox(f"Source of Water for Well {i+1}",options.irrigation_source_values , key=f"well_source_{i}")

    st.header("Farm Activities Information")
    num_activities = st.session_state.get('activities', 0)
    if num_activities > 0:
        for i in range(num_activities):
            st.write(f"### Activity {i+1}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.selectbox(f"Status of Farm Activity {i+1}", ["Active", "Abandoned"], key=f"farm_activity_status_{i}")
                st.selectbox(f"Season of Farm Activity {i+1}", options.farming_season_values, key=f"farm_activity_season_{i}")
            with col2:
                st.selectbox(f"Type of Farm Activity {i+1}", options.farm_type_values, key=f"farm_type_activity_{i}")
            with col3:
                st.selectbox(f"Main Crop Type of Farm Activity {i+1}", options.main_crops_type_values, key=f"main_crop_activity_{i}")
                
                

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go Back"):
            st.session_state.page = 0
            st.experimental_rerun()
    with col2:
        if st.button("Next"):
            st.session_state.page = 2
            st.experimental_rerun()

def page_3():
    st.title("Summary and Map")

    st.subheader("The estimated electrical consumption for the farm is between  X kW and Y kW")
    st.header("Farm Location Map")

    # Sample data for the map (you can replace this with actual data)
    map_data = pd.DataFrame({
        'lat': [st.session_state.get('y_coordinate', 0)],
        'lon': [st.session_state.get('x_coordinate', 0)]
    })

    # Create a deck.gl map using pydeck with satellite style
    layer = pdk.Layer(
        "ScatterplotLayer",
        map_data,
        get_position="[lon, lat]",
        get_color="[200, 30, 0, 160]",
        get_radius=200,
    )
    view_state = pdk.ViewState(
        latitude=26.440113,	 # st.session_state.get('y_coordinate', 0),
        longitude=43.713412,	 # st.session_state.get('x_coordinate', 0),
        zoom=12,
        pitch=0,
    )
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/satellite-v9",
        # tooltip={"text": "Latitude: {lat}\nLongitude: {lon}"}
        tooltip= True
    )
    st.pydeck_chart(r)

    if st.button("Go Back"):
        st.session_state.page = 1
        st.experimental_rerun()

if __name__ == "__main__":
    main()
