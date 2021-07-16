# Parlament-schema

Schema and validator for the data of Parlament de Catalunya. The validator is written in python.

## Validate

To launch the validator, the only requisite is lxml.

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

After the installation simply:

```
python validate.py parlament.xml parlament.xsd
```

## Summary of the schema/Resum de l'esquema

L'esquema d'xml està dissenyat amb la plantilla de matrioixca, que els elements únics només apareixen dins d'un altre element específic. 

```
source
└── session
    ├── sequence
    │   └── intervention
    └── transcriptions
        └── transcriptions_url
```

Aquesta estructura bàsica és gairebé igual a la jerarquia de DOM de la plataforma de parlament.cat actual amb dues excepcions:

*media_url:*
El primer; l'esquema està optimitzat per les dues estructures diferents de la pàgina web vella i la pàgina web nova; amb l'objectiu de facilitar l'extracció d'una intervenció especifica cercada.

La diferencia de les estructures noves i velles del parlament.cat és la quantitat de fitxers d'àudio per sessió. En la versió vella, hi havia un enregistrament per intervenció, en canvi ara parlament.cat proporciona els enregistraments sencers (podrien ser múltiples però no més de 3 o 4) de cada sessió, i per cada intervenció desitjada la plataforma ensenya la part de l’enregistrament pertinent.

Per assegurar la consistència entre les estructures diferents del parlament.cat, l'url del fitxer d'àudio apareix dins de l'element "intervention." Aquesta manera els urls de la vella estructura puguin aparèixer al nivell adequat d'esquema. Per les intervencions de la nova estructura, com que els urls apunten a un vídeo llarg de la sessió especifica, aquesta informació repeteix per cada intervenció pertinent. Però mitjançant les metadades de data i temps d'inici i durada de la intervenció, i la data i hora d'inici de l'enregistrament, que apareixen dins de l'element "intervention," es pot generar els talls/segments pertinents senzillament, sense accedir els elements pares. 

*transcriptions:*
El segon element que no compleix amb l'estructura del DOM de parlament.cat és els urls de les transcripcions; que són en dos llocs diferents.

El pdf del diari de la sessió, ´diari_url´, és l'element fill de la "session" i és un element obligatori. A més hi ha elements de ´transcriptions´ que poden tenir els "types" ´en brut´ o ´automatica´. El type ´en brut´ fa referencia a les transcripcions publicades temporalment a parlament.cat, abans de la publicació del diari final i editat. Com que no està decidit encara la disponibilitat continua de les transcripcions en brut o automàtiques, aquests elements no són obligatoris.

Un fet molt important és els elements transcription_url tenen "l'attribute" ´order´ que defineix l'ordre de les transcripcions en temps. Aquesta és la informació mínima per vincular el timestamp de cada intervenció i la transcripció pertinent. En principi el repositori ´parlament_scrape´ connecta les transcripcions amb el segment de vídeo mitjançant un alineament seqüència a seqüència, comparant els intervinents dels diaris/transcripcions i del DOM dels enregistraments. Per això informació addicional, com la data i l'hora d'inici de les transcripcions no són necessàries, sempre que l'ordre dels múltiples fitxers/urls de les transcripcions són correctes.

Tal com està la plataforma de parlament.cat aquesta informació tant dels diaris com de les transcripcions no apareixen a la pàgina dels enregistraments, i per vincular els enregistraments amb les transcripcions cal buscar-les a un altre lloc segons les dates corresponents.
