from face_2_ui import Ui_MainWindow
from login_ui import Ui_Dialog
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox,QDialog, QStackedWidget
from database import Database
import sys, bcrypt,inspect
import matplotlib.pyplot as plt


class Manager(QMainWindow, Ui_MainWindow):
    '''Lớp quản lí giao diện chính của ứng dụng'''
    def __init__(self):
        '''kế thừa các khỏi tạo giao diện'''
        super().__init__()
    
        
        self.setupUi(self)
        '''Khởi tạo tên cửa sổ'''
        self.setWindowTitle('SALES MANAGEMENT APP')
        '''Tuy cập vào database để lấy dữ liệu'''
        self.db = Database(host="localhost", user="root", password="Thanhthuy111#", database="management", auth_plugin='mysql_native_password')
        
        self.Menu_icons.setHidden(True)
        '''Hiển thị Trang chủ đầu tiên'''
        self.stackedWidget.setCurrentIndex(0)

        self.show_entries()
        '''Thiết lập sự kiện chuyển tab'''
        self.Product.clicked.connect(lambda: self.switch_to_page(1))
        self.icon_Product.clicked.connect(lambda: self.switch_to_page(1))
        self.Bill.clicked.connect(lambda: self.switch_to_page(2))
        self.icon_Bill.clicked.connect(lambda: self.switch_to_page(2))
        self.Home.clicked.connect(lambda: self.switch_to_page(0))
        self.icon_home.clicked.connect(lambda: self.switch_to_page(0))
        self.Revenue.clicked.connect(lambda: self.switch_to_page(3))
        self.icon_Revenue.clicked.connect(lambda: self.switch_to_page(3))
        
        '''Thiết lập các sụ kiện thêm, xóa, sủa, tìm kiếm, đăng xuất'''
        self.icon_add.clicked.connect(self.add_entry)
        self.icon_fix.clicked.connect(self.update_entry)
        self.icon_delete.clicked.connect(self.delete_entry)
        self.icon_search.clicked.connect(self.search_entries)
        self.grap.clicked.connect(self.plotData)
        self.logout.clicked.connect(self.openDialog)

    def openDialog(self):
        '''Phương thức mở cửa sổ đăng nhập sau khi đăng xuất'''
        dialog = LoginDialog()
        dialog.exec_()
        

    def switch_to_page(self, index):
        '''Thay đổi trang theo chỉ định 
        Tham số: 
        index: chỉ số trang
        Sau khi chuyển trang sẽ hiện thị toàn bộ thông tin đang có'''

        self.stackedWidget.setCurrentIndex(index)
        self.show_entries()

        if index == 3:  # Chuyển đến trang Doanh thu
            self.calculate_daily_revenue()

    def show_entries(self, entries=None):
        '''Hiển thị danh sách dữ liệu lên bảng ứng với trang hiện tại'''

        if self.stackedWidget.currentIndex() == 1:
            table = self.Product_table
        elif self.stackedWidget.currentIndex() == 2:
            table = self.Order_table
        elif self.stackedWidget.currentIndex() == 3:
            table = self.Revenue_table
        else:
            return
        table.setRowCount(0)

        if entries is None:
            entries = self.get_entries()
            #return 

        for row, entry in enumerate(entries):
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            for col, data in enumerate(entry):
                table.setItem(row, col+1, QTableWidgetItem(str(data)))

    def get_entries(self):
        '''Lấy danh sách từ cơ sở dữ liệu ứng với trang hiện tại'''

        if self.stackedWidget.currentIndex() == 1 :
            return self.db.get_products()
        elif self.stackedWidget.currentIndex() == 2:
            return self.db.get_orders()
        else:
            return []

    def add_entry(self):
        '''Thêm dữ liệu mới vào CSDL tùy vào thông tin mỗi trang'''

        if self.stackedWidget.currentIndex() == 1:
            name,price, quantity =self.name.text(),float(self.price.text()), self.quantity.value()
            self.db.add_product(name, price, quantity)
        
        elif self.stackedWidget.currentIndex() == 2:
            phone, address,email = self.phone.text(), self.address.text(), self.email.text()

            order_name,order_item,order_quantity,order_date,status = self.name_customer.text(), self.order_item.text(), self.order_quantity.value(), self.order_date.date().toString("yyyy-MM-dd"), self.status.currentText()
          
            self.db.add_order(order_name,phone,address, email,order_item,order_quantity,order_date,status)

        self.show_entries()

    def delete_entry(self):
        '''Xóa dữ liệu từ các bảng trong CSDL ứng với trang hiện tại'''

        if self.stackedWidget.currentIndex() == 1:
            table = self.Product_table
        elif self.stackedWidget.currentIndex() == 2:
            table = self.Order_table

        selected_row = table.currentRow()
        if selected_row >= 0:
            entry_name = table.item(selected_row, 1).text()
            if QMessageBox.question(self, 'Xác nhận', f'Bạn có chắc muốn xóa mục "{entry_name}"?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
                if self.stackedWidget.currentIndex() == 1:
                    self.db.delete_product(entry_name)
                elif self.stackedWidget.currentIndex() == 2:
                    self.db.delete_order(entry_name)
                self.show_entries()
        else:
            QMessageBox.warning(self, 'Lỗi', 'Vui lòng chọn mục để xóa.')

    def update_entry(self):
        '''Cập nhật lại giữ liệu trong bảng CSDL ứng với trang hiện tại'''
        current_page = self.stackedWidget.currentIndex()
        if current_page == 1:
            selected_row = self.Product_table.currentRow()
            old_name = self.name.text()
            new_name = self.name.text()
            price = float(self.price.text())
            quantity = self.quantity.value()
            update_method = self.db.update_product
        elif current_page == 2:
            selected_row = self.Order_table.currentRow()
            old_name = self.name_customer.text()
            new_name = self.name_customer.text()
            phone = self.phone.text()
            address = self.address.text()
            email = self.email.text()
            date = self.order_date.date().toString("yyyy-MM-dd")
            status = self.status.currentText()
            update_method = self.db.update_order
        else:
            return

        if selected_row >= 0:
            if QMessageBox.question(self, 'Xác nhận', f'Bạn có chắc muốn sửa mục "{old_name}"?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
                if current_page == 1 :
                    update_method(old_name, new_name, price, quantity) 
                elif current_page == 2:
                    update_method(old_name,new_name,phone,address,email, date, status)
                self.show_entries()
        else:
            QMessageBox.warning(self, 'Lỗi', 'Vui lòng chọn mục để sửa.')

    def search_entries(self):
        '''Tìm kiếm dữ liệu trong CSDl Ứng với trang hiện tại 
        Tham số:
        keyword: dữ liệu cần tìm
        Trả về danh sách tìm được
        Hiển thị lên bảng'''

        keyword = self.search.text()
        
        if self.stackedWidget.currentIndex() == 1:
            entries = self.db.search_products(keyword)
        elif self.stackedWidget.currentIndex() == 2:
            entries = self.db.search_orders(keyword)
        else:
            entries = []
        self.show_entries(entries)

    def calculate_daily_revenue(self):
        '''Tính doanh thu mỗi ngày'''
        revenues = self.db.get_all_daily_revenues()
        self.display_revenue(revenues)

    def display_revenue(self, revenues):
        '''Hiển thị doanh thu vào bảng trong giao diện '''

        for row, (date, total_revenue) in enumerate(revenues):
            self.Revenue_table.insertRow(row)
            self.Revenue_table.setItem(row, 1, QTableWidgetItem(str(date)))
            self.Revenue_table.setItem(row, 2, QTableWidgetItem(str(total_revenue) if total_revenue is not None else "0"))
            
    def plotData(self):
        '''Lấy dữ liệu từ bảng doanh thu và tạo biểu đồ'''
        x_data = []
        y_data = []
        for row in range(self.Revenue_table.rowCount()):
            x_data.append(self.Revenue_table.item(row, 1).text())
            y_data.append(float(self.Revenue_table.item(row, 2).text())if self.Revenue_table.item(row, 2) is not None else 0)       
        plt.clf()
        plt.plot(x_data, y_data)
        plt.xlabel('Date')
        plt.ylabel('Total Revenue')
        plt.title('Daily Revenue')
        plt.xticks(rotation=45)  
        plt.tight_layout()
        plt.show()
        plt.draw()  
        plt.pause(0.1)

class Product(Manager):
    '''Lớp sản phẩm kế thừa từ lớp manager
    Tham số:
        get_entries(self): Truy vấn và lấy dữ liệu sản phẩm từ cơ sở dữ liệu'''

    def __init__(self):
        super().__init__()
        

    def get_entries(self):
        '''Lấy dữ liệu sản phẩm từ CSDL
        TRả về:
        danh sách các sản phẩm'''

        return self.db.get_products()

class Order(Manager):
    '''Lớp đơn hàng kế thừa từ lớp manager
    Tham số:
        get_entries(self): Truy vấn và lấy dữ liệu đơn hàng từ cơ sở dữ liệu'''
    def __init__(self):
        super().__init__()

    def get_entries(self):
        '''Lấy dữ liệu đơn hàng từ CSDL
        TRả về:
        danh sách các đơn hàng'''
        return self.db.get_orders()

class LoginDialog(QDialog,Ui_Dialog):
    '''Màn hình đăng nhập'''

    def __init__(self):
        super().__init__()
        '''Thiết lập giao diện, tiêu đề'''
        self.setupUi(self)
        self.setWindowTitle("HELLO")
        self.db = Database(host="localhost", user="root", password="Thanhthuy111#", database="management", auth_plugin='mysql_native_password')
        '''Ban đầu chưa đăng nhập'''
        self.logged_in = False
        
        '''Mặc định trang đăng nhập xuất hiện đầu tiên'''
        self.stackedWidget.setCurrentIndex(0)
        
        '''Kết nối nút đăng nhập với phương thức xử lý đăng nhập'''
        self.login.clicked.connect(self.login_process)
        '''Kết nối nút chuyển đến trang đăng ký với phương thức tương ứng'''
        self.register_2.clicked.connect(self.switch_to_register)

    def login_process(self):
        ''' Xử lý quá trình đăng nhập người dùng'''
        username = self.user_name.text()
        password = self.password.text()
        

        if self.db.authenticate(username, password):
            self.logged_in = True
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
            self.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")
    def switch_to_register(self):
        '''Chuyển đến trang đăng ký từ trang đăng nhập'''
        self.stackedWidget.setCurrentIndex(1)

        self.register_1.clicked.connect(self.register_process)
            
    def register_process(self):
        '''Xử lý quá trình đăng ký tài khoản'''
        username = self.user_name_1.text()
        password = self.password_1.text()
        confirm_password = self.confirm.text()

        ''' Kiểm tra mật khẩu và xác nhận mật khẩu có khớp nhau không'''
        if password != confirm_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu và xác nhận mật khẩu không khớp")
            return

        '''Thực hiện kiểm tra và xử lý đăng ký'''
        if self.validate_registration(username, password):
            QMessageBox.information(self, "Thông báo", "Đăng ký thành công")
            self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Lỗi", "Đăng ký không thành công. Tên đăng nhập đã tồn tại")

    def validate_registration(self, username, password):
        ''' Kiểm tra và xác nhận quá trình đăng ký tài khoản.

        Tham số:
            username (str): Tên đăng nhập được nhập.
            password (str): Mật khẩu được nhập.

        Trả về:
             True nếu đăng ký thành công, False nếu tên đăng nhập đã tồn tại'''

        '''Kiểm tra xem người dùng có tồn tại hay không'''    
        if self.db.user_exists(username):
            return False
        '''Mã hóa mật khẩu'''
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        '''Thêm vào CSDL người dùng'''
        self.db.add_user(username, hashed_password)
        return True


