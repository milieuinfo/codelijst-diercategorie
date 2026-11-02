# /// script
# requires-python = ">=3.10"
# dependencies = ["pyarrow", "numpy>=2"]
# ///
# Uitvoeren:  uv run src/test/test_parquet_reducerende_maatregel.py
"""Test het datatype van de kolom reducerende_maatregel in de parquet-export.

Verwacht: de kolom is een lijst van strings, fysiek geschreven als standaard
Parquet LIST (`optional group ... (List) { repeated group list { element } }`),
en elke rij is een lijst (eventueel leeg) waarvan elk element een URI-string is.

Gebruik (vanuit de projectroot):
    uv run src/test/test_parquet_reducerende_maatregel.py [pad/naar/bestand.parquet]
"""
import sys
from collections import Counter

import pyarrow as pa
import pyarrow.parquet as pq

DEFAULT = ("src/main/resources/be/vlaanderen/omgeving/data/id/conceptscheme/"
           "diercategorie/diercategorie.parquet")
KOLOM = "reducerende_maatregel"

pad = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
tabel = pq.read_table(pad)
fouten = []

# 1. schema: list<string>
veld = tabel.schema.field(KOLOM)
print(f"schema {KOLOM}: {veld.type}")
if not (pa.types.is_list(veld.type) and pa.types.is_string(veld.type.value_type)):
    fouten.append(f"kolomtype is {veld.type}, verwacht list<string>")

# 2. fysiek schema: standaard LIST-annotatie (3-level), niet de legacy `repeated <type>`.
#    pyarrow leest beide als list<string>; viewers zoals die van IntelliJ niet.
fysiek = pq.ParquetFile(pad).schema
paden = [fysiek.column(i).path for i in range(len(fysiek)) if fysiek.column(i).path.split(".")[0] == KOLOM]
groep = next((r.strip() for r in str(fysiek).splitlines()
              if r.strip().split(" {")[0].split(" ")[-2:-1] == [KOLOM] or f" {KOLOM} " in r), "")
print(f"fysiek {KOLOM}: {groep.rstrip(' {')}  (kolompad: {', '.join(paden)})")
if paden != [f"{KOLOM}.list.element"] or "(List)" not in groep:
    fouten.append(f"geen standaard LIST-annotatie: {groep.rstrip(' {') or '?'} (kolompad {', '.join(paden) or '?'}), "
                  f"verwacht `optional group {KOLOM} (List) {{ repeated group list {{ optional binary element }} }}`")

# 3. elke waarde: lijst van niet-lege URI-strings
ids = tabel.column("id").to_pylist()
waarden = tabel.column(KOLOM).to_pylist()
soorten = Counter()
for id_, waarde in zip(ids, waarden):
    if waarde is None:
        soorten["null"] += 1
        fouten.append(f"{id_}: null in plaats van lijst")
        continue
    if not isinstance(waarde, list):
        soorten[type(waarde).__name__] += 1
        fouten.append(f"{id_}: {type(waarde).__name__} in plaats van lijst")
        continue
    soorten["leeg" if not waarde else ("1 element" if len(waarde) == 1 else ">1 elementen")] += 1
    for element in waarde:
        if not isinstance(element, str):
            fouten.append(f"{id_}: element {element!r} is {type(element).__name__}, verwacht str")
        elif not element.startswith("https://"):
            fouten.append(f"{id_}: element {element!r} is geen URI")

print(f"rijen: {len(waarden)}  " + "  ".join(f"{k}: {v}" for k, v in sorted(soorten.items())))

if fouten:
    print(f"\nFAALT: {len(fouten)} fout(en)")
    for f in fouten[:20]:
        print("  -", f)
    if len(fouten) > 20:
        print(f"  ... en nog {len(fouten) - 20}")
    sys.exit(1)
print("OK: alle waarden zijn lijsten van URI-strings")
