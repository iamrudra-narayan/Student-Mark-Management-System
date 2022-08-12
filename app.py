from flask_mysqldb import MySQL
from flask import Flask,render_template,request,redirect

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'gugula12'
app.config['MYSQL_DB'] = 'student'

mysql = MySQL(app)

@app.route("/", methods=["GET","POST"])
def entry():
    if request.method == "POST":
        details = request.form
        roll = details[roll]
        name = details['name']
        clg_name = details['cname']
        dob = details['dob']
        eptd = details['eptd']
        em = details['em']
        foc = details['foc']
        ed = details['ed']
        cs = details['cs']
        total = details['total']
        per = details['per']
        grade = details['grade']

        #connect to databae
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student_marksheet(roll, name, clg_name, dob, EPTD, EM, FOC, ED, CS, total, per, grade) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(roll,name,clg_name,dob,eptd,em,foc,ed,cs,total,per,grade))
        
        mysql.connection.commit()
        cur.close()
        return redirect('/', msg='Uploaded Successfully.')
    return render_template('mark_entry.html')

@app.route("/result")
def show():
    if request.method == "POST":
        roll = request.form
        roll_no = roll['roll']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM mark_sheet WHERE roll=(%d)",(roll_no))
        
        mysql.connection.fet()
        cur.close()
        return redirect('/result', msg='Uploaded Successfully.')

    return render_template('show_result.html')

if __name__=="__main__":    
    app.run(debug=True)