from base import db, Information

# Creating
info = Information('meow', 5)
db.session.add(info)
db.session.commit()

# Read

all_info = Information.query.all()
print(all_info)

# Selection id
info_one = Information.query.get(1)
print(info_one.name)

# Filter
info_frank = Information.query.filter_by(name = 'frank')
print(info_frank.all())

# Update
first_info = Information.query.get(1)
first_info.age = 30
db.session.add(first_info)
db.session.commit()

# Delete
second_info = Information.query.get(2)
db.session.delete(second_info)
db.session.commit()

all_info = Information.query.all()
print(all_info)
