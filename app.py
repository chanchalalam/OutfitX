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



import streamlit as st
import random
from PIL import Image
import io

# Simulated classification function
def single_classification(image):
    categories = ["top", "bottom", "foot"]
    sub = random.choice(categories)
    info = f"{sub.capitalize()} - Sample Item"
    return sub, info

# Store uploaded items
if "tops" not in st.session_state:
    st.session_state.tops = []
if "bottoms" not in st.session_state:
    st.session_state.bottoms = []
if "shoes" not in st.session_state:
    st.session_state.shoes = []

st.title("OutfitX: Where Style Meets Simplicity🔥👕✨")

# Sidebar - Upload clothing images
st.sidebar.header("Upload Clothing Items")
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Convert uploaded file to an image object
    image = Image.open(uploaded_file)
    
    # Convert image to bytes for storing in session state
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")  # Save image as PNG in memory
    img_bytes = img_bytes.getvalue()

    st.sidebar.image(image, caption="Uploaded Image", use_container_width=True)

    if st.sidebar.button("Classify and Add"):
        sub, info = single_classification(image)
        
        if sub == "top":
            st.session_state.tops.append((info, img_bytes))
        elif sub == "bottom":
            st.session_state.bottoms.append((info, img_bytes))
        elif sub == "foot":
            st.session_state.shoes.append((info, img_bytes))
        
        st.sidebar.success(f"✅ {info} added!")

# Display clothing collection
st.header("Seamless Style: Effortless Fashion, Every Day✨ ")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👕 Tops")
    for idx, (label, img) in enumerate(st.session_state.tops):
        st.image(Image.open(io.BytesIO(img)), caption=label, width=100)
        if st.button(f"🗑️ Remove", key=f"top_{idx}"):
            st.session_state.tops.pop(idx)
            st.rerun()

with col2:
    st.subheader("👖 Bottoms")
    for idx, (label, img) in enumerate(st.session_state.bottoms):
        st.image(Image.open(io.BytesIO(img)), caption=label, width=100)
        if st.button(f"🗑️ Remove", key=f"bottom_{idx}"):
            st.session_state.bottoms.pop(idx)
            st.rerun()

with col3:
    st.subheader("👟 Shoes")
    for idx, (label, img) in enumerate(st.session_state.shoes):
        st.image(Image.open(io.BytesIO(img)), caption=label, width=100)
        if st.button(f"🗑️ Remove", key=f"shoe_{idx}"):
            st.session_state.shoes.pop(idx)
            st.rerun()

# Generate outfit recommendation
if st.button("👗 Generate Outfit Recommendation"):
    if not st.session_state.tops or not st.session_state.bottoms or not st.session_state.shoes:
        st.warning("⚠️ Please add more clothing items to generate an outfit.")
    else:
        top_choice = random.choice(st.session_state.tops)
        bottom_choice = random.choice(st.session_state.bottoms)
        shoe_choice = random.choice(st.session_state.shoes)

        st.subheader("Today's Recommended Outfit:")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(Image.open(io.BytesIO(top_choice[1])), caption=top_choice[0], width=200)
        with col2:
            st.image(Image.open(io.BytesIO(bottom_choice[1])), caption=bottom_choice[0], width=200)
        with col3:
            st.image(Image.open(io.BytesIO(shoe_choice[1])), caption=shoe_choice[0], width=200)
