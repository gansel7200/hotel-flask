from flask import Flask, render_template, url_for, request, redirect, flash, session
import model
from functools import wraps
from database import init_db
from database import db
from models.hotel import Hotel
from models.user import User
from models.district import District
from models.reservation import Reservation
from form.hotel.add import Add as AddHotelForm
from form.hotel.update import Update as UpdateHotelForm
from form.hotel.delete import Delete as DeleteHotelForm
from form.user.add import Add as AddUserForm
from form.user.update import Update as UpdateUserForm
from form.user.delete import Delete as DeleteUserForm
from form.reservation.add import Add as AddReservationForm
from form.user.login import Login as UserLoginForm
import json
import datetime
from sqlalchemy import and_
import requests


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.secret_key = "dakshgahgahgh"

    init_db(app)

    return app


app = create_app()


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('get_login'))

    return wrap


def admin_login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session and session["user"]["admin"] == 1:  #管理員後台admin是1

            return f(*args, **kwargs)
        else:
            flash("Please Login first")
            return redirect(url_for('get_login'))

    return wrap


@app.route('/')
def index():
    hotels = Hotel.query.filter( Hotel.deleted_at==None ).all() #顯示不要出現倫理刪除

    return render_template("index.html", hotels=hotels)


@app.route("/hotel/<id>")
def get_hotel_name(id):
    hotel = Hotel.query.get(id)

    result = {
        "hotel_name": hotel.name,
        "station": hotel.station
    }
    return json.dumps(result)


@app.route('/detail/<id>')
def detail(id):
    hotel = Hotel.query.get(id)
    if hotel is None:
        return redirect(url_for("index"))

    return render_template("detail.html", hotel=hotel)


@app.route('/hotel/add', methods=['GET', "POST"])
@login_required
def hotel_add():
    form = AddHotelForm(request.form)
    if request.method == 'POST' and form.validate():
        hotel = Hotel(
            name=form.name.data,
            name_en=form.name_en.data,
            img_src=form.img_src.data,
            district=form.district.data,
            address=form.address.data,
            price=form.price.data,
            station=form.station.data,
            summary=form.summary.data,
            introduction=form.introduction.data,
            room_size=form.room_size.data,
            max_ppl=form.max_ppl.data,
            equipments=form.equipments.data,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )

        db.session.add(hotel)
        db.session.commit()
        flash('登録しました')
        return redirect(url_for('index'))

    return render_template(
        "hotel/add.html",
        message="ホテルの情報を書いてください。",
        form=form
    )


@app.route('/hotel/update/<id>', methods=['GET', 'POST'])
@login_required
def hotel_update(id):
    hotel = Hotel.query.get(id)
    form = UpdateHotelForm(request.form, obj=hotel)

    districts = District.query.all()

    if hotel is None:
        return redirect(url_for("index"))

    if request.method == 'POST' and form.validate():
        hotel = Hotel.query.get(form.id.data)
        hotel.name = form.name.data
        hotel.name_en = form.name_en.data
        hotel.img_src = form.img_src.data
        hotel.address = form.address.data
        hotel.price = form.price.data
        hotel.district = form.district.data
        hotel.station = form.station.data
        hotel.summary = form.summary.data
        hotel.introduction = form.introduction.data
        hotel.room_size = form.room_size.data
        hotel.max_ppl = form.max_ppl.data
        hotel.equipments = form.equipments.data

        hotel.updated_at = datetime.datetime.now()
        db.session.add(hotel)
        db.session.commit()
        flash('修正しました')
        return redirect(url_for('index'))

    return render_template(
        'hotel/update.html',
        message="修正情報を入力してください。",
        districts=districts,
        hotel=hotel,
        form=form,
        id=id
    )


@app.route('/hotel/delete/<id>', methods=['GET', 'POST'])
@login_required
def hotel_delete(id):

    hotel = Hotel.query.get(id)
    form = DeleteHotelForm(request.form, obj=hotel)

    if hotel is None:
        return redirect(url_for("index"))

    if request.method == 'POST' and form.validate():
        hotel = Hotel.query.get(form.id.data)

        hotel.deleted_at = datetime.datetime.now()
        db.session.add(hotel)
        db.session.commit()

        flash('消除しました')
        return redirect(url_for('index'))

    return render_template(
        'hotel/delete.html',
        message="情報は全て削除してますか？",
        hotel=hotel,
        form=form,
        id=id
    )


@app.route('/user/add', methods=['Get', 'POST'])
@login_required
def user_add():
    form = AddUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            name=form.name.data,
            katakana_name=form.katakana_name.data,
            mail=form.mail.data,
            password=form.password.data,
            telephone=form.telephone.data,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )

        db.session.add(user)
        db.session.commit()
        flash('登録しました')
        return redirect(url_for('index'))

    return render_template(
        "user/add.html",
        message="使用者の情報を書いてください。",
        form=form
    )


@app.route('/user/update', methods=['GET', 'POST'])
@login_required
def user_update():

    id = session['user']["id"]  #從login取到session中的使用者資料的字典，我只要取裡面的id

    user = User.query.get(id)  #這裡的id是session id從數據庫抓取的最新資料

    form = UpdateUserForm(request.form, obj=user)

    if user is None:
        return redirect(url_for("index"))

    if request.method == 'POST' and form.validate():
        user = User.query.get(form.id.data)
        user.name = form.name.data
        user.katakana_name = form.katakana_name.data
        user.mail = form.mail.data
        user.password = form.password.data
        user.telephone = form.telephone.data

        user.updated_at = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('修正しました')
        return redirect(url_for('index'))

    return render_template(
        'user/update.html',
        message="修正情報を入力してください。",
        user=user,
        form=form
    )


