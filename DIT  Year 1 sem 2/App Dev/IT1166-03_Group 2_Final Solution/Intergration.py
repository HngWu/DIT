from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, send_file
from UserData import Userdetails
from Graphs import Linegraph, Piechart
import shelve
from Classes import *
from Reportgeneration import generate_pdf_file


from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

from datetime import datetime
from flask import Flask, jsonify, render_template, request, redirect, url_for
from accounts_management import Account
import accounts_management
from accounts_management import Account, AccountsManagement
from order_management import OrderManagement, OrderWithState
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import shelve
from wtforms.validators import DataRequired, NumberRange, Length
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields import EmailField
from uuid import uuid4
from accounts_management import Account, AccountsManagement
from order_management import OrderManagement, OrderWithState
from datetime import datetime
from Forms import CreateUserForm
from User import User
from UserData import Userdetails
from Graphs import Linegraph, Piechart
from Reportgeneration import generate_pdf_file
from accounts_management import Account
import accounts_management
from accounts_management import Account, AccountsManagement
from order_management import OrderManagement, OrderWithState


app = Flask(__name__)
productDict = {}
db = shelve.open("products.db", "c")
try:
    if "Products" in db:
        productDict = db["Products"]
    else:
        db["Products"] = productDict
except IOError:
    print("Error in opening products.db.")


cart = ShoppingCart()
allOrders = load_orders_from_database()
# Start of Jingfan's side


@app.route("/")
def home():
    print("hello world")
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        date_of_birth = datetime.strptime(request.form["date_of_birth"], "%Y-%m-%d")
        email = request.form["email"]
        password = request.form["password"]
        gender = int(request.form["gender"])
        receive_newsletters = "receive_newsletters" in request.form

        account_manager = AccountsManagement("accounts")
        new_account = Account(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            password=password,
            gender=gender,
            receive_newsletters=receive_newsletters,
        )
        print(
            "account created: "
            + str(account_manager.create_account(account=new_account))
        )

        return redirect(url_for("home"))
    else:
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        account_manager = AccountsManagement("accounts")

        user_id = account_manager.login(email, password)
        admin_id = account_manager.login_as_admin(email, password)

        if admin_id is not None:
            print("logging in as admin")
            return redirect(url_for("adminoverview"))

        elif user_id is not None:
            print("logging in as user")
            return redirect(url_for("loggedin", userid=user_id))

        else:
            print("Login failed")
            return render_template("login.html", error="Invalid email or password")
    else:
        return render_template("login.html")


@app.route("/loggedin/<userid>", methods=["GET"])
def loggedin(userid):
    print(userid)
    return render_template("loggedin.html", user_id=userid)


@app.route("/get_account_info")
def get_account_info():
    account_id = request.args.get("userid")
    account_manager = AccountsManagement("accounts")
    account: Account = account_manager.get_account_by_id(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account.__dict__)


@app.route("/delete_account", methods=["DELETE"])
def delete_account():
    account_id = request.args.get("account_id")
    accounts_manager = AccountsManagement("accounts")
    if account_id:
        result = accounts_manager.delete_account(account_id)
        if result:
            return jsonify({"message": "Account deleted successfully"}), 303
        else:
            return jsonify({"message": "Account not found"}), 404
    else:
        return jsonify({"message": "Account ID is required"}), 400


@app.route("/update_account", methods=["PUT"])
def update_account():
    print("updating acc")
    data = request.json
    account_id = data.get("account_id")
    account_data = data.get("account")

    if not account_id or not account_data:
        return jsonify({"error": "Missing account_id or account data"}), 400

    account = Account(
        first_name=account_data.get("first_name"),
        last_name=account_data.get("last_name"),
        date_of_birth=datetime.strptime(account_data.get("date_of_birth"), "%Y-%m-%d"),
        email=account_data.get("email"),
        password=account_data.get("password"),
        gender=int(account_data.get("gender")),
        receive_newsletters=account_data.get("receive_newsletters"),
        user_id=account_data.get("id"),
    )

    accounts_management = AccountsManagement("accounts")
    result = accounts_management.update_account(account_id, account)

    if result:
        return jsonify({"message": "Account updated successfully"}), 200
    else:
        return jsonify({"error": "Account not found or data invalid"}), 404


@app.route("/order_management")
def order_management():
    return render_template("ordermanagement.html")


@app.route("/add_order", methods=["POST"])
def add_order():
    user_id = request.form.get("user_id")
    new_order = request.form.get("order")
    print("userid: " + user_id)
    order_management = OrderManagement(user_id, "orders")
    order_management.add_order(new_order)
    return jsonify({"message": "Order added successfully"})


@app.route("/get_order", methods=["GET"])
def get_orders():
    user_id = request.args.get("user_id")
    order_id = request.args.get("order_id")
    order_management = OrderManagement(user_id, "orders")
    order = order_management.get_order(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict())


