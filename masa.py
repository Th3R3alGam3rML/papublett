def kilogramos_a_gramos(kilogramos):
    return kilogramos *1000

def gramos_a_kilogramos(gramos):
    return gramos /1000

if __name__=="__main__":
    kilogramos = 2,5
    gramos = kilogramos_a_gramos
    print(f"{kilogramos} kilogramos son equivalentes a {gramos} gramos")