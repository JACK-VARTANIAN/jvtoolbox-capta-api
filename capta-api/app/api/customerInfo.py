import json
import pandas as pd
from app.authentication import token_required
from flask_restful import Resource
from app.connection import connection

class customerInfo(Resource):
   @token_required
   def get(self, customer):
      conn = connection()
      query = f"""
         SELECT a.iclis,
            a.rclis,
            a.sexos,
            a.estcivils,
            a.cpfs,
            a.nascs,
            a.dtcasas,
            a.contavens,
            a.ddds,
            a.faxs,
            a.tel1s,
            a.tel2s,
            a.tel3s,
            a.emails,
            a.grupos,
            a.conjuges,
            a.cpfcs,
            a.ceps,
            a.endes,
            a.nums,
            a.compls,
            a.bairs,
            a.cidas,
            a.estas,
            a.paises,
            a.situas,
            a.fpubls,
            a.ultcomps,
            a.dataincs,
            a.dtalts,
            a.obs,
            a.inativas
         FROM sljcli a WITH(NOLOCK)
            LEFT OUTER JOIN sljscli b WITH(NOLOCK) ON a.situas=b.codigos
            LEFT OUTER JOIN sljfpubl c WITH(NOLOCK) ON a.fpubls=c.cods
            LEFT OUTER JOIN sljcli d WITH(NOLOCK) ON a.contavens=d.iclis
         WHERE a.grupos IN ('CLIENTES',
                           'PROSPECT',
                           'ACOMP LOJA',
                           'P SOCIAL',
                           'PRODUTORES',
                           'IMPRENSA')
         AND a.iclis LIKE '%{customer}%'                  
                        """
      df = pd.read_sql(query, conn).applymap(lambda x: x.strip() if isinstance(x, str) else x).to_json(orient='index')
          
      response = json.loads(df)
      
      return response

