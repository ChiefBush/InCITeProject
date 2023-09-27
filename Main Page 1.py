# Menu Page 1: Admin or User
# Create radio buttons for Admin and User
user_type = tk.StringVar()
user_type.set("User")
admin_radio = tk.Radiobutton(root, text="Admin", variable=user_type, value="Admin")
user_radio = tk.Radiobutton(root, text="User", variable=user_type, value="User")
admin_radio.pack()
user_radio.pack()
