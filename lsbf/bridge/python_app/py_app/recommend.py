import tkinter as tk
import utils.Info as Util
from tkinter import messagebox


class Application(tk.Frame):
    master = None
    gender = None
    country = None

    def __init__(self, master=None):
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
        self.master.title('Clothes recommend')
        self.master.geometry('500x700')
        self.label = tk.Label(self, text="Clothes Recommend App", height=10, font=20)
        self.label.pack()
        return self

    def create_widgets(self):
        self.create_age()
        self.create_radio(Util.gender_list, 'gender')
        self.create_radio(Util.country_list, 'country')
        self.create_button()
        return self

    def create_age(self):
        age_frame = tk.Frame(self)
        age_frame.pack(fill=tk.X, padx=5, pady=2)

        age_label = tk.Label(age_frame, text="age:")
        age_label.pack(side=tk.LEFT)

        self.age_entry = tk.Entry(age_frame, textvariable=self.age)
        self.age_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def create_radio(self, labels, key):
        radio_frame = tk.Frame(self)
        radio_frame.pack(fill=tk.X, padx=5, pady=2)
        radio_label = tk.Label(radio_frame, text=key)
        radio_label.pack(side=tk.LEFT)
        var = getattr(self, key)
        for i, label in enumerate(labels):
            radio = tk.Radiobutton(radio_frame, text=label, variable=var, value=i)
            radio.pack(side=tk.LEFT)

    def create_button(self):
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, padx=5, pady=10)

        button = tk.Button(
            button_frame,
            text="Submit",
            command=self.submit,
            width=20,
            relief=tk.RAISED,
            bg='#4CAF50',
            fg='#1970ff',
        )
        button.pack(side=tk.TOP, anchor=tk.CENTER)

    def submit(self):
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
        if not Util.checkFileExists(image_path):
            messagebox.showerror("Error", f"Image not found: {image_path}")
            return

        try:
            if self.canvas:
                self.canvas.delete("all")
            else:
                self.canvas = tk.Canvas(self, width=300, height=700)
                self.canvas.pack(pady=10)

            self.photo = tk.PhotoImage(file=image_path)
            scale_factor = 1024 // 300
            self.photo = self.photo.subsample(scale_factor, scale_factor)
            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.photo)

        except Exception as e:
            print(f"Error in insert_image: {str(e)}")
            messagebox.showerror("Error", f"Failed to load image: {e}")


window = tk.Tk()
app = Application(master=window)
app.show_window().create_widgets().mainloop()
