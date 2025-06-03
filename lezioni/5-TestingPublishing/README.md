# Testing e Publishing in Python

In questa sezione approfondiremo le tecniche di testing in Python e il processo di pubblicazione dei pacchetti, competenze fondamentali per lo sviluppo di software affidabile e condivisibile.

<!-- New section -->

## Sommario

1. **Python Debugger (pdb)** e breakpoint
2. **Tipi di test** (Unit, Integration, Acceptance, Regression)
3. **Assertions e unittest**
4. **PyTest**: fixtures, monkeypatch, mock
5. **Coverage dei test**
6. **Continuous Delivery e Deployment** con GitHub
7. **Tag e release Git**
8. **Pubblicazione su PyPI** con uv
9. **Accenni su documentazione**

<!-- New section -->

## 1. Python Debugger (pdb) e breakpoint

Il debug è un processo fondamentale nello sviluppo software, che permette di individuare e risolvere gli errori nel codice. Python offre strumenti integrati per facilitare questa attività.

### Il modulo pdb

<!-- .element: class="fragment" data-fragment-index="1" -->

Il Python Debugger (`pdb`) è un modulo della libreria standard che fornisce funzionalità di debugging interattivo. Permette di:
- Eseguire il codice passo-passo
- Ispezionare variabili durante l'esecuzione
- Impostare breakpoint condizionali
- Esaminare lo stack delle chiamate

<!-- .element: class="fragment" data-fragment-index="1" -->

<!-- New subsection -->

### Come usare pdb

Ci sono diversi modi per avviare il debugger:

1. **Chiamata esplicita nel codice**:
```python
import pdb
pdb.set_trace()  # Il programma si ferma qui quando eseguito
```

2. **Dalla linea di comando**:
```bash
python -m pdb mio_script.py
```

3. **Usando la funzione breakpoint()** (Python 3.7+):
```python
# Nel codice, dove si desidera fermare l'esecuzione
breakpoint()  # Equivalente a import pdb; pdb.set_trace()
```

<!-- New subsection -->

### Comandi principali di pdb

Una volta attivato il debugger, si possono usare vari comandi:

- `n` (next): esegue la linea corrente e passa alla successiva
- `s` (step): entra nella funzione chiamata
- `c` (continue): continua l'esecuzione fino al prossimo breakpoint
- `q` (quit): esce dal debugger
- `l` (list): mostra il codice circostante
- `u` (up): sale nello stack delle chiamate
- `d` (down): scende nello stack delle chiamate

<!-- New subsection -->

### Debug in ambiente IDE

La maggior parte degli IDE moderni (VS Code, PyCharm, ecc.) offrono interfacce grafiche per il debugging che semplificano il processo:

