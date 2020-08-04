# Követelmények

**Aláírás feltétele**: összes házifeladat határidőre történő helyes leadása, valamint a ZH-k elégséges szinten történő teljesítése

**Vizsgajegy**: ZH eredmények, és otthon elkészített beadandó feladat alapján, amit vizsgán meg kell védeni

## Házifeladatok

Heti, kétheti rendszerességgel feladott, határidős feladatok GitHub Classroom felületen. A megoldásokat otthon kell elkészíteni, melyen automatikus tesztek futnak le. Hiba esetén többször is le lehet adni egészen addig, amíg a határidő le nem jár.
**Házifeladat pótlására nincs lehetőség**

## ZH-k

Két ZH a félév során, ahol helyben kell időlimitet betartva bizonyosságot tenni a megszerzett tudásról.

Az első zh nagyjából a hatodik hét környékén lesz, papíros, algoritmizálási készségeket tesztel pszeudo kód / blockdiagramm szinten. 

A második zh a félév végén lesz, konkrét programozási feladatokat kell gépteremben python nyelven megoldani, és a megoldást feltölteni. GitHub Classroom itt is használva lesz, de a sikeres check-eket követően az oktató még további kifogásokkal élhet. 

## Vizsga

A hallgató feladata, hogy az aláírás sikeres megszerzése esetén egy saját témából beadandót készítsen. 
A témát a hallgató egyezteti az oktatóval, aki ezután létrehoz e célra egy GitHub repository-t, ahol a hallgatónak dolgoznia kell. 

A beadandóval kapcsolatos elvárások:
 - Használni kell az összes, félév során tanult technikát (vezérlési szerkezetek, függvények, összetett adatszerkezetek)
 - Az elkészült kód legyen moduláris, logikailag indokolt részekre szétszedve. 
 - Minden elkészített függvénynek legyen egy tömör, rövid fejlesztői dokumentációja angol nyelven.
 - Készüljön a forrás mellé tesztadat, minta, mellyel a program működése demózható.
 - Készüljön egy angol vagy magyar nyelvű felhasználóid dokumentáció md formátumban.
 
Vizsgán a hallgató bemutatja, megvédi a munkáját, melyet a vizsgáztató tesztel, kérdéseket tesz fel vele kapcsolatban. Szükség esetén a vizsgáztató kisebb módosításokat kér a vizsgázótól a vizsga során.

A vizsgáztató által javasolt jegyen a hallgató ha javítani szeretne, a vizsgáztató plusz feladatokat, módosítási kéréseket jelöl meg, melyeket issue-k formájában rögzít is.

A hallgató egy következő vizsgán ezen kéréseknek eleget tevő változtatásokkal újra megvédheti a beadandóját.

Mintaképpen egy beadandó feladat elérhető lesz ebben a repository-ban.

# Heti beosztás

