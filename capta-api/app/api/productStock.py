import pandas as pd
import json
from app.config.authentication import token_required
from flask_restful import Resource
from app.config.connection import connection 
from flask import request

class productStock(Resource):
    def __init__(self, **kwargs):
        self.conn=kwargs["conn"]    
    @token_required
    def post(self):
        references = request.get_json(force=True)["products"]
        conn = self.conn
        
        search = f"RTRIM(a.cpros) = '{references[0]}'"
        if len(references) > 1:
            for ref in range(1, len(references)):
                print(ref)
                search += f" OR RTRIM(a.cpros) = '{references[ref]}'"
                
        query = f"""
                SELECT 
                        a.cpros,
                        a.codtams,
                        CASE
                                WHEN a.codtams <> '' THEN CONCAT(RTRIM(a.cpros), '-', a.codtams)
                                ELSE CONCAT(RTRIM(a.cpros), '-')
                        END as vtexskuref,
                        SUM(a.qtds) as qtds,
                        a.empos,
                        c.rclis
                FROM sljeti a WITH (NOLOCK)
                LEFT JOIN sljpro b WITH (NOLOCK) ON a.cpros = b.cpros
                LEFT JOIN sljcli c WITH (NOLOCK) ON a.contas = c.iclis
                LEFT JOIN sljgru f WITH (NOLOCK) ON b.cgrus = f.cgrus
                WHERE a.contas <> ''
                        AND b.mercs = 'PA'
                        AND f.dgrus <> 'MOD' 
                        AND RTRIM(c.rclis) = 'ESTOQUE VENDA'
                        AND ({search})
                GROUP BY a.codtams, a.cpros, a.codtams, a.empos, c.rclis
                """


        df = pd.read_sql(query, conn).applymap(lambda x: x.strip() if isinstance(x, str) else x).to_json(orient='index')
          
        response = json.loads(df)

        return response

