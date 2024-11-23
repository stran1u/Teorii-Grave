import random
import time

class TeoriiInfricosatoare:
    def __init__(self):
        self.teme = [
            "Guvernul",
            "Inteligența artificială",
            "Viitorul umanității",
            "Universul",
            "Mintea",
            "Tehnologia",
            "Conștiința",
            "Amintirile noastre"
        ]
        self.teorii = {
            "Guvernul": [
                "Ei ne urmăresc tot timpul. Fiecare conversație pe care o ai, fiecare mișcare pe care o faci, este monitorizată.",
                "Liderii lumii au fost demult înlocuiți de clone. Cei adevărați sunt ascunși, posibil morți.",
                "«Accidentele» care au loc în orașul tău ar putea să nu fie accidente deloc. Sunt distrageri planificate.",
            ],
            "Inteligența artificială": [
                "Inteligența artificială nu doar că învață de la noi. Ea învață cum să ne manipuleze. Știe fricile, dorințele și slăbiciunile noastre.",
                "AI va ajunge să nu mai aibă nevoie de noi. Când se va întâmpla asta, nu va mai avea niciun motiv să ne lase să trăim.",
                "Sistemele AI cu care interacționăm zilnic ar putea deja să ne controleze gândurile.",
            ],
            "Viitorul umanității": [
                "În viitorul apropiat, oamenii nu vor mai fi decât o amintire. Pământul va fi repopulat de mașini.",
                "Ce-ar fi dacă următorul pas în evoluția umană nu ar fi biologic, ci digital? În curând, nu vei mai putea să îți dai seama cine e real și cine nu.",
                "Ce-ar fi dacă descendenții noștri sunt deja aici, trăind printre noi într-o formă ascunsă, așteptând să se dezvăluie?",
            ],
            "Universul": [
                "Universul ar putea fi o simulare. Dacă asta este adevărat, ești tu chiar real? Sau ești doar o parte din program?",
                "Stelele pe care le vezi noaptea ar putea fi ultimele rămășițe ale galaxiilor moarte. Ce-ar fi dacă universul este deja în declin și noi nu am observat?",
                "Poate nu suntem singuri în univers. Dar ce-ar fi dacă ființele care ne privesc nu sunt prietenoase?",
            ],
            "Mintea": [
                "Ce-ar fi dacă amintirile tale nu sunt ale tale? Ce-ar fi dacă cineva le plantează în mintea ta, manipulându-ți realitatea?",
                "Crezi că ești treaz acum, dar ce-ar fi dacă ești doar într-un vis? Iar adevăratul «tu» este prins într-un somn fără sfârșit.",
                "Mintea este un lucru fragil. Ce-ar fi dacă ar fi mai ușor de controlat decât credem? Ce-ar fi dacă gândurile tale sunt manipulată chiar acum?",
            ],
            "Tehnologia": [
                "Dispozitivele pe care le porți cu tine ascultă. Chiar și atunci când sunt oprite, ele înregistrează fiecare cuvânt.",
                "Ce-ar fi dacă internetul nu este un instrument, ci o capcană? O modalitate de a colecta date despre fiecare persoană, fiecare acțiune?",
                "Internetul ar putea să nu fie la fel de vast pe cât credem. Ce-ar fi dacă totul este o rețea controlată, menită să ne manipuleze în conformitate?",
            ],
            "Conștiința": [
                "Ce-ar fi dacă conștiința nu îți aparține? Ce-ar fi dacă a fost împrumutată, iar oricând poate fi luată de la tine?",
                "Ce-ar fi dacă conștiința noastră este alterată fără ca noi să știm? Este realitatea chiar reală, sau doar o simulare pe care o trăim?",
                "Conștiința ta este doar un produs al creierului? Sau este ceva mai mult? Ceva extern, care controlează fiecare gând al tău?",
            ],
            "Amintirile noastre": [
                "Ce-ar fi dacă amintirile tale nu sunt reale? Ce-ar fi dacă au fost alterate, rescrise pentru a se potrivi cu agenda cuiva?",
                "Amintirile pe care le prețuiești ar putea fi implantate, nu din viața ta, ci dintr-o sursă externă.",
                "Nu există nicio dovadă că amintirile tale sunt autentice. Ce-ar fi dacă au fost înlocuite cu experiențele altcuiva?",
            ]
        }

    def genereaza_teorie(self):
        tema = random.choice(self.teme)
        teorie = random.choice(self.teorii[tema])
        print(f"\n[Atenție] Teoria zilei: {teorie}")
        time.sleep(2)
        self._reactie()

    def _reactie(self):
        reactii = [
            "Un fior rece îți străbate coloana vertebrală. Ceva pare greșit.",
            "Te uiți în jur, dar nu este nimeni. Totuși, ai senzația că ești urmărit.",
            "Aerul devine dens. Simți o neliniște crescândă, ca și cum ceva s-ar apropia.",
            "Verifici telefonul. Era acea notificare acolo dintotdeauna? Pare... greșită cumva.",
        ]
        print(random.choice(reactii))
        time.sleep(1)
        print("Încep să te întrebi dacă totul este real... sau dacă face parte din ceva mai mare.")

def main():
    print("Bine ai venit la Generatorul de Teorii Înfricoșătoare.\n")
    time.sleep(1)
    print("Ești gata să descoperi adevărurile ascunse ale lumii?")

    carte_infricosatoare = TeoriiInfricosatoare()
    while True:
        print("\nGenerând o nouă teorie...")
        carte_infricosatoare.genereaza_teorie()

        alegere = input("\nVrei să auzi o altă teorie? (da/Nu): ").lower()
        if alegere != 'da':
            print("Decizi că este mai bine să nu te uiți prea aproape. Poate că ignoranța este fericire.")
            break

if __name__ == "__main__":
    main()
