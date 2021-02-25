import mysql.connector

def get_hotels():

	data = []

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	cur.execute("SELECT * FROM hotels")
	rows = cur.fetchall()

	for row in rows:

		record = {
			"id": row[0],
			"name": row[1],
			"name_en": row[2],
			"img_src": row[3],
			"district_id": row[4],
			"address": row[5],
			"price": row[6],
			"station":row[7],
			"summary":row[8],
			"introduction":row[9],
			"room_size": row[10],
			"max_ppl": row[11],
			"equipments":row[12]
		}
		
		data.append(record)

	cur.close()
	conn.close()

	return data


def get_hotel_by_id(id):

	data = {}

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql = "SELECT * FROM hotels WHERE id=" + str(id)


	cur.execute(sql)
	row = cur.fetchone()

	data["id"] = row[0]
	data["name"] = row[1]
	data["name_en"]= row[2]
	data["img_src"]= row[3]
	data["districtsict_id"] = row[4]
	data["address"] = row[5]
	data["price"] = row[6]
	data["station"] = row[7]
	data["summary"] = row[8]
	data["introduction"] = row[9]
	data["room_size"] =row[10]
	data["max_pll"] =row[11]
	data["equipments"] = row[12]


	cur.close()
	conn.close()
	
	return data


def add_hotel(name,name_en,img_src,district_id,address,price,station,summary,introduction,room_size,max_ppl,equipments):

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """
	
	INSERT INTO hotels(name,name_en,img_src,district_id,address,price,station,summary,introduction,room_size,max_ppl,equipments,created_at,updated_at)
	VALUES("{name}","{name_en}","{img_src}",{district_id},"{address}",{price},"{station}","{summary}","{introduction}",{room_size},{max_ppl},"{equipments}",NOW(),NOW())
	
	"""

	sql = sql_format.format(
		name=name,
		name_en=name_en,
		img_src=img_src,
		district_id=district_id,
		address=address,
		price=price,
		station=station,
		summary=summary,
		introduction=introduction,
		room_size=room_size,
		max_ppl=max_ppl,
		equipments=equipments
	)

	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()


def update_hotel(id,name,name_en,img_src,district_id,address,price,station,summary,introduction,room_size,max_ppl,equipments):

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """

		UPDATE hotels 
		SET name="{name}", name_en="{name_en}", img_src="{img_src}",district_id={district_id}, address="{address}", price={price},station="{station}",summary="{summary}",introduction="{introduction}",room_size={room_size},max_ppl={max_ppl},equipments="{equipments}",updated_at=NOW()
		WHERE id={id}

	"""

	sql = sql_format.format(
		id=id,
		name=name,
		name_en=name_en,
		img_src=img_src,
		district_id=district_id,
		address=address,
		price=price,
		station=station,
		summary=summary,
		introduction=introduction,
		room_size=room_size,
		max_ppl=max_ppl,
		equipments=equipments
	)

	
	cur.execute(sql)
	conn.commit()


	cur.close()
	conn.close()


def delete_hotel(id):
	
	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """

		DELETE FROM hotels 
		WHERE id={id}

	"""

	sql = sql_format.format(
		id=id
	)

	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()




def get_districts():

	data = []

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	cur.execute("SELECT * FROM districts")
	rows = cur.fetchall()

	for row in rows:

		record = {
			"id": row[0],
			"name": row[1],
		}

		data.append(record)
	
	cur.close()
	conn.close()

	return data


def get_district_by_id(id):

	data = {}

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql = "SELECT * FROM districts WHERE id=" + str(id)

	cur.execute(sql)
	row = cur.fetchone()

	data["id"] = row[0]
	data["name"] = row[1]


	cur.close()
	conn.close()

	return data


def add_district(name):

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """
	
	INSERT INTO districts(name,created_at,updated_at)
	VALUES("{name}",NOW(),NOW())
	
	"""

	sql = sql_format.format(
		name=name
	)

	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()


def update_district(id,name):

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """

		UPDATE districts 
		SET name="{name}", updated_at=NOW()
		WHERE id={id}

	"""

	sql = sql_format.format(
		id=id,
		name=name
	)
	
	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()


def delete_district(id):
	
	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """

		DELETE FROM districts 
		WHERE id={id}

	"""

	sql = sql_format.format(
		id=id
	)

	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()




def get_users():

	data = []

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	cur.execute("SELECT * FROM users")
	rows = cur.fetchall()

	for row in rows:

		record = {
			"id": row[0],
			"name": row[1],
			"katakana_name": row[2],
			"mail": row[3],
			"password": row[4],
			"telephone": row[5]
		}

		data.append(record)
	
	cur.close()
	conn.close()

	return data


def get_user_by_id(id):
	
	data = {}

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql = "SELECT * FROM users WHERE id=" + str(id)

	cur.execute(sql)
	row = cur.fetchone()

	data["id"] = row[0]
	data["name"] = row[1]
	data["name_en"] = row[2]
	data["mail"] = row[3]
	data["password"] =row[4]
	data["telephone"] =row[5]


	cur.close()
	conn.close()

	return data


def add_user(name,katakana_name,mail,password,telephone):

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """
	
	INSERT INTO users(name,katakana_name,mail,password,telephone,created_at,updated_at)
	VALUES("{name}","{katakana_name}","{mail}","{password}","{telephone}",NOW(),NOW())
	
	"""

	sql = sql_format.format(
		name=name,
		katakana_name=katakana_name,
		mail=mail,
		password=password,
		telephone=telephone
	)

	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()


def update_user(id,name,katakana_name,mail,password,telephone):

	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """

		UPDATE users 
		SET name="{name}", katakana_name="{katakana_name}", mail="{mail}", password="{password}", telephone="{telephone}", updated_at=NOW()
		WHERE id={id}

	"""

	sql = sql_format.format(
		id=id,
		name=name,
		katakana_name=katakana_name,
		mail=mail,
		password=password,
		telephone=telephone
	)
	
	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()


def delete_user(id):
	
	conn = mysql.connector.connect(
		host='localhost',
		port='3306',
		user='root',
		password='Li009294',
		database='tokyo_hotels'
	)

	cur = conn.cursor()

	sql_format = """

		DELETE FROM users 
		WHERE id={id}

	"""

	sql = sql_format.format(
		id=id
	)

	cur.execute(sql)
	conn.commit()

	cur.close()
	conn.close()







