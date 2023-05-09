from app.errors import errors_bp


@errors_bp.errorhandler(404)
def not_found_error(error):
    return 404
