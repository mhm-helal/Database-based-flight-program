import tkinter as tk
from tkinter import ttk, messagebox
from database import update_reservation

class EditReservationPage:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback
        
        # إنشاء الإطار الرئيسي
        self.main_frame = ttk.Frame(root)
        
        # متغيرات حقول الإدخال
        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.flight_number_var = tk.StringVar()
        self.departure_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.seat_number_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        """إنشاء عناصر واجهة صفحة التعديل"""
        # عنوان الصفحة
        title_label = ttk.Label(
            self.main_frame, 
            text="✏️ تعديل الحجز", 
            font=('Arial', 18, 'bold')
        )
        title_label.pack(pady=20)
        
        # معلومات الحجز الحالي
        self.current_info_label = ttk.Label(
            self.main_frame, 
            text="", 
            font=('Arial', 10),
            foreground='blue'
        )
        self.current_info_label.pack(pady=10)
        
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
        
        # زر حفظ التعديلات
        save_btn = ttk.Button(
            buttons_frame,
            text="💾 حفظ التعديلات",
            command=self.save_changes,
            width=20
        )
        save_btn.pack(side='left', padx=10)
        
        # زر إعادة تعيين البيانات
        reset_btn = ttk.Button(
            buttons_frame,
            text="🔄 إعادة تعيين",
            command=self.reset_form,
            width=20
        )
        reset_btn.pack(side='left', padx=10)
        
        # زر إلغاء والعودة
        cancel_btn = ttk.Button(
            buttons_frame,
            text="❌ إلغاء والعودة",
            command=self.back_callback,
            width=20
        )
        cancel_btn.pack(side='left', padx=10)
    
    def load_reservation_data(self, reservation_data):
        """تحميل بيانات الحجز للتعديل"""
        # حفظ البيانات الأصلية للإعادة تعيين
        self.original_data = reservation_data
        
        # تحميل البيانات في الحقول
        self.id_var.set(reservation_data[0])
        self.name_var.set(reservation_data[1])
        self.flight_number_var.set(reservation_data[2])
        self.departure_var.set(reservation_data[3])
        self.destination_var.set(reservation_data[4])
        self.date_var.set(reservation_data[5])
        self.seat_number_var.set(reservation_data[6])
        
        # عرض معلومات الحجز الحالي
        info_text = f"تعديل حجز رقم: {reservation_data[0]} | الراكب: {reservation_data[1]} | الرحلة: {reservation_data[2]}"
        self.current_info_label.config(text=info_text)
    
    def reset_form(self):
        """إعادة تعيين البيانات للقيم الأصلية"""
        if hasattr(self, 'original_data'):
            self.load_reservation_data(self.original_data)
    
    def save_changes(self):
        """حفظ التعديلات في قاعدة البيانات"""
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
        
        # تأكيد التعديل
        result = messagebox.askyesno(
            "تأكيد التعديل", 
            f"هل أنت متأكد من حفظ التعديلات على حجز:\n\n"
            f"الراكب: {self.name_var.get()}\n"
            f"رقم الرحلة: {self.flight_number_var.get()}\n"
            f"من {self.departure_var.get()} إلى {self.destination_var.get()}\n"
            f"بتاريخ: {self.date_var.get()}\n"
            f"مقعد رقم: {self.seat_number_var.get()}"
        )
        
        if not result:
            return
        
        try:
            # تحديث الحجز
            update_reservation(
                self.id_var.get(),
                self.name_var.get().strip(),
                self.flight_number_var.get().strip(),
                self.departure_var.get().strip(),
                self.destination_var.get().strip(),
                self.date_var.get().strip(),
                self.seat_number_var.get().strip()
            )
            
            # رسالة نجح العملية
            messagebox.showinfo("✅ تم بنجاح", "تم تحديث الحجز بنجاح!\nسيتم العودة إلى صفحة الحجوزات.")
            
            # العودة لصفحة الحجوزات
            self.back_callback()
            
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء التحديث:\n{str(e)}")
    
    def show(self):
        """عرض صفحة التعديل"""
        self.main_frame.pack(fill='both', expand=True)
    
    def hide(self):
        """إخفاء صفحة التعديل"""
        self.main_frame.pack_forget()