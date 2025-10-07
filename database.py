import sqlite3

def create_database():
    """إنشاء قاعدة البيانات وجدول الحجوزات"""
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    
    # إنشاء جدول الحجوزات إذا لم يكن موجود
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        date TEXT NOT NULL,
        seat_number TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()
    print("تم إنشاء قاعدة البيانات وجدول الحجوزات بنجاح!")

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    """إضافة حجز جديد"""
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, flight_number, departure, destination, date, seat_number))
    
    conn.commit()
    conn.close()
    print("تم إضافة الحجز بنجاح!")

def get_all_reservations():
    """عرض جميع الحجوزات"""
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM reservations')
    reservations = cursor.fetchall()
    
    conn.close()
    return reservations

def update_reservation(id, name, flight_number, departure, destination, date, seat_number):
    """تحديث حجز موجود"""
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    UPDATE reservations 
    SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
    WHERE id=?
    """, (name, flight_number, departure, destination, date, seat_number, id))
    
    conn.commit()
    conn.close()
    print("تم تحديث الحجز بنجاح!")

def delete_reservation(id):
    """حذف حجز"""
    conn = sqlite3.connect('flights.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM reservations WHERE id=?', (id,))
    
    conn.commit()
    conn.close()
    print("تم حذف الحجز بنجاح!")

# تشغيل الدالة لإنشاء القاعدة عند تشغيل الملف مباشرة
if __name__ == "__main__":
    create_database()