import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from fpdf import FPDF

# Function to read file and generate a PDF report
def generate_report():
    # Option 1: Select file manually
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Option 2: Use a fixed file path
    file_path = "D:/Pyrhon/Internship/pd.read_csv()"  # 🔹 Replace with actual file path

    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    try:
        # Read data from CSV file
        df = pd.read_csv(file_path)

        # Perform basic analysis (summary statistics)
        summary = df.describe().to_string()

        # Generate PDF report
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, "Data Analysis Report", ln=True, align="C")
        pdf.ln(10)
        pdf.multi_cell(0, 10, summary)

        # Save the PDF file
        pdf_file = "D:/Pyrhon/Internship/Data_Report.pdf"  # 🔹 Change if needed
        pdf.output(pdf_file)

        messagebox.showinfo("Success", f"Report saved as {pdf_file}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {str(e)}")

# Create a simple Tkinter UI
root = tk.Tk()
root.title("CSV Data Analyzer")
root.geometry("300x200")

label = tk.Label(root, text="D:/Pyrhon/Internship", font=("Arial", 12))
label.pack(pady=10)

button = tk.Button(root, text="Generate Report", command=generate_report, font=("Arial", 12), bg="lightblue")
button.pack(pady=20)

root.mainloop()
