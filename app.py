# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk  # ✅ For image preview
# import numpy as np
# import sys
# from py.recognition_module import * # ✅ Ensure this module exists

# class OutfitRecommenderApp:
#     """A Tkinter-based GUI for outfit recommendation."""

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Outfit Recommendation System")
#         self.root.geometry("900x600")
#         self.root.configure(bg="#2C2F33")

#         # Lists for storing outfit data
#         self.top = []
#         self.bottom = []
#         self.shoes = []

#         # Labels for categories
#         tk.Label(root, text="Top", fg="white", bg="#2C2F33", font=("Arial", 14)).grid(row=0, column=0, padx=10)
#         tk.Label(root, text="Bottom", fg="white", bg="#2C2F33", font=("Arial", 14)).grid(row=0, column=1, padx=10)
#         tk.Label(root, text="Shoes", fg="white", bg="#2C2F33", font=("Arial", 14)).grid(row=0, column=2, padx=10)

#         # Listboxes to display added items
#         self.top_list = tk.Listbox(root, width=30, height=10, bg="#23272A", fg="white")
#         self.bottom_list = tk.Listbox(root, width=30, height=10, bg="#23272A", fg="white")
#         self.shoe_list = tk.Listbox(root, width=30, height=10, bg="#23272A", fg="white")

#         self.top_list.grid(row=1, column=0, padx=10, pady=5)
#         self.bottom_list.grid(row=1, column=1, padx=10, pady=5)
#         self.shoe_list.grid(row=1, column=2, padx=10, pady=5)

#         # Buttons for Adding/Editing/Deleting
#         tk.Button(root, text="Add Photo", command=self.ALL_PREDICT, bg="#7289DA", fg="white", font=("Arial", 12)).grid(row=2, column=0, pady=5)
#         tk.Button(root, text="Generate Outfit", command=self.Generate, bg="#43B581", fg="white", font=("Arial", 12)).grid(row=2, column=1, pady=5)

#         # Image Labels for Preview
#         self.top_image_label = tk.Label(root, bg="#2C2F33")
#         self.bottom_image_label = tk.Label(root, bg="#2C2F33")
#         self.shoe_image_label = tk.Label(root, bg="#2C2F33")

#         self.top_image_label.grid(row=3, column=0, padx=10, pady=5)
#         self.bottom_image_label.grid(row=3, column=1, padx=10, pady=5)
#         self.shoe_image_label.grid(row=3, column=2, padx=10, pady=5)

#     def ALL_PREDICT(self):
#         """Loads an image, classifies it, and adds it to the appropriate category."""
#         file_path = filedialog.askopenfilename(title="Select an image")

#         if file_path:
#             sub, info, res_place_holder = single_classification(file_path)

#             if sub == "top":
#                 self.top_list.insert(tk.END, info)
#                 self.top.append(res_place_holder)

#             elif sub == "bottom":
#                 self.bottom_list.insert(tk.END, info)
#                 self.bottom.append(res_place_holder)

#             elif sub == "foot":
#                 self.shoe_list.insert(tk.END, info)
#                 self.shoes.append(res_place_holder)

#         else:
#             messagebox.showwarning("Warning", "No file selected.")

#     def Generate(self):
#         """Generates an outfit recommendation."""
#         top_right_season = [i for i in self.top if i[3] == toseason]
#         ad_top = np.random.choice(top_right_season or self.top)

#         helper_bot = [i for i in self.bottom if i[4] == ad_top[4]]
#         helper_sho = [i for i in self.shoes if i[4] == ad_top[4]]

#         ad_bot = np.random.choice(helper_bot or self.bottom)
#         ad_sho = np.random.choice(helper_sho or self.shoes)

#         self.display_image(ad_top[-1], self.top_image_label)
#         self.display_image(ad_bot[-1], self.bottom_image_label)
#         self.display_image(ad_sho[-1], self.shoe_image_label)

#     def display_image(self, img_path, label):
#         """Displays an image on the given Tkinter label."""
#         image = Image.open(img_path)
#         image = image.resize((150, 150))
#         photo = ImageTk.PhotoImage(image)

#         label.configure(image=photo)
#         label.image = photo  # Keep a reference

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = OutfitRecommenderApp(root)
#     root.mainloop()









# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk
# from PIL import Image, ImageTk  # ✅ For image preview
# import numpy as np
# import sys
# from py.recognition_module import *  # ✅ Ensure this module exists

# class OutfitRecommenderApp:
#     """A Tkinter-based GUI for outfit recommendation with an enhanced interface."""

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Outfit Recommendation System")
#         self.root.geometry("950x650")
#         self.root.configure(bg="#2C2F33")

#         # ====== Frames for Better Layout ======
#         self.top_frame = tk.Frame(root, bg="#2C2F33")
#         self.top_frame.pack(pady=10)

