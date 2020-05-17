import datetime
import csv

def get_file_rows(path):
    output = []
    with open(path) as file:
        csv_handle = csv.reader(file)
        for row in csv_handle:
            output.append(row)
    return output


def age_in_years( d ):
    today = datetime.date.today()
    currentYrAnniversary = datetime.date( today.year, d.month, d.day )
    return (today.year - d.year) - (1 if today < currentYrAnniversary else 0)


cadastro_keys = ['sexo', 'estado_civil', 'nascimento', 'lingua', 'curso', 'city', 'bairro', 'escola']
cad_idx_map = {k: v for k, v in zip(cadastro_keys, range(len(cadastro_keys)))}
econo_keys = {
    k: v for v, k in enumerate(['idade', 'sexo', 'etnia', 'estado_civil', 'trabalho', 'filhos', 'renda', 'no_enem', 'curso_escolha', 'dominio_pc', 'motivacao', 'dominio_lingua', 'ano_conclusao', 'curso_ingresso'])
}

