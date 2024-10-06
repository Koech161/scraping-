from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    img_src = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Product {self.id}, {self.title}, {self.price}, {self.img_src}>'
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'img_src': self.img_src
        }