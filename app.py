from flask import Flask,url_for, render_template, request, redirect
import mysql.connector

app = Flask(__name__, static_folder="static")

mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="", 
    database="repair_service"
)


#добавление нового устройства в базу
@app.route('/add_device', methods=['GET','POST'])
def add_device():
    if request.method == 'GET':
        return render_template('add_device_form.html')
    elif request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        problem_description = request.form['problem_description']
        repair_cost = request.form['repair_cost']
        cursor = mydb.cursor()
        query = "INSERT INTO device_list (brand, model, problem_description, repair_cost) VALUES (%s, %s, %s, %s)"
        values = (brand, model, problem_description, repair_cost)
        cursor.execute(query, values)
        mydb.commit()
        return redirect('/')

#список устройств
@app.route('/devices_list')
def devices_list():
    #Запрос на выборку устройств из базы данных
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM device_list")
    devices = cursor.fetchall()
    #Вывод списка устройств на страницу
    return render_template('devices_list.html', devices=devices)
#форма для добавления устройства в список  
@app.route('/add_device_form')
def add_device_form():
    return render_template('add_device_form.html')

# удаление устройства из базы
@app.route('/delete_device/<int:device_id>', methods=['POST'])
def delete_device(device_id):
    cursor = mydb.cursor()
    query = "DELETE FROM device_list WHERE id = %s"
    value = (device_id,)
    cursor.execute(query, value)
    mydb.commit()
    return redirect('/devices_list')
# Редактирование информации об устройстве в базе
@app.route('/update_device/<int:device_id>', methods=['GET', 'POST'])
def update_device(device_id):
    if request.method == 'GET':
        # Запрос на выборку устройства из базы данных
        cursor = mydb.cursor()
        query = "SELECT * FROM device_list WHERE id = %s"
        value = (device_id,)
        cursor.execute(query, value)
        devices = cursor.fetchone()
        # Вывод формы для редактирования информации об устройстве
        return render_template('update_device_form.html', devices=devices)
    elif request.method == 'POST':
        # Обработка отправленной формы с обновленной информацией об устройстве
        brand = request.form['brand']
        model = request.form['model']
        problem_description = request.form['problem_description']
        repair_cost = request.form['repair_cost']
        cursor = mydb.cursor()
        query = "UPDATE device_list SET brand = %s, model = %s, problem_description = %s, repair_cost = %s WHERE id = %s"
        values = (brand, model, problem_description, repair_cost, device_id)
        cursor.execute(query, values)
        mydb.commit()
        return redirect('/devices_list')

#домашняя страница сайта
@app.route('/')
def home():
    return render_template('home.html')


#Список мастеров
@app.route('/master_list')
def master_list():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM master_list")
    masters = cursor.fetchall()
    return render_template('master_list.html', master_list=masters)
#добавление нового мастера в базу
@app.route('/add_master', methods=['GET','POST'])
def add_master():
    if request.method == 'GET':
        return render_template('add_master_form.html')
    elif request.method == 'POST':
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        middle_name = request.form['middle_name']
        qualification = request.form['qualification']
        cursor = mydb.cursor()
        query = "INSERT INTO master_list (first_name, second_name, middle_name, qualification) VALUES (%s, %s, %s, %s)"
        values = (first_name, second_name, middle_name, qualification)
        cursor.execute(query, values)
        mydb.commit()
        return redirect('/')
#форма для добавления мастера
@app.route('/add_master_form')
def add_master_form():
    return render_template('add_master_form.html')
    

#Список клиентов
@app.route('/client_list')
def client_list():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM client_list")
    clients = cursor.fetchall()
    return render_template('client_list.html', client_list=clients)
#добавление нового клиента в базу
@app.route('/add_client', methods=['GET','POST'])
def add_client():
    if request.method == 'GET':
        return render_template('add_client_form.html')
    elif request.method == 'POST':
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        middle_name = request.form['middle_name']
        phone_number = request.form['phone_number']
        cursor = mydb.cursor()
        query = "INSERT INTO client_list (first_name, second_name, middle_name, phone_number) VALUES (%s, %s, %s, %s)"
        values = (first_name, second_name, middle_name, phone_number)
        cursor.execute(query, values)
        mydb.commit()
        return redirect('/')
#форма для добавления клиента
@app.route('/add_client_form')
def add_client_form():
    return render_template('add_client_form.html')


# список заказов
@app.route('/order_list')
def order_list():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM order_list")
    orders = cursor.fetchall()
    return render_template('order_list.html', order_list=orders)
#добавление нового заказа в базу
@app.route('/add_order', methods=['GET','POST'])
def add_order():
    if request.method == 'GET':
        return render_template('add_order_form.html')
    elif request.method == 'POST':
        registration_date = request.form['registration_date']
        problem_description = request.form['problem_description']
        order_completion_date = request.form['order_completion_date']
        the_contractor_of_the_order = request.form['the_contractor_of_the_order']
        order_status = request.form['order_status']
        type_of_repair = request.form['type_of_repair']
        cursor = mydb.cursor()
        query = "INSERT INTO order_list (registration_date, problem_description, order_completion_date, the_contractor_of_the_order, order_status, type_of_repair) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (registration_date, problem_description, order_completion_date, the_contractor_of_the_order, order_status, type_of_repair)
        cursor.execute(query, values)
        mydb.commit()
        return redirect('/')

   
if __name__ == '__main__':
    app.run()