import pyodbc
from flask import Flask, request, redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import session
from flask import url_for
app = Flask(__name__)
@app.route('/')
def insert_data():
    return """
    <html>
    <head>
    <style>
    body {
        background-color: grey;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .class1 {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin-bottom: 20vh;
        margin-left: 15vw;
        margin-right: -10vw;
        margin-top: -5vh;
    }
    .class2 {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin-right: 20vw;
    }
    </style>
    </head>
    <body>
    <div class="class1">
    <h1>Afla ce BMI ai</h1>
    </div>
    <div class="class2">
        <form action="/insert_confirm" method="POST">
            <label for="nume">Nume:</label>
            <input type="text" id="nume" name="nume" required><br><br>
            
            <label for="prenume">Prenume:</label>
            <input type="text" id="prenume" name="prenume" required><br><br>
        
            <label for="greutate">Greutate:</label>
            <input type="text" id="greutate" name="greutate" required><br><br>
            
            <label for="inaltime">Inaltime:</label>
            <input type="text" id="inaltime" name="inaltime" required><br><br>
            
            <input type="submit" value="Continuati">
        </form>
    </div>
    </body>
    </html>
    """
@app.route('/insert_confirm', methods=['POST', 'GET'])
def insert_confirm():
    nume = request.form.get('nume')
    prenume = request.form.get('prenume')
    greutate = int(request.form.get("greutate"))
    inaltime = int(request.form.get("inaltime"))
    inaltime = inaltime/100
    rezultat = greutate/(inaltime*inaltime)
    rezultat = round(rezultat, 2)
    rezultat1=18.5*inaltime*inaltime
    rezultat2=25*inaltime*inaltime
    session["nume"]=nume
    session["prenume"]=prenume
    if rezultat < 18.5:
        session["rezultatf"]=rezultat1-greutate
        return """
    <html>
    <head>
    <style>
    body {
        background-color: lightblue;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .class3 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>
    <div class="class3">
    <pre style="font-size: 2vh;">
                            <b style="font-size:4vh;">Subponderal</b>
                <b style="font-size:3vh;">Indicele de masa corporala este: """ + str(rezultat) + """</b>
                

        Adaugă calorii sănătoase. Nu este nevoie să îți schimbi radical dieta. Poți crește 
    aportulcaloric adăugând topping-uri cu nuci sau semințe, brânză și garnituri sănătoase. 
    Încearcă migdale, semințe de floarea-soarelui, fructe sau pâine integrală din grâu.

        Optează pentru densitate nutritivă. În loc să consumi calorii goale și alimente nesănătoase,
    alege alimente bogate în nutrienți. Ia în considerare carnea cu conținut ridicat de proteine, 
    care te poate ajuta să construiești mușchi. De asemenea, alege carbohidrați nutriționali, cum ar fi 
    orezul brun și alte cereale integrale. Acest lucru ajută la asigurarea că organismul tău primește cât 
    mai multe substanțe hrănitoare posibil, chiar dacă te confrunți cu o poftă redusă de mâncare.

        Fă gustări. Bucură-te de gustări care conțin o mulțime de proteine și carbohidrați sănătoși.
    Ia în considerare opțiuni precum mixuri de fructe și nuci, batoane sau băuturi proteice și biscuiți 
    cu humus sau unt de arahide. De asemenea, savurează gustări care conțin "grăsimi bune", care sunt 
    importante pentru un inimă sănătoasă. Exemple includ nuci și avocado.

        Mănâncă mese mici. Dacă te confrunți cu o poftă slabă de mâncare, din cauza problemelor medicale sau 
    emoționale, consumul de cantități mari de alimente poate să nu pară atractiv. Ia în considerare consumul
    de mese mai mici pe parcursul zilei pentru a-ți crește aportul caloric.

        Crește masa musculară. În timp ce prea mult exercițiu aerob va arde calorii și va lucra împotriva obiectivului
    tău de greutate, antrenamentul de forță te poate ajuta. Acesta include ridicarea de greutăți sau practicarea yoga.
    Câștigi în greutate prin construirea masei musculare.
    </pre>
    <form action="/schimbare" method="GET,">
    <input type="submit" value="Doresc o schimbare!">
    </form>
    </div>
    </body>
    </html>
    
        """
    if rezultat >= 18.5 and rezultat < 25:
        return"""
    <html>
    <head>
    <style>
    body {
        background-color: green;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>
    <div class="class2">
    <h2>Normal, indicele de masa corporala este: """ +str(rezultat)+""" Nu trebuie sa faci schimbari la stilul tau de viata!</h2>
    </div>
    </body>
    </html>

    """
    if rezultat >= 25 and rezultat < 30:
        session["rezultatf"]=rezultat2-greutate
        return """
    <html>
    <head>
    <style>
    body {
        background-color: yellow;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .class3 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>
    <div class="class3">
    <pre style="font-size:2vh;">
                            <b style="font-size:4vh;">Supraponderal</b>
                <b style="font-size:3vh;">Indicele de masa corporala este: """ + str(rezultat) + """</b>
                
                
        Înainte de a începe orice program de pierdere în greutate, este recomandat să consulți
    un specialist în nutriție sau medic. Aceștia te pot ghida în funcție de nevoile și condițiile tale individuale
        Setează obiective realiste și atingibile. Pierderea în greutate în mod gradual
    și constant este mai sustenabilă și mai sănătoasă pe termen lung.
        Mănâncă o varietate de alimente sănătoase, inclusiv fructe, legume, proteine slabe, 
    cereale integrale și lactate cu conținut scăzut de grăsimi. Redu consumul de alimente procesate,
    zaharuri adăugate și grăsimi saturate.
        Monitorizează dimensiunea porțiilor și încearcă să mănânci porții mai mici și echilibrate.
    Acest lucru poate contribui la reducerea aportului caloric.
        Asigură-te că bei suficientă apă. Uneori, senzația de sete poate fi confundată cu foamea.
        Include exerciții fizice în rutina ta zilnică. Combinați activități aerobice cu exerciții 
    de forță pentru a obține beneficii maxime.
        Redu consumul de grăsimi saturate și trans. Optează pentru surse sănătoase de grăsimi, cum 
    ar fi cele găsite în avocado, nuci și ulei de măsline.
        Redu consumul de zaharuri adăugate și alimente bogate în calorii goale. Alege surse naturale
    de dulce, cum ar fi fructele.
        Menține un jurnal alimentar și monitorizează progresul tău. Acest lucru îți va oferi o perspectivă
    asupra obiceiurilor tale alimentare și te poate ajuta să faci ajustări în consecință.
        Dormi între 7-9 ore pe noapte. Lipsa somnului poate afecta pofta de mâncare și poate 
    contribui la luarea în greutate.
        Alege activități fizice care îți plac și pe care le poți menține pe termen lung. 
    Astfel, exercițiile vor deveni o parte naturală a vieții tale.
        În procesul de pierdere în greutate, este esențial să fii răbdător și să te concentrezi
    pe adoptarea unui stil de viață sănătos, în loc de diete restrictive sau schimbări bruște.
    Consultarea cu profesioniști în domeniul sănătății poate fi de mare ajutor în stabilirea unui
    plan personalizat și sustenabil.
    </pre>
    <form action="/schimbare" method="GET">
    <input type="submit" value="Doresc o schimbare!">
    </form>
    </div>
    </body>
    </html>
    
    """
    
        
    elif rezultat >= 30 and rezultat < 35:
        session["rezultatf"]=rezultat2-greutate
        return """
    <html>
    <head>
    <style>
    body {
        background-color:rgb(255, 127, 80);
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .class3 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>

    <div class="class3">
    <pre style="font-size: 2vh;">
                            <b style="font-size:4vh;">Obezitate gradul I</b>
                <b style="font-size:3vh;">Indicele de masa corporala este: """ + str(rezultat) + """</b>
                
                
        Începe prin a consulta un medic sau un specialist în nutriție. Aceștia vor 
    putea să îțievalueze starea de sănătate și să ofere recomandări personalizate.

        Setează obiective realiste și pe termen lung pentru pierderea în greutate. Pierderea a 
    5-10 la suta din greutatea corporală totală poate aduce beneficii semnificative pentru sănătate.

        Adoptă o dietă echilibrată și sănătoasă. Mănâncă porții mai mici și evită alimentele 
    procesateși bogate în calorii goale. Planifică-ți mesele și gustările în avans pentru a 
    evita mâncatul impulsiv. Consumă mese mai mici și mai frecvente pentru a controla foamea.

        Asigură-te că bei suficientă apă. Uneori, senzația de sete poate fi confundată cu cea de foame.

        Introduce treptat exerciții fizice moderate și regulate în rutina ta. Consultă medicul înainte de
    a începe un program intens de exerciții, mai ales dacă există probleme de sănătate preexistente.

        Menține un jurnal alimentar și de exerciții pentru a urmări progresul. Aceasta poate oferi o
    perspectivă asupra obiceiurilor tale alimentare și de activitate. Înțelege impactul emoțional al 
    pierderii în greutate și consideră să te adresezi unui specialist în sănătate mentală sau să 
    participi la grupuri de susținere.

        Învață mai multe despre nutriție și alimente sănătoase. Înțelegerea corectă a alimentelor te
    poate ajuta să faci alegeri mai bune.

        Adoptă tehnici de gestionare a stresului, cum ar fi meditația, yoga sau plimbările relaxante.
    Stresul poate influența obiceiurile alimentare și nivelul de activitate.Efectuează controale medicale
    regulate pentru a monitoriza sănătatea ta globală pe parcursul procesului de pierdere în greutate.
    Este important să abordezi procesul de pierdere în greutate cu grijă și să te bazezi pe sprijinul 
    profesional pentru a asigura o abordare sigură și sustenabilă. O echipă multidisciplinară,
    inclusiv medicul, nutriționistul și eventual un psiholog, poate oferi o abordare holistică pentru 
    atingerea obiectivelor tale.
    </pre>
    <form action="/schimbare" method="GET">
    <input type="submit" value="Doresc o schimbare!">
    </form>
    </div>
    </body>
    </html>
    
    """
    elif rezultat >= 35 and rezultat < 40:
        session["rezultatf"]=rezultat2-greutate
        return """
    <html>
    <head>
    <style>
    body {
        background-color: rgb(236, 88, 0);
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .class3 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>
    <div class="class3">
    <pre style="font-size: 2vh;">
                            <b style="font-size:4vh;">Obezitate gradul II</b>
                <b style="font-size:3vh;">Indicele de masa corporala este: """ + str(rezultat) + """</b>
                
                
        Consultă un medic, un nutriționist și, posibil, un specialist în sănătate mentală. Ei vor 
    putea oferi o evaluare detaliată și un plan personalizat pentru pierderea în greutate.

        Setează obiective realiste și sigure. Pierderea în greutate treptată și constantă este mai sănătoasă
    și mai sustenabilă pe termen lung.

        Realizează controale medicale regulate pentru a monitoriza evoluția ta și a adapta planul de pierdere
    în greutate în funcție de nevoile tale.

        Lucrează împreună cu un nutriționist pentru a stabili un regim alimentar echilibrat și controlat caloric.
    Redu consumul de alimente bogate în calorii, grăsimi și zaharuri.

        Monitorizează dimensiunea porțiilor și alege alimente bogate în nutrienți pentru a asigura organismului 
    substanțele esențiale.

        Introduce exerciții fizice sub supraveghere. Consultă un specialist în fitness pentru a crea un program
    adaptat condițiilor tale fizice și de sănătate. Planifică activități fizice pe termen lung, astfel încât
    acestea să devină o parte integrată a vieții tale cotidiene. Combinați activitățile aerobice cu cele de rezistență.

        Lucrează cu un specialist pentru a identifica și aborda comportamentele alimentare nesănătoase sau emoționale
    care pot contribui la luarea în greutate. Angajează-te în consiliere sau terapie psihologică pentru a aborda aspectele
    psihologice ale obezității. Acest aspect este adesea crucial în procesul de pierdere în greutate.
        
        Învață mai multe despre nutriție, sănătate și fitness pentru a lua decizii informate și a menține progresul
    pe termen lung. Fii conștient de necesitatea unei abordări pe termen lung. Învață să te bucuri de schimbările mici
    și să fii răbdător cu procesul. Pierderea în greutate în cazul obezității de gradul II necesită un angajament
    semnificativ și o abordare echilibrată, iar sprijinul profesional este esențial. Un plan personalizat
    și sustenabil te va ajuta să atingi și să menții un BMI normal într-un mod sănătos și eficient.
    </pre>
    <form action="/schimbare" method="GET">
    <input type="submit" value="Doresc o schimbare!">
    </form>
    </div>
    </body>
    </html>
    
    """
    elif rezultat >= 40 and rezultat < 70:
        session["rezultatf"]=rezultat2-greutate
        return """
    <html>
    <head>
    <style>
    body {
        background-color: red;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .class3 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>
    <div class="class3">
    <pre style="font-size: 2vh;">
                            <b style="font-size:4vh;">Obezitate morbida</b>
                <b style="font-size:3vh;">Indicele de masa corporala este: """ + str(rezultat) + """</b>
                
                
        Caută îndrumare medicală de la un echipaj de specialiști, inclusiv medici, nutriționiști,
    psihiatri și specialiști în activitate fizică. Un plan personalizat este esențial.

        Realizează evaluări medicale periodice pentru a monitoriza evoluția sănătății tale și
    pentru a ajusta planul de pierdere în greutate în consecință. Adresează-te și gestionează 
    orice afecțiuni medicale asociate obezității, cum ar fi diabetul, hipertensiunea arterială
    sau problemele cardiace.

        Consultă un chirurg bariatric dacă intervenția chirurgicală este o opțiune viabilă
    și recomandată în cazul tău.

        Lucrează cu o echipă multidisciplinară care să ofere asistență în aspecte medicale,
    nutriționale, psihologice și de activitate fizică.Lucrând împreună cu un nutriționist, 
    creează un plan alimentar echilibrat și controlat caloric, care să fie adaptat nevoilor 
    tale specifice și care să promoveze pierderea în greutate într-un mod sănătos.

        Introduce exerciții fizice sub supraveghere. Activități cum ar fi înotul sau ciclismul 
    pot fi mai ușoare pentru articulații și pot fi adaptate la condițiile individuale.

        Consultă un specialist în sănătate mentală pentru a aborda aspectele psihologice ale 
    obezității morbide. Psihoterapia poate fi utilă pentru gestionarea stresului, a anxietății 
    și a altor probleme legate de alimentație. Participă la grupuri de suport pentru a împărtăși 
    experiențele cu alții care trec prin aceeași provocare și pentru a primi sprijin și înțelegere.

        Continuă să te educi despre nutriție, sănătate și moduri de a menține o greutate sănătoasă
    pe termen lung.Fii pregătit pentru o călătorie îndelungată și angajează-te într-o abordare sustenabilă. 
    Răbdarea și perseverența sunt chei în această situație.Reține că pierderea în greutate în cazul 
    obezității morbide poate fi o provocare, dar cu sprijinul corect și o abordare multidisciplinară, 
    poți face pași semnificativi spre îmbunătățirea sănătății tale. Este esențial să lucrezi cu profesioniști 
    și să îți personalizezi abordarea în funcție de nevoile tale individuale.
    </pre>
    <form action="/schimbare" method="GET">
    <input type="submit" value="Doresc o schimbare!">
    </form>
    </div>
    </body>
    </html>
    
    """
    elif rezultat >= 70:
        
        return """
    <html>
    <head>
    <style>
    body {
        background-color: red;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>
    <div class="tenor-gif-embed" data-postid="5325429658232930898" data-share-method="host" data-aspect-ratio="1.77778" data-width="100%"><a href="https://tenor.com/view/falling-from-a-coffin-i-think-you-should-leave-with-tim-robinson-broken-coffin-naked-corpse-broken-casket-gif-5325429658232930898">Falling From A Coffin I Think You Should Leave With Tim Robinson GIF</a>from <a href="https://tenor.com/search/falling+from+a+coffin-gifs">Falling From A Coffin GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
    </body>
    </html>
    
    """


