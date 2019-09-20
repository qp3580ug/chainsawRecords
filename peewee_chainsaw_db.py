from peewee import *

db = SqliteDatabase('chainsaw_juggle_records.db')

class recordHolder(Model):
    holder = CharField()
    country = CharField()
    catches = IntegerField()


    class Meta:
        database = db

    def __str__(self):
        return f'{self.holder} is from {self.country} and has {self.catches} catches.'

db.connect()
db.create_tables([recordHolder])

newHolder = input('Enter Record Holder\'s Full Name: ')
newCountry = input('Enter Record Holder\'s Country: ')
newCatches = int(input('Enter their total number of catches: '))

newEntry = recordHolder(holder=newHolder, country=newCountry, catches=newCatches)
newEntry.save()

recordHolderSearch = input('Enter Record Holder\'s Full Name you Would Like to Search: ')

searchResults = recordHolder.select().where(recordHolder.holder == recordHolderSearch)

for row in searchResults:
    print(row)

updateHolder = input('Enter Record Holder\'s name you would like to change: ')
updatedCatches = int(input('Enter a new number of catches for the Record Holder: '))

changedRows = recordHolder.update(catches=updatedCatches).where(recordHolder.holder == updateHolder).execute()

print('Rows Updated: ', changedRows)

holderToDelete = input('Enter Record Holder\'s name you would like to delete: ')

holdersDeleted = recordHolder.delete().where(recordHolder.holder == holderToDelete).execute()

print('Rows Deleted: ', holdersDeleted)