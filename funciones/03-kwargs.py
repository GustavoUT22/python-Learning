# keyword arguments

def get_products(**datos):
    print(datos["id"], datos["name"])


get_products(id="id")  # {'id': 'id'}
get_products(id="id",
             name="iPhone",
             desc="descriocion")
