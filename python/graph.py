from flask import Flask, render_template,jsonify,request,render_template
import pandas as pd

df = pd.read_csv('3M_India_Ltd..csv')
dc =  pd.DataFrame(df[["Date","High"]],)

#dc.index= pd.to_datetime(dc[""])
dc.set_index("Date",inplace=True)
print(dc.head())
print(type(dc.reset_index().values))




app = Flask(__name__)
@app.route('/')
def home():
    return render_template('basic.html',d = dc.to_json(orient='table') )

if __name__ == '__main__':
    app.run(port = 5000,debug = True )
