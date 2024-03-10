class Paciente:
    pacientes = []

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []
        self.paciente = {'Nome': self.nome, 'Idade': self.idade, 'Historico': self.historico}
        Paciente.pacientes.append(self.paciente)

        print(f"""\n****** PACIENTE CADASTRADO COM SUCESSO *****\n
                \n Nome: {self.nome}
                \n Idade: {self.idade}\n""")
                
    def visualizarConsulta(self):
        for consulta in self.historico:
            print(f"""\n*********** HISTÓRICO ***********\n
                        \n Data da consulta: {consulta[0]}
                        \n Paciente: {consulta[1]}
                        \n Médico responsável: {consulta[2]}
                        \n Diagnótico: {consulta[3]}
                        \n Regitrado por: {consulta[4]}\n""")

class Funcionario:
    funcionarios = []

    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo  
                
class Atendente(Funcionario):
    def __init__(self, nome, cargo):
        super().__init__(nome, cargo)
        self.funcionario = {'Nome': self.nome, 'Cargo': self.cargo}
        Funcionario.funcionarios.append(self.funcionario)

        print(f"""\n****** ATENDENTE CADASTRADO COM SUCESSO *****\n
                \n Atendente: {self.nome}
                \n Cargo: {self.cargo}\n""")
        
    def agendarConsulta(self, data, paciente_nome, medico_nome, especialidade):
        responsavel = self.nome
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                for funcionario in Funcionario.funcionarios:
                    if funcionario['Nome'] == medico_nome:
                        consulta = (data, paciente_nome, medico_nome, especialidade, responsavel)
                        paciente['Historico'].append(consulta)
                        print(f"""\n ************ CONSULTA AGENDADA ************\n
                                    \n Data: {data}
                                    \n Paciente: {paciente_nome}
                                    \n Médico: {medico_nome}
                                    \n Especialidade: {especialidade}
                                    \n Registro: {responsavel}\n""")
                        break
                    else:
                        print('Médico não encontrado na base de dados.')
            else:
                print('Paciente não encontrado na base de dados.')
                
class Medico(Funcionario):
    def __init__(self, nome, cargo, especialidade, crm):
        super().__init__(nome, cargo)
        self.especialidade = especialidade
        self.crm = crm
        self.funcionario = {'Nome': self.nome, 'Cargo': self.cargo, 'Especialidade': self.especialidade, 'CRM': self.crm}
        Funcionario.funcionarios.append(self.funcionario)

        print(f"""\n****** MÉDICO CADASTRADO COM SUCESSO *****\n
                \n Médico: {self.nome}
                \n Cargo: {self.cargo}
                \n Especialidade: {self.especialidade}
                \n CRM: {self.crm}\n""")

    def prescreverMedicamento(self, paciente_nome, medicamento, prescricao):
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                print(f"""\n*********** RECEITA ***********\n
                        \n Paciente: {paciente_nome}
                        \n Medicamento: {medicamento}
                        \n Prescrição: {prescricao}
                        \n Assinatura do Médico: {self.nome}\n""")
                break
            else:
                print('Paciente não encontrado.')

    def realizarExame(self, data, paciente_nome, exame):
        medico = self.nome
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                exame = (data, paciente_nome, medico, exame)
                paciente['Historico'] += exame
                print(f"""\n ************* EXAME *************\n
                        \n Data do exame: {data}
                        \n Exame: {exame[3]}
                        \n Paciente: {paciente_nome}
                        \n Médico responsável: {medico}
                        \n Registro concluído com sucesso!\n""")
            else:
                print('Paciente não encontrado.')
                
class Enfermeiro(Funcionario):
    def __init__(self, nome, cargo, coren):
        super().__init__(nome, cargo)
        self.coren = coren
        self.funcionario = {'Nome': self.nome, 'Cargo': self.cargo, 'COREN': self.coren}
        Funcionario.funcionarios.append(self.funcionario)
        # print(Funcionario.funcionarios)

        print(f"""\n****** ENFERMEIRO CADASTRADO COM SUCESSO *****\n
                \n Enfermeiro: {self.nome}
                \n Cargo: {self.cargo}
                \n COREN: {self.coren}\n""")
        
    def aplicarInjecao(self, paciente_nome, medicamento):
        enfermeiro = self.nome
        for paciente in Paciente.pacientes:
            if paciente['Nome'] == paciente_nome:
                print(f"""\n ************ MEDICAÇÃO *************\n
                        \n Tipo de medicação: Injeção
                        \n Medicamento: {medicamento}
                        \n Paciente: {paciente_nome}
                        \n Enfermeiro responsável: {enfermeiro}
                        \n Medicação aplicada com sucesso!""")
        

pac = Paciente('Caroline', '26')
med = Medico('José', 'Médico', 'Oftalmologista', 12345)
ate = Atendente('Fernando', 'Atendente')
enf = Enfermeiro('Julia', 'Enfermeira', 54321)

ate.agendarConsulta('06/03/2024', 'Caroline', 'José', 'Oftalmologista')

pac.visualizarConsulta()

med.prescreverMedicamento('Caroline','Dipirona','tomar de 8 em 8h')

med.realizarExame('10/03/2024','Caroline','Refração')

enf.aplicarInjecao('Caroline','Benzetacil')

ate.agendarConsulta('06/03/2024', 'Caroline', 'José', 'Sintomas gripais, remedio administrado.')
pac.visualizarConsulta()

med.prescreverMedicamento('Caroline','Dipirona','tomar de 8 em 8h')
