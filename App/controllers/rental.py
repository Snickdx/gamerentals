from App.models import Rental, Listing, User
from App.database import db

def create_rental(userId, listingId):
    listing = Listing.query.filter_by(listingId=listingId, status='available')
    if listing:
        listing.status = 'rented'
        rental = Rental(userId, listingId)
        db.session.add(rental)
        db.session.commit()
        return True
    return False

def get_outstanding_user_rentals(userId):
    user = User.query.get(userId)
    if user :
        return Rental.query.filter_by(userId=userId, return_date=None)
    return False
        
def get_outstanding_rentals():
    return Rental.query.filter_by(return_date=None)

def return_rental(userId, rentalId):
    rental = Rental.query.filter_by(rentalId=rentalId, userId=userId).first()
    if rental:
        return rental
    return False

