import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="streamlit")


import streamlit as st
import datetime
import random
import os
from PIL import Image
# from py.recognition_module1 import single_classification
import uuid
import hashlib
import base64
import numpy as np
# --------------------------
# Helper Functions
# --------------------------

def single_classification(single_path):
    
    """
    This function take a single path of a photo, then do reshape to fit the models, and do classification
    Input is a path of a certain photo
    Output is a tuple which contains subtype(for being send to a correct sub-model), 
                                     info(a string having all info of a clothes), 
                                     res(a list having all info of a clothes)
    """
    
    # Our model only applies to dataframes. 
    # Therefore, in order to enable the model to predict a single picture, 
    # we turn this picture into a dataframe with only one row.
    train_images = np.zeros((1,80,60,3))
  
    path = single_path#/content/images   
    img = cv2.imread(path)
    
    #reshape img to apply the model
    if img.shape != (80,60,3):
        img = image.load_img(path, target_size=(80,60,3))

    train_images[0] = img

    
    result2 = sub_list[np.argmax(sub_model.predict(train_images))]
    
    # According to the results of the first model, branch to three other models
    if result2=="top":
        res = single_helper(train_images,top_model,top_list)
    elif result2=="bottom":
        res = single_helper(train_images,bottom_model,bottom_list)
    elif result2=="foot":
        res = single_helper(train_images,foot_model,foot_list)
    res.append(single_path)
    res_str = f"{res[0]}, {res[1]}, {color_classification(single_path)}, {res[3]}, {res[4]}, {single_path}" 
    
    return (result2,res_str,res)


def compute_file_hash(uploaded_file):
    """Compute MD5 hash of uploaded file content"""
    return hashlib.md5(uploaded_file.getvalue()).hexdigest()

def get_current_season():
    month = datetime.datetime.now().month
    if 3 <= month <= 5:
        return 'spring'
    elif 6 <= month <= 8:
        return 'summer'
    elif 9 <= month <= 11:
        return 'autumn'
    else:
        return 'winter'

def initialize_session_state():
    if 'tops' not in st.session_state:
        st.session_state.tops = []
    if 'bottoms' not in st.session_state:
        st.session_state.bottoms = []
    if 'shoes' not in st.session_state:
        st.session_state.shoes = []
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'processed_hashes' not in st.session_state:
        st.session_state.processed_hashes = set()
    if 'uploader_key' not in st.session_state:
        st.session_state.uploader_key = 0

def save_uploaded_file(uploaded_file):
    try:
        file_path = os.path.join('uploads', uploaded_file.name)
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        return None

# --------------------------
# UI Functions
# --------------------------

def display_category(items, category_name):
    """Displays clothing items with a hover button for details"""
    if not items:
        st.info(f"No {category_name} available. Upload items using the sidebar!")
        return

    for idx, item in enumerate(items):
        cols = st.columns([1, 4])

        with cols[0]:
            try:
                st.image(item['thumbnail'], use_container_width=True)
            except Exception as e:
                st.error(f"Error loading thumbnail: {str(e)}")

        with cols[1]:
            with st.expander("🔍 Item Details"):
                st.markdown(f"**{item['name']}**")
                st.markdown(f"- **Category:** {category_name.title()}")
                st.markdown(f"- **Season:** {item['season'].title()}")
                st.markdown(f"- **Style:** {item['style'].title()}")

                if st.button(f"🗑 Delete {item['name']}", key=f"del_{category_name}_{idx}"):
                    st.session_state[category_name].pop(idx)
                    st.session_state.processed_hashes = {i['file_hash'] for i in 
                                                         st.session_state.tops + 
                                                         st.session_state.bottoms + 
                                                         st.session_state.shoes}
                    st.rerun()

# --------------------------
# Main Application
# --------------------------

