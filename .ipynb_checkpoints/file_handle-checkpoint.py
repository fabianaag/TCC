import datetime
import csv

def get_file_rows(path):
    with open(path) as file:
        csv_handle = csv.reader(file)
        for row in csv_handle:
            yield row

cadastro_keys = ['nome', 'estado_civil', 'nascimento', 'lingua', 'opt_curso', 'city', 'bairro', 'escola']
cadastro = {k: v for k, v in zip(cadastro_keys, range(len(cadastro_keys)))}


def ageInYears( d ):
    today = datetime.date.today()
    currentYrAnniversary = datetime.date( today.year, d.month, d.day )
    return (today.year - d.year) - (1 if today < currentYrAnniversary else 0)



if __name__ == "__main__":
    main()