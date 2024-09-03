import tkinter as tk
from tkinter import ttk, colorchooser
import matplotlib.pyplot as plt
from colour import plotting

def plot_cie_chromaticity_with_custom_points(points_with_labels, title):
    plotting.plot_chromaticity_diagram_CIE1931(standalone=False)

    for (x, y, label, (x_offset, y_offset), point_style) in points_with_labels:
        plt.plot(x, y, 
                 marker=point_style.get('marker', 'o'), 
                 color=point_style.get('color', 'red'), 
                 markersize=point_style.get('size', 10))
        plt.text(x + x_offset, y + y_offset, 
                 f'{label}',
                 color=point_style.get('color', 'red'), 
                 fontsize=9)

    plt.title(title)
    plt.xlabel('CIE x')
    plt.ylabel('CIE y')
    plt.show()

def add_point():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
    except ValueError:
        tk.messagebox.showerror("Invalid input", "Please enter valid coordinates.")
        return
    
    label = entry_label.get()
    marker = combo_marker.get()
    size = int(entry_size.get())
    color = color_btn['bg']
    x_offset = float(entry_x_offset.get())
    y_offset = float(entry_y_offset.get())
    
    points.append((x, y, label, (x_offset, y_offset), {'color': color, 'size': size, 'marker': marker}))

    listbox_points.insert(tk.END, f"{label}: ({x}, {y})")

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")[1]
    if color_code:
        color_btn.config(bg=color_code)

def plot_points():
    title = entry_title.get()
    plot_cie_chromaticity_with_custom_points(points, title)

def clear_points():
    points.clear()
    listbox_points.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("CIE 1931 Chromaticity Diagram")

# Initialize points list
points = []

# Create input fields and labels
frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

tk.Label(frame_input, text="X Coordinate:").grid(row=1, column=0)
entry_x = tk.Entry(frame_input)
entry_x.grid(row=1, column=1)

tk.Label(frame_input, text="Y Coordinate:").grid(row=2, column=0)
entry_y = tk.Entry(frame_input)
entry_y.grid(row=2, column=1)

tk.Label(frame_input, text="Label:").grid(row=3, column=0)
entry_label = tk.Entry(frame_input)
entry_label.grid(row=3, column=1)

tk.Label(frame_input, text="Marker:").grid(row=4, column=0)
combo_marker = ttk.Combobox(frame_input, values=['o', 's', 'D', '^', 'v', '<', '>', 'p', '*', 'h', '+', 'x'])
combo_marker.grid(row=4, column=1)
combo_marker.current(0)

tk.Label(frame_input, text="Size:").grid(row=5, column=0)
entry_size = tk.Entry(frame_input)
entry_size.grid(row=5, column=1)
entry_size.insert(0, "8")

tk.Label(frame_input, text="Color:").grid(row=6, column=0)
color_btn = tk.Button(frame_input, text="Choose Color", bg="red", command=choose_color)
color_btn.grid(row=6, column=1)

tk.Label(frame_input, text="X Offset:").grid(row=7, column=0)
entry_x_offset = tk.Entry(frame_input)
entry_x_offset.grid(row=7, column=1)
entry_x_offset.insert(0, "0.01")

tk.Label(frame_input, text="Y Offset:").grid(row=8, column=0)
entry_y_offset = tk.Entry(frame_input)
entry_y_offset.grid(row=8, column=1)
entry_y_offset.insert(0, "0.01")

tk.Label(frame_input, text="Plot Title:").grid(row=0, column=0)
entry_title = tk.Entry(frame_input)
entry_title.grid(row=0, column=1)
entry_title.insert(0, "CIE 1931 Chromaticity Diagram")

# Listbox to show points
frame_points = tk.Frame(root)
frame_points.pack(padx=10, pady=10)

listbox_points = tk.Listbox(frame_points, width=40)
listbox_points.pack(side=tk.LEFT)

# Add, Clear, and Plot buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=10)

btn_add_point = tk.Button(frame_buttons, text="Add Point", command=add_point)
btn_add_point.pack(side=tk.LEFT, padx=5)

btn_clear_points = tk.Button(frame_buttons, text="Clear Points", command=clear_points)
btn_clear_points.pack(side=tk.LEFT, padx=5)

btn_plot_points = tk.Button(frame_buttons, text="Plot Points", command=plot_points)
btn_plot_points.pack(side=tk.LEFT, padx=5)

# Run the main loop
root.mainloop()
