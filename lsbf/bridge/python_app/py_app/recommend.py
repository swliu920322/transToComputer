import tkinter as tk
import utils.Info as Util
from tkinter import messagebox


class Application(tk.Frame):
    """Main application class for clothing recommendations based on weather conditions"""
    master = None
    gender = None
    country = None

    def __init__(self, master=None):
        # Initialize the application and set up initial variables
        super().__init__(master)
        self.canvas = None
        self.label = None
        self.master = master
        self.age = tk.StringVar()
        self.gender = tk.IntVar(value=0)
        self.country = tk.IntVar(value=0)
        self.photo = None
        self.pack()

    def show_window(self):
        # Configure the main window properties and title
        self.master.title('Clothes recommend')
        self.master.geometry('500x700')
        self.label = tk.Label(self, text="Clothes Recommend App", height=10, font=20)
        self.label.pack()
        return self

    def create_widgets(self):
        # Create all UI components for the form
        self.create_age()
        self.create_radio(Util.gender_list, 'gender')
        self.create_radio(Util.country_list, 'country')
        self.create_button()
        return self

    def create_age(self):
        # Create age input field with label
        age_frame = tk.Frame(self)
        age_frame.pack(fill=tk.X, padx=5, pady=2)

        age_label = tk.Label(age_frame, text="age:", width=8, anchor=tk.W)
        age_label.pack(side=tk.LEFT)

        self.age_entry = tk.Entry(age_frame, textvariable=self.age)
        self.age_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def create_radio(self, labels, key):
        # Create radio button groups for selection options
        radio_frame = tk.Frame(self)
        radio_frame.pack(fill=tk.X, padx=5, pady=2)
        
        radio_label = tk.Label(radio_frame, text=key, width=8, anchor=tk.W)
        radio_label.pack(side=tk.LEFT)
        
        var = getattr(self, key)
        for i, label in enumerate(labels):
            radio = tk.Radiobutton(radio_frame, text=label, variable=var, value=i)
            radio.pack(side=tk.LEFT, padx=2)

    def create_button(self):
        # Create the submit button with enhanced styling
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, padx=5, pady=10)

        button = tk.Button(
            button_frame,
            text="Submit",
            command=self.submit,
            width=20,
            relief=tk.RAISED,
            bg='#4CAF50',  # Darker blue background for better visibility
            fg='#1970ff',  # White text for contrast
            font=('Arial', 11, 'bold'),
            padx=8,
            pady=5,
            cursor="hand2",
            activebackground='#3CAF50',  # Slightly lighter blue when active
            activeforeground='#1970ff'   # Keep white text when active
        )
        button.pack(side=tk.TOP, anchor=tk.CENTER)
        
        # Add hover effect for better user interaction
        button.bind("<Enter>", lambda e: button.config(bg='#1565C0'))
        button.bind("<Leave>", lambda e: button.config(bg='#0D47A1'))

    def submit(self):
        # Process form submission and get recommendation
        country = Util.country_list[self.country.get()]
        gender = Util.gender_list[self.gender.get()]
        self.get_recommend(country, gender)

    def get_recommend(self, country, gender):
        try:
            weather = Util.get_weather_by_country(country)
            pic_weather = Util.get_weather_by_response(weather)
            image_path = './assets/' + Util.dict_image[gender][pic_weather]
            self.insert_image(image_path)
        except Exception as e:
            messagebox.showerror("get api error", f"{e}")
            print(f"get api error: {str(e)}")

    def insert_image(self, image_path):
        # Display the recommended clothing image to the user
        if not Util.checkFileExists(image_path):
            messagebox.showerror("Error", f"Image not found: {image_path}")
            return

        try:
            # Clear existing canvas or create a new one
            if self.canvas:
                self.canvas.delete("all")
            else:
                self.canvas = tk.Canvas(self, width=300, height=400, bg='#FFFFFF')
                self.canvas.pack(pady=10)

            # Load and resize the image
            self.photo = tk.PhotoImage(file=image_path)
            scale_factor = 1024 // 300
            self.photo = self.photo.subsample(scale_factor, scale_factor)
            
            # Center the image in the canvas
            self.canvas.create_image(150, 200, anchor=tk.CENTER, image=self.photo)

        except Exception as e:
            print(f"Error displaying image: {str(e)}")
            messagebox.showerror("Error", f"Failed to load image: {e}")


# Application initialization
window = tk.Tk()
app = Application(master=window)
app.show_window().create_widgets().mainloop()
