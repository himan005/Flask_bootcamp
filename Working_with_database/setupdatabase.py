from base import db, Information

db.create_all()

john = Information('John', 24)
frank = Information('Frankie', 26)

print(john.id)
print(frank.id)

db.session.add_all([john, frank])

db.session.commit()


