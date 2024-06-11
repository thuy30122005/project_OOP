import mysql.connector
from PySide6.QtWidgets import QMessageBox
import bcrypt


class Database:
    '''các phương thức để tương tác với cơ sở dữ liệu MySQL và quản lý dữ liệu sản phẩm, đơn hàng, người dùng và doanh thu
    Tham số:

    host: Địa chỉ máy chủ cơ sở dữ liệu (mặc định: 'localhost')
    user: Tên người dùng truy cập cơ sở dữ liệu (mặc định: 'root')
    password: Mật khẩu truy cập cơ sở dữ liệu (mặc định: 'Thanhthuy111#')
    database: Tên cơ sở dữ liệu cần kết nối (mặc định: 'management')
    auth_plugin: Plugin xác thực (mặc định: 'mysql_native_password')'''

    def __init__(self, host, user, password, database,auth_plugin):
        self.connection = mysql.connector.connect(
           password= 'Thanhthuy111#',
           user= 'root',
           host= 'localhost',
           database= 'management',
           auth_plugin= 'mysql_native_password'
        )
        self.cursor = self.connection.cursor()
    
    def get_products(self):
        ''' Lấy tất cả sản phẩm từ bảng 'products'
        Trả về danh sách các tuple, mỗi tuple đại diện cho một sản phẩm (tên, số lượng, giá)
        '''
        
        self.cursor.execute("SELECT name, quantity, price FROM products")
        return self.cursor.fetchall()

    def add_product(self, name, price, quantity):
        '''Thêm sản phẩm mới vào bảng 'products'.
        Tham số:

        name: Tên sản phẩm
        price: Giá sản phẩm
        quantity: Số lượng sản phẩm trong kho'''

        self.cursor.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
        self.connection.commit()

    def delete_product(self, name):
        ''' Xóa sản phẩm khỏi bảng 'products'.
        Tham số:

        name: Tên sản phẩm cần xóa'''

        self.cursor.execute("DELETE FROM products WHERE name=%s", (name,))
        self.connection.commit()

    def update_product(self, old_name, new_name, price, quantity):
        '''Cập nhật thông tin sản phẩm hiện có trong bảng 'products'
        Tham số:

        old_name: Tên gốc của sản phẩm
        new_name: Tên mới của sản phẩm
        price: Giá cập nhật của sản phẩm
        quantity: Số lượng cập nhật của sản phẩm trong kho'''

        self.cursor.execute("UPDATE products SET name=%s, price=%s, quantity=%s WHERE name=%s", (new_name, price, quantity, old_name))
        self.connection.commit()

    def search_products(self,keyword):
        '''Tìm kiếm sản phẩm trong bảng 'products' dựa trên từ khóa được cung cấp.
        Tham số:

        keyword: Từ khóa để tìm kiếm (tương ứng với tên, giá hoặc số lượng).

        Trả về danh sách các tuple, mỗi tuple đại diện cho một sản phẩm phù hợp với tìm kiếm'''

        pattern = f"%{keyword}%"
        self.cursor.execute("SELECT * FROM products WHERE name LIKE %s OR price LIKE %s OR quantity LIKE %s", (pattern, pattern, pattern))
        return self.cursor.fetchall()


    '''Các phương thức quản lí ĐƠN HÀNG'''
    def get_product_price(self,order_item):
        '''Lấy giá của sản phẩm được đặt trong đơn hàng.
Tham số:

    order_item: Tên sản phẩm trong đơn hàng.

Trả về giá sản phẩm, nếu không tìm thấy sản phẩm trả về 0.0'''

        query = "SELECT price FROM products WHERE name = %s"
        self.cursor.execute(query, (order_item,))
        result = self.cursor.fetchone()
        return result[0] if result else 0.0

    def get_orders(self):
        '''Lấy tất cả đơn hàng từ bảng 'orders'.
Trả về danh sách các tuple, mỗi tuple đại diện cho một đơn hàng'''
        query = "SELECT * FROM orders"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_order(self, order_name,phone, address, email,order_item,order_quantity, order_date, status):
        '''Thêm đơn hàng mới vào bảng 'orders'.
Tham số:

    order_name: Tên đơn hàng.
    phone: Số điện thoại khách hàng.
    address: Địa chỉ khách hàng.
    email: Email khách hàng.
    order_item: Tên sản phẩm trong đơn hàng.
    order_quantity: Số lượng sản phẩm được đặt.
    order_date: Ngày đặt hàng.
    status: Trạng thái đơn hàng'''

        item_price = self.get_product_price(order_item)
        if item_price == 0.0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Lỗi!Mặt hàng '{order_item}' không tồn tại.")
            msg.setWindowTitle("Lỗi")
            msg.exec_()
            return

        total_price = item_price *order_quantity
        self.cursor.execute( """
        INSERT INTO orders (order_name,phone,address,email,order_item,order_quantity,price_item,order_date, total_price, status)
        VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)
        """,(order_name,phone,address,email,order_item,order_quantity,item_price,order_date, total_price, status))
        self.connection.commit()

    def delete_order(self, order_name):
        '''óa đơn hàng khỏi bảng 'orders'.
Tham số:

    order_name: Tên đơn hàng cần xóa'''

        query = "DELETE FROM orders WHERE order_name = %s"
        self.cursor.execute(query, (order_name,))
        self.connection.commit()

    def update_order(self, old_name,new_name,phone,address,email, date, status):
        '''Cập nhật thông tin đơn hàng hiện có trong bảng 'orders'.
Tham số:

    old_name: Tên gốc của đơn hàng.
    new_name: Tên mới của đơn hàng.
    phone: Số điện thoại khách hàng (cập nhật).
    address: Địa chỉ khách hàng (cập nhật).
    email: Email khách hàng (cập nhật).
    date: Ngày đặt hàng (cập nhật).
    status: Trạng thái đơn hàng (cập nhật).

Nâng lỗi nếu xảy ra lỗi trong quá trình cập nhật đơn hàng'''

        query = "UPDATE orders SET order_name = %s,phone=%s,address=%s,email=%s, order_date=%s, status = %s WHERE order_name = %s"
        self.cursor.execute(query, (new_name,phone,address,email,date, status,old_name))
        self.connection.commit() 

    def search_orders(self, keyword):
        '''Tìm kiếm đơn hàng trong bảng 'orders' dựa trên từ khóa được cung cấp.
Tham số:

    keyword: Từ khóa để tìm kiếm (tương ứng với tên đơn hàng, số điện thoại, sản phẩm, địa chỉ, email, hoặc trạng thái).

Trả về danh sách các tuple, mỗi tuple đại diện cho một đơn hàng phù hợp với tìm kiếm.'''

        pattern = f"%{keyword}%"
        query = "SELECT * FROM orders WHERE order_name LIKE %s OR phone LIKE %s OR order_item LIKE %s OR address LIKE %s OR email LIKE %s OR status LIKE %s"
        self.cursor.execute(query, (pattern,pattern,pattern,pattern,pattern,pattern))
        return self.cursor.fetchall()

    '''Các phương thúc quản lí DOANH THU'''
    def get_all_daily_revenues(self):
        '''Lấy doanh thu hàng ngày từ tất cả các đơn hàng.
Trả về danh sách các tuple, mỗi tuple bao gồm ngày và doanh thu tương ứng'''

        query = """
        SELECT DATE(order_date), SUM(total_price)
        FROM orders 
        GROUP BY DATE(order_date) 
        ORDER BY DATE(order_date)
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    ''' Quản lí NGƯỜI DÙNG'''
    def user_exists(self, username):
        '''Kiểm tra xem tên người dùng đã tồn tại hay chưa.
Tham số:

    username: Tên người dùng cần kiểm tra.

Trả về True nếu tên người dùng đã tồn tại, False nếu chưa'''
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def add_user(self,username,hashed_password):
        '''Thêm người dùng mới vào bảng 'users'.
Tham số:

    username: Tên người dùng mới.
    hashed_password: Mật khẩu được băm của người dùng mới.

Nâng lỗi nếu xảy ra lỗi trong quá trình thêm người dùng'''
        self.cursor.execute("INSERT INTO users (username,password) VALUES ( %s, %s)", (username,hashed_password))
        self.connection.commit()

    def authenticate(self, username, password):
        '''Xác thực thông tin đăng nhập của người dùng.
Tham số:

    username: Tên người dùng.
    password: Mật khẩu nhập vào.

Trả về True nếu đăng nhập thành công, False nếu thất bại'''
        try:
            query = "SELECT password FROM users WHERE username = %s"
            self.cursor.execute(query, (username,))
            result = self.cursor.fetchone()

            if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
                return True
            else:
                return False

        except Exception as e:
            # Xử lý các trường hợp ngoại lệ, ví dụ: in ra lỗi và trả về False
            print("Error:", e)
            return False
