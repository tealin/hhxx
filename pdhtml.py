
class pdhtml():
    def __init__(self,df,index=0):
        self.index=index
        self.head = '''<!Doctype html>
<html xmlns=http://www.w3.org/1999/xhtml>
<head>
   <meta http-equiv=Content-Type content="text/html;charset=utf-8">
   <title>DataFrame html</title>  
    <style type="text/css">
    table.dataframe {
        font-family: verdana,arial,sans-serif;
        font-size:11px;
        color:#333333;
        border-width: 1px;
        border-color: #666666;
        border-collapse: collapse;
    }
    table.dataframe th {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #666666;
        background-color: #dedede;
    }
    table.dataframe td {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #666666;
        background-color: #ffffff;
    }
    </style>

</head>
<body>'''

        self.footer = '''
</body>
</html>
            '''

        self.table = df.to_html(index=self.index)

    def to_html(self,file):
        with open(file,'w',-1,'utf-8')as f:
            f.write(self.head)
            f.write(self.table)
            f.write(self.footer)


if __name__ == '__main__':
    import pandas as pd
    a =[
     [1,2,3,4],
     [2,3,4,5],
     [3,4,5,6]
     ]
    df = pd.DataFrame(a,columns=['one','two','three','four'])
    pdhtml(df).to_html('temp.html')


