import json
import pandas as pd

from app.authentication import token_required
from flask_restful import Resource, request
from app.connection import connection

class productInfo(Resource):
    @token_required
    def get(self, reference):
        endpoint=request.path.split("/")[2]

        colToSearch=''
        if endpoint == "products_by_cpros":
           colToSearch="cpros"
        elif endpoint == "products_by_colecoes":
           colToSearch="colecoes"
        elif endpoint == "products_by_cgrus":
           colToSearch="cgrus"

        conn = connection()
        query = f"""
                SELECT cpros, cgrus, sgrus, codcors, dpros, dtincs, metals, mercs, pvens, colecoes 
                FROM SLJPRO
                WHERE mercs = 'PA' AND {colToSearch} LIKE '%{reference}%'
                """

        if endpoint == "products_by_cpros":
           df = pd.read_sql(query, conn).applymap(lambda x: x.strip() if isinstance(x, str) else x).to_json(orient='records')[1:-1].replace('},{', '} {')
        else: 
           df = pd.read_sql(query, conn).applymap(lambda x: x.strip() if isinstance(x, str) else x).to_json(orient='index')
          
        response = json.loads(df)
        return response

