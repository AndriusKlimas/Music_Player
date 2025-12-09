from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#Route get-catalog, returns jinja template
@app.route('/get-catalog')
def get_catalog():
    """ Return the catalog as a web page """
    response = requests.get("http://catalog-svc:5000/get-catalog", timeout=5)
    catalog = response.json()
    # Get username from cookie
    username = request.cookies.get('userID')
    #render and return the template
    return render_template("shop-front.html.j2", products=catalog['catalog'].values(), username=username)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    