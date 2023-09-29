import tkinter as tk

# Define global variables for registration form fields
name_entry = None
email_entry = None
phone_entry = None
submission_entry = None
university_entry = None
dob_entry = None
doi_entry = None

def on_button_click(button_text):
    global name_entry, email_entry, phone_entry, submission_entry, university_entry, dob_entry, doi_entry

    if button_text == "Home":
        content_label.config(text="Welcome to InCITe 2024!", font=("Arial", 24, "bold"))
        content_text.config(text="")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "About":
        add_content("About", "The impact of the 4th Industrial revolution has changed how we live, work and communicate. This revolution is largely driven by four specific technical areas like high speed mobile Internet, AI Automation with augmentation, the use of big data analytics and cloud computing. It's reshaping government, education, healthcare, and commerce—almost every aspect of life. In the future, it can also change the things we value and the way we value them. The purpose of International Conference on Information Technology InCITe 2023 Next Generation Technology Summit on the theme Decision Intelligence: Transform Your World is to explore and discover the practical aspects of Decision Intelligence and its impact on society.")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "Committees":
        add_content("Committees", "The organizing committee is responsible for planning and executing the conference. The program committee oversees the selection of papers and presentations. The advisory committee provides guidance and expertise to ensure the success of the conference. Our dedicated team of professionals is committed to delivering an outstanding conference experience for all participants.")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "Speakers":
        add_content("Speakers", "We are honored to have a distinguished lineup of speakers who are experts in various fields of Information Technology. They will share their knowledge and insights with the attendees, providing valuable perspectives on the latest advancements in the industry. Our speakers represent a diverse range of backgrounds and experiences, offering a comprehensive view of the IT landscape.")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "Registration":
        display_registration_form()
    elif button_text == "Sponsorship":
        add_content("Sponsorship", "Become a sponsor and showcase your brand to a global audience. Various sponsorship packages are available to suit your marketing goals. Contact us for more information on how you can partner with us for InCITe 2024.")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "Past Conferences":
        add_content("Past Conferences", "Explore our previous conferences and gain insights into the diverse range of topics covered, along with the esteemed speakers who graced our events. Visit our archive section to delve into the history of InCITe.")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "PhD Symposium":
        add_content("PhD Symposium", "The PhD Symposium provides a platform for doctoral students to present and discuss their research with peers and experts. Submit your research proposal for consideration and join us for this enriching experience.")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "Contact us":
        add_content("Contact Us", "For any inquiries or assistance, feel free to reach out to us at info@incite2024.com. We're here to help and look forward to hearing from you.")
        # Clear registration form fields
        clear_registration_form()
    elif button_text == "Program Schedule":
        add_content("Program Schedule", "View the detailed program schedule for InCITe 2024. Stay tuned for updates on session topics and speakers. Plan your participation to make the most of this knowledge-packed event.")
        # Clear registration form fields
        clear_registration_form()

def add_content(title, text):
    content_label.config(text=title, font=("Arial", 16, "bold"))
    content_text.config(text=text, font=("Arial", 12), wraplength=600)

def display_registration_form():
    global name_entry, email_entry, phone_entry, submission_entry, university_entry, dob_entry, doi_entry

    content_label.config(text="Call for Papers - Registration", font=("Arial", 24, "bold"))
    
    # Clear previous content and form fields
    content_text.config(text="")
    clear_registration_form()

    # Create form fields
    name_label = tk.Label(content_frame, text="Name:", font=("Arial", 12), bg='#ffffff')
    name_label.pack(anchor='w')
    name_entry = tk.Entry(content_frame, font=("Arial", 12), width=40)
    name_entry.pack(anchor='w')

    email_label = tk.Label(content_frame, text="Email:", font=("Arial", 12), bg='#ffffff')
    email_label.pack(anchor='w')
    email_entry = tk.Entry(content_frame, font=("Arial", 12), width=40)
    email_entry.pack(anchor='w')

    phone_label = tk.Label(content_frame, text="Phone Number:", font=("Arial", 12), bg='#ffffff')
    phone_label.pack(anchor='w')
    phone_entry = tk.Entry(content_frame, font=("Arial", 12), width=40)
    phone_entry.pack(anchor='w')

    submission_label = tk.Label(content_frame, text="Submission for Paper:", font=("Arial", 12), bg='#ffffff')
    submission_label.pack(anchor='w')
    submission_entry = tk.Entry(content_frame, font=("Arial", 12), width=40)
    submission_entry.pack(anchor='w')

    university_label = tk.Label(content_frame, text="University:", font=("Arial", 12), bg='#ffffff')
    university_label.pack(anchor='w')
    university_entry = tk.Entry(content_frame, font=("Arial", 12), width=40)
    university_entry.pack(anchor='w')

    dob_label = tk.Label(content_frame, text="DOB:", font=("Arial", 12), bg='#ffffff')
    dob_label.pack(anchor='w')
    dob_entry = tk.Entry(content_frame, font=("Arial", 12), width=40)
    dob_entry.pack(anchor='w')

    doi_label = tk.Label(content_frame, text="DOI:", font=("Arial", 12), bg='#ffffff')
    doi_label.pack(anchor='w')
    doi_entry = tk.Entry(content_frame, font=("Arial", 12), width=40)
    doi_entry.pack(anchor='w')

    submit_button = tk.Button(content_frame, text="Submit", command=submit_registration_form, font=("Arial", 12))
    submit_button.pack(pady=(10,20))