@app.route('/schimbare', methods=['POST','GET'])
def schimbare():
    return """
    <html>
    <head>
    <style>
    body {
        background-color: grey;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .class1 {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin-bottom: 20%;
        margin-left: 15%;
        margin-right: -17%;
        margin-top: -10%;
        
    }
    .class2 {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin-right: 20%;
    }
    </style>
    </head>
    <body>
    <div class="class1">
    <h1>Schimbarea ta incepe aici!</h1>
    </div>
    <div class="class2">
        <form action="/schimbare_confirm" method="POST">
            <label for="apa">Cati L de apa bei zilnic?</label><br>
            <input type="text" id="apa" name="apa" required><br><br>
            
            <label for="somn">Cate ore dormi pe noapte?</label><br>
            <input type="text" id="somn" name="somn" required><br><br>
            
            <label for="mese">Cate mese mananci pe zi?</label><br>
            <input type="text" id="mese" name="mese" required><br><br>
            
            <label for="gustari">Cate gustari mananci pe zi?</label><br>
            <input type="text" id="gustari" name="gustari" required><br><br>
            
            <label for="sport">Cate minute de sport faci pe zi?</label><br>
            <input type="text" id="sport" name="sport" required><br><br>
            
            <label for="email">Introdu adresa de email:</label><br>
            <input type="text" id="email" name="email" required><br><br>
            <input type="submit" value="Continuati">
        </form>
    </div>
    </body>
    </html>
    """
