# [Python](https://python.org) nyelv története, főbb tulajdonságai

 - Magas szintű, általános célú programozási nyelv.
 - Alapvetően interpretált nyelv.
 - Dinamikusan típusos nyelv, garbage collector-ral rendelkezik.
 - Több programozási paradigmát is támogat: procedurális, objektum-orientált, funkcionális.
 - Gazdag alapértelmezett modulkönyvtár.
 - 40 éves nyelv, jelenleg a 3-as változat támogatott, mely visszafele nem kompatibilis a 2-es (2.7.18-as) változattal

### Magas szintű nyelv
Nem hardverhez közeli utasítások az alapvető építőkövek (pl.: regiszterben lévő érték növelése adott memóriacímen található értékkel), hanem magasabb szintűek (változó értékének növelése másik változóval), valamint adottak magas szintű vezérlési szekezetek, összetett adattípusok, stb.

### Általános célú
A nyelv [Turing teljes](https://en.wikipedia.org/wiki/Turing_completeness), azaz tetszőleges algoritmus megvalósítható benne.

### Interpretált
Bár létezik JIT fordító, valamint a nyelv egyes részhalmazaihoz C/C++ fordító, a referencia implementáció ([CPython](https://github.com/python/cpython)) egy interpreter.


# Korábbi utasítások, vezérlési szerkezetek Python megfelelője

| Pszeudo kód          | Python               |
|----------------------|----------------------|
| Amíg (feltétel)      | `while expression:`  |
| Ha (feltétel)        | `if expression:`     |
| Különben             | `else:`              |
| Be: változó          | `variable = input()` |
| Ki: változó          | `print(variable)`    |
| változó = kifejezés  | `variable=expression`|
| Vége                 | `exit()`             |

# Minta kód

A Kollatz sejtéshez kapcsolódó sorozat pszeudo kódja így nézett ki:

```
Be: szám
Amíg (szám≠1)
──┐ Ki: szám
  │ Ha (szám páros)
  ├──┐ szám=szám/2
  │ 
  │ Különben
  ├──┐ szám=3⋅szám+1
```
Aminek a python megvalósítása:

```python
num=input()
while num!=1:
    print(num)
    if num%2==0:
        num/=2
    else:
        num=3*num+1
```