def clear_registration_form():
    global name_entry, email_entry, phone_entry, submission_entry, university_entry, dob_entry, doi_entry
    if name_entry:
        name_entry.destroy()
    if email_entry:
        email_entry.destroy()
    if phone_entry:
        phone_entry.destroy()
    if submission_entry:
        submission_entry.destroy()
    if university_entry:
        university_entry.destroy()
    if dob_entry:
        dob_entry.destroy()
    if doi_entry:
        doi_entry.destroy()

def submit_registration_form():
    # Retrieve data from entry fields
    name = name_entry.get()
    email = email_entry.get()
    phone_number = phone_entry.get()
    paper_submission = submission_entry.get()
    university = university_entry.get()
    dob = dob_entry.get()
    doi = doi_entry.get()

    # Store the data
    with open("registrations.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Phone: {phone_number}, Submission: {paper_submission}, University: {university}, DOB: {dob}, DOI: {doi}\n")

    # Clear entry fields after submission
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    submission_entry.delete(0, tk.END)
    university_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    doi_entry.delete(0, tk.END)

root = tk.Tk()
root.title("InCITe 2024")
root.geometry("800x600")

# Header
header_frame = tk.Frame(root, bg='#1A73E8', height=80)
header_frame.pack(fill=tk.X)

# Logo 
'''
logo = tk.PhotoImage(file='logo.png')
logo_label = tk.Label(header_frame, image=logo, bg='#1A73E8')
logo_label.pack(side=tk.LEFT, padx=10)
'''

# Navigation Bar
nav_bar = tk.Frame(root, bg='#333333')
nav_bar.pack(fill=tk.X)

buttons = ["Home", "About", "Committees", "Speakers", "Call for papers",
           "Registration", "Sponsorship", "Past Conferences", "PhD Symposium", "Contact us", "Program Schedule"]

for button_text in buttons:
    button = tk.Button(nav_bar, text=button_text, command=lambda text=button_text: on_button_click(text), fg='#ffffff', bg='#333333', font=("Arial", 12, "bold"))
    button.pack(side=tk.LEFT, padx=10, pady=5)

# Banner with Background Image 
'''
banner_frame = tk.Frame(root, height=150)
banner_frame.pack(fill=tk.X)

# Load and display the background image (Replace 'banner.jpg' with your own image file)
background_image = tk.PhotoImage(file='banner.jpg')
background_label = tk.Label(banner_frame, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
'''

# Main Content
content_frame = tk.Frame(root, bg='#ffffff')
content_frame.pack(fill=tk.BOTH, expand=True)

content_label = tk.Label(content_frame, text="Welcome to InCITe 2024!", font=("Arial", 24, "bold"), bg='#ffffff', pady=20)
content_label.pack()

content_text = tk.Label(content_frame, text="", font=("Arial", 12), bg='#ffffff', justify='left', wraplength=600)
content_text.pack(padx=(20,5), anchor='w')

# Footer
footer_frame = tk.Frame(root, bg='#333333', height=40)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

footer_label = tk.Label(footer_frame, text="© 2024 Your Organization. All Rights Reserved.", font=("Arial", 10), fg='#ffffff', bg='#333333')
footer_label.pack()

root.mainloop()
