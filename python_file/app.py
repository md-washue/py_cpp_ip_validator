import tkinter as tk
import subprocess
import sys
import os 
def validate_ip():
    ip_input= entry_ip.get().strip()

    if not ip_input:
        label_result.config(text="Please enter an IP address.",fg="#0059ff")
        return

    exe_name = "validator.exe" if sys.platform == "win32" else "./validator"

    if not os.path.exists(exe_name) and not os.path.exists(exe_name.replace('./', '')):
        label_result.config(text="Error: C++ validator not compiled.", fg="red")
        return

    try:
        result = subprocess.run([exe_name, ip_input], capture_output=True, text=True)
        output = result.stdout.strip()
        
        if output == "Valid IPv4":
            label_result.config(text=f"✔ {output}", fg="#4CAF50")
        elif output == "Valid IPv6":
            label_result.config(text=f"✔ {output}", fg="#2196F3")
        else:
            label_result.config(text=f"✖ {output}", fg="#f44336")
            
    except Exception as e:
        label_result.config(text="Error communicating with backend.", fg="red")

def clear_input():
    entry_ip.delete(0, tk.END)
    label_result.config(text="Result will appear here.", fg="gray")

root = tk.Tk()
root.title("IP Address Validator")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter IP Address:", font=("Arial", 12)).pack(pady=(20, 5))

entry_ip = tk.Entry(root, font=("Arial", 14), width=25, justify="center")
entry_ip.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Validate", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", 
          width=10, relief="flat", command=validate_ip).pack(side=tk.LEFT, padx=10)
          
tk.Button(btn_frame, text="Clear", font=("Arial", 10), bg="#e0e0e0", fg="black", 
          width=10, relief="flat", command=clear_input).pack(side=tk.LEFT, padx=10)

tk.Frame(root, height=2, bd=0, bg="#e0e0e0").pack(fill=tk.X, padx=30, pady=10)


label_result = tk.Label(root, text="Result will appear here.", font=("Arial", 12, "bold"), fg="gray")
label_result.pack(pady=5)

root.mainloop()



