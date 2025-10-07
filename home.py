import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, root, show_booking_callback, show_reservations_callback):
        self.root = root
        self.show_booking_callback = show_booking_callback
        self.show_reservations_callback = show_reservations_callback
        
        # إنشاء الإطار الرئيسي للصفحة
        self.main_frame = ttk.Frame(root)
        
        self.create_widgets()
    
    def create_widgets(self):
        """إنشاء عناصر الواجهة الرسومية"""
        # عنوان التطبيق
        title_label = ttk.Label(
            self.main_frame, 
            text="نظام حجز رحلات الطيران", 
            font=('Arial', 20, 'bold')
        )
        title_label.pack(pady=30)
        
        # نص الترحيب
        welcome_label = ttk.Label(
            self.main_frame, 
            text="مرحباً بك في نظام حجز الطيران\nاختر من القائمة التالية:", 
            font=('Arial', 12),
            justify='center'
        )
        welcome_label.pack(pady=20)
        
        # إطار الأزرار
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(pady=30)
        
        # زر حجز رحلة جديدة
        book_flight_btn = ttk.Button(
            buttons_frame,
            text="🛫 حجز رحلة جديدة",
            command=self.show_booking_callback,
            width=25
        )
        book_flight_btn.pack(pady=15)
        
        # زر عرض الحجوزات
        view_reservations_btn = ttk.Button(
            buttons_frame,
            text="📋 عرض جميع الحجوزات",
            command=self.show_reservations_callback,
            width=25
        )
        view_reservations_btn.pack(pady=15)
    
    def show(self):
        """إظهار الصفحة الرئيسية"""
        self.main_frame.pack(fill='both', expand=True)
    
    def hide(self):
        """إخفاء الصفحة الرئيسية"""
        self.main_frame.pack_forget()