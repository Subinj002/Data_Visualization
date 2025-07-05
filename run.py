from app import create_app, db
from app.models import Inventory
app = create_app()

with app.app_context():
    db.create_all()
    db.session.add(Inventory(item_name="Pallet A", quantity=100, category="Raw Materials"))
    db.session.add(Inventory(item_name="Box B", quantity=45, category="Finished Goods"))
    db.session.add(Inventory(item_name="Crate C", quantity=20, category="Packing Materials"))

    db.session.commit()
    print("✅ Sample inventory data inserted.")
if __name__ == '__main__':
    app.run(debug=True)
