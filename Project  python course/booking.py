import tkinter as tk
from tkinter import ttk, messagebox
from database import add_reservation

class BookingPage:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback
        
        # إنشاء الإطار الرئيسي
        self.main_frame = ttk.Frame(root)
        
        # متغيرات حقول الإدخال
        self.name_var = tk.StringVar()
        self.flight_number_var = tk.StringVar()
        self.departure_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.seat_number_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        """إنشاء عناصر واجهة صفحة الحجز"""
        # عنوان الصفحة
        title_label = ttk.Label(
            self.main_frame, 
            text="🛫 حجز رحلة جديدة", 
            font=('Arial', 18, 'bold')
        )
        title_label.pack(pady=20)
        
        # إطار النموذج
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(pady=20, padx=50)
        
        # حقل الاسم
        ttk.Label(form_frame, text="اسم الراكب:", font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=8, padx=5)
        name_entry = ttk.Entry(form_frame, textvariable=self.name_var, width=35, font=('Arial', 10))
        name_entry.grid(row=0, column=1, pady=8, padx=10)
        
        # حقل رقم الرحلة
        ttk.Label(form_frame, text="رقم الرحلة:", font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=8, padx=5)
        flight_entry = ttk.Entry(form_frame, textvariable=self.flight_number_var, width=35, font=('Arial', 10))
        flight_entry.grid(row=1, column=1, pady=8, padx=10)
        
        # حقل المغادرة
        ttk.Label(form_frame, text="مطار المغادرة:", font=('Arial', 10)).grid(row=2, column=0, sticky='w', pady=8, padx=5)
        departure_entry = ttk.Entry(form_frame, textvariable=self.departure_var, width=35, font=('Arial', 10))
        departure_entry.grid(row=2, column=1, pady=8, padx=10)
        
        # حقل الوجهة
        ttk.Label(form_frame, text="مطار الوجهة:", font=('Arial', 10)).grid(row=3, column=0, sticky='w', pady=8, padx=5)
        destination_entry = ttk.Entry(form_frame, textvariable=self.destination_var, width=35, font=('Arial', 10))
        destination_entry.grid(row=3, column=1, pady=8, padx=10)
        
        # حقل التاريخ
        ttk.Label(form_frame, text="تاريخ الرحلة:", font=('Arial', 10)).grid(row=4, column=0, sticky='w', pady=8, padx=5)
        date_entry = ttk.Entry(form_frame, textvariable=self.date_var, width=35, font=('Arial', 10))
        date_entry.grid(row=4, column=1, pady=8, padx=10)
        ttk.Label(form_frame, text="مثال: 2025-12-25", font=('Arial', 8), foreground='gray').grid(row=4, column=2, sticky='w', padx=5)
        
        # حقل رقم المقعد
        ttk.Label(form_frame, text="رقم المقعد:", font=('Arial', 10)).grid(row=5, column=0, sticky='w', pady=8, padx=5)
        seat_entry = ttk.Entry(form_frame, textvariable=self.seat_number_var, width=35, font=('Arial', 10))
        seat_entry.grid(row=5, column=1, pady=8, padx=10)
        ttk.Label(form_frame, text="مثال: A15, B22", font=('Arial', 8), foreground='gray').grid(row=5, column=2, sticky='w', padx=5)
        
        # إطار الأزرار
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(pady=30)
        
        # زر حفظ الحجز
        save_btn = ttk.Button(
            buttons_frame,
            text="💾 حفظ الحجز",
            command=self.save_reservation,
            width=20
        )
        save_btn.pack(side='left', padx=10)
        
        # زر مسح الحقول
        clear_btn = ttk.Button(
            buttons_frame,
            text="🗑️ مسح الحقول",
            command=self.clear_form,
            width=20
        )
        clear_btn.pack(side='left', padx=10)
        
        # زر العودة للرئيسية
        back_btn = ttk.Button(
            buttons_frame,
            text="🏠 العودة للرئيسية",
            command=self.back_callback,
            width=20
        )
        back_btn.pack(side='left', padx=10)
    
    def save_reservation(self):
        """حفظ الحجز في قاعدة البيانات"""
        # التحقق من إدخال جميع البيانات
        if not all([
            self.name_var.get().strip(),
            self.flight_number_var.get().strip(),
            self.departure_var.get().strip(),
            self.destination_var.get().strip(),
            self.date_var.get().strip(),
            self.seat_number_var.get().strip()
        ]):
            messagebox.showerror("خطأ", "يرجى إدخال جميع البيانات المطلوبة")
            return
        
        try:
            # حفظ الحجز
            add_reservation(
                self.name_var.get().strip(),
                self.flight_number_var.get().strip(),
                self.departure_var.get().strip(),
                self.destination_var.get().strip(),
                self.date_var.get().strip(),
                self.seat_number_var.get().strip()
            )
            
            # رسالة نجح العملية
            messagebox.showinfo("✅ تم بنجاح", "تم حفظ الحجز بنجاح!\nيمكنك الآن عرض جميع الحجوزات أو إضافة حجز جديد.")
            
            # مسح الحقول بعد الحفظ
            self.clear_form()
            
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الحفظ:\n{str(e)}")
    
    def clear_form(self):
        """مسح جميع الحقول"""
        self.name_var.set("")
        self.flight_number_var.set("")
        self.departure_var.set("")
        self.destination_var.set("")
        self.date_var.set("")
        self.seat_number_var.set("")
    
    def show(self):
        """عرض صفحة الحجز"""
        self.main_frame.pack(fill='both', expand=True)
    
    def hide(self):
        """إخفاء صفحة الحجز"""
        self.main_frame.pack_forget()