@app.route("/get_all_orders", methods=["GET"])
def get_all_orders():
    user_id = request.args.get("user_id")
    order_management = OrderManagement(user_id, "orders")
    orders = order_management.get_all_orders()
    return jsonify([order.to_dict() for order in orders])


@app.route("/update_order", methods=["PUT"])
def update_order():
    user_id = request.form.get("user_id")
    order_id = request.form.get("order_id")
    state = int(request.form.get("state"))
    order_date = datetime.strptime(request.form.get("order_date"), "%Y-%m-%d")
    estimated_arrival_date_str = request.form.get("estimated_arrival_date")
    estimated_arrival_date = datetime.strptime(estimated_arrival_date_str, "%Y-%m-%d")

    order_management = OrderManagement(user_id, "orders")
    order = order_management.get_order(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    updated_order = OrderWithState(
        order.id, order.order, state, order_date, estimated_arrival_date
    )
    order_management.update_order(updated_order)

    return jsonify({"message": "Order updated successfully"})


@app.route("/remove_order/<user_id>/<order_id>", methods=["DELETE"])
def remove_order(user_id, order_id):
    print("user_id: " + str(user_id))
    print("order_id: " + str(order_id))
    order_management = OrderManagement(user_id, "orders")
    result = order_management.remove_order(order_id)
    if result:
        return jsonify({"message": "Order removed successfully"}), 200
    else:
        return jsonify({"error": "Order not found"}), 404


# end of Jingfan's side
# start of Don's Side


@app.route("/adminoverview", methods=["GET", "POST"])
def adminoverview():

    account_manager = AccountsManagement("accounts")

    accounts_list = account_manager.get_all_accounts()

    # graph variables
    # Define Plot Data

    Linegraph.set_data_n_label(Linegraph)
    data = Linegraph.get_data(Linegraph)
    labels = Linegraph.get_label(Linegraph)

    return render_template(
        "Adminoverviewpage.html", accounts=accounts_list, data=data, labels=labels
    )


@app.route("/adminstatistics", methods=["GET", "POST"])
def statistics():
    Linegraph.set_data_n_label(Linegraph)
    Piechart.set_data_and_label(Piechart)

    llabels = Linegraph.get_label(Linegraph)
    ldata = Linegraph.get_data(Linegraph)

    pvalues = Piechart.get_data(Piechart)
    plabels = Piechart.get_label(Piechart)

    return render_template(
        "Adminstatspage.html",
        data=ldata,
        labels=llabels,
        plabels=plabels,
        pvalues=pvalues,
    )


@app.route("/generate-pdf", methods=["GET", "POST"])
def generate_pdf():
    if request.method == "POST":
        pdf_file = generate_pdf_file()
        return send_file(pdf_file, as_attachment=True, download_name="Sales report.pdf")


@app.route("/adminuserlists", methods=["GET", "POST"])
def adminuserlist():

    account_manager = AccountsManagement("accounts")

    accounts_list = account_manager.get_all_accounts()
    return render_template("adminuserlist.html", accounts=accounts_list)


@app.route("/adminuserlists-delete", methods=["GET", "POST"])
def delete():

    account_manager = AccountsManagement("accounts")

    uids = account_manager.get_all_accounts()
    if request.method == "POST":
        selected_uid = request.form.get("uid")
        accounts_management.delete_account(selected_uid)
        return redirect(url_for("delete_account"))
    return render_template("Deletepage.html", uids=uids)


@app.route("/adminuserlists-deleteprocess", methods=["GET", "POST"])
def deleteprocess():
    if request.method == "POST":
        name = request.form["name"]
        db = shelve.open("user_data")
        del db[name]
        users = {UID: db[UID] for UID in db.keys()}
        db.close()
        return render_template("Adminuserlist.html", users=users)


app.config["SECRET_KEY"] = "your-secret-key"


class AddUserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/adminuserlists-add", methods=["GET", "POST"])
def admin_user_lists_add():

    print("testing 123")
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        date_of_birth = datetime.strptime(request.form["date_of_birth"], "%Y-%m-%d")
        email = request.form["email"]
        password = request.form["password"]
        gender = int(request.form["gender"])
        receive_newsletters = "receive_newsletters" in request.form
        e_admin_status = request.form["admin-status"]
        print("e_admin_status: " + str(e_admin_status))
        admin_status = e_admin_status == "0"
        account_manager = AccountsManagement("accounts")
        new_account = Account(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            password=password,
            gender=gender,
            admin_status=admin_status,
            receive_newsletters=receive_newsletters,
        )
        print("is admin: " + str(admin_status))
        print(
            "account created: "
            + str(account_manager.create_account(account=new_account))
        )

        return redirect(url_for("adminuserlist"))
    else:
        return render_template("Test.html")


@app.route("/adminuserlists-update", methods=["GET", "POST"])
def update():
    print("updating account 1...")
    account_manager = AccountsManagement("accounts")
    uids = account_manager.get_all_uids()  # Function to get all UIDs
    if request.method == "POST":
        selected_uid = request.form.get(
            "uid"
        )  # Assuming 'uid' is the name of the select field
        if selected_uid in uids:  # Check if the selected UID is valid
            # Process the selected UID...
            pass
        else:
            # Handle invalid UID selection...
            pass
    print("updating account 2...")
    return render_template("adminupdatelist.html", uids=uids)


@app.route("/test", methods=["GET", "POST"])
def test():
    print("testing 123")
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        date_of_birth = datetime.strptime(request.form["date_of_birth"], "%Y-%m-%d")
        email = request.form["email"]
        password = request.form["password"]
        gender = int(request.form["gender"])
        receive_newsletters = "receive_newsletters" in request.form
        e_admin_status = request.form["admin-status"]
        print("e_admin_status: " + str(e_admin_status))
        admin_status = e_admin_status == "0"
        account_manager = AccountsManagement("accounts")
        new_account = Account(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            password=password,
            gender=gender,
            admin_status=admin_status,
            receive_newsletters=receive_newsletters,
        )
        print("is admin: " + str(admin_status))
        print(
            "account created: "
            + str(account_manager.create_account(account=new_account))
        )

        return redirect(url_for("adminuserlist"))
    else:
        return render_template("Test.html")


# code for all products page
@app.route("/all_products")
def all_products():
    num_products = len(productDict)
    return render_template(
        "all_products.html",
        productDict=productDict,
        num_products=num_products,
        current_year=datetime.now().year,
    )


@app.route("/keyboards")
def keyboards():

    # Filter out only the 'keyboard' products
    keyboard_products = {
        sku: product
        for sku, product in productDict.items()
        if product.get_product_type().lower() == "keyboard"
    }

    num_products = len(keyboard_products)
    return render_template(
        "Keyboards.html",
        productDict=keyboard_products,
        num_products=num_products,
        current_year=datetime.now().year,
    )


@app.route("/filtered_keyboard", methods=["POST"])
def filtered_keyboard():
    selected_categories = request.form.getlist("selected_categories[]")
    product_type = "keyboard"  # set product_type to 'keyboard'

    if "keyboard" in selected_categories:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if product.get_product_type().lower() == product_type.lower()
        }
    else:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if (
                product.get_product_type().lower() == product_type.lower()
                and product.get_product_type().lower()
                in map(str.lower, selected_categories)
            )
        }

    return render_template(
        "Keyboards.html",
        productDict=filtered_catalog,
        num_products=len(filtered_catalog),
        current_year=datetime.now().year,
    )