- Breakpoint visuali (cliccando sul margine dell'editor)
- Visualizzazione delle variabili in finestre dedicate
- Valutazione di espressioni durante l'esecuzione
- Visualizzazione dello stack di chiamate

Queste interfacce sono spesso più intuitive rispetto all'uso diretto di pdb, ma è comunque utile conoscere i comandi base per situazioni in cui non si dispone dell'IDE.

<!-- New section -->

## 2. Tipi di test

Nel software engineering, esistono diversi tipi di test che servono a verificare aspetti diversi dell'applicazione. I principali sono:

### Unit Test

<!-- .element: class="fragment" data-fragment-index="1" -->

I test unitari verificano il funzionamento di singole unità di codice (funzioni, metodi o classi) in isolamento.
**Caratteristiche**:
- Testano una funzionalità specifica
- Sono rapidi da eseguire
- Non dipendono da componenti esterni (DB, servizi web, filesystem)
- Seguono spesso il pattern Arrange-Act-Assert (AAA)

<!-- .element: class="fragment" data-fragment-index="1" -->

<!-- New subsection -->

### Integration Test

I test di integrazione verificano l'interazione tra diversi componenti o sistemi.

**Caratteristiche**:
- Testano il funzionamento combinato di più unità
- Possono richiedere l'uso di mocking o servizi di test
- Verificano il corretto passaggio di dati tra componenti
- Sono più lenti degli unit test ma più realistici

<!-- New subsection -->

### Acceptance Test

I test di accettazione verificano se l'applicazione soddisfa i requisiti di business e le aspettative degli utenti.

**Caratteristiche**:
- Basati su scenari d'uso e criteri di accettazione
- Spesso eseguiti dal punto di vista dell'utente finale
- Possono essere sia automatizzati che manuali
- Verificano il sistema completo, includendo UI, database, ecc.

<!-- New subsection -->

### Regression Test

I test di regressione assicurano che le modifiche recenti al codice non abbiano danneggiato funzionalità preesistenti.

**Caratteristiche**:
- Rieseguono test precedentemente passati dopo modifiche
- Fondamentali durante il refactoring
- Possono includere una selezione di tutti i tipi di test precedenti
- Aiutano a mantenere la stabilità del software nel tempo

<!-- New subsection -->

### La piramide dei test

Un approccio equilibrato al testing prevede una "piramide" con:

- Molti unit test alla base (veloci ed economici)
- Un numero medio di test di integrazione al centro
- Pochi test di accettazione/end-to-end al vertice (complessi e costosi)

![Piramide dei test](https://martinfowler.com/articles/practical-test-pyramid/testPyramid.png)

<!-- New section -->

## 3. Assertions e unittest

### Assertions

Le assertion sono verifiche inserite nel codice che controllano che una determinata condizione sia vera. In Python, si usano con la parola chiave `assert`:

```python
def dividi(a, b):
    assert b != 0, "Il divisore non può essere zero"
    return a / b
```

Se la condizione è falsa, viene lanciata un'eccezione `AssertionError` con il messaggio specificato.

<!-- New subsection -->

Le assertion sono utili per:
- Verificare precondizioni e postcondizioni
- Documentare assunzioni nel codice
- Individuare rapidamente errori logici

> **Attenzione**: Le assertion vengono disabilitate quando Python è eseguito in modalità ottimizzata (`python -O`), quindi non andrebbero usate per controlli di sicurezza o validazione di input esterni.

<!-- New subsection -->

### Il modulo unittest

`unittest` è un framework di testing incluso nella libreria standard Python, ispirato al framework JUnit di Java. Fornisce strumenti per organizzare e automatizzare i test.

Elementi principali:
- **TestCase**: classe base per definire test
- **Assertion methods**: metodi per verificare condizioni
- **Test runner**: componente che esegue i test
- **Test suite**: raggruppamenti di test correlati

<!-- .element: class="fragment" data-fragment-index="1" -->

<!-- New subsection -->

Esempio di utilizzo:

```python
import unittest

def somma(a, b):
    return a + b

class TestSomma(unittest.TestCase):
    def test_numeri_positivi(self):
        self.assertEqual(somma(1, 2), 3)
        
    def test_numeri_negativi(self):
        self.assertEqual(somma(-1, -2), -3)

if __name__ == '__main__':
    unittest.main()
```

<!-- New subsection -->

### Assertion Methods di unittest

Il modulo unittest fornisce vari metodi per effettuare asserzioni:

- `assertEqual(a, b)`: verifica che a == b
- `assertNotEqual(a, b)`: verifica che a != b
- `assertTrue(x)`: verifica che bool(x) è True
- `assertFalse(x)`: verifica che bool(x) è False
- `assertIs(a, b)`: verifica che a is b
- `assertIsNot(a, b)`: verifica che a is not b
- `assertIsNone(x)`: verifica che x is None
- `assertIsNotNone(x)`: verifica che x is not None
- `assertIn(a, b)`: verifica che a in b
- `assertNotIn(a, b)`: verifica che a not in b
- `assertRaises(eccezione, callable, *args, **kwds)`: verifica che la funzione lanci l'eccezione

<!-- New subsection -->

### Setup e Teardown

Unittest permette di definire metodi che vengono eseguiti prima e dopo ogni test:

```python
class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Eseguito prima di ogni test"""
        self.db = Database.connect("test.db")
        self.db.create_tables()
    
    def tearDown(self):
        """Eseguito dopo ogni test"""
        self.db.drop_tables()
        self.db.close()
    
    def test_insert(self):
        self.db.insert("users", {"name": "Mario"})
        self.assertEqual(self.db.count("users"), 1)
```

Esistono anche `setUpClass` e `tearDownClass` per inizializzazioni e pulizia a livello di classe, utili per ottimizzare operazioni costose.

<!-- .element: class="fragment" data-fragment-index="1" -->

<!-- New section -->

## 4. PyTest: fixtures, monkeypatch, mock

### Introduzione a PyTest

PyTest è un framework di testing più moderno e potente rispetto a unittest, con una sintassi più semplice e maggiore flessibilità.

Vantaggi principali:
- Sintassi semplificata (usa funzioni invece di classi)
- Assertion più intuitive (usa assert standard di Python)
- Sistema di plugin estensibile
- Migliore gestione di setup/teardown con fixtures
- Report dettagliati e colorati
- Parallelizzazione dei test

<!-- New subsection -->

### Test basilari con PyTest

Con PyTest, i test sono semplici funzioni che iniziano con `test_`:

```python
# test_esempio.py
def somma(a, b):
    return a + b

def test_somma_base():
    assert somma(2, 3) == 5
    
def test_somma_negativi():
    assert somma(-1, -1) == -2
```

Per eseguire i test:
```bash
pytest test_esempio.py
```

<!-- New subsection -->

### Fixtures

Le fixtures sono uno dei cardini di PyTest: forniscono dati, oggetti o ambiente necessari ai test, con gestione automatica delle risorse.

```python
import pytest

@pytest.fixture
def database():
    # Setup
    db = Database.connect(":memory:")
    db.create_tables()
    
    # Passa l'oggetto al test
    yield db
    
    # Teardown (eseguito dopo il test)
    db.close()

def test_inserimento(database):
    database.insert("users", {"name": "Mario"})
    assert database.count("users") == 1
```

<!-- New subsection -->

### Parametrizzazione dei test

PyTest permette di eseguire lo stesso test con parametri diversi:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (5, True),
    (9, False),
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected
```

<!-- New subsection -->

### Monkeypatch

`monkeypatch` è una fixture che permette di modificare temporaneamente oggetti, classi o funzioni durante i test:

```python
def get_weather(city):
    # In un caso reale, questa funzione farebbe una richiesta API
    # che non vogliamo eseguire durante i test
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()

def test_get_weather(monkeypatch):
    # Creiamo una funzione mock che sostituisce requests.get
    def mock_get(url):
        class MockResponse:
            def json(self):
                return {"temperature": 25, "city": "Roma"}
        return MockResponse()
    
    # Applichiamo il monkeypatch
    monkeypatch.setattr("requests.get", mock_get)
    
    # Il test usa la funzione mock invece di quella reale
    result = get_weather("Roma")
    assert result["temperature"] == 25
```

<!-- New subsection -->

### Mock di unittest

Per situazioni più complesse, PyTest può utilizzare il modulo `unittest.mock`:

```python
from unittest.mock import Mock, patch

def test_with_mock():
    # Creazione di un mock
    mock_db = Mock()
    mock_db.count.return_value = 5
    
    # Uso del mock
    assert mock_db.count("users") == 5
    mock_db.count.assert_called_once_with("users")

@patch("module.requests.get")
def test_with_patch(mock_get):
    # Configurazione del mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "test"}
    
    # Funzione che usa requests.get
    from module import fetch_data
    result = fetch_data("url")
    
    # Verifiche
    assert result == {"data": "test"}
    mock_get.assert_called_once_with("url")
```

<!-- New section -->

## 5. Coverage dei test

La coverage dei test (copertura) misura quanto codice è stato eseguito durante i test, aiutando a identificare parti non testate.

### Libreria coverage

`coverage.py` è lo strumento standard in Python per misurare la copertura del codice durante l'esecuzione dei test.

Installazione:
```bash
pip install coverage
```

<!-- New subsection -->

### Utilizzo base

Per misurare la copertura:

```bash
# Esegue il programma raccogliendo statistiche di copertura
coverage run -m pytest

# Genera un report
coverage report

# Genera un report HTML più dettagliato
coverage html
```

Il report mostrerà per ogni file la percentuale di linee di codice eseguite.

<!-- New subsection -->

### Esempio di report

```
Name                      Stmts   Miss  Cover
---------------------------------------------
mypackage/__init__.py        10      0   100%
mypackage/module1.py         45     10    78%
mypackage/module2.py         32     16    50%
---------------------------------------------
TOTAL                        87     26    70%
```

Il report HTML offre una visualizzazione più dettagliata, con evidenziate le linee non coperte dai test.

<!-- New subsection -->

### Integrazione con PyTest

PyTest offre un plugin dedicato alla copertura:

```bash
pip install pytest-cov
```

Utilizzo:
```bash
pytest --cov=mypackage tests/
pytest --cov=mypackage --cov-report=html tests/
```

<!-- New subsection -->

### Analisi della copertura

La copertura del codice può essere misurata in diversi modi:

1. **Line coverage**: quante linee di codice sono state eseguite
2. **Branch coverage**: quanti rami condizionali sono stati eseguiti
3. **Path coverage**: quanti percorsi possibili sono stati eseguiti

Una buona copertura dei test non garantisce l'assenza di bug, ma riduce significativamente la probabilità di errori non rilevati.

<!-- New section -->

## 6. Continuous Delivery e Deployment con GitHub

### Continuous Integration (CI)

La CI è una pratica che prevede l'integrazione frequente del codice nel repository condiviso, con verifica automatica della correttezza tramite build e test.

**Benefici**:
- Identificazione rapida di errori
- Riduzione del "merge hell"
- Feedback costante sulla qualità del codice
- Automazione di processi ripetitivi

<!-- New subsection -->

### GitHub Actions

GitHub Actions è lo strumento di GitHub per implementare CI/CD (Continuous Integration/Continuous Delivery):

- Workflow definiti in file YAML nella directory `.github/workflows/`
- Trigger configurabili (push, pull request, schedule, ecc.)
- Esecuzione su runner gestiti da GitHub o self-hosted
- Ampio marketplace di azioni predefinite
- Integrazione nativa con GitHub

<!-- New subsection -->

### Esempio di workflow per Python

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Run tests
      run: |
        pytest
```

<!-- New subsection -->

### Continuous Delivery vs. Continuous Deployment

- **Continuous Delivery**: processo di automazione che prepara il codice per il rilascio, ma richiede approvazione manuale per il deployment
- **Continuous Deployment**: processo completamente automatizzato che porta il codice dalla fase di sviluppo alla produzione senza intervento umano

<!-- New section -->

## 7. Tag e Release Git

### Tagging in Git

I tag Git sono riferimenti a punti specifici nella storia del repository, usati principalmente per marcare versioni del software:

- Offrono un modo per identificare versioni specifiche
- Possono essere annotated (con metadati) o lightweight
- Sono statici (non si muovono come i branch)
- Tipicamente seguono convenzioni di semantic versioning (X.Y.Z)

<!-- New subsection -->

### Creare Tag

```bash
# Creare un tag lightweight
git tag v1.0.0

# Creare un tag annotated (consigliato per le release)
git tag -a v1.0.0 -m "Versione 1.0.0: prima release stabile"

# Taggare un commit specifico
git tag -a v1.0.0 -m "Versione 1.0.0" 9fceb02

# Pushare i tag al repository remoto
git push origin v1.0.0
# oppure pushare tutti i tag
git push origin --tags
```

<!-- New subsection -->

### Semantic Versioning

Il [Semantic Versioning](https://semver.org/) è uno standard per numerare le versioni del software:

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: cambiamenti incompatibili con le versioni precedenti
- **MINOR**: funzionalità aggiunte in modo retrocompatibile
- **PATCH**: correzioni di bug retrocompatibili

Esempi: 1.0.0, 1.2.3, 2.0.0-alpha.1

<!-- New subsection -->

### Release su GitHub

Una release su GitHub è un modo per condividere software compilato, note di rilascio e collegamenti per ogni versione taggata:

1. Navigare alla sezione "Releases" del repository
2. Cliccare "Draft a new release"
3. Selezionare un tag (esistente o nuovo)
4. Aggiungere titolo e descrizione (note di rilascio)
5. Opzionalmente allegare file compilati (.zip, .tar.gz, ecc.)
6. Pubblicare la release

Le release sono ideali per distribuire il software a utenti non tecnici o per documentare cambiamenti tra versioni.

<!-- New section -->

## 8. Pubblicazione su PyPI con uv

### Python Package Index (PyPI)

PyPI è il repository ufficiale per pacchetti Python, da cui gli utenti possono installare software con pip:

- Ospita più di 400.000 progetti
- Permette installazioni con `pip install nome_pacchetto`
- Richiede standard di packaging specifici
- Può ospitare sia pacchetti open source che privati

<!-- New subsection -->

### Preparazione di un pacchetto

Per pubblicare su PyPI, il progetto deve avere:

1. Un file `pyproject.toml` (o `setup.py`) con metadati del pacchetto
2. Una struttura di cartelle adeguata
3. Documentazione (README.md, etc.)
4. Test funzionanti
5. Versione incrementata (di solito nei tag git)

<!-- New subsection -->

### Esempio di pyproject.toml

```toml
[project]
name = "miopackage"
version = "0.1.0"
description = "Una descrizione del mio pacchetto"
readme = "README.md"
authors = [
    {name = "Il Mio Nome", email = "email@example.com"}
]
license = {text = "MIT"}
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.28.0",
    "numpy>=1.22.0",
]

[project.urls]
Homepage = "https://github.com/username/miopackage"
Issues = "https://github.com/username/miopackage/issues"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

<!-- New subsection -->

### Pubblicazione con uv

[uv](https://docs.astral.sh/uv/) è un gestore di pacchetti Python veloce, sviluppato in Rust, che offre funzionalità per pubblicare su PyPI:

```bash
# Build del pacchetto
uv build

# Pubblicazione su PyPi
uv publish

# Per i test, si può pubblicare su TestPyPI
uv publish --repository testpypi
```

<!-- New subsection -->

### Registrazione su PyPI

Prima di pubblicare, è necessario:

1. Creare un account su [PyPI](https://pypi.org/account/register/)
2. Generare un token API nelle impostazioni account
3. Passare il token come parametro o variabile d'ambiente durante la pubblicazione
```bash
uv publish --token PYPI_TOKEN
```

<!-- New subsection -->

### Best practices per il publishing

- Usare sempre un ambiente virtuale per i test di installazione
- Verificare che il pacchetto sia installabile con `uv pip install .` prima della pubblicazione
- Testare la pubblicazione su [TestPyPI](https://test.pypi.org/) prima di PyPI
- Includere documentazione chiara nel README.md
- Specificare licenza e requisiti di Python
- Seguire il semantic versioning
- Automatizzare il processo di rilascio con CI/CD

<!-- New section -->

## 9. Accenni su documentazione

La documentazione è un aspetto cruciale dello sviluppo software, che aiuta gli utenti e gli sviluppatori a comprendere come utilizzare e contribuire al progetto.

<!-- New subsection -->

### Sphinx

Uno dei tool più comuni per la documentazione in Python è Sphinx, un generatore open source che permette di creare la documentazione in vari formati (HTML, PDF, etc.) a partire da docstring e file Markdown.

### Creazione di un progetto Sphinx
```bash
sphinx-quickstart
```

Questo comando guida l'utente nella creazione di un progetto Sphinx, generando la struttura di cartelle e i file di configurazione necessari.

<!-- New subsection -->

### Configurazione di Sphinx
Il file di configurazione principale è `conf.py`, dove si possono impostare vari parametri come il tema, le estensioni da usare e le directory da includere.

<!-- New subsection -->

### Generazione della documentazione
Per generare la documentazione in HTML, si usa il comando:
```bash
sphinx-build -b html source/ build/
```
Questo comando prende i file sorgente nella cartella `source/` e genera la documentazione HTML nella cartella `build/`.

<!-- New subsection -->

### Integrazione con docstring

Sphinx può estrarre automaticamente le docstring dalle funzioni e classi Python per generare la documentazione. Per farlo, è necessario usare il formato di docstring compatibile, come Google style o NumPy style.

<!-- New subsection -->

### Esempio di docstring in Google style
```python
def somma(a: int, b: int) -> int:
    """
    Calcola la somma di due numeri.

    Args:
        a (int): Il primo numero.
        b (int): Il secondo numero.

    Returns:
        int: La somma di a e b.
    """
    return a + b
```

<!-- New subsection -->

### Esempio di docstring in NumPy style
```python
def somma(a: int, b: int) -> int:
    """
    Calcola la somma di due numeri.

    Parameters
    ----------
    a : int
        Il primo numero.
    b : int
        Il secondo numero.

    Returns
    -------
    int
        La somma di a e b.
    """
    return a + b
```

<!-- New subsection -->

### Estensioni utili per Sphinx
- **autodoc**: per generare documentazione a partire dalle docstring
- **napoleon**: per supportare Google e NumPy style docstrings
- **intersphinx**: per collegare la documentazione di progetti diversi
- **sphinx_rtd_theme**: per usare il tema Read the Docs, molto popolare

<!-- New subsection -->

## pdoc

Un'alternativa a Sphinx è [pdoc](https://pdoc.dev/), un generatore di documentazione semplice e veloce che si concentra sulle docstring e sulla generazione di API documentation.

### Generazione della documentazione con pdoc

Per generare la documentazione di un pacchetto, si usa il comando:
```bash
pdoc <cartella-progetto> -o docs
```
Questo comando genera la documentazione HTML nella cartella `docs/`, a partire dalle docstring presenti nel codice.
Se `-o` è omesso, pdoc creerà un server web locale per visualizzare la documentazione direttamente nel browser.
