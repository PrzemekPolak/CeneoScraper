from app import app
from flask import render_template, request, url_for
from flaskext.markdown import Markdown
from app.forms import ProductForm
import requests
from app.models import Opinion, Product
import pandas as pd
Markdown(app)

app.config['SECRET_KEY'] = 'tajny'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    content = ''
    with open('README.md', 'r', encoding='UTF-8') as f:
        content = f.read()
    return render_template('about.html', text=content)

@app.route('/extract', methods=['POST', 'GET'])
def extract():
    form = ProductForm()
    if form.validate_on_submit():
        product_id = form.product_id.data
        page_response = requests.get("https://www.ceneo.pl/"+product_id)
        if page_response.status_code == requests.codes['ok']:
            product = Product(product_id)
            product.extract_product()
            product.save_product()
            return redirect(url_for('product', id=product_id))
        else:
            form.product_id.errors.append('Podana wartość nie jest poprawnym kodem produktu.')
    return render_template('extract.html', form=form)

@app.route('/product/<id>')
def product(id):
    product = Product(id)
    product.read_product()
    opinions = pd.DataFrame.from_records([opinion.__dict__() for opinion in product.opinions])
    opinions['stars'] = opinions['stars'].map(lambda x: float(x.split('/')[0].replace(',', '.')))
    return render_template(
        'product.html'
        tables = [
            opinions.to_html(
                classes= 'table table-bordered table-sm table-responsive',
                table_id= 'opinions',
                index= False
            )
        ],
        titles = opinions.columns.values
    )

    # opinions = pd.read_json('app/opinions_json/' + id + '.json')
    # opinions = opinions.set_index('opinion_id')

@app.route('/products')
def products():
    pass