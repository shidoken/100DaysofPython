from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, url
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee = ['✘','☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕']
wifi = ['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪']
power = ['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌']

# the form
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), url()])
    open_time = StringField('Opening Time e.g. 8am', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30pm', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee, validate_choice=True )
    wifi_rating = SelectField('Wifi Strength Rating', choices=wifi, validate_choice=True )
    poweroutlet_rating = SelectField('Power Socket Availability', choices=power , validate_choice=True)
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        list = [form.cafe.data, form.url.data, form.open_time.data, form.closing_time.data, form.coffee_rating.data, form.wifi_rating.data, form.poweroutlet_rating.data]
        with open("cafe-data.csv", 'a', newline='') as csv_file:
            wr = csv.writer(csv_file, dialect="excel")
            wr.writerow(list)
        return cafes()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
