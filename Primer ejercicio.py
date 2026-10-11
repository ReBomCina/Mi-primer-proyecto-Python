print("Bienvenido a la calculadora de Propinas") 
print("-" * 40) 

cuenta = float(input("¿De cuanto fue el total de la cuenta?:"))
porcentaje_propina = int(input("¿Que porcentaje de propina quieres dejar?:"))
personas = int(input("¿Entre cuantas personas se va a dividir la cuenta?:"))

dinero_propina = cuenta * (porcentaje_propina / 100)

cuenta_total = cuenta + dinero_propina

pago_por_persona = cuenta_total / personas

print("-" * 40)
print(f"Cada persona debe pagar un total de $¨{pago_por_persona}")
