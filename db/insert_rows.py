from create_tables import db

def insert_row(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    db.session.commit()
