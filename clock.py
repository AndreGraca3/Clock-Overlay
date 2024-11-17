import tkinter as tk
import time

class AlwaysOnTopClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes('-topmost', True)  # Always on top
        self.root.attributes('-alpha', 0.3)  # More transparent background (lower alpha)

        # Setting a darker transparent background (grayish)
        self.root.configure(bg='#333333')  # Darker background with alpha transparency

        # Set the window size and position (smaller size, bottom-right corner)
        self.root.geometry('50x10+0+0')

        # Label to display the time with a smaller font
        self.label = tk.Label(self.root, font=('Arial', 8), fg='white', bg='#333333')  # Smaller font size
        self.label.pack(expand=True)

        self.update_clock()

    def update_clock(self):
        """Update the clock every second."""
        current_time = time.strftime('%H:%M:%S')
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = AlwaysOnTopClock()
    app.run()
