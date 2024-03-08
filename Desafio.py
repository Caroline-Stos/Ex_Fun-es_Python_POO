class Paciente:
    pacientes = {}

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []
        Paciente.pacientes[nome] = self

        # print(f"""\n ******PACIENTE CADASTRADO COM SUCESSO***** \n
        #         Nome: {self.nome} \n
        #         Idade: {self.idade} \n
        #         """)

    def visualizarConsulta(self):
        print("""Data da consulta: {self.data} \n
                Paciente: {self.paciente} \n
                Médico responsável: {self.medico} \n
                Regitrado por: {self.responsavel}
            """)

class Funcionario:
    funcionarios = []

    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
    def agendarConsulta(self, data, paciente_nome, medico):
        self.data = data
        self.medico = medico
        self.responsavel = self.nome

        if paciente_nome in Paciente.pacientes:
            paciente = Paciente.pacientes[paciente_nome]
            consulta = (data, paciente.nome, medico, self.responsavel)
            paciente.historico.append(consulta)
            print(f"Consulta agendada para {paciente.nome}.")
        else:
            print("Paciente não encontrado.")

class Atendente(Funcionario):
    def __init__(self, nome, cargo):
        super().__init__(nome, cargo)
        # print(f"""\n ******ATENDENTE CADASTRADO COM SUCESSO***** \n
        #         Atendente: {self.nome} \n
        #         Cargo: {self.cargo} \n
        #         """)
  
class Medico(Funcionario):
    def __init__(self, nome, cargo, especialidade, crm):
        super().__init__(nome, cargo)
        self.nome = nome
        self.cargo = cargo
        self.especialidade = especialidade
        self.crm = crm
        medico = (nome, cargo, especialidade, crm)
        Funcionario.funcionarios.append(medico)
        # print(f"""\n ******MÉDICO CADASTRADO COM SUCESSO***** \n
        #         Médico: {self.nome} \n
        #         Cargo: {self.cargo} \n
        #         Especialidade: {self.especialidade} \n
        #         CRM: {self.crm}""")
        
    def prescreverMedicamento(self, paciente_nome, medicamento):
        paciente = paciente_nome


class Enfermeiro(Funcionario):
    def __init__(self, nome, cargo, coren):
        super().__init__(nome, cargo)
        self.nome = nome
        self.cargo = cargo
        self.coren = coren
        enfermeiro = (nome, cargo, coren)
        Funcionario.funcionarios.append(enfermeiro)
        # print(f"""\n ******ENFERMEIRO CADASTRADO COM SUCESSO***** \n
        #         Enfermeiro: {self.nome} \n
        #         Cargo: {self.cargo} \n
        #         COREN: {self.coren}""")

pac = Paciente('Caroline','26')
med = Medico('José', 'Médico','Oftalmologista', 12345)
ate = Atendente('Fernando','Atendente')
enf = Enfermeiro('Julia', 'Enfermeira', 54321)

ate.agendarConsulta('06/03/2024','Caroline','José')