@app.route('/schimbare_confirm', methods=['POST'])
def schimbare_confirm():
    if "nume" in session:
        nume=session["nume"]
        prenume=session["prenume"]
    
    apa = int(request.form.get("apa"))
    somn = int(request.form.get("somn"))
    mese = int(request.form.get("mese"))
    gustari = int(request.form.get("gustari"))
    sport=int(request.form.get("sport"))
    apa1=4-apa
    somn1=8-somn
    mese1=3-mese
    gustari1=3-gustari
    sport1=45-sport
    if "rezultatf" in session:
        rezultatf=session["rezultatf"]
        if rezultatf<0:
            rezultatf=0-rezultatf
            rezultatf=round(rezultatf,2)
            textt6="Ai nevoie sa slabesti cu "+str(rezultatf)+" kg pentru a ajunge la o greutate normala pentru inaltimea ta"
        else:
            rezultatf=round(rezultatf,2)
            textt6="Ai nevoie sa te ingrasi cu "+str(rezultatf)+" kg pentru a ajunge la o greutate normala pentru inaltimea ta"
    textt="In urma analizei tale am ajuns la concluzia ca ar trebui sa faci urmatoarele schimbari:"
    if apa1<0:
        apa1=0-apa1
        textt1="Ai baut prea multa apa, ar trebui sa bei cu "+str(apa1)+" L mai putin"
    elif apa1>0:
        textt1="Ai baut prea putina apa, ar trebui sa bei cu "+str(apa1)+" L mai mult"
    else:
        textt1="Ai baut cantitatea recomandata de apa"
    if somn1<0:
        somn1=0-somn1
        textt2="Ai dormit prea mult, ar trebui sa dormi cu "+str(somn1)+" ore mai putin"
    elif somn1>0:
        textt2="Ai dormit prea putin, ar trebui sa dormi cu "+str(somn1)+" ore mai mult"
    else:
        textt2="Ai dormit numarul recomandat de ore"
    if mese1<0:
        mese1=0-mese1
        textt3="Ai mancat prea mult, ar trebui sa mananci cu "+str(mese1)+" mese mai putin"
    elif mese1>0:
        textt3="Ai mancat prea putin, ar trebui sa mananci cu "+str(mese1)+" mese mai mult"
    else:
        textt3="Ai mancat numarul recomandat de mese"
    if gustari1<0:
        gustari1=0-gustari1
        textt4="Ai mancat prea multe gustari, ar trebui sa mananci cu "+str(gustari1)+" gustari mai putin"
    elif gustari1>0:
        textt4="Ai mancat prea putine gustari, ar trebui sa mananci cu "+str(gustari1)+" gustari mai mult"
    else:
        textt4="Ai mancat numarul recomandat de gustari"
    if sport1>0:
        textt5="Ai facut prea putin sport, ar trebui sa faci cu "+str(sport1)+" minute mai mult"
    else:
        textt5="Ai facut numarul recomandat de minute de sport"
    
    
    myEmail='resultbmi@gmail.com'
    smtp_server='smtp.gmail.com'
    smtp_port=587
    msg = MIMEMultipart('alternative')
    msg['Subject']='Rezultatul Tau BMI'
    msg['From']=myEmail
    email = request.form.get('email')
    msg['to'] = email
    text="Buna {nume} {prenume}, \n\n {textt}\n\n {textt6}\n\n {textt1}\n\n {textt2}\n\n {textt3}\n\n {textt4}\n\n {textt5}\n\nMultumim ca ai ales echipa BMI!".format(textt=textt,textt1=textt1,textt2=textt2,textt3=textt3,textt4=textt4,textt5=textt5,nume=nume,prenume=prenume,textt6=textt6)
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    
    server=smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(myEmail,'ijet qzyq nkxh bxhb')

    server.send_message(msg)
    server.quit()
    return """
    <html>
    <head>
    <style>
    body {
        background-color: lightblue;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    </head>
    <body>
    <div class="class1">
    <h1>SA INCEAPA SCHIMBAREA!</h1>
    </div>
    <div class="class2">
    <h2>Am trimis un email la adresa: """ + str(email) + """,SUCCES!</h2>
    </div>
    </body>
    </html>

    """
    
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
