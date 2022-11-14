config = Blueprint('config', __name__)


@blogs.route('/')
def index():
    return render_template("index.html")
