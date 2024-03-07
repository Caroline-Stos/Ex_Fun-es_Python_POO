class Paciente:
    pacientes = []

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []
        paciente = (nome, idade)
        Paciente.pacientes.append(paciente)
        print(f"""\n ******PACIENTE CADASTRADO COM SUCESSO***** \n
                Nome: {self.nome} \n
                Idade: {self.idade} \n
                """)

    def visualizarConsulta(self):
        print("""Data da consulta: {data} \n
                Paciente: {paciente} \n
                Médico responsável: {medico} \n
                Regitrado por: {responsavel}
            """)

class Funcionario:
    funcionarios = []

    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
    def agendarConsulta(self, data, paciente, medico):
        data = data
        paciente = paciente
        medico = medico
        responsavel = self.nome

        consulta = (data, paciente, medico, responsavel)
        # print(consulta)
        # for paciente in Paciente.pacientes:
        #     if paciente == self.nome:
        #         self.historico.append(consulta)
        #         paciente.visualizarConsulta()*********************

class Atendente(Funcionario):
    def __init__(self, nome, cargo):
        super().__init__(nome, cargo)
        print(f"""\n ******ATENDENTE CADASTRADO COM SUCESSO***** \n
                Atendente: {self.nome} \n
                Cargo: {self.cargo} \n
                """)
  
class Medico(Funcionario):
    def __init__(self, nome, cargo, especialidade, crm):
        super().__init__(nome, cargo)
        self.nome = nome
        self.cargo = cargo
        self.especialidade = especialidade
        self.crm = crm
        medico = (nome, cargo, especialidade, crm)
        Funcionario.funcionarios.append(medico)
        print(f"""\n ******MÉDICO CADASTRADO COM SUCESSO***** \n
                Médico: {self.nome} \n
                Cargo: {self.cargo} \n
                Especialidade: {self.especialidade} \n
                CRM: {self.crm}""")
        
class Enfermeiro(Funcionario):
    def __init__(self, nome, cargo, coren):
        super().__init__(nome, cargo)
        self.nome = nome
        self.cargo = cargo
        self.coren = coren
        enfermeiro = (nome, cargo, coren)
        Funcionario.funcionarios.append(enfermeiro)
        print(f"""\n ******ENFERMEIRO CADASTRADO COM SUCESSO***** \n
                Enfermeiro: {self.nome} \n
                Cargo: {self.cargo} \n
                COREN: {self.coren}""")

paciente = Paciente('Caroline','26')
medico_1 = Medico('José', 'Médico','Oftalmologista', 12345)
atd = Atendente('Fernando','Atendente')
enf = Enfermeiro('Julia', 'Enfermeira', 54321)

atd.agendarConsulta('06/03/2024', 'Caroline','José')
