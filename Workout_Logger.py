import tkinter as tk
from tkinter import ttk
import sqlite3

main = tk.Tk()
main.title("Workout Log")
main.configure(background="pink")

def create_db():
    con = sqlite3.connect('workout_logger.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS workouts (id INTEGER PRIMARY KEY, workout_type TEXT, duration_minutes INTEGER)")
    con.commit()
    con.close()

def add_workout():
    workout = workout_type_entry.get()
    duration = duration_entry.get()
    if workout and duration:
        con = sqlite3.connect('workout_logger.db')
        cur = con.cursor()
        cur.execute('INSERT INTO workouts(workout_type, duration_minutes) VALUES (?, ?)', (workout, int(duration)))
        con.commit()
        con.close()
        update_listbox()
        message = f"Workout added: {workout} for {duration} minutes"
        popup = tk.Toplevel(main)
        popup.title("Confirmation")
        popup_label = tk.Label(popup, text=message, font=('calibre',14,'normal'))
        popup_label.pack()

def update_listbox():
    listbox.delete(0, tk.END)
    con = sqlite3.connect('workout_logger.db')
    cur = con.cursor()
    cur.execute('SELECT workout_type, duration_minutes FROM workouts')
    for workout in cur.fetchall():
        listbox.insert(tk.END, f"{workout[0]} for {workout[1]} minutes")
    con.close()

tk.Label(main, text="Workout Type:", background='pink', foreground='black').pack()
workout_type_entry = ttk.Entry(main, width=30)
workout_type_entry.pack()

tk.Label(main, text="Length of Time(mins):", background='pink', foreground='black').pack()
duration_entry = ttk.Entry(main, width=30)
duration_entry.pack()

submit_button = tk.Button(main,
    text="Add Workout",
    font=('calibre',14,'normal'),
    command=add_workout)
submit_button.pack()

listbox = tk.Listbox(main, height=10, width=50)
listbox.pack()

create_db()
update_listbox()
main.mainloop()