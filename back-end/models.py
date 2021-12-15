from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    cpf = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.email + ", " + self.cpf
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf
        }

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    ementa = db.Column(db.String(254))
    ch = db.Column(db.String(254))


    # método para expressar os carros em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.ementa + ", " + self.ch
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "ementa": self.ementa,
            "ch": self.ch
        }

class EstudanteDisciplina(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    semestre = db.Column(db.String(254))
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable = False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable = False)
    mediaFinal = db.Column(db.String(254))
    frequencia = db.Column(db.String(254))

    pessoa = db.relationship("Pessoa")
    disciplina = db.relationship("Disciplina")

    # método para expressar os carros em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.semestre + ", " + self.pessoa + ", " + self.disciplina + ", " + self.mediaFinal + ", " + self.frequencia
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "semestre": self.semestre,
            "pessoa_id": self.pessoa_id,
            "disciplina_id": self.disciplina_id,
            "mediaFinal": self.mediaFinal,
            "frequencia": self.frequencia,
            "pessoa": self.pessoa.json(),
            "disciplina": self.disciplina.json()
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    p1 = Pessoa(nome = "Rodrigo", email = "rodrigo@gmail.com", cpf = "1234567890")
    p2 = Pessoa(nome = "Hylson", email = "hylson@gmail.com", cpf = "0987654321")

    d1 = Disciplina(nome = "Matematica", ementa = "equações de 1° grau", ch = "40")
    d2 = Disciplina(nome = "Portugues", ementa = "Verbos no infinitivo", ch = "70")

    db.session.add(d1)
    db.session.add(d2)
    db.session.add(p1) 
    db.session.add(p2)   
       
    db.session.commit()

