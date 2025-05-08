from fetch_data import fetch_data
from preprocessor import preprocessor
from indicators import generate_indicators_report
import tkinter as tk
import tkinter.messagebox as messagebox


def main(symbol, interval):
    data = fetch_data(symbol=symbol, interval=interval)
    if len(data) == 0:
        messagebox.showerror("خطا", f"خطا هنگام دریافت داده های قیمتی ارز {symbol}")
        return
    data = preprocessor(data)
    try:
        report = generate_indicators_report(data)
    except:
        messagebox.showerror("خطا", f"خطا هنگام تحلیل تکنیکال")
        return
    result_window = tk.Toplevel()
    result_window.title("گزارش تحلیل تکنیکال")

    label = tk.Label(result_window, text=report, font=("Arial", 14), justify="right")
    label.pack(padx=20, pady=20)
        

def gui():
    root = tk.Tk()
    root.title("اطلاعات تحلیل تکنیکال ارز های دیجیتال")
    root.geometry("300x360")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    label = tk.Label(frame, text="نماد ارز")
    label.grid(row=0, column=2, pady=5, padx=15)

    entry = tk.Entry(frame)
    entry.insert(0, "btc")
    entry.grid(row=0, column=1, pady=5)

    label = tk.Label(frame, text="تایم فریم")
    label.grid(row=2, column=2, pady=5)
    
    radio_var = tk.StringVar(value="1d")

    radio_1 = tk.Radiobutton(frame, text="روزانه", variable=radio_var, value="1d")
    radio_1.grid(row=2, column=0, pady=5, sticky="w")

    radio_2 = tk.Radiobutton(frame, text="1 دقیقه", variable=radio_var, value="1m")
    radio_2.grid(row=3, column=0, pady=5, sticky="w")

    radio_3 = tk.Radiobutton(frame, text="5 دقیقه", variable=radio_var, value="5m")
    radio_3.grid(row=4, column=0, pady=5, sticky="w")

    radio_4 = tk.Radiobutton(frame, text="15 دقیقه", variable=radio_var, value="15m")
    radio_4.grid(row=5, column=0, pady=5, sticky="w")

    radio_5 = tk.Radiobutton(frame, text="30 دقیقه", variable=radio_var, value="30m")
    radio_5.grid(row=6, column=0, pady=5, sticky="w")

    radio_6 = tk.Radiobutton(frame, text="یک ساعته", variable=radio_var, value="1h")
    radio_6.grid(row=7, column=0, pady=5, sticky="w")

    radio_7 = tk.Radiobutton(frame, text="هفتگی", variable=radio_var, value="1wk")
    radio_7.grid(row=8, column=0, pady=5, sticky="w")

    button = tk.Button(frame, text="دریافت اطلاعات", command=lambda: main(entry.get(), radio_var.get()))    
    button.grid(row=9, column=1, pady=10)
    
    root.mainloop()


if __name__ == '__main__':
    gui()
    