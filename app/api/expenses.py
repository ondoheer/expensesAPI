from flask import Blueprint, jsonify, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.exc import NoResultFound

from app.models import db
from app.models.user import User
from app.models.expense import Expense
from app.models.month import Month



expenses = Blueprint("expenses", __name__)

@expenses.route("/expense", methods=["GET"])
@jwt_required
def query():
    """
    The following parameters WILL alter the query:

    last = True // will bring only the last one

    """

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({'error': 'not authorized'}), 401

    # Query parameters
    last = request.args.get('last', False) #this one is used for the add expenses form 
    per_page = int(request.args.get('per_page', 10))
    page = int(request.args.get('page', 1))
    search = request.args.get('search', False)

    user = User.query.filter_by(email=current_user).first()

    ## BASE QUERY
    ## We order by id because it's fastet han date and it's increasing automatically
    _base_query = db.session.query(Expense).filter_by(user_id=user.id).order_by(Expense.id.desc())
    



    ## only used to retrieve the last expense
    if last:
        
        expense = _base_query.first();
        return jsonify(Expense.serialize(expense)), 200

    # Search doesn't paginate
    if search:
        expenses = _base_query.filter(Expense.name.ilike(
                        f"%{search}%")).all()
        to_return = {
            "expenses": Expense.serialize_list(expenses),
            "status": "from search"
        }
        return jsonify(to_return)
    
    # just get the paginated objects
    else:

        paginated_query = _base_query.paginate(page=page, per_page=per_page, error_out=False) # paginated object on error empty list returned
        
        expenses = paginated_query.items

        to_return = {
            'expenses': Expense.serialize_list(expenses),
            'has_next':paginated_query.has_next,
            'has_prev': paginated_query.has_prev,
            'next_num': paginated_query.next_num,
            'prev_num': paginated_query.prev_num,
            'pages': paginated_query.pages
        }

        return jsonify(to_return), 200




@expenses.route("/expense", methods=['POST'])
@jwt_required
def create():
    

    current_user = get_jwt_identity()

    if not current_user:
        return jsonify({'error': 'not authorized'}), 401

    user = User.query.filter_by(email=current_user).first()

    params = request.get_json()
    amount = params.get('amount', None)
    name = params.get('name', None)
    category_id = params.get('category_id', None)



    # This ought to be better validated
    if not amount or not name or not category_id:
        return jsonify({"msg": "Bad request"}), 400

    new_expense = Expense(
        name=name,
        amount=amount,
        category_id=category_id,
        user_id=user.id
    )

    month_code = Month.build_user_month_code(user.id)
    try:
        month = db.session.query(Month).filter(
            Month.year_month_usr == month_code
        ).one()
    except NoResultFound:

        month = Month(year_month_usr=month_code, user_id=user.id)
    # new expense for the month
    month.expenses.append(new_expense)
    db.session.add(month)

    # db.session.add(new_expense)
    db.session.commit()

    return jsonify({'msg': 'Expense added'}), 201

