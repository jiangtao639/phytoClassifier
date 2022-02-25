# phytoClassifier
Python Classifier for plant secondary metabolites. PhytoClassifier is a database-based tool for classifying plant compounds.

## Installing phytoClassifier

```shell
pip install phytoClassifier==0.0.4
# or 
py -m pip install phytoClassifier==0.0.4
```

## Example Usage 

```python
import phytoClassifier as pc

# get class by SMILES
cls = pc.getClassBySmiles("CC(C)CCCC(C)C1CCC2C1(CCCC2=CC=C3CC(CC(C3=C)O)O)C")

# get class by PubChem Id
cls1 = pc.getClassByCid("131")

# get class by InChICode
cls2 = pc.getClassByInchi("InChI=1S/C8H12NO6P/c1-5-8(11)7(3-10)6(2-9-5)4-15-16(12,13)14/h2,10-11H,3-4H2,1H3,(H2,12,13,14)")

# get class by InChIKey
cls3 = pc.getClassByInChiKey("HXVZGASCDAGAPS-UHFFFAOYSA-N")

# get class by Name !!Fuzzy search, deprecated! returns multiple entries.
cls4 = pc.getClassByName("Anthrapurpurin")

print(cls,cls1,cls2,cls3,cls4,sep="\n")
```

## Python Dependencies

- sqlite3
- pkg_resources
