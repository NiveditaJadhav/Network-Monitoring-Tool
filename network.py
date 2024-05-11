import tkinter as tk
import psutil

def update_stats():
    net_stats = psutil.net_io_counters(pernic=True)
    stats_text = ""
    for interface, stats in net_stats.items():
        stats_text += f"Interface: {interface}\n"
        stats_text += f"  Bytes Sent: {stats.bytes_sent}\n"
        stats_text += f"  Bytes Received: {stats.bytes_recv}\n"
        stats_text += f"  Packets Sent: {stats.packets_sent}\n"
        stats_text += f"  Packets Received: {stats.packets_recv}\n\n"

    label.config(text=stats_text)
    root.after(1000, update_stats)  # Update every 1 second

root = tk.Tk()
root.title("Network Interface Stats")

label = tk.Label(root, text="", justify=tk.LEFT)
label.pack()

update_stats()  # Initial update
root.mainloop()
