#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import os
import string
import random
from datetime import datetime


f_name = ""
l_name = ""

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
					   user='root',
					   password='',
					   db='ticketing',
					   charset='utf8mb4',
					   cursorclass=pymysql.cursors.DictCursor)

#Define a route to index function
@app.route('/')
def index():
	return render_template('index.html')


#HOME
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/staffHome')
def staffHome():
	return render_template('staffHome.html')


#FlightSearch
@app.route('/flight')
def flight():
	return render_template('flightSearch.html')


@app.route('/loginFlight')
def loginFlight():
	return render_template('loginFlightSearch.html')

@app.route('/staffloginFlight')
def staffloginFlight():
	return render_template('staffloginFlightSearch.html')

#One
@app.route('/oneWay')
def oneWay():
	return render_template('oneWay.html')

#Round
@app.route('/roundTrip')
def roundTrip():
	return render_template('roundTrip.html')

@app.route('/loginOneWay')
def loginOneWay():
	return render_template('loginOneWay.html')

@app.route('/staffloginOneWay')
def staffloginOneWay():
	return render_template('staffloginOneWay.html')


@app.route('/staffloginRoundTrip')
def staffloginRoundTrip():
	return render_template('staffloginRoundTrip.html')

@app.route('/loginRoundTrip')
def loginRoundTrip():
	return render_template('loginRoundTrip.html')

#LOGIN Either customer or staff
@app.route('/login')
def login():
	return render_template('login.html')

# Customer Login
@app.route('/customerLogin')
def customerLogin():
	return render_template('customerLogin.html')

# Staff Login
@app.route('/staffLogin')
def staffLogin():
	return render_template('staffLogin.html')

#Define route for register
@app.route('/register')
def register():
	return render_template('register.html')

#Define route for customer
@app.route('/customerRegister')
def customerRegister():
	return render_template("customerRegister.html")

@app.route('/staffRegister')
def staffRegister():
	return render_template("staffRegister.html")

@app.route('/createFlight')
def createFlight():
	return render_template("createFlight.html")

@app.route('/changeStatus')
def changeStatus():
	return render_template("changeStatus.html")

@app.route('/addAirplane')
def addAirplane():
	return render_template("addAirplane.html")

@app.route('/addAirport')
def addAirport():
	return render_template('addAirport.html')

@app.route('/createTicket')
def createTicket():
	return render_template('createTicket.html')

@app.route('/purchaseTicket')
def purchaseTicket():
	return render_template('purchaseTicket.html')

@app.route('/cancelFlight')
def cancelFlight():
	return render_template('cancelFlight.html')

@app.route('/leaveReview')
def leaveReview():
	return render_template('leaveReview.html')

@app.route('/viewRating')
def viewRating():
	return render_template('viewRating.html')

