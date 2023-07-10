import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import os
import platform

def get_default_terminal_command():
    # Try to get the default terminal command on Linux
    # based on the DE (Desktop Environment) or WM (Window Manager) in use
    de = os.environ.get('DESKTOP_SESSION')
    wm = os.environ.get('XDG_CURRENT_DESKTOP')

    if de:
        if 'gnome' in de.lower():
            return 'gnome-terminal'
        elif 'kde' in de.lower():
            return 'konsole'
        elif 'plasma' in de.lower():
            return 'konsole'
        elif 'xfce' in de.lower():
            return 'xfce4-terminal'
        elif 'cinnamon' in de.lower():
            try:
                return 'gnome-terminal'
            except Exception as e:
                pass
            else:
                return 'xfce4-terminal'
        elif 'mate' in de.lower():
            return 'mate-terminal'
        elif 'lxde' in de.lower():
            return 'lxterminal'
        elif 'lxqt' in de.lower():
            return 'qterminal'
        elif 'budgie' in de.lower():
            try:
                return 'gnome-terminal'
            except Exception as e:
                pass
            else:
                return 'tilix'
        elif 'deepin' in de.lower():
            return 'deepin-terminal'
    elif wm:
        if 'gnome' in wm.lower():
            return 'gnome-terminal'
        elif 'kde' in wm.lower():
            return 'konsole'
        elif 'plasma' in wm.lower():
            return 'konsole'
        elif 'xfce' in wm.lower():
            return 'xfce4-terminal'
        elif 'cinnamon' in wm.lower():
            try:
                return 'gnome-terminal'
            except Exception as e:
                pass
            else:
                return 'xfce4-terminal'
        elif 'cinnamon' in wm.lower():
            return 'gnome-terminal'
        elif 'mate' in wm.lower():
            return 'mate-terminal'
        elif 'lxde' in wm.lower():
            return 'lxterminal'
        elif 'lxqt' in wm.lower():
            return 'qterminal'
        elif 'budgie' in wm.lower():
            try:
                return 'gnome-terminal'
            except Exception as e:
                pass
            else:
                return 'tilix'
        elif 'deepin' in wm.lower():
            return 'deepin-terminal'
    else:
    # If we couldn't determine the default terminal command, fall back to 'x-terminal-emulator'
        return 'cmd'

def execute_command(command):
    try:
        if platform.system() == "Windows":
            hashcat_path = os.path.join(os.getcwd(), "hashcat.exe")
            comand = f'"{hashcat_path}" {command}'
        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        terminal_text.insert(tk.END, output.decode())
        terminal_text.insert(tk.END, error.decode())
    except Exception as e:
        terminal_text.insert(tk.END, f"Ошибка при выполнении команды: {e}\n")

def select_hc_file():
    hc_file_path = filedialog.askopenfilename(filetypes=[("Hashcat File", "*.hc22000")])
    hc_file_entry.delete(0, tk.END)
    hc_file_entry.insert(tk.END, hc_file_path)

def select_dictionary():
    dictionary_path = filedialog.askopenfilename()
    dictionary_entry.delete(0, tk.END)
    dictionary_entry.insert(tk.END, dictionary_path)

def dictionary_attack():
    hc_file = hc_file_entry.get()
    dictionary = dictionary_entry.get()
    selected_gpu = gpu_entry.get()
    command = f"hashcat -m 22000 --status-timer 10 --status -d {selected_gpu} {hc_file} {dictionary}"
    execute_command(command)

def custom_mask_attack():
    hc_file = hc_file_entry_custom.get()
    custom_mask = custom_mask_entry.get()
    selected_gpus = gpu_entry_custom.get()
    command = f"hashcat -m 22000 -d {selected_gpus} -w 2 -a 3 {hc_file} {custom_mask}"
    execute_command(command)

# Создание главного окна
window = tk.Tk()
window.title("hashcatGUI")
window.geometry("750x650")

# Создание вкладок
notebook = ttk.Notebook(window)

# Создание вкладки "Атака по словарю"
dictionary_tab = ttk.Frame(notebook)
notebook.add(dictionary_tab, text="Атака по словарю")

# Поле выбора пути к файлу .hc22000
hc_file_label = tk.Label(dictionary_tab, text="Файл .hc22000:")
hc_file_label.pack()

hc_file_entry = tk.Entry(dictionary_tab)
hc_file_entry.pack()

hc_file_button = tk.Button(dictionary_tab, text="Выбрать файл", command=select_hc_file)
hc_file_button.pack()

# Поле выбора пути к словарю
dictionary_label = tk.Label(dictionary_tab, text="Словарь:")
dictionary_label.pack()

dictionary_entry = tk.Entry(dictionary_tab)
dictionary_entry.pack()

dictionary_button = tk.Button(dictionary_tab, text="Выбрать словарь", command=select_dictionary)
dictionary_button.pack()

# Комбобокс выбора G
gpu_label = tk.Label(dictionary_tab, text="Введите номер(а) видеокарт(ы) (через ','): ")
gpu_label.pack()

gpu_entry = ttk.Entry(dictionary_tab)
gpu_entry.pack()

# Кнопка для запуска атаки по словарю
attack_button = tk.Button(dictionary_tab, text="Запустить", command=dictionary_attack)
attack_button.pack()

# Создание вкладки "Пользовательская маска"
custom_mask_tab = ttk.Frame(notebook)
notebook.add(custom_mask_tab, text="Пользовательская маска")

# Поле выбора пути к файлу .hc22000
hc_file_label_custom = tk.Label(custom_mask_tab, text="Файл .hc22000:")
hc_file_label_custom.pack()

hc_file_entry_custom = tk.Entry(custom_mask_tab)
hc_file_entry_custom.pack()

hc_file_button_custom = tk.Button(custom_mask_tab, text="Выбрать файл", command=select_hc_file)
hc_file_button_custom.pack()

# Поле ввода пользовательской маски
custom_mask_label = tk.Label(custom_mask_tab, text="Пользовательская маска:")
custom_mask_label.pack()

custom_mask_entry = tk.Entry(custom_mask_tab)
custom_mask_entry.pack()

# Комбобокс выбора GPU
gpu_label_custom = tk.Label(custom_mask_tab, text="Введите номер(а) видеокарт(ы) (через ','): ")
gpu_label_custom.pack()

gpu_entry_custom = ttk.Entry(custom_mask_tab)
gpu_entry_custom.pack()

# Кнопка для запуска пользовательской маски
custom_mask_button = tk.Button(custom_mask_tab, text="Запустить", command=custom_mask_attack)
custom_mask_button.pack()

terminal_frame = tk.Frame(window)
terminal_frame.pack(side="bottom", fill="both", expand=True)
terminal_label = tk.Label(terminal_frame, text="Терминал: ")
terminal_label.pack()
terminal_text = tk.Text(terminal_frame, height=11, width=80, bg="black", fg="white")
terminal_text.pack()

# Размещение вкладок
notebook.pack(fill="both", expand=True)

# Запуск главного цикла обработки событий
window.mainloop()