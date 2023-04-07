import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

timeToMessage = 60


class Searcher:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("300x320")
        self.root.title("omegle auto bot")

        self.icon = tk.PhotoImage(file="icon.png")
        self.root.wm_iconphoto(False, self.icon)
        self.root.configure(bg="#2b2a27")

        self.title = tk.Label(self.root, text="omegle auto bot ", font=('Lato 25 bold'), bg="#2b2a27", fg="white")
        self.title.pack(pady=10)

        self.label = tk.Label(self.root, text="Enter the tags: ", font=('Lato 11 bold'), bg="#2b2a27", fg="white")
        self.label.pack()

        self.tag_entry = tk.Entry(self.root, width=34, border=0)
        self.tag_entry.pack(pady=5)

        self.label_two = tk.Label(self.root, text="Enter what you want to say: ", font=('Lato 11 bold'), bg="#2b2a27", fg="white")
        self.label_two.pack()

        self.user_entry = tk.Text(self.root, width=30, border=0, height=3)
        self.user_entry.pack(pady=5)

        def search():
            self.PATH = "C:\Program Files (x86)\chromedriver.exe"
            self.driver = webdriver.Chrome(self.PATH)
            self.driver.get("https://www.omegle.com/")
            self.tags = self.tag_entry.get()
            self.text = self.user_entry.get(1.0, "end")
            self.time = self.slider.get()

            self.input = self.driver.find_element(By.CLASS_NAME, "newtopicinput")
            self.input.send_keys(self.tags)
            self.input.send_keys(Keys.RETURN)

            time.sleep(2)

            self.text_btn = self.driver.find_element(By.ID, "textbtn")
            self.text_btn.click()

            self.checkbox = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/p[1]/label/input")
            self.checkbox.click()

            self.secondCheckbox = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/p[2]/label/input")
            self.secondCheckbox.click()
            self.continueBtn = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/p[3]/input")
            self.continueBtn.click()

            while True:
                try:
                    self.textbox = self.driver.find_element(By.CLASS_NAME, "chatmsg ")
                    time.sleep(2)
                    self.textbox.send_keys(self.text)
                    self.textbox.send_keys(Keys .RETURN)
                    time.sleep(int(self.slider.get()))
                    self.skip = self.driver.find_element(By.CLASS_NAME, "disconnectbtn")
                    for i in range(3):
                        self.skip.click()
                except:
                    pass
        self.slider_label = tk.Label(self.root,text="Time until skip: ", font=('Lato 11 bold'), bg="#2b2a27", fg="white")
        self.slider_label.pack()
        self.slider = tk.Scale(self.root, from_=0, to=100, orient="horizontal", bg="#2b2a27", fg="white", length="150",sliderlength="25", troughcolor="#5c5a54", highlightthickness="0",sliderrelief="flat")
        self.slider.pack()

        self.search_button = tk.Button(self.root, text="Start", font=('Arial', 13), background="Grey", command=search, border=0, width=7)
        self.search_button.pack(pady=15)

        self.root.mainloop()


Searcher()
