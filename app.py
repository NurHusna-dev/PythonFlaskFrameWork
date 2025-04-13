from flask import Flask, render_template

app = Flask(__name__)


app_name = "My Application Name is: Dimas dan Desi"

# 1 App Route di Flask "hello world"
@app.route("/")
def hello_world():
    return f"<p>Hello, semuanya, apa kabar! {app_name}</p>"


# 2 App Route di Flask
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Selamat Datang di Aplikasi Flask</p>"


# 3 App Route dengan HTML
@app.route("/about/")
def about():
    return render_template('about_without_bootstrap.html')

# 4 App Route dengan HTML without bootstrap
@app.route("/about-bootstrap/")
def about_bootstrap():
    return render_template('about.html')


#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(nama_mahasiswa):
    return "nama anda adalah {}".format(nama_mahasiswa)

#6 App Route ID
@app.route('/user/<int:user_id>')  # hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

#7 App Route Variabel Global
@app.route('/variabel-global/')
def variabel_global():
    return f"Welcome {app_name}"

#8 App Route Dictionary Variabel
@app.route('/data')
def data():
    user = {"name": "Disel", "age": 20, "city": "Palembang"}
    return render_template('data.html', user=user)
if __name__ == "__main__":
    app.run()