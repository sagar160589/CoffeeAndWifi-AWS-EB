import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import csv

from forms import CoffeeForm
from models import db, Coffee

app = Flask(__name__)

with app.app_context():

    secret_key = os.environ.get('SECRET_KEY')
    app.config['SECRET_KEY'] = secret_key
    #app.config['SECRET_KEY'] = 'anycoolsecretkey'
    rds_endpoint = os.environ.get('RDS_ENDPOINT')
    app.config['SQLALCHEMY_DATABASE_URI'] = rds_endpoint
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coffeewifi.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    Bootstrap(app)
    db.create_all()


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/cafes')
def all_cafes():
    with open('cafe-data.csv', mode='r', encoding="utf8") as cafes:
        column_list = []
        row_list = []
        spamreader = csv.reader(cafes, delimiter=',')
        line_count = 0
        for row in spamreader:
            if line_count == 0:
                column_list.extend(row)
                line_count += 1
            # else:
            #     row_list.append(row)
            #     line_count += 1
    row_list = Coffee.query.all()
    print(row_list)
    return render_template('cafes.html', cafe_columns = column_list, cafe_rows= row_list)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    coffeeForm = CoffeeForm()
    if coffeeForm.validate_on_submit():
        coffee_add = [coffeeForm.name.data, coffeeForm.location.data, coffeeForm.openTime.data,
                      coffeeForm.closeTime.data, coffeeForm.coffee.data, coffeeForm.wifi.data, coffeeForm.power.data]

        # with open('cafe-data.csv', mode='a', encoding="utf8", newline='') as cafes:
        #     csvwriter = csv.writer(cafes)
        #     csvwriter.writerow(coffee_add)
        coffee_add = Coffee(name=coffeeForm.name.data,location=coffeeForm.location.data,openTime=coffeeForm.openTime.data,
                            closeTime=coffeeForm.closeTime.data,coffee=coffeeForm.coffee.data,wifi=coffeeForm.wifi.data,
                            power=coffeeForm.power.data)
        db.session.add(coffee_add)
        db.session.commit()
        return redirect(url_for('all_cafes'))

    return render_template('add.html', cafe_form = coffeeForm )


if __name__ == ('__main__'):
    app.run(debug=True)