def main():
    initialize_session_state()
    
    st.title("OutfitX - Effortless Fashion, Every Day 👗✨")
    st.markdown("---")

    # --------------------------
    # Sidebar - File Upload
    # --------------------------
    
    with st.sidebar:
    
        st.header("📤✨ Add to Your Closet!")
        uploaded_files = st.file_uploader(
        "📸 Upload Your Stylish Pieces",
        type=["png", "jpg", "jpeg", "bmp", "gif"],
        accept_multiple_files=True,
        key=f"file_uploader_{st.session_state.uploader_key}"
        )

        if uploaded_files:
            new_hashes = set()
            for uploaded_file in uploaded_files:
                file_hash = compute_file_hash(uploaded_file)

                if file_hash in st.session_state.processed_hashes:
                    st.warning(f"⚠️ {uploaded_file.name} already exists")
                    continue

                file_path = save_uploaded_file(uploaded_file)
                if file_path:
                    try:
                        sub, info, res_place_holder = single_classification(file_path)
                        item = {
                            "id": str(uuid.uuid4()),
                            "name": info,
                            "season": res_place_holder[3],
                            "style": res_place_holder[4],
                            "image_path": file_path,
                            "thumbnail": Image.open(file_path).resize((100, 100)),
                            "file_hash": file_hash
                        }

                        if sub == "top":
                            st.session_state.tops.append(item)
                        elif sub == "bottom":
                            st.session_state.bottoms.append(item)
                        elif sub == "foot":
                            st.session_state.shoes.append(item)

                        st.success(f"Added {sub}: {info}")
                        new_hashes.add(file_hash)
                    except Exception as e:
                        st.error(f"Error processing {uploaded_file.name}: {str(e)}")

            if new_hashes:
                st.session_state.processed_hashes.update(new_hashes)
                st.session_state.uploader_key += 1
                st.rerun()

        # --------------------------
        # Manually Re-Add Deleted Item
        # --------------------------
        st.header("🔄 Re-Add Deleted Item Manually")

        re_add_name = st.text_input("Item Name")
        re_add_category = st.selectbox("Category", ["Top", "Bottom", "Shoe"])
        re_add_season = st.selectbox("Season", ["Spring", "Summer", "Autumn", "Winter"])
        re_add_style = st.selectbox("Style" , ["Casual", "Formal", "Sport"])
        re_add_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

        if st.button("✅ Add Item"):
            if not re_add_name or not re_add_style or not re_add_image:
                st.warning("⚠️ Please fill in all fields and upload an image.")
            else:
                file_path = save_uploaded_file(re_add_image)
                if file_path:
                    item = {
                        "id": str(uuid.uuid4()),
                        "name": re_add_name,
                        "season": re_add_season.lower(),
                        "style": re_add_style.lower(),
                        "image_path": file_path,
                        "thumbnail": Image.open(file_path).resize((100, 100)),
                        "file_hash": compute_file_hash(re_add_image)
                    }

                    if re_add_category.lower() == "top":
                        st.session_state.tops.append(item)
                    elif re_add_category.lower() == "bottom":
                        st.session_state.bottoms.append(item)
                    elif re_add_category.lower() == "shoe":
                        st.session_state.shoes.append(item)

                    st.success(f"✅ Successfully re-added: {re_add_name} ({re_add_category})")

    # Display Items
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("👚 Tops Collection")
        display_category(st.session_state.tops, "tops")

    with col2:
        st.subheader("👖 Bottoms Collection")
        display_category(st.session_state.bottoms, "bottoms")

    with col3:
        st.subheader("👟 Shoes Collection")
        display_category(st.session_state.shoes, "shoes")

    st.markdown("---")

    # Outfit Recommendation
    if st.button("✨ Generate Smart Outfit Recommendation"):
        if not st.session_state.tops or not st.session_state.bottoms or not st.session_state.shoes:
            st.warning("Please add items in all categories first!")
            return

        current_season = get_current_season()

        def filter_items(items):
            return [item for item in items]

        tops = filter_items(st.session_state.tops)
        bottoms = filter_items(st.session_state.bottoms)
        shoes = filter_items(st.session_state.shoes)

        seasonal_tops = [t for t in tops if t["season"].lower() == current_season]
        top = random.choice(seasonal_tops if seasonal_tops else tops)

        matching_bottoms = [b for b in bottoms if b["style"] == top["style"]]
        bottom = random.choice(matching_bottoms if matching_bottoms else bottoms)

        matching_shoes = [s for s in shoes if s["style"] == top["style"]]
        shoe = random.choice(matching_shoes if matching_shoes else shoes)

        st.subheader("🌟 Today's Perfect Outfit")

        cols = st.columns(3)

        with cols[0]:
            st.markdown("### Top")
            st.image(top["image_path"], use_container_width=True)
            st.markdown(f"**{top['name']}**\n\n- **Style:** {top['style'].title()}\n- **Season:** {top['season'].title()}")

        with cols[1]:
            st.markdown("### Bottom")
            st.image(bottom["image_path"], use_container_width=True)
            st.markdown(f"**{bottom['name']}**\n\n- **Style:** {bottom['style'].title()}\n- **Season:** {bottom['season'].title()}")

        with cols[2]:
            st.markdown("### Shoes")
            st.image(shoe["image_path"], use_container_width=True)
            st.markdown(f"**{shoe['name']}**\n\n- **Style:** {shoe['style'].title()}\n- **Season:** {shoe['season'].title()}")

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    main()

