from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

from databases.database import Database
from services.product_categories_service import ProductCategoriesService
from services.products_service import ProductsService

__author__ = "Michael Pogrebinsky - www.topdeveloperacademy.com"

app = Flask(__name__, static_url_path='', static_folder="resources/web/static")

# The lab is behind a http proxy, so it's not aware of the fact that it should use https.
# We use ProxyFix to enable it: https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/#proxy-setups
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Used for any other security related needs by extensions or application, i.e. csrf token
app.config['SECRET_KEY'] = 'mysecretkey'

# Required for cookies set by Flask to work in the preview window that's integrated in the lab IDE
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True

# Required to render urls with https when not in a request context. Urls within Udemy labs must use https
app.config['PREFERRED_URL_SCHEME'] = 'https'

# Creating application databases and business logic
database = Database()
products_categories_service = ProductCategoriesService(database)
products_service = ProductsService(database)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/categories/")
def categories():
    return products_categories_service.get_all_supported_categories()


@app.route("/deals_of_the_day/<int:number_of_products>")
def get_deals_of_the_day(number_of_products: int):
    products = products_service.get_deals_of_the_day(number_of_products)
    return {"products": [product.to_dict() for product in products]}


@app.route("/products")
def get_products_for_category():
    category = request.args.get('category')
    if category is not None:
        products = products_service.get_products_by_category(category)
    else:
        products = products_service.get_all_products()
    return {"products": [product.to_dict() for product in products]}


@app.route("/checkout", methods=["POST"])
def checkout():
    return "success"
