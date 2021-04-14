def create_db():
    engine = create_engine(db_name)
    Base.metadata.create_all(engine)
    print("Database created!")


def drop_db():
    if database_exists(db_name):
        drop_database(db_name)
        print("Database dropped!")


def reset_db():
    session.query(Fines).delete()
    session.query(Gendarmes).delete()
    session.query(Citizens).delete()
    session.query(Districts).delete()
    session.commit()
    print("Database reseted!")

def create_user(email, password):
    if get_user_by_email(email):
        return False
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user


def create_user_from_login_session():
    name = login_session['name']
    email = login_session['email']
    if not email:
        return False
    user = get_user_by_email(email)
    if user:
        return user
    user = create_user(email, name)
    return user


def get_all_users():
    return session.query(User).all()


def get_user_by_id(id):
    try:
        return session.query(User).filter_by(id=id).one()
    except:
        return None


def get_user_by_email(email):
    try:
        return session.query(User).filter_by(email=email).one()
    except:
        return None


def get_current_user():
    email = login_session.get('email')
    return get_user_by_email(email) if email else None


def get_current_user_id():
    user = get_current_user()
    return user.id if user else None


def update_current_user_info(**kwargs):
    user = get_current_user()
    if not user:
        return False
    name = kwargs.get('name')
    bio = kwargs.get('bio')
    picture_url = kwargs.get('picture_url')
    if name:
        user.name = name
    if bio:
        user.bio = bio
    if picture_url:
        user.picture_url = picture_url
    session.add(user)
    session.commit()
    return user


def update_current_user_info_from_login_session():
    name = login_session['name']
    email = login_session['email']
    picture_url = login_session['picture']
    if not email:
        return False
    user = get_user_by_email(email)
    if not user:
        return False
    user.name = name
    user.picture_url = picture_url
    session.add(user)
    session.commit()
    return user

def create_or_update_current_user_from_login_session():
    email = login_session['email']
    user = get_user_by_email(email)
    if user:
        update_current_user_info_from_login_session()
        return user
    else:
        return create_user_from_login_session()


def delete_current_user():
    user = get_current_user()
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True
