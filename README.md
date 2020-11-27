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

| Hét | Előadás | Gyakorlat |
|-----|---------|-----------|
|1| Követelmények ismertetése, alapvető, programozással kapcsolatos fogalmak tisztázása (szoftverfejlesztés, tesztelés, algoritmizálás, programozási nyelvek, forráskód, gépi kód, köztes kód, fordító, interpreter, IDE, syntax highlight, stb.), valamint korábbi tapasztalatok felmérése. | Fejlesztői környezet telepítése (vscode), alapvető szövegszerkesztési technikák, shortcutok megismerése. GitHub regisztráció, első repository létrehozása, `README.md` szerkesztése, GitHub alapvető használatának elsajátítása (1 branch, 1 user), fontosabb felületek megismerése (code / commits). vscode és GitHub összekötése. |
| 2 | Elágazás és egyszerű ciklus mint vezérlési adatszerkezet megismerése, szöveges algoritmizálás, pszeudo kód megismerése absztrakt magas szintű utasításokon mellett. | Alapvető vezérlési szerkezetek gyakorlása életszerű példákon, pszeudo kód szinten.|
| 3 | Absztraktabb példák, változó fogalmának bevezetése. Egyerű bekérés, kiiratás (egész változókra szorítkozva) és alapvető vezérlési szerkezetek használata továbbra is pszeudo kód szintjén.  | Példákon keresztül gyakorlás. Először oktató által adott kód végrehajtása, majd saját kód tervezése.|
| [4](04/) | Python legalapabb nyelvi elemeinek ismertetése, annak használata. Pszeudo kód és python közötti megfeleltetés, különbségek.  | Korábbi példák megvalósítása python nyelven.|
| [5](05/) | Listák, alapvető függvnyeik, alap programozási feladatok listákkal, pl: minimumkeresés, Fibonacci sorozat felépítése, buborékrendezés. | Listákat igénylő feladatokon keresztüli gyakorlás. |
| [6](06/) | További nyelvi elemek bevezetése, pl `range`, `for ... in`, `break`, list slicing, főbb típusok stb. | Néhány korábbi kód átírása, lerövidítése a megismert új eszközökkel, valamint új feladatokon gyakorlás|
| [7](07/) | Függvények alapjai | Okt. 23.  miatt szünet |
| [8](08/) | **ZH**, scope, referenciák, pass-by-reference-value, immutability | Gyakorlás  |
| [9](09/) |  Dictionary és Tupple, összetett adatszerkezetek egymásba ágyazása | Gyakorlás az új adattípusokkal, adatok lemodellezéséhez helyes típusok kiválasztása |
| [10](10/) |  Pythontutor, fájlkezelés, pickle, JSON | Egyszerű, adatmenedzselő programok, JSON "adatbázissal" |
| [11](11/) |  Minta, gyakorlás beadandóhoz |  |
| [12](12/) |  Format string, random, modulokba szerezés | |

További tervezett témák:
 - try-except
 - egyszerűbb gráfalgoritmusok
 - fejlesztői dokumentáció
