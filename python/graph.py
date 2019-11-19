from flask import Flask, render_template,jsonify,request,render_template
import pandas as pd

df = pd.read_csv('3M_India_Ltd..csv')
dc =  pd.DataFrame(df[["Date","High"]],)

#dc.index= pd.to_datetime(dc[""])
dc.set_index("Date",inplace=True)
print(dc.head())
print(type(dc.reset_index().values))

k = [[1,2],[4,8]]


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('basic.html',d = dc.reset_index().values ) # If you replace dc.reset_index().values with k then it work fine # If you replace dc.to_json(orient='table') with k then it work fine

if __name__ == '__main__':
    app.run(port = 5000,debug = True )