#         self.middle_frame = tk.Frame(root, bg="#2C2F33")
#         self.middle_frame.pack(pady=5)

#         self.bottom_frame = tk.Frame(root, bg="#2C2F33")
#         self.bottom_frame.pack(pady=10)

#         # ====== Outfit Category Labels ======
#         ttk.Label(self.top_frame, text="Top", foreground="white", background="#2C2F33",
#                   font=("Arial", 14)).grid(row=0, column=0, padx=20)
#         ttk.Label(self.top_frame, text="Bottom", foreground="white", background="#2C2F33",
#                   font=("Arial", 14)).grid(row=0, column=1, padx=20)
#         ttk.Label(self.top_frame, text="Shoes", foreground="white", background="#2C2F33",
#                   font=("Arial", 14)).grid(row=0, column=2, padx=20)

#         # ====== Listboxes for Outfit Selection ======
#         self.top_list = tk.Listbox(self.top_frame, width=30, height=8, bg="#23272A", fg="white", bd=0,
#                                    highlightthickness=0, selectbackground="#7289DA", font=("Arial", 12))
#         self.bottom_list = tk.Listbox(self.top_frame, width=30, height=8, bg="#23272A", fg="white", bd=0,
#                                       highlightthickness=0, selectbackground="#7289DA", font=("Arial", 12))
#         self.shoe_list = tk.Listbox(self.top_frame, width=30, height=8, bg="#23272A", fg="white", bd=0,
#                                     highlightthickness=0, selectbackground="#7289DA", font=("Arial", 12))

#         self.top_list.grid(row=1, column=0, padx=20, pady=5)
#         self.bottom_list.grid(row=1, column=1, padx=20, pady=5)
#         self.shoe_list.grid(row=1, column=2, padx=20, pady=5)

#         # ====== Buttons with Hover Effects ======
#         self.add_photo_btn = ttk.Button(self.middle_frame, text="📸 Add Photo", command=self.ALL_PREDICT,
#                                         style="TButton")
#         self.generate_btn = ttk.Button(self.middle_frame, text="🎲 Generate Outfit", command=self.Generate,
#                                        style="TButton")

#         self.add_photo_btn.grid(row=0, column=0, padx=10, pady=10)
#         self.generate_btn.grid(row=0, column=1, padx=10, pady=10)

#         # ====== Image Labels for Preview ======
#         self.top_image_label = tk.Label(self.bottom_frame, bg="#2C2F33")
#         self.bottom_image_label = tk.Label(self.bottom_frame, bg="#2C2F33")
#         self.shoe_image_label = tk.Label(self.bottom_frame, bg="#2C2F33")

#         self.top_image_label.grid(row=0, column=0, padx=10, pady=5)
#         self.bottom_image_label.grid(row=0, column=1, padx=10, pady=5)
#         self.shoe_image_label.grid(row=0, column=2, padx=10, pady=5)

#         # Apply Hover Effect
#         self.add_photo_btn.bind("<Enter>", lambda e: self.add_photo_btn.configure(style="Hover.TButton"))
#         self.add_photo_btn.bind("<Leave>", lambda e: self.add_photo_btn.configure(style="TButton"))
#         self.generate_btn.bind("<Enter>", lambda e: self.generate_btn.configure(style="Hover.TButton"))
#         self.generate_btn.bind("<Leave>", lambda e: self.generate_btn.configure(style="TButton"))

#         # Outfit Data
#         self.top = []
#         self.bottom = []
#         self.shoes = []

#     def ALL_PREDICT(self):
#         """Loads an image, classifies it, and adds it to the appropriate category."""
#         file_path = filedialog.askopenfilename(title="Select an image")

#         if file_path:
#             sub, info, res_place_holder = single_classification(file_path)

#             if sub == "top":
#                 self.top_list.insert(tk.END, info)
#                 self.top.append(res_place_holder)

#             elif sub == "bottom":
#                 self.bottom_list.insert(tk.END, info)
#                 self.bottom.append(res_place_holder)

#             elif sub == "foot":
#                 self.shoe_list.insert(tk.END, info)
#                 self.shoes.append(res_place_holder)

#         else:
#             messagebox.showwarning("Warning", "No file selected.")

#     def Generate(self):
#         """Generates an outfit recommendation."""
#         if not self.top or not self.bottom or not self.shoes:
#             messagebox.showerror("Error", "Please add at least one top, bottom, and shoes before generating an outfit.")
#             return

#         ad_top = np.random.choice(self.top)
#         ad_bot = np.random.choice(self.bottom)
#         ad_sho = np.random.choice(self.shoes)

#         self.display_image(ad_top[-1], self.top_image_label)
#         self.display_image(ad_bot[-1], self.bottom_image_label)
#         self.display_image(ad_sho[-1], self.shoe_image_label)