@app.route('/viewRevenue')
def viewRevenue():
	return render_template("viewRevenue.html")

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
	#grabs information from the forms
	email = request.form['email']
	password = request.form['password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM customer WHERE email = %s and password = %s'
	cursor.execute(query, (email, password))
	#stores the results in a variable
	data = cursor.fetchone()
	
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['email'] = email
		return redirect(url_for('home'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or email'
		return render_template('customerLogin.html', error=error)
	

@app.route('/loginAuthStaff', methods=['GET', 'POST'])
def loginAuthStaff():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM airline_staff WHERE username = %s and password = %s'
	cursor.execute(query, (username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		first_name = data['f_name']
		last_name = data['l_name']
		session['username'] = username
		return redirect(url_for('staffHome'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('staffLogin.html', error=error)


#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
	#grabs information from the forms
	email = request.form['email']
	password = request.form['password']
	f_name = request.form['f_name']
	l_name = request.form['l_name']
	bldg_num = request.form['bldg_num']
	st_name = request.form['st_name']
	apt_num = request.form['apt_num']
	city = request.form['city']
	state = request.form['state']
	zip_code = request.form['zip_code']
	passport_num = request.form['passport_num']
	passport_exp = request.form['passport_exp']
	passport_country = request.form['passport_country']
	dob = request.form['dob']
	
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM customer WHERE email = %s'
	cursor.execute(query, (email))
	#stores the results in a variable
	data = cursor.fetchone()

	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = 'INSERT INTO customer (email, password, f_name, l_name, bldg_num, st_name, apt_num, city, state, zip_code, passport_num, passport_exp, passport_country, dob) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'
		cursor.execute(ins, (email, password, f_name, l_name, bldg_num, st_name, apt_num, city, state, zip_code, passport_num, passport_exp, passport_country, dob))
		conn.commit()
		cursor.close()
		return render_template('index.html')
	

@app.route('/registerAuthStaff', methods=['GET', 'POST'])
def registerAuthStaff():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']
	f_name = request.form['f_name']
	l_name = request.form['l_name']
	airline_name = request.form['airline_name']
	dob = request.form['dob']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM airline_staff_email WHERE username = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	session['username'] = username

	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('staffRegister.html', error = error)
	else:
		ins = 'INSERT INTO airline_staff (username, airline_name, password, f_name,l_name, dob) VALUES(%s, %s, %s, %s, %s, %s )'
		cursor.execute(ins, (username, airline_name, password, f_name,l_name, dob))
		conn.commit()
		cursor.close()
		
		return render_template('staffPhone.html')

@app.route('/registerStaffPhone', methods=['GET', 'Post'])
def registerStaffPhone():
	num = request.form['num']
	username = session.get('username')
	cursor = conn.cursor()
	query = 'INSERT INTO airline_staff_phone_num (username, num) VALUES (%s, %s)'
	cursor.execute(query, (username, num))
	conn.commit()
	cursor.close()
	return render_template('staffEmail.html')

@app.route('/registerStaffEmail', methods=['GET', 'Post'])
def registerStaffEmail():
	email = request.form['email']
	username = session.get('username')
	cursor = conn.cursor()
	query = 'INSERT INTO airline_staff_email (username, email) VALUES (%s, %s)'
	cursor.execute(query, (username, email))
	conn.commit()
	cursor.close()
	return render_template('staffHome.html')


# One Way route
@app.route('/oneWaySearch', methods=['GET', 'POST'])
def oneWayFlight():
	departingFrom = request.form['departingFrom']
	arrivingAt = request.form['arrivingAt']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	departingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'
	arrivingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'

	cursor.execute(departingLocQuery, (departingFrom, departingFrom))
	departData = cursor.fetchone() 
	departLoc = departData['code']

	cursor.execute(arrivingLocQuery, (arrivingAt, arrivingAt))
	arrivalData = cursor.fetchone()
	arrivalLoc = arrivalData['code']
	
	# FROM -> TO (ONE WAY)
	arrivalToDepartureQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s'
	cursor.execute(arrivalToDepartureQuery, (departLoc, arrivalLoc))
	arrivalToDepartureData = cursor.fetchall()
	arraySize = (len(arrivalToDepartureData))
	sizeEachTuple = (len(arrivalToDepartureData[0]))
	print(sizeEachTuple)
	

	if (arrivalToDepartureData and (arrivalLoc != departLoc)):
		return render_template('oneWayFlightInfo.html', arrivalToDepartureData = arrivalToDepartureData, arraySize = arraySize)
	else:
		error = "Invalid City"
		return render_template('oneWay.html', error = error)
	
@app.route('/loginOneWaySearch', methods=['GET', 'POST'])
def loginOneWayFlight():
	departingFrom = request.form['departingFrom']
	arrivingAt = request.form['arrivingAt']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	departingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'
	arrivingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'

	cursor.execute(departingLocQuery, (departingFrom, departingFrom))
	departData = cursor.fetchone() 
	departLoc = departData['code']

	cursor.execute(arrivingLocQuery, (arrivingAt, arrivingAt))
	arrivalData = cursor.fetchone()
	arrivalLoc = arrivalData['code']
	
	# FROM -> TO (ONE WAY)
	arrivalToDepartureQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s'
	cursor.execute(arrivalToDepartureQuery, (departLoc, arrivalLoc))
	arrivalToDepartureData = cursor.fetchall()
	sizeArray = (len(arrivalToDepartureData))
	sizeEachTuple = (len(arrivalToDepartureData[0]))
	print(sizeEachTuple)
	

	if (arrivalToDepartureData and (arrivalLoc != departLoc)):
		return render_template('loginOneWayFlightInfo.html', arrivalToDepartureData = arrivalToDepartureData, sizeArray = sizeArray)
	else:
		error = "Invalid City"
		return render_template('loginOneWay.html', error = error)
	
@app.route('/staffloginOneWaySearch', methods=['GET', 'POST'])
def staffloginOneWayFlight():
	departingFrom = request.form['departingFrom']
	arrivingAt = request.form['arrivingAt']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	departingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'
	arrivingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'

	cursor.execute(departingLocQuery, (departingFrom, departingFrom))
	departData = cursor.fetchone() 
	departLoc = departData['code']

	cursor.execute(arrivingLocQuery, (arrivingAt, arrivingAt))
	arrivalData = cursor.fetchone()
	arrivalLoc = arrivalData['code']
	
	# FROM -> TO (ONE WAY)
	arrivalToDepartureQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s'
	cursor.execute(arrivalToDepartureQuery, (departLoc, arrivalLoc))
	arrivalToDepartureData = cursor.fetchall()
	sizeArray = (len(arrivalToDepartureData))
	sizeEachTuple = (len(arrivalToDepartureData[0]))
	print(sizeEachTuple)
	

	if (arrivalToDepartureData and (arrivalLoc != departLoc)):
		return render_template('staffloginOneWayFlightInfo.html', arrivalToDepartureData = arrivalToDepartureData, sizeArray = sizeArray)
	else:
		error = "Invalid City"
		return render_template('staffloginOneWay.html', error = error)
# Round Trip route
@app.route('/roundTripSearch', methods=['GET', 'POST'])
def roundTripFlight():
	departingFrom = request.form['departingFrom']
	arrivingAt = request.form['arrivingAt']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query

	##input can be either the airport city or airport code, but the output is always the airport code
	departingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'
	arrivingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'

	cursor.execute(departingLocQuery, (departingFrom, departingFrom))
	departData = cursor.fetchone() 
	# airport code of the departing location
	departLoc = departData['code']

	cursor.execute(arrivingLocQuery, (arrivingAt, arrivingAt))
	arrivalData = cursor.fetchone()
	# airport code of the arriving city
	arrivalLoc = arrivalData['code']
	
	# Depart -> Arrival (Going)
	arrivalToDepartureQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s'
	cursor.execute(arrivalToDepartureQuery, (departLoc, arrivalLoc))
	arrivalToDepartureData = cursor.fetchall()

	sizeArray = (len(arrivalToDepartureData))
	sizeEachTuple = (len(arrivalToDepartureData[0]))

	# Arrival -> Depart (Returning)
	departureToArrivalQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s' 
	cursor.execute(departureToArrivalQuery, (arrivalLoc, departLoc))
	departureToArrivalData = cursor.fetchall()

	if (departureToArrivalData and (arrivalLoc != departLoc)):
		return render_template('roundTripFlightInfo.html', arrivalToDepartureData = arrivalToDepartureData, departureToArrivalData = departureToArrivalData, sizeArray = sizeArray)
	else:
		error = "Invalid City"
		return render_template('roundTrip.html', error = error)

# Round Trip route
@app.route('/loginRoundTripSearch', methods=['GET', 'POST'])
def loginRoundTripFlight():
	departingFrom = request.form['departingFrom']
	arrivingAt = request.form['arrivingAt']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query

	##input can be either the airport city or airport code, but the output is always the airport code
	departingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'
	arrivingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'

	cursor.execute(departingLocQuery, (departingFrom, departingFrom))
	departData = cursor.fetchone() 
	# airport code of the departing location
	departLoc = departData['code']

	cursor.execute(arrivingLocQuery, (arrivingAt, arrivingAt))
	arrivalData = cursor.fetchone()
	# airport code of the arriving city
	arrivalLoc = arrivalData['code']
	
	# Depart -> Arrival (Going)
	arrivalToDepartureQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s'
	cursor.execute(arrivalToDepartureQuery, (departLoc, arrivalLoc))
	arrivalToDepartureData = cursor.fetchall()

	sizeArray = (len(arrivalToDepartureData))
	sizeEachTuple = (len(arrivalToDepartureData[0]))

	# Arrival -> Depart (Returning)
	departureToArrivalQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s' 
	cursor.execute(departureToArrivalQuery, (arrivalLoc, departLoc))
	departureToArrivalData = cursor.fetchall()

	if (departureToArrivalData and (arrivalLoc != departLoc)):
		return render_template('loginRoundTripFlightInfo.html', arrivalToDepartureData = arrivalToDepartureData, departureToArrivalData = departureToArrivalData, sizeArray = sizeArray)
	else:
		error = "Invalid City"
		return render_template('loginRoundTrip.html', error = error)

	
@app.route('/staffloginRoundTripSearch', methods=['GET', 'POST'])
def staffloginRoundTripFlight():
	departingFrom = request.form['departingFrom']
	arrivingAt = request.form['arrivingAt']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query

	##input can be either the airport city or airport code, but the output is always the airport code
	departingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'
	arrivingLocQuery = 'SELECT code FROM airport WHERE city = %s or code = %s'

	cursor.execute(departingLocQuery, (departingFrom, departingFrom))
	departData = cursor.fetchone() 
	# airport code of the departing location
	departLoc = departData['code']

	cursor.execute(arrivingLocQuery, (arrivingAt, arrivingAt))
	arrivalData = cursor.fetchone()
	# airport code of the arriving city
	arrivalLoc = arrivalData['code']
	
	# Depart -> Arrival (Going)
	arrivalToDepartureQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s'
	cursor.execute(arrivalToDepartureQuery, (departLoc, arrivalLoc))
	arrivalToDepartureData = cursor.fetchall()

	sizeArray = (len(arrivalToDepartureData))
	sizeEachTuple = (len(arrivalToDepartureData[0]))

	# Arrival -> Depart (Returning)
	departureToArrivalQuery = 'SELECT * FROM flight WHERE departure_airport_code = %s AND arrival_airport_code = %s' 
	cursor.execute(departureToArrivalQuery, (arrivalLoc, departLoc))
	departureToArrivalData = cursor.fetchall()

	if (departureToArrivalData and (arrivalLoc != departLoc)):
		return render_template('staffroundTripFlightInfo.html', arrivalToDepartureData = arrivalToDepartureData, departureToArrivalData = departureToArrivalData, sizeArray = sizeArray)
	else:
		error = "Invalid City"
		return render_template('staffroundTrip.html', error = error)



@app.route('/createFlightAuth', methods=['GET', 'POST'])
def createFlightAuth():
	airline_name = request.form['airline_name']		# CHECK FORIEGN
	departure_airport_code = request.form['departure_airport_code'] # CHECK FORIEGN
	arrival_airport_code = request.form['arrival_airport_code'] # CHECK FORIEGN
	airplane_id = request.form['airplane_id']
	cursor = conn.cursor()
	airlineCheck = 'SELECT * FROM airline WHERE name = %s'
	cursor.execute(airlineCheck, (airline_name))
	data1 = cursor.fetchone()
	
	departureAirportCheck = 'SELECT * FROM airport WHERE code = %s'
	cursor.execute(departureAirportCheck, (departure_airport_code))
	data2 = cursor.fetchone()

	arrivalAirportCheck = 'SELECT * FROM airport WHERE code = %s'
	cursor.execute(arrivalAirportCheck, (arrival_airport_code))
	data3 = cursor.fetchone()

	airplane_idCheck = 'SELECT * FROM airplane WHERE id = %s'
	cursor.execute(airplane_idCheck, (airplane_id))
	data4 = cursor.fetchone()

	if(data1 and data2 and data3):
		num = request.form['num']
		departure_datetime = request.form['departure_datetime']
		arrival_datetime = request.form['arrival_datetime']
		base_price = request.form['base_price']
		status = request.form['status']
		ins = 'INSERT INTO flight (num, departure_datetime, airline_name, arrival_datetime, base_price, departure_airport_code, arrival_airport_code, airplane_id, status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s )'
		cursor.execute(ins, (num, departure_datetime, airline_name, arrival_datetime, base_price, departure_airport_code, arrival_airport_code, airplane_id, status))
		conn.commit()

		return render_template('staffHome.html')


@app.route('/changeStatusAuth', methods = ['GET', 'POST'])
def changeStatusAuth():
	num = request.form['num']
	status = request.form['status']
	cursor = conn.cursor()
	updateQuery = 'UPDATE flight SET status = %s WHERE num = %s'
	cursor.execute(updateQuery, (status, num))
	conn.commit()
	cursor.close()
	return render_template("staffHome.html")

@app.route('/addAirplaneAuth', methods = ['GET', 'POST'])
def addAirplaneAuth():
	id = request.form['id']
	airline_name = request.form['airline_name']
	num_seats = request.form['num_seats']
	manufacturer = request.form['manufacturer']
	manufacture_date = request.form['manufacture_date']

	cursor = conn.cursor()
	airline_nameCheckQuery = "SELECT * FROM airline WHERE airline_name = %s"
	if(airline_nameCheckQuery):
		ins = 'INSERT INTO airplane (id, airline_name, num_seats, manufacturer, manufacture_date) VALUES(%s, %s, %s, %s, %s )'
		cursor.execute(ins, (id, airline_name, num_seats, manufacturer, manufacture_date))
		conn.commit()
		cursor.close()
		return render_template("staffHome.html")

@app.route("/addAirportAuth", methods = ['GET', 'POST'])
def addAirportAuth():
	code = request.form['code']
	name = request.form['name']
	city = request.form['city']
	country = request.form['country']
	type = request.form['type']
	cursor = conn.cursor()
	ins = 'INSERT INTO airport(code, name, city, country, type) VALUES(%s, %s, %s, %s, %s )'
	cursor.execute(ins, (code, name, city, country, type))
	conn.commit()
	cursor.close()
	return render_template("staffHome.html")


@app.route("/createTicketAuth", methods = ['GET', 'POST'])
def createTicketAuth():
	ticket_id = request.form['id']
	flight_number = request.form['flight']
	cursor = conn.cursor()
	query1 = "SELECT * FROM flight WHERE num = %s"
	cursor.execute(query1, flight_number)
	data = cursor.fetchone()
	if(data):
		ins = 'INSERT INTO ticket(id, flight_number) VALUES(%s, %s)'
		cursor.execute(ins, (ticket_id, flight_number))
		conn.commit()
		cursor.close()
		return render_template("staffHome.html")

@app.route("/purchaseTicketAuth", methods = ['GET', 'POST'])
def purchaseTicketAuth():
	departure_airport_code = request.form['departure_airport_code']
	arrival_aiport_code = request.form['arrival_aiport_code']
	cursor = conn.cursor()
	query1 = "SELECT * FROM flight WHERE (departure_airport_code = %s AND arrival_airport_code = %s) AND CURRENT_TIMESTAMP < departure_datetime;"
	cursor.execute(query1,(departure_airport_code, arrival_aiport_code))
	data = cursor.fetchall()
	sizeArray = len(data)	
	      
	if(data):
		print("EXIST")
		print(sizeArray)
		return render_template("paymentInfo.html", data = data, sizeArray = sizeArray)
	else:
		print("ticket is not available")
		return render_template("purchaseTicket.html")
	
@app.route("/buyTicket", methods = ['GET', 'POST'])
def buyTicket():
	num = request.form['num']
	cursor = conn.cursor()
	query = "SELECT id, flight_number FROM ticket WHERE flight_number = %s AND email is NULL"
	cursor.execute(query, (num))
	data = cursor.fetchall()
	sizeArray = len(data)
	return render_template("buyTicket.html", data = data, sizeArray = sizeArray)

@app.route("/reserveTicket", methods=['GET', 'POST'])
def reserveTicket():
	id = request.form['id']
	flight_number = request.form['flight_number']
	payment_type = request.form['payment_type']
	payment_number = request.form['payment_num']
	payment_name = request.form['payment_name']
	payment_exp_date = request.form['payment_exp_date']

	cursor = conn.cursor()
	email = session.get("email")
	customerInfoQuery = 'SELECT * FROM customer WHERE email = %s'
	cursor.execute(customerInfoQuery, email)
	data = cursor.fetchone()
	f_name = data['f_name']
	l_name = data['l_name']
	dob = data['dob']
	print(dob)
	updateQuery = 'UPDATE ticket SET email = %s, f_name = %s, l_name = %s, dob = %s, payment_type = %s, payment_num = %s, payment_name = %s, payment_exp_date = %s, purchase_datetime = CURRENT_TIMESTAMP WHERE id = %s AND flight_number = %s'
	cursor.execute(updateQuery, (email, f_name, l_name, dob, payment_type, payment_number, payment_name, payment_exp_date, id, flight_number))
	conn.commit()
	cursor.close()
	return render_template("/home.html")

@app.route('/cancellation', methods = ['GET', 'POST'])
def cancellation():
	flight = request.form['flight']
	email = session.get('email')
	query = "UPDATE ticket SET email = null, f_name = null, l_name = null, dob = null, payment_type = null, payment_num = null, payment_name = null, payment_exp_date = null, purchase_datetime = null WHERE email = %s AND flight_number = %s"
	cursor = conn.cursor()
	cursor.execute(query, (email, flight))
	conn.commit()
	cursor.close()
	return render_template("/home.html")

@app.route('/viewMyFlight')
def viewMyFlight():
	email = session.get('email')
	ticketQuery = "SELECT flight_number, id FROM ticket WHERE email = %s"
	cursor = conn.cursor()
	cursor.execute(ticketQuery, email)
	data = cursor.fetchall()
	size = (len(data))
	lst = []

	for i in range(size):
		flight = data[i]['flight_number']
		flightQuery = "SELECT * FROM flight WHERE num = %s "
		cursor.execute(flightQuery, flight)
		data2 = cursor.fetchone()
		lst.append(data2)

	return render_template("/viewIt.html", lst = lst)

@app.route('/makeReview', methods = ['GET','POST'])
def makeReview():
	email = session.get('email')
	flight_number = request.form['flight_number']
	rating = request.form['rating']
	comment = request.form['comment']
	cursor = conn.cursor()

	query = 'SELECT id FROM ticket WHERE email = %s AND flight_number = %s'
	cursor.execute(query, (email, flight_number))
	data = cursor.fetchone()
	id = data['id']
	print(id)
	print(data)


	if(data):
		flightQuery = "SELECT departure_datetime FROM flight WHERE num = %s"
		cursor.execute(flightQuery, (flight_number))
		data2 = cursor.fetchone()
		departureDataTime = (data2['departure_datetime'])

		flightQuery2 = "SELECT airline_name FROM flight WHERE num = %s"
		cursor.execute(flightQuery2, (flight_number))
		data3 = cursor.fetchone()
		airline_name = (data3['airline_name'])

		insert = "INSERT INTO flight_rating(ticket_id, flight_num, departure_datetime, airline_name, rating, comment) VALUES (%s, %s, %s, %s, %s, %s)"
		cursor.execute(insert, (id, flight_number, departureDataTime, airline_name, rating, comment))
		conn.commit()
		cursor.close()
		return render_template('/home.html')
	else:
		return render_template("/leaveReview.html")
	
@app.route('/viewRatingAuth', methods = ['GET', 'POST'])
def viewRatingAuth():
	flight_number = request.form['flight_number']
	query = "SELECT * FROM flight_rating WHERE flight_num = %s"
	cursor = conn.cursor()
	cursor.execute(query, flight_number)
	data = cursor.fetchall()
	print(data)
	if(data):
		return render_template('/viewRatingAuth.html', data = data)
	else:
		return render_template('/viewRating.html')

@app.route('/viewRevenueAuth', methods = ['GET', 'POST'])
def viewRevenueAuth():
	startDate = request.form['startDate']
	endDate = request.form['endDate']
	userName = session.get('username')
	cursor = conn.cursor()
	findAirlineQuery = "SELECT airline_name FROM airline_staff WHERE username = %s"
	cursor.execute(findAirlineQuery, userName)
	data = cursor.fetchone()
	airline = data["airline_name"]
	
	query = "SELECT flight_number FROM ticket WHERE (email IS NOT NULL) AND (purchase_datetime BETWEEN %s AND %s) "
	cursor.execute(query, (startDate, endDate))
	cost = []
	allFlights = cursor.fetchall()
	for flight in allFlights:
		query = "SELECT base_price FROM flight WHERE num = %s"
		cursor.execute(query, flight['flight_number'])
		data = cursor.fetchone()
		cost.append(data['base_price'])
	
	totalRevenue = sum(cost)
	return render_template("/showRevenue.html", totalRevenue = totalRevenue)	



@app.route('/logout')
def logout():
	try:
		if(session['username']):
			session.pop('username')
			return redirect('/')
	except:
		pass

	try:
		if(session['email']):
			session.pop("email")
			return redirect('/')
	except:
		pass

app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
