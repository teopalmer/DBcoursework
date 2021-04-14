from flask_bcrypt import Bcrypt

# CREATE

def create_user(email, password, g_id=None, g_credentials=None):
    if password is not None:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    else:
        hashed_password = None

    user = User(email=email,
                hashed_password=hashed_password,
                g_id=g_id,
                g_credentials=g_credentials)
    db.session.add(user)
    db.session.commit()
    return user
    
def newFine():
    if request.method == 'POST':
        description = request.form['description'] or None
        cost = request.form.['cost'] or []
        offender_id = request.form['offender_id'] or None
        prosecutor_id = request.form['prosecutor_id'] or None
        date_posted = request.form['date_posted'] or None

        if not offender_id or not prosecutor_id or not cost:
            flash('Please fill in the blanks', 'danger')
            return;

        book = dbh.create_book(name=name,
                               description=description,
                               genres_ids=genres_ids,
                               cover_image_url=cover_image_url,
                               page_count=page_count,
                               author_name=author_name,
                               year=year)

        if book:
            flash('Book Added!', 'success')
        return h.redirect_books()

# READ

def get_offender(fine_id):
    fine = Fines.query.get(fine_id)
    return derfine.offender_id
    
def get_citizens_by_rank(rank):
    condition = (Citizens.rank == rank)
    cits = (Citizens.query
                    .filter(condition)
                    .all())
    return cits
    
def get_fines_to_date(date):
    condition = (Fines.date_posted <= date)
    fins = (Fines.query
                        .filter(condition)
                        .all())
    return fins

# UPDATE

def update_fine_status(fine_id, status):
    fine = Fines.query.get(fine_id)
    fine.status = status
    db.session.commit()
    return fine
