# Követelmények

**Aláírás feltétele**: összes házifeladat határidőre történő helyes leadása, valamint a ZH-k elégséges szinten történő teljesítése

**Vizsgajegy**: ZH eredmények, és otthon elkészített beadandó feladat alapján, amit vizsgán meg kell védeni

## Házifeladatok

Heti, kétheti rendszerességgel feladott, határidős feladatok GitHub felületen. A megoldásokat otthon kell elkészíteni, melyen automatikus tesztek futnak le. Hiba esetén többször is le lehet adni egészen addig, amíg a határidő le nem jár.
**Házifeladat pótlására nincs lehetőség**

## ZH-k

Két ZH a félév során, ahol helyben kell időlimitet betartva bizonyosságot tenni a megszerzett tudásról.

Az első zh nagyjából a 8. hét környékén lesz, papíros, algoritmizálási készségeket tesztel pszeudo kód / blockdiagramm szinten. 

A második zh a félév végén lesz, konkrét programozási feladatokat kell gépteremben python nyelven megoldani, és a megoldást feltölteni. Automatikus GitHub check itt is használva lesz, de a sikeres check-eket követően az oktató még további kifogásokkal élhet. 

## Vizsga

A hallgató feladata, hogy az aláírás sikeres megszerzése esetén saját témából egy beadandót készítsen. 
A témát a hallgató egyezteti az oktatóval, aki ezután létrehoz e célra egy GitHub repository-t, ahol a hallgatónak dolgoznia kell. 

A beadandóval kapcsolatos elvárások:
 - Használni kell az összes, félév során tanult technikát (vezérlési szerkezetek, függvények, összetett adatszerkezetek)
 - Az elkészült kód legyen moduláris, logikailag indokolt részekre szétszedve. 
 - Minden elkészített függvénynek legyen egy tömör, rövid fejlesztői dokumentációja angol nyelven.
 - Készüljön a forrás mellé tesztadat, minta, mellyel a program működése demózható.
 - Készüljön angol vagy magyar nyelvű felhasználói dokumentáció md formátumban.
 
Vizsgán a hallgató bemutatja, megvédi a munkáját, melyet a vizsgáztató tesztel, kérdéseket tesz fel vele kapcsolatban. Szükség esetén a vizsgáztató kisebb módosításokat kér a vizsgázótól a vizsga során.

Ha a javasolt jegyen a hallgató javítani szeretne, a vizsgáztató plusz feladatokat, módosítási kéréseket jelöl meg, melyeket issue-k formájában rögzít is.

A hallgató egy következő vizsgán ezen kéréseknek eleget tevő változtatásokkal újra megvédheti a beadandóját.

Mintaképpen egy beadandó feladat elérhető lesz ebben a repository-ban.

# Heti beosztás

<table style="width:100%">
  <tr>
    <th>Hét</th>
    <th>Előadás</th>
    <th>Gyakorlat</th>
  </tr>
  <tr>
    <th>1</th>
    <td>
     Követelmények ismertetése, alapvető, programozással kapcsolatos fogalmak tisztázása (szoftverfejlesztés, tesztelés, algoritmizálás, programozási nyelvek, forráskód, gépi kód, köztes kód, fordító, interpreter, IDE, syntax highlight, stb.), valamint korábbi tapasztalatok felmérése.
    </td>
    <td>
     Fejlesztői környezet telepítése (vscode), alapvető szövegszerkesztési technikák, shortcutok megismerése. GitHub regisztráció, első repository létrehozása, `README.md` szerkesztése, GitHub alapvető használatának elsajátítása (1 branch, 1 user), fontosabb felületek megismerése (code / commits). vscode és GitHub összekötése.
    </td>
  </tr>
  <tr>
    <th>2</th>
    <td>Elágazás és egyszerű ciklus mint vezérlési adatszerkezet megismerése, szöveges algoritmizálás, pszeudo kód megismerése absztrakt magas szintű utasításokon mellett.</td>
    <td>Alapvető vezérlési szerkezetek gyakorlása életszerű példákon, pszeudo kód szinten.</td>
  </tr>
  <tr>
   <th>3</th>
   <td>
    Absztraktabb példák, változó fogalmának bevezetése. Egyerű bekérés, kiiratás (egész változókra szorítkozva) és alapvető vezérlési szerkezetek használata továbbra is pszeudo kód szintjén. 
   </td>
   <td>
    Példákon keresztül gyakorlás. Először oktató által adott kód végrehajtása, majd saját kód tervezése.
   </td>
  </tr>
  <tr>
   <th>4</th>
   <td>
    Összetettebb feladatok a megadott eszközökkel, alap minták, pl.: minimumkeresés, bekérés adott elemig, stb. 2-3 egymásba ágyazott blokk szintjéig.
   </td>
   <td>
    Példákon keresztül gyakorlás. Először oktató által adott kód végrehajtása, majd saját kód tervezése.
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
  </tr>
  <tr>
   <th>6</th>
   <td>
    Listák, alapvető függvnyeik, alap programozási feladatok listákkal, pl: minimumkeresés, Fibonacci sorozat felépítése, buborékrendezés.
   </td>
   <td>
    Listákat igénylő feladatokon keresztüli gyakorlás. 
   </td>
  </tr>
  <tr>
   <th>7</th>
   <td>
    További nyelvi elemek bevezetése, pl `for ... in`, `break`, splicing stb.
    Logikai és lebegőpontos változók, változó típusok, konvertálás.
   </td>
   <td>
    Néhány korábbi kód átírása, lerövidítése a megismert új eszközökkel, valamint új feladatokon gyakorlás
   </td>
  </tr>
  <tr>
   <th>8</th>
   <td>
    String típus, egyszerű szöveges fájlkezelés.
   </td>
   <td>
    ZH + Gyakorlás feladatokkal.
   </td>
  </tr>
  <tr>
   <th>9</th>
   <td>
    Függvények. Kód absztrakt megtervezése függvények szintjén egy bonyolultabb feladat példáján. 
   </td>
   <td>
    Fügvények gyakorlása, korábbi feladatok újrastruktúrálása.
   </td>
  </tr>
  <tr>
   <th>10</th>
   <td>
    Paraméterátadás, immutability, pass-by-value-of-reference megértése,tuple-ök.
   </td>
   <td>
    Olyan példákkal is gyakorlás, ahol listák is átadásra kerülnek, tipikus pitfall-ok hibák elkerülése.
   </td>
  </tr>
  <tr>
   <th>11</th>
   <td>
    Dictionary, tipikus alkalmazási esetei.
   </td>
   <td>
    Gyakorlás olyan példákon, amik dictionary nélkül nagyon körülményesek lennének.
   </td>
  </tr>
  <tr>
   <th>12</th>
   <td>
    További praktikus python nyelvi elemek megismerése, pl.: listák másolása, JSON formátum és parzolás, további hasznos beépített függvények, stb.
   </td>
   <td>
    Gyakorlás ZH-ra.
   </td>
  </tr>
  <tr>
   <th>13</th>
   <td>
    Fák, gráfok, implementálásuk pythonban, egyszerűbb algoritmusok, bejárások. 
   </td>
   <td>
    ZH + beadandó témák egyeztetése.
   </td>   
  </tr>
</table>
