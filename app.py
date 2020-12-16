# 
# IMPORTS
# 

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import Flask, render_template, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy
#
# APP/CONFIG
#
app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'

# change the following .db file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WorldCultures-Project-JuanP.db'
# this line is to prevent SQLAlchemy from throwing a warning
# if you don't get one with out it, feel free to remove
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#
# DB SETUP
# 
db = SQLAlchemy(app)

# This are our models (tables)
class Countries(db.Model):
    __tablename__ = "Countries"
    CountryId = db.Column(db.Integer, primary_key=True) ##how to autoincrment on sqlalchemy
    CountryName = db.Column(db.String(255), nullable=False)
    CountryDescription = db.Column(db.Text, nullable=True)

class WorldCultures(db.Model):
    __tablename__ = "World Cultures"
    CountryGroupId = db.Column(db.Integer, primary_key=True)
    CultureCountryGroup = db.Column(db.String(255), nullable=False)
    CountryGroupURL = db.Column(db.String(255), nullable=False)

class CultureOfCountries(db.Model):
    __tablename__ = "Culture of Countries"
    CountryCultureID = db.Column(db.Integer, primary_key=True)
    CountryID = db.Column(db.Integer, nullable=True)
    CountryGroupURL = db.Column(db.String(255), nullable=True)
    CultureCountryName = db.Column(db.String(150), nullable = True)
    CultureCountryName = db.Column(db.String(150), nullable = True)                    
    FoodInDailyLife = db.Column(db.String (255), nullable = True)
    FoodCustomsAtCeremonialOccasions = db.Column(db.String (255), nullable = True)
    BasicEconomy = db.Column(db.String(255), nullable = True)
    LandTenureAndProperty = db.Column(db.String(255), nullable = True)
    CommercialActivities = db.Column(db.String(255), nullable = True)
    MajorIndustries = db.Column(db.String(255), nullable = True)
    Trade = db.Column(db.String(255), nullable = True)
    DivsionOfLabor = db.Column(db.String(255), nullable = True)
    
#
# VIEWS 
#
@app.route('/', methods=['GET'])
def home():
    table = WorldCultures.query.all()
    d = []
    for row in table[9:]:
        row_as_dict = {
            'Culture': row.CultureCountryGroup,
            'URL': row.CountryGroupURL
        }
        d.append(row_as_dict)
    return render_template('home.html', data = d)

@app.route('/visuals', methods=['GET'])
def visuals():
    table = Countries.query.all()
    table2 = WorldCultures.query.all()

    headings = ['# of Cultures', 'Number of Continental Cultures']
    
    d2 = []
    for row in table2[9:]:
        row_as_dict = {
            'Culture': row.CultureCountryGroup,
            'URL': row.CountryGroupURL
        }
        d2.append(row_as_dict)
    
    d = []
    for row in table:
        row_as_dict = {
            'Culture': row.CountryName,
            'Description': row.CountryDescription
        }
        d.append(row_as_dict)

    

    return render_template('visuals.html', headings =headings,  data = len(d), data2 = len(d2)-2)

@app.route("/tables", methods=['GET'])
def show_tables():
    headings = ['Country Names', 'Culture Description']
    table = Countries.query.all()
    d = []
    for row in table:
        row_as_dict = {
            'Culture': row.CountryName,
            'Description': row.CountryDescription
        }
        d.append(row_as_dict)
    return render_template('tables.html',headings=headings, data=d)

@app.route("/tables", methods=['POST'])
def cult_result():
    #culture = request.form.get("culture")
    headings = ['Country Names', 'Culture Description']
    table = Countries.query.all()
    d = []
    for row in table:
        row_as_dict = {
            'Culture': row.CountryName,
            'Description': row.CountryDescription
        }
        d.append(row_as_dict)
    return render_template('tables.html',headings=headings, data=d)

# include other views that return html here:
@app.route('/other')
def other():
    return render_template('other.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # if not name or not email or not message:
    #     return render_template('failure.html')
    return render_template("contact.html", name = name, email = email, message = message)

# set up the following views to allow users to make
# GET requests to get your data in json
# POST requests to store/update some data
# DELETE requests to delete some data

# change this to return your data
@app.route('/api', methods=['GET'])
def get_data():
    table = Countries.query.all()
    d = {row.CountryName:row.CountryDescription for row in table}
    return jsonify(d)

# change this to allow users to add/update data
@app.route('/api', methods=['POST'])
def add_data():
    for k,v in request.args.items():
        pass
    return jsonify({})
        
# change this to allow the deletion of data
@app.route('/api', methods=['DELETE'])
def delete_data():
    for k,v in request.args.items():
        pass
    return jsonify({})

#
# CODE TO BE EXECUTED WHEN RAN AS SCRIPT
#

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
