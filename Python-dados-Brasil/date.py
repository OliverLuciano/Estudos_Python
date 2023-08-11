from datetime import datetime

class DatasBr:
    def __init__(self) -> None:
        self.time_stamp = datetime.today()
        
    def __str__(self) -> str:
        data_formatada = self.time_stamp.strftime("%A %d/%m/%Y  %H:%M")
        return data_formatada
        
    def mes_cadastro(self):
        meses_ano = [
            "janeiro", "fevereiro", "março", 
            "abril", "maio", "junho", 
            "julho", "agosto", "setembro", 
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.time_stamp.month
        return meses_ano(mes_cadastro - 1)
        
    def dia_semana(self):
        dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        dia_semana = self.time_stamp.weekday()
        return dias_semana[dia_semana - 1]