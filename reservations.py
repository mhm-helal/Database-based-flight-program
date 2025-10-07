import tkinter as tk
from tkinter import ttk, messagebox
from database import get_all_reservations, delete_reservation

class ReservationsPage:
    def __init__(self, root, back_callback, edit_callback):
        self.root = root
        self.back_callback = back_callback
        self.edit_callback = edit_callback
        
        # إنشاء الإطار الرئيسي
        self.main_frame = ttk.Frame(root)
        
        self.create_widgets()
    
    def create_widgets(self):
        """إنشاء عناصر واجهة صفحة عرض الحجوزات"""
        # عنوان الصفحة
        title_label = ttk.Label(
            self.main_frame, 
            text="📋 جميع الحجوزات", 
            font=('Arial', 18, 'bold')
        )
        title_label.pack(pady=20)
        
        # إطار الجدول
        table_frame = ttk.Frame(self.main_frame)
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # إنشاء الجدول
        columns = ('ID', 'الاسم', 'رقم الرحلة', 'المغادرة', 'الوجهة', 'التاريخ', 'المقعد')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=12)
        
        # تحديد عناوين وعرض الأعمدة
        column_widths = {'ID': 50, 'الاسم': 120, 'رقم الرحلة': 100, 'المغادرة': 120, 'الوجهة': 120, 'التاريخ': 100, 'المقعد': 80}
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100), anchor='center')
        
        # إضافة شريط التمرير العمودي
        v_scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scrollbar.set)
        
        # إضافة شريط التمرير الأفقي
        h_scrollbar = ttk.Scrollbar(table_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(xscrollcommand=h_scrollbar.set)
        
        # ترتيب الجدول وأشرطة التمرير
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # معلومات عن عدد الحجوزات
        self.info_label = ttk.Label(self.main_frame, text="", font=('Arial', 10))
        self.info_label.pack(pady=10)
        
        # إطار الأزرار
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(pady=20)
        
        # زر تحديث البيانات
        refresh_btn = ttk.Button(
            buttons_frame,
            text="🔄 تحديث البيانات",
            command=self.load_reservations,
            width=18
        )
        refresh_btn.pack(side='left', padx=8)
        
        # زر تعديل الحجز المحدد
        edit_btn = ttk.Button(
            buttons_frame,
            text="✏️ تعديل الحجز",
            command=self.edit_selected_reservation,
            width=18
        )
        edit_btn.pack(side='left', padx=8)
        
        # زر حذف الحجز المحدد
        delete_btn = ttk.Button(
            buttons_frame,
            text="🗑️ حذف الحجز",
            command=self.delete_selected_reservation,
            width=18
        )
        delete_btn.pack(side='left', padx=8)
        
        # زر العودة للرئيسية
        back_btn = ttk.Button(
            buttons_frame,
            text="🏠 العودة للرئيسية",
            command=self.back_callback,
            width=18
        )
        back_btn.pack(side='left', padx=8)
    
    def load_reservations(self):
        """تحميل الحجوزات من قاعدة البيانات"""
        # مسح البيانات الحالية
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            reservations = get_all_reservations()
            for reservation in reservations:
                self.tree.insert('', 'end', values=reservation)
            
            # تحديث معلومات عدد الحجوزات
            count = len(reservations)
            if count == 0:
                self.info_label.config(text="❌ لا توجد حجوزات مسجلة حتى الآن")
                messagebox.showinfo("معلومة", "لا توجد حجوزات مسجلة حتى الآن")
            else:
                self.info_label.config(text=f"✅ إجمالي الحجوزات: {count} حجز")
                
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء تحميل البيانات:\n{str(e)}")
            self.info_label.config(text="❌ خطأ في تحميل البيانات")
    
    def get_selected_reservation(self):
        """الحصول على الحجز المحدد"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("تحذير", "يرجى اختيار حجز من القائمة أولاً")
            return None
        
        item = self.tree.item(selected_item[0])
        return item['values']
    
    def edit_selected_reservation(self):
        """تعديل الحجز المحدد"""
        reservation = self.get_selected_reservation()
        if reservation:
            self.edit_callback(reservation)
    
    def delete_selected_reservation(self):
        """حذف الحجز المحدد"""
        reservation = self.get_selected_reservation()
        if not reservation:
            return
        
        # تأكيد الحذف
        result = messagebox.askyesno(
            "❓ تأكيد الحذف", 
            f"هل أنت متأكد من حذف حجز الراكب:\n\n"
            f"الاسم: {reservation[1]}\n"
            f"رقم الرحلة: {reservation[2]}\n"
            f"من {reservation[3]} إلى {reservation[4]}\n\n"
            f"⚠️ لا يمكن التراجع عن هذا الإجراء!"
        )
        
        if result:
            try:
                delete_reservation(reservation[0])
                messagebox.showinfo("✅ تم بنجاح", f"تم حذف حجز {reservation[1]} بنجاح")
                self.load_reservations()  # تحديث القائمة
            except Exception as e:
                messagebox.showerror("خطأ", f"حدث خطأ أثناء الحذف:\n{str(e)}")
    
    def show(self):
        """عرض صفحة الحجوزات"""
        self.load_reservations()  # تحميل البيانات عند العرض
        self.main_frame.pack(fill='both', expand=True)
    
    def hide(self):
        """إخفاء صفحة الحجوزات"""
        self.main_frame.pack_forget()