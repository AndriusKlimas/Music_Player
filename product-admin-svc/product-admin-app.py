from flask import Flask, redirect, render_template, request
import requests

app = Flask(__name__)
#route add product
@app.route('/add-product-page')
def add_product_page():
    """ Return the add product page """
    return render_template("add-product.html.j2")

#route add-product
@app.route('/add-product', methods=['POST'])
def add_product():
    """ Add product to catalog service """
    product = {
        "name": request.form['name'],
        "artist": request.form['artist'],
        "album": request.form['album'],
        "audio_mp3": request.form['audio_mp3']

    }
    requests.post("http://catalog-svc:5000/add-product", json=product, timeout=5)

    return redirect("/get-catalog")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)