@app.route("/keycaps")
def keycaps():

    # Filter out only the 'keycaps' products
    keycaps_products = {
        sku: product
        for sku, product in productDict.items()
        if product.get_product_type().lower() == "keycaps"
    }

    num_products = len(keycaps_products)
    return render_template(
        "Keycaps.html",
        productDict=keycaps_products,
        num_products=num_products,
        current_year=datetime.now().year,
    )


@app.route("/filtered_keycaps", methods=["POST"])
def filtered_keycaps():
    selected_categories = request.form.getlist("selected_categories[]")
    product_type = "keycaps"  # set product_type to 'keycaps'

    if "keycaps" in selected_categories:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if product.get_product_type().lower() == product_type.lower()
        }
    else:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if (
                product.get_product_type().lower() == product_type.lower()
                and product.get_product_type().lower()
                in map(str.lower, selected_categories)
            )
        }

    return render_template(
        "Keycaps.html",
        productDict=filtered_catalog,
        num_products=len(filtered_catalog),
        current_year=datetime.now().year,
    )


@app.route("/switches")
def switches():

    # Filter out only the 'switches' products
    switches_products = {
        sku: product
        for sku, product in productDict.items()
        if product.get_product_type().lower() == "switches"
    }

    num_products = len(switches_products)
    return render_template(
        "Switches.html",
        productDict=switches_products,
        num_products=num_products,
        current_year=datetime.now().year,
    )


@app.route("/filtered_switches", methods=["POST"])
def filtered_switches():
    selected_categories = request.form.getlist("selected_categories[]")
    product_type = "switches"  # set product_type to 'switches'

    if "switches" in selected_categories:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if product.get_product_type().lower() == product_type.lower()
        }
    else:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if (
                product.get_product_type().lower() == product_type.lower()
                and product.get_product_type().lower()
                in map(str.lower, selected_categories)
            )
        }

    return render_template(
        "Switches.html",
        productDict=filtered_catalog,
        num_products=len(filtered_catalog),
        current_year=datetime.now().year,
    )


