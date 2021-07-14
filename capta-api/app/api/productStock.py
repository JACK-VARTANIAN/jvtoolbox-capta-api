import pandas as pd
from app.authentication import token_required
from flask_restful import Resource
from app.connection import connection 

class productStock(Resource):
    def __init__(self, **kwargs):
        self.conn=kwargs["conn"]    
    @token_required
    def get(self, reference):
        conn = self.conn
        query = f"""
                SELECT 
                b.cpros,
                a.codtams,
                a.qtds,
                a.emps,
                a.contas,
                z.rclis,
                CONVERT ( CHAR,a.cbars) AS barra,

                CASE
                WHEN b.encoms = 1 THEN 'Sim'
                ELSE 'Não'
                END AS encomendavel,

                CASE
                WHEN b.situas = 1 THEN 'Ativo'
                ELSE 'Inativo'
                END AS status

                FROM sljeti a with(nolock)
                LEFT JOIN sljcli z with(nolock) ON a.contas = z.iclis
                LEFT JOIN sljgccr y with(nolock) ON a.grupos = y.codigos
                LEFT JOIN sljpro b WITH(NOLOCK) ON a.cpros = b.cpros
                LEFT JOIN sljcor c WITH(NOLOCK) ON b.codcors = c.cods
                LEFT JOIN sljgru f WITH(NOLOCK) ON b.cgrus = f.cgrus
                LEFT JOIN sljsgru g WITH(NOLOCK) ON b.cgrus+ + b.sgrus = g.cgrucods
                LEFT JOIN sljcol e WITH(NOLOCK) ON b.colecoes = e.colecoes
                WHERE a.contas <> '' AND b.mercs = 'PA' AND b.cpros LIKE '%{reference}%' AND z.rclis LIKE '%ESTOQUE VENDA%'
                """


        df = pd.read_sql(query, conn).applymap(lambda x: x.strip() if isinstance(x, str) else x)
        response ={
                "product":reference,
                "stock": "1" 
        } 

        return response

