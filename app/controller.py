from flask import render_template, request, redirect, url_for, flash, session
from app import app, bcrypt


@app.route('/')
def admin():
    if 'name' in session:
        best = productBest()
        new = productNewest(3)
        a = len(lenProduct())
        b = len(lenCategory())
        c = len(lenUser())
        d = len(lenWriter())
        session['product'] = a
        session['category'] = b
        session['user'] = c
        session['writer'] = d
        return render_template('dashboard/display/index.html', data = best, product=new)
    data = Widget()
    product = productRecomendation()
    oldest = productNewest(4)
    return render_template('admin/index.html', title='Admin Page', product=product, data=data, oldest = oldest)

@app.route('/register', methods=['GET', 'POST'])
def register():
    UPLOAD_FOLDER = '.\\static\\profile-pict'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        name = form.name.data
        username = form.username.data
        email = form.email.data
        if 'pic' not in request.files:
            return "no file"
        else:
            pic = request.files['pic']
            filename = pic.filename
        user = checkUser(email)
        if not user:
            if pic and allowed_file(filename):
                filename = secure_filename(filename)
                pic.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))            
                addUser(name, username, email, hash_password, filename)
                flash('Hai, '+ name +'! Your account has been registering')
                return redirect(url_for('login'))
        else:
            if name == user[1]:
                flash('Your name already has account')
                return redirect(url_for('register'))
            elif username == user[2]:
                flash('Your username already takken')
                return redirect(url_for('register'))
            elif email == user[3]:
                flash('Your email already has account')
                return redirect(url_for('register'))
    return render_template('admin/register.html', form=form, title="Registeration Page")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        email = form.email.data 
        pwd = form.password.data       
        user = checkUser(email)
        if email == user[3]:
            if bcrypt.check_password_hash(user[4], pwd):    
                if user[6] == 1:
                    session['username'] = user[2]
                    flash('Welcome ' + (session['username']) + '! You are logedin now!')
                    return redirect(url_for('admin'))
                else:
                    session['name'] = user[1]
                    flash('Welcome ' + (session['name']) + '! Keep everything inside secret!')
                    return redirect(url_for('admin'))
            else:
                flash('ERROR : Wrong password')
        else:
            flash('ERROR : This email is not used yet')
    return render_template('admin/login.html', form=form, title="Login Page")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/library")
def library():
    a = productAll()
    session['productPage'] = ''
    return render_template('admin/buku.html', product = a, all = "all")

@app.route("/library-latest")
def productLatests():
    a = productLatest()
    return render_template('admin/buku.html', product = a, all = "all", latest="new")

@app.route("/library-priceL")
def productPriceLow():
    a = productPriceLtH()
    return render_template('admin/buku.html', product = a, all = "all", low = 'low')

@app.route("/library-priceH")
def productPriceHigh():
    a = productPriceHtL()
    return render_template('admin/buku.html', product = a, all = "all", high = 'high')

@app.route("/cooking")
def cooking():
    a = productPerCategory('Cooking')
    session['productPage'] = 'COOKING'
    return render_template('admin/buku.html', product = a)

@app.route("/fairytale")
def fairytale():
    a = productPerCategory('Fairytale')
    session['productPage'] = 'FAIRYTALE'
    return render_template('admin/buku.html', product = a)

@app.route("/novel")
def novel():
    a = productPerCategory('Novel')
    session['productPage'] = 'NOVEL'
    return render_template('admin/buku.html', product = a)

@app.route("/notes")
def notes():
    a = productPerCategory('Notes')
    session['productPage'] = 'NOTE'
    return render_template('admin/buku.html', product = a)

@app.route("/education")
def education():
    a = productPerCategory('Education')
    session['productPage'] = 'EDUCATION'
    return render_template('admin/buku.html', product = a)

@app.route("/<name>")
def detailProduct(name):
    data = productDetails(name)
    product = productMayYouLike(name)
    return render_template("products/detail.html", data=data, product=product)