@app.route("/accessories")
def accessories():

    # Filter out only the 'accessories' products
    accessories_products = {
        sku: product
        for sku, product in productDict.items()
        if product.get_product_type().lower() == "accessories"
    }

    num_products = len(accessories_products)
    return render_template(
        "Accessories.html",
        productDict=accessories_products,
        num_products=num_products,
        current_year=datetime.now().year,
    )


@app.route("/filtered_accessories", methods=["POST"])
def filtered_accessories():
    selected_categories = request.form.getlist("selected_categories[]")
    product_type = "accessories"  # set product_type to 'accessories'

    if "accessories" in selected_categories:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if product.get_product_type().lower() == product_type.lower()
        }
    else:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if (
                product.get_product_type().lower() == product_type.lower()
                and product.get_product_type().lower()
                in map(str.lower, selected_categories)
            )
        }

    return render_template(
        "Accessories.html",
        productDict=filtered_catalog,
        num_products=len(filtered_catalog),
        current_year=datetime.now().year,
    )


@app.route("/secondhandproducts")
def secondhandproducts():

    # Filter out only the 'SecondHandProducts' products
    secondhand_products = {
        sku: product
        for sku, product in productDict.items()
        if product.get_product_type().lower() == "secondhandproducts"
    }

    num_products = len(secondhand_products)
    return render_template(
        "SecondHandProducts.html",
        productDict=secondhand_products,
        num_products=num_products,
        current_year=datetime.now().year,
    )


@app.route("/filtered_secondhandproducts", methods=["POST"])
def filtered_secondhandproducts():
    selected_categories = request.form.getlist("selected_categories[]")
    product_type = "secondhandproducts"  # set product_type to 'secondhandproducts'

    if "secondhandproducts" in selected_categories:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if product.get_product_type().lower() == product_type.lower()
        }
    else:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if (
                product.get_product_type().lower() == product_type.lower()
                and product.get_product_type().lower()
                in map(str.lower, selected_categories)
            )
        }

    return render_template(
        "SecondHandProducts.html",
        productDict=filtered_catalog,
        num_products=len(filtered_catalog),
        current_year=datetime.now().year,
    )


@app.route("/filtered_catalog", methods=["POST"])
def filtered_catalog():
    selected_categories = request.form.getlist("selected_categories[]")
    product_type = request.form.get("type")

    if "all" in selected_categories:
        filtered_catalog = productDict
    else:
        filtered_catalog = {
            product_id: product
            for product_id, product in productDict.items()
            if (
                product.get_product_type().lower() == product_type.lower()
                and product.get_product_type().lower()
                in map(str.lower, selected_categories)
            )
        }

    return render_template(
        "all_products.html",
        productDict=filtered_catalog,
        num_products=len(filtered_catalog),
        current_year=datetime.now().year,
    )


@app.route("/search_catalog", methods=["POST"])
def search_catalog():
    search_query = request.form.get("search_query", "").lower()

    if not search_query:
        return redirect(url_for("all_products"))

    # Filter products based on the search query
    search_catalog_results = {
        product_id: product
        for product_id, product in productDict.items()
        if (
            search_query in product.get_product_id().lower()
            or search_query in product.get_product_name().lower()
            or search_query in product.get_product_sku().lower()
        )
    }

    return render_template(
        "all_products.html",
        products=search_catalog_results,
        num_products=len(search_catalog_results),
        current_year=datetime.now().year,
    )


# start of code for footer pages
@app.route("/about-us")
def about_us():
    return render_template("AboutUs.html", current_year=datetime.now().year)


@app.route("/terms")
def terms():
    return render_template("terms.html", current_year=datetime.now().year)


@app.route("/FAQ")
def FAQ():
    return render_template("FAQ.html", current_year=datetime.now().year)


@app.route("/sus")
def sus():
    return render_template(
        "SustainabilityEffort.html", current_year=datetime.now().year
    )


@app.route("/privacy_statement")
def privacy_statement():
    return render_template("privacystat.html", current_year=datetime.now().year)


# end of code for footer pages


# start of code for contact us
@app.route("/thank_you")
def thank_you():
    return render_template("TYpage.html", current_year=datetime.now().year)


@app.route("/ContactUs", methods=["GET", "POST"])
def create_user():  # create user's question  and store into
    create_user_form = CreateUserForm(request.form)
    if request.method == "POST" and create_user_form.validate():
        User.create_user(
            str(uuid4()),
            create_user_form.name.data,
            create_user_form.email.data,
            create_user_form.subject.data,
            create_user_form.remarks.data,
        )

        return redirect(
            url_for("thank_you")
        )  # Redirect to TYpage.html after form submission
    return render_template(
        "ContactUs.html", form=create_user_form, current_year=datetime.now().year
    )


# end of terrence code

if __name__ == "__main__":
    app.run()
