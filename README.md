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
    └── sequence
	    └── intervention
```

Aquesta estructura bàsica és gairebé igual a la jerarquia de DOM de la plataforma de parlament.cat actual amb només una excepció. L'esquema esta optimitzat per les dues estructures diferents de la pàgina web vella i la pàgina web nova; amb l'objectiu de facilitar l'extracció d'una intervenció especifica cercada.

La diferencia de les estructures noves i velles del parlament.cat és la quantitat de fitxers d'àudio per sessió. En la versió vella, hi havia un enregistrament per intervenció, en canvi ara parlament.cat proporciona els enregistraments sencers (podrien ser múltiples però no més de 3 o 4) de cada sessió, i per cada intervenció desitjada la plataforma ensenya la part de l’enregistrament pertinent.

Per assegurar la consistència entre les estructures diferents del parlament.cat, l'url del fitxer d'àudio apareix dins de l'element "intervention." Aquesta manera els urls de la vella estructura puguin aparèixer al nivell adequat d'esquema. Per les intervencions de la nova estructura, com que els urls apunten a un vídeo llarg de la sessió especifica, aquesta informació repeteix per cada intervenció pertinent. Però mitjançant les metadades de data i temps d'inici i durada de la intervenció, i la data i hora d'inici de l'enregistrament, que apareixen dins de l'element "intervention," es pot generar els talls/segments pertinents senzillament, sense accedir els elements pares. 

Un altre element important és l'existència d'urls de les transcripcions (pdf del diari de la sessió) vinculat directament amb la sessió pertinent. Tal com està la plataforma de parlament.cat aquesta informació no apareix a la pàgina dels enregistraments, i per vincular els enregistraments amb les transcripcions cal buscar-les a un altre lloc segons les dates corresponents. 
