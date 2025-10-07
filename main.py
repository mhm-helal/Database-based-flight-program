import tkinter as tk
from tkinter import ttk, messagebox
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage
from database import create_database

class FlightReservationApp:
    def __init__(self):
        # إنشاء النافذة الرئيسية
        self.root = tk.Tk()
        self.root.title("✈️ نظام حجز رحلات الطيران")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # تحديد الحد الأدنى لحجم النافذة
        self.root.minsize(800, 600)
        
        # جعل النافذة تظهر في المنتصف
        self.center_window()
        
        # تهيئة قاعدة البيانات
        try:
            create_database()
        except Exception as e:
            messagebox.showerror("خطأ في قاعدة البيانات", f"فشل في تهيئة قاعدة البيانات:\n{str(e)}")
            return
        
        # إنشاء جميع الصفحات
        self.create_pages()
        
        # بدء التطبيق بالصفحة الرئيسية
        self.current_page = None
        self.show_home_page()
    
    def center_window(self):
        """توسيط النافذة على الشاشة"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        window_width = 900
        window_height = 700
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def create_pages(self):
        """إنشاء جميع صفحات التطبيق"""
        # الصفحة الرئيسية
        self.home_page = HomePage(
            self.root, 
            self.show_booking_page,      # callback لعرض صفحة الحجز
            self.show_reservations_page  # callback لعرض صفحة الحجوزات
        )
        
        # صفحة الحجز
        self.booking_page = BookingPage(
            self.root,
            self.show_home_page          # callback للعودة للصفحة الرئيسية
        )
        
        # صفحة عرض الحجوزات
        self.reservations_page = ReservationsPage(
            self.root,
            self.show_home_page,         # callback للعودة للصفحة الرئيسية
            self.show_edit_page          # callback لعرض صفحة التعديل
        )
        
        # صفحة تعديل الحجز
        self.edit_page = EditReservationPage(
            self.root,
            self.show_reservations_page  # callback للعودة لصفحة الحجوزات
        )
    
    def hide_all_pages(self):
        """إخفاء جميع الصفحات"""
        if self.current_page:
            self.current_page.hide()
    
    def show_home_page(self):
        """عرض الصفحة الرئيسية"""
        self.hide_all_pages()
        self.home_page.show()
        self.current_page = self.home_page
        self.root.title("✈️ نظام حجز رحلات الطيران - الصفحة الرئيسية")
    
    def show_booking_page(self):
        """عرض صفحة الحجز"""
        self.hide_all_pages()
        self.booking_page.show()
        self.current_page = self.booking_page
        self.root.title("✈️ نظام حجز رحلات الطيران - حجز رحلة جديدة")
    
    def show_reservations_page(self):
        """عرض صفحة الحجوزات"""
        self.hide_all_pages()
        self.reservations_page.show()
        self.current_page = self.reservations_page
        self.root.title("✈️ نظام حجز رحلات الطيران - جميع الحجوزات")
    
    def show_edit_page(self, reservation_data):
        """عرض صفحة التعديل مع تحميل بيانات الحجز المحدد"""
        self.hide_all_pages()
        self.edit_page.load_reservation_data(reservation_data)
        self.edit_page.show()
        self.current_page = self.edit_page
        self.root.title("✈️ نظام حجز رحلات الطيران - تعديل الحجز")
    
    def on_closing(self):
        """التعامل مع إغلاق التطبيق"""
        if messagebox.askokcancel("إغلاق التطبيق", "هل أنت متأكد من الرغبة في إغلاق التطبيق؟"):
            self.root.destroy()
    
    def run(self):
        """تشغيل التطبيق"""
        # ربط حدث الإغلاق
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # بدء حلقة الأحداث
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("خطأ في التطبيق", f"حدث خطأ غير متوقع:\n{str(e)}")

def main():
    """الدالة الرئيسية لتشغيل التطبيق"""
    try:
        app = FlightReservationApp()
        app.run()
    except Exception as e:
        # في حالة حدوث خطأ عند إنشاء التطبيق
        root = tk.Tk()
        root.withdraw()  # إخفاء النافذة الرئيسية
        messagebox.showerror("خطأ في بدء التطبيق", f"فشل في بدء التطبيق:\n{str(e)}")
        root.destroy()

if __name__ == "__main__":
    main()