#     def display_image(self, img_path, label):
#         """Displays an image on the given Tkinter label."""
#         image = Image.open(img_path)
#         image = image.resize((200, 200))
#         photo = ImageTk.PhotoImage(image)

#         label.configure(image=photo)
#         label.image = photo  # Keep a reference

# if __name__ == "__main__":
#     # Create and configure styles
#     root = tk.Tk()
#     style = ttk.Style()
#     style.configure("TButton", font=("Arial", 12), padding=8, background="#7289DA", foreground="white")
#     style.configure("Hover.TButton", background="#5A6EA7")

#     app = OutfitRecommenderApp(root)
#     root.mainloop()
#     root.lift()
#     root.attributes('-topmost', True)
#     root.after(1000, lambda: root.attributes('-topmost', False))  # Ensures it doesn't stay always on top



# import streamlit as st
# import random
# from PIL import Image
# import io


# # Simulated classification function
# def single_classification(image):
#     categories = ["top", "bottom", "foot"]
#     sub = random.choice(categories)
#     info = f"{sub.capitalize()} - Sample Item"
#     return sub, info

# # Store uploaded items
# if "tops" not in st.session_state:
#     st.session_state.tops = []
# if "bottoms" not in st.session_state:
#     st.session_state.bottoms = []
# if "shoes" not in st.session_state:
#     st.session_state.shoes = []

# st.title("OutfitX: Where Style Meets Simplicity🔥👕✨")

# # Sidebar - Upload clothing images
# st.sidebar.header("Upload Clothing Items")
# uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# if uploaded_file:
#     # Convert uploaded file to an image object
#     image = Image.open(uploaded_file)
    
#     # Convert image to bytes for storing in session state
#     img_bytes = io.BytesIO()
#     image.save(img_bytes, format="PNG")  # Save image as PNG in memory
#     img_bytes = img_bytes.getvalue()

#     st.sidebar.image(image, caption="Uploaded Image", use_container_width=True)

#     if st.sidebar.button("Classify and Add"):
#         sub, info = single_classification(image)
        
#         if sub == "top":
#             st.session_state.tops.append((info, img_bytes))
#         elif sub == "bottom":
#             st.session_state.bottoms.append((info, img_bytes))
#         elif sub == "foot":
#             st.session_state.shoes.append((info, img_bytes))
        
#         st.sidebar.success(f"✅ {info} added!")

# # Display clothing collection
# st.header("Seamless Style: Effortless Fashion, Every Day✨ ")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.subheader("👕 Tops")
#     for idx, (label, img) in enumerate(st.session_state.tops):
#         st.image(Image.open(io.BytesIO(img)), caption=label, width=100)
#         if st.button(f"🗑️ Remove", key=f"top_{idx}"):
#             st.session_state.tops.pop(idx)
#             st.rerun()

# with col2:
#     st.subheader("👖 Bottoms")
#     for idx, (label, img) in enumerate(st.session_state.bottoms):
#         st.image(Image.open(io.BytesIO(img)), caption=label, width=100)
#         if st.button(f"🗑️ Remove", key=f"bottom_{idx}"):
#             st.session_state.bottoms.pop(idx)
#             st.rerun()

# with col3:
#     st.subheader("👟 Shoes")
#     for idx, (label, img) in enumerate(st.session_state.shoes):
#         st.image(Image.open(io.BytesIO(img)), caption=label, width=100)
#         if st.button(f"🗑️ Remove", key=f"shoe_{idx}"):
#             st.session_state.shoes.pop(idx)
#             st.rerun()

# # Generate outfit recommendation
# if st.button("👗 Generate Outfit Recommendation"):
#     if not st.session_state.tops or not st.session_state.bottoms or not st.session_state.shoes:
#         st.warning("⚠️ Please add more clothing items to generate an outfit.")
#     else:
#         top_choice = random.choice(st.session_state.tops)
#         bottom_choice = random.choice(st.session_state.bottoms)
#         shoe_choice = random.choice(st.session_state.shoes)

#         st.subheader("Today's Recommended Outfit:")
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.image(Image.open(io.BytesIO(top_choice[1])), caption=top_choice[0], width=200)
#         with col2:
#             st.image(Image.open(io.BytesIO(bottom_choice[1])), caption=bottom_choice[0], width=200)
#         with col3:
#             st.image(Image.open(io.BytesIO(shoe_choice[1])), caption=shoe_choice[0], width=200)












import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="streamlit")


import streamlit as st
import datetime
import random
import os
from PIL import Image
# from py.recognition_module import single_classification
# from py.recognition_module import * 
import uuid
import hashlib
import base64

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


# --------------------------
# Helper Functions
# --------------------------

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

