# ISTAT-unità-amministrative-sql
###### Converte i dati pubblicati dall'ISTAT: "CODICI STATISTICI DELLE UNITÀ AMMINISTRATIVE TERRITORIALI: COMUNI, CITTÀ METROPOLITANE, PROVINCE E REGIONI" da CSV a SQL

<br>

Tool scritto in python utile per generare i dati sql a partire dalle tabelle fornite dall'ISTAT. Genera inserimenti per Comuni, Regioni e Provincie.

Link alla pagina dell'ISTAT: https://www.istat.it/it/archivio/6789

<br>

File considerati nello specifico:
- Provincie e regioni: https://www.istat.it/storage/codici-unita-amministrative/Codici-statistici-e-denominazioni-delle-ripartizioni-sovracomunali.zip
- Comuni: https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv

---

## Utilizzo

1. Scaricare i file
2. Estrarre il file CSV dallo zip
3. Posizionare lo script python e i CSV nella stessa cartella
4. Lanciare lo script: `python ISTAT_parser.py`
5. Finito, troverete un file .sql con i dati

---

## Schema database di riferimento

```sql
CREATE TABLE region
(
    id   INT(10) UNSIGNED NOT NULL,
    name VARCHAR(32)      NOT NULL,

    CONSTRAINT `region_pk` PRIMARY KEY (id)
);

CREATE TABLE province
(
    id     CHAR(2)          NOT NULL,
    name   VARCHAR(64)      NOT NULL,
    region INT(10) UNSIGNED NOT NULL,

    CONSTRAINT `province_pk` PRIMARY KEY (id),
    CONSTRAINT `province_fk_region` FOREIGN KEY (region) REFERENCES region (id)
);

CREATE TABLE city
(
    id       INT(10) UNSIGNED NOT NULL,
    name     VARCHAR(64)      NOT NULL,
    province CHAR(2)          NOT NULL,

    CONSTRAINT `city_pk` PRIMARY KEY (id),
    CONSTRAINT `city_fk_province` FOREIGN KEY (province) REFERENCES province (id)
);
```

---

## Esempio del file generato:
```
-- province
INSERT INTO province VALUES(`TO`, `Torino`, 1);
INSERT INTO province VALUES(`VC`, `Vercelli`, 1);
INSERT INTO province VALUES(`NO`, `Novara`, 1);
INSERT INTO province VALUES(`CN`, `Cuneo`, 1);
INSERT INTO province VALUES(`AT`, `Asti`, 1);
INSERT INTO province VALUES(`AL`, `Alessandria`, 1);
INSERT INTO province VALUES(`BI`, `Biella`, 1);
INSERT INTO province VALUES(`VB`, `Verbano-Cusio-Ossola`, 1);
INSERT INTO province VALUES(`AO`, `Valle d'Aosta/Vallée d'Aoste`, 2);
...
```
