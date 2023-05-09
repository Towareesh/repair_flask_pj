from app.auth import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'Auth Route'