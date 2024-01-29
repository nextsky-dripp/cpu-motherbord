print("Her kan du lege samen en prosessor og hovedkort for og fine ut om de er kompatibel")
print("Programet fungerer bare med intel eller amd ryzen ")

a = 14 
b = 13 
c = 12
d = 11

intel_amd = 1

while intel_amd:
    valg = int(input("Skriv in talet det står for prosessoren du har:\n 1) Intel\n 2) Amd Ryzen\n 3) info\n 4) Hjelp\n"))
    match valg:
        case 1:
           i_generasjon = input("Hva er generasjon til prosessor en. hvist du ikke vet hvordan gå til bake og gå på hjelp ")

        case 2:
             R_generasjon = input("Hva er generasjon til prosessor en. hvist du ikke vet hvordan gå til bake og gå på hjelp ")
             
        case 3:
            print("")

        case 4:
          hjelp_prosessor = input("Skriv (A) for og fine ut vilken generasjon prosesprem din er. ")   

        case _:
                print("Sorry med det går ikke ")