@app.route('/user/delete/<id>', methods=['GET', 'POST'])
@login_required
def user_delete(id):

    user = User.query.get(id)
    form = DeleteUserForm(request.form, obj=user)

    if user is None:
        return redirect(url_for("index"))

    if request.method == 'POST' and form.validate():
        user = User.query.get(form.id.data)

        user.deleted_at = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()

        flash('消除しました')
        return redirect(url_for('index'))

    return render_template(
        'user/delete.html',
        message="情報は全て削除してますか？",
        user=user,
        form=form,
        id=id
    )


@app.route('/login', methods=['GET'])
def get_login():

    form = UserLoginForm(request.form)

    return render_template(
        "login.html",
        message="メールとパスワードを入力してください。",
        form=form
    )


@app.route('/logout', methods=['GET'])
def get_logout():
    if "user" in session:
        session.pop("user")

    flash("logout success.")
    return redirect(url_for("get_login"))


@app.route('/login', methods=['POST'])
def post_login():

    mail = request.form["mail"]
    password = request.form["password"]

    user = model.login(
        mail=mail,
        password=password,
    )

    if user is None:
        flash("正しいメールとパスワードを入力してください。")
        return redirect(url_for('get_login'))

    session["user"] = user

    return redirect(url_for("index"))


@app.route('/reservation/<id>', methods=['GET'])
@login_required
def get_reservation(id):
    hotel = Hotel.query.get(id)
    user_id = session['user']["id"]
    user = User.query.get(user_id)
    form = AddReservationForm()
    form.user_id.data = user_id
    form.hotel_id.data = hotel.id

    return render_template(
        "reservation/add.html",
        message="入力してくださる。",
        hotel=hotel,
        user=user,
        form=form

    )


@app.route('/reservation', methods=['POST'])
@login_required
def post_reservation():
    form = AddReservationForm(request.form)

    if request.method == 'POST' and form.validate():

        check_in = form.check_in.data
        check_out = form.check_out.data

        check_in_not_ok = Reservation.query.filter(and_(Reservation.check_in <= check_in, Reservation.check_out > check_in, Reservation.deleted_at == None)).count()
        check_out_not_ok = Reservation.query.filter(and_(Reservation.check_in < check_in, Reservation.check_out >= check_in, Reservation.deleted_at == None)).count()
        if check_in_not_ok > 0 or check_out_not_ok > 0:
            return render_template(
                'reservation/add.html',
                message="予約時間はすでに予約ずみです。",
                form=form,
                hotel=Hotel.query.get(form.hotel_id.data),
                user=User.query.get(form.user_id.data)
            )

        reservation = Reservation(
            user_id=form.user_id.data,
            hotel_id=form.hotel_id.data,
            check_in=form.check_in.data,
            check_out=form.check_out.data,
            status=1,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )

        db.session.add(reservation)
        db.session.commit()
        flash('予約ありがとうございます')
        return redirect(url_for('index'))

    return render_template(
        'reservation/add.html',
        message="ホテルを予約してください",
        form=form,
        hotel=Hotel.query.get(form.hotel_id.data),
        user=User.query.get(form.user_id.data)
    )


@app.route("/user/reservation")
def user_reservation():

    user_id = session["user"]['id']
    reservations = Reservation.query.filter(Reservation.user_id == user_id, Reservation.deleted_at==None).all()

    return render_template("reservation/user_reservation.html", reservations=reservations)


@app.route("/user/reservation/delete", methods=["POST"])
def reservation_delete():
    reservation_id = request.form.get("reservation_id")
    reservation = Reservation.query.get(reservation_id)
    reservation.deleted_at = datetime.datetime.now()
    db.session.add(reservation)
    db.session.commit()

    flash('消除しました')
    return redirect(url_for('index'))


@app.route("/admin", methods=['GET', "POST"])
@admin_login_required
def admin():
    reservations = Reservation.query.filter(Reservation.deleted_at == None).all()

    if request.method == 'POST':
        reservation_id = request.form.get("reservation_id")
        new_status = request.form.get("status")

        reservation = Reservation.query.get(reservation_id)
        reservation.status = new_status

        reservation.updated_at = datetime.datetime.now()
        db.session.add(reservation)
        db.session.commit()
        flash('変更しました')
        return redirect(url_for('admin'))

    return render_template("reservation/admin.html", reservations=reservations)


@app.route("/ajax/reservation/status/<reservation_id>/<status>")
def ajax_reservation_status(reservation_id, status):

    reservation = Reservation.query.get(reservation_id)
    reservation.status = status
    db.session.add(reservation)
    db.session.commit()

    result = {
        "id": reservation_id,
        "status": status
    }

    return json.dumps(result)


@app.route("/test/<post_code>")
def post_code(post_code):

    query = {'zipcode': post_code}
    response = requests.get('https://zipcloud.ibsnet.co.jp/api/search', params=query)
    result = response.json()

    if result["status"] == 200:
        address_1 = result["results"][0]["address1"]
        address_2 = result["results"][0]["address2"]
        address_3 = result["results"][0]["address3"]

        address = address_1+address_2+address_3

        return address

    else:
        return result["message"]



if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
