import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        
        if weight <= 0 or height <= 0:
            bmi_result.config(text="Please enter valid values")
            return
        
        bmi = weight / (height * height)
        bmi_result.config(text=f"Your BMI: {bmi:.2f}")
        
        # Interpretation of BMI
        if bmi < 18.5:
            interpretation = "Underweight"
        elif bmi < 25:
            interpretation = "Normal weight"
        elif bmi < 30:
            interpretation = "Overweight"
        else:
            interpretation = "Obese"
        
        bmi_interpretation.config(text=f"Interpretation: {interpretation}")
    
    except ValueError:
        bmi_result.config(text="Please enter valid values")

def restart():
    weight_entry.delete(0, 'end')
    height_entry.delete(0, 'end')
    bmi_result.config(text="")
    bmi_interpretation.config(text="")
    root.after(500, calculate_bmi) 

root = tk.Tk()
root.title(" **BMI Calculator**")


input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)


weight_label = tk.Label(input_frame, text="Enter Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(input_frame)
weight_entry.pack()


height_label = tk.Label(input_frame, text="Enter Height (cm):")
height_label.pack()

height_entry = tk.Entry(input_frame)
height_entry.pack()


calculate_button = tk.Button(input_frame, text="Compute", command=restart)
calculate_button.pack(pady=10)


bmi_result = tk.Label(root, text="")
bmi_result.pack()


bmi_interpretation = tk.Label(root, text="")
bmi_interpretation.pack()


root.mainloop()