<table style="width:100%">
  <tr>
    <th>Hét</th>
    <th>Előadás</th>
    <th>Gyakorlat</th>
   <th>Megjegyzés</th>
  </tr>
  <tr>
    <th>1</th>
    <td>
     Követelmények ismertetése, alapvető, programozással kapcsolatos fogalmak tisztázása (szoftverfejlesztés, tesztelés, algoritmizálás, programozási nyelvek, forráskód, gépi kód, köztes kód, fordító, interpreter, IDE, syntax highlight, stb.), valamint korábbi tapasztalatok felmérése.
    </td>
    <td>
     Fejlesztői környezet telepítése (vscode), alapvető szövegszerkesztési technikák, shortcutok megismerése. GitHub regisztráció, első repository létrehozása, `README.md` szerkesztése, GitHub alapvető használatának elsajátítása (1 branch, 1 user), fontosabb felületek megismerése (code / commits). vscode és GitHub összekötése 
    </td>
    <td>
     Amennyiben az előadáson marad idő, néhány dologban tehermentesíti a gyakorlatot.
    </td>
  </tr>
  <tr>
    <th>2</th>
    <td>Elágazás és egyszerű ciklus mint vezérlési adatszerkezet megismerése, szöveges algoritmizálás, pszeudo kód megismerése absztrakt magas szintű utasításokon keresztül.</td>
    <td>Alapvető vezérlési szerkezetek gyakorlása életszerű példákon, pszeudo kód szinten.</td>
    <td>Csak "Amíg" és "Ha" semmi foreach, else, do-while, stb. Változók nincsenek, az alapvető utasítások magas szintűek, pl: "van fal a bal oldalamon". 
  </tr>
  <tr>
   <th>3</th>
   <td>
    Absztraktabb példák, változó fogalmának bevezetése. Egyerű bekérés, kiiratás és alapvető vezérlési szerkezetek használata továbbtra is pszeudo kód szintjén. 
   </td>
   <td>
    Példákon keresztül gyakorlás. Először oktató által adott kód végrehajtása, majd saját kód tervezése.
   </td>
   <td>
    Csak egész változók. A kód "mélysége" legfeljebb kettő (pl elágazás ciklustörzsben).
   </td>   
  </tr>
  <tr>
   <th>4</th>
   <td>
    Összetettebb feladatok a megadott eszközökkel, alap minták, pl.: minimumkeresés, bekérés adott elemig, stb. 
   </td>
   <td>
    Példákon keresztül gyakorlás. Először oktató által adott kód végrehajtása, majd saját kód tervezése.
   </td>
   <td>
    Csak egész változók. Az előző héthez képest a kódok bonyolultsága emelkedik, a gyakorlat második felében már 3 mélységű kódok is előfordulhatnak. Valamikor GitHub Classroom megmutatása, ez történhet elméleten is.
   </td>   
  </tr>
  <tr>
   <th>5</th>
   <td>
    Python legalapabb nyelvi elemeinek ismertetése, annak használata. Pszeudo kód és python közötti megfeleltetés, különbségek. 
   </td>
   <td>
    Korábbi példák megvalósítása python nyelven.
   </td>
   <td>
    Csak `if` és `while`, `print`, `input`, alapvető operátorok, nincs szó típusokról. 
   </td>   
  </tr>
  <tr>
   <th>6</th>
   <td>
    Listák, alapvető függvnyeik, alap programozási feladatok listákkal, pl: minimumkeresés, Fibonacci sorozat felépítése, buborékrendezés.
   </td>
   <td>
    Listákat igénylő feladatokon keresztüli gyakorlás. 
   </td>
   <td>
    Továbbra is csak `if` és `while`. 
   </td>   
  </tr>
  <tr>
   <th>7</th>
   <td>
    Szép kódot szolgáló nyelvi elemek bevezetése, pl `for ... in`, `break`, stb.
    Logikai és lebegőpontos változók, változó típusok, konvertálás, dinamikus hibák.
   </td>
   <td>
    Néhány korábbi kód átírása, lerövidítése a megismert új eszközökkel, valamint új feladatok.
   </td>
   <td>
    Valamikor érdemes megmutatni parancssori argumentumok használatát a tesztelés megkönnyítésének érdekében.
   </td>   
  </tr>
  <tr>
   <th>8</th>
   <td>
    String típus, nagyon alap szöveges fájlkezelés.
   </td>
   <td>
    Gyakorlás feladatokkal.
   </td>
   <td>
    A cél, hogy ne a kódba égessenek bemeneteket vagy billentyűzetről pötyögjék őket be folyton, hanem legyen egy file, amit beolvasnak, és használnak, újrafuttatáshoz pedig csak azt módosítják.
   </td>   
  </tr>
  <tr>
   <th>9</th>
   <td>
    Függvények. Kód absztrakt megtervezése függvények szintjén egy bonyolultabb feladat példáján. 
   </td>
   <td>
    Fügvények gyakorlása, esetleg korábbi feladatok újrastruktúrálása.
   </td>
   <td>
    Tuple-ökről részletesen nem esik szó, de több visszatérési érték megengedett. Egyelőre olyan feladatok, ahol pass-by-? problémák nem jönnek elő (argumentumok legyenek immutable dolgok).
   </td>   
  </tr>
  <tr>
   <th>10</th>
   <td>
    Paraméterátadás, immutability megértésse, mi történik a memóriában.
   </td>
   <td>
    Olyan példákkal is gyakorlás, ahol listák is átadásra kerülnek, pitfall-ok hibák elkerülése.
   </td>
   <td>
    
   </td>   
  </tr>
  <tr>
   <th>11</th>
   <td>
    Dictionary, tipikus használati esetek. 
   </td>
   <td>
    Gyakorlás olyan példákon, amik dictionary nélkül nagyon körülményesek lennének.
   </td>
   <td>
    
   </td>   
  </tr>
  <tr>
   <th>12</th>
   <td>
    Praktikus python funkciók, listák másolása, JSON formátum és parzolás, hasznos beépített függvények, stb.
   </td>
   <td>
    Gyakorlás.
   </td>
   <td>
    Bizonyos itt ismertetett feature-ök "elcsepegtetve" már korábban előjöhetnek gyakorlaton.
   </td>   
  </tr>
  <tr>
   <th>13</th>
   <td>
    Fák, gráfok, implementálásuk pythonban, egyszerűbb algoritmusok, bejárások. 
   </td>
   <td>
    Gyakorlás.
   </td>
   <td>
    Csak nagyon alap dolgok. 
   </td>   
  </tr>
</table>
