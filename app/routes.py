from flask import Blueprint, render_template
from app.models import Inventory
import pandas as pd
import plotly.express as px

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    data = Inventory.query.all()
    df = pd.DataFrame([{
        'Item': item.item_name,
        'Quantity': item.quantity,
        'Category': item.category
    } for item in data])

    fig = px.bar(df, x='Item', y='Quantity', color='Category', title="Inventory Levels")
    graph_html = fig.to_html(full_html=False)

    return render_template('dashboard.html', graph=graph_html)
