def findDecision(obj): #obj[0]: História, obj[1]: Dívida, obj[2]: Garantia, obj[3]: Renda, obj[4]: Idade, obj[5]: Emprego
   # {"feature": "Renda", "instances": 30, "metric_value": 0.3796, "depth": 1}
   if obj[3] == '15-35k':
      # {"feature": "Hist\u00f3ria", "instances": 12, "metric_value": 0.4778, "depth": 2}
      if obj[0] == 'Boa':
         # {"feature": "Emprego", "instances": 5, "metric_value": 0.0, "depth": 3}
         if obj[5] == 'Estável':
            return 'Baixo'
         elif obj[5] == 'Instável':
            return 'Moderado'
         else:
            return 'Baixo'
      elif obj[0] == 'Desconhecida':
         # {"feature": "D\u00edvida", "instances": 4, "metric_value": 0.0, "depth": 3}
         if obj[1] == 'Alta':
            return 'Alto'
         elif obj[1] == 'Baixa':
            return 'Moderado'
         else:
            return 'Alto'
      elif obj[0] == 'Ruim':
         # {"feature": "D\u00edvida", "instances": 3, "metric_value": 0.0, "depth": 3}
         if obj[1] == 'Alta':
            return 'Alto'
         elif obj[1] == 'Baixa':
            return 'Moderado'
         else:
            return 'Alto'
      else:
         return 'Moderado'
   elif obj[3] == '0-15k':
      # {"feature": "Emprego", "instances": 9, "metric_value": 0.0, "depth": 2}
      if obj[5] == 'Instável':
         return 'Alto'
      elif obj[5] == 'Estável':
         return 'Moderado'
      else:
         return 'Alto'
   elif obj[3] == '>35k':
      # {"feature": "Hist\u00f3ria", "instances": 9, "metric_value": 0.0, "depth": 2}
      if obj[0] == 'Boa':
         return 'Baixo'
      elif obj[0] == 'Desconhecida':
         return 'Baixo'
      elif obj[0] == 'Ruim':
         return 'Moderado'
      else:
         return 'Baixo'
   else:
      return 'Alto'
