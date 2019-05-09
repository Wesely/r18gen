# r18gen
Generating string resource files for your project from .tsv file (Tab-saperate-values). 
- Which means your strings' content cannot conain tab: `\t`
- Translate grouping tags into prefix and comments, that makes translator can work easier.
- For this first version, just translate Excel/spreadsheets TSV to XML

## Steps
1. Prepare a SpreadSheets in this format
![image](https://github.com/Wesely/r18gen/blob/master/Spreadsheet_example.png?raw=true)


2. Download/Export it as a TSV file 

3. Open `gen.py` change the `FILENAME` to your `filename.tsv`.

4. run `python gen.py` then you'll see your files in the `output` folder.


## Example

`values_jp/strings.xml`
``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<!-- mainpage -->
	<string name="mainpage_title">こんにちは</string>
	<string name="mainpage_content">世界</string>
<!-- footer -->
	<string name="footer_terms_of_service">利用規約</string>
	<string name="footer_privacy_policy">プライバシー規約</string>
<!-- dummy -->
	<string name="dummy_engineer">エンジニア</string>
	<string name="dummy_software">ソフトウェア</string>
	<string name="dummy_agree">同意する</string>
</resources>
```

`values_zh/strings.xml`
``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<!-- mainpage -->
	<string name="mainpage_title">哈囉</string>
	<string name="mainpage_content">世界</string>
<!-- footer -->
	<string name="footer_terms_of_service">服務條款</string>
	<string name="footer_privacy_policy">隱私權政策</string>
<!-- dummy -->
	<string name="dummy_engineer">工程師</string>
	<string name="dummy_software">軟體</string>
	<string name="dummy_agree">同意</string>
</resources>
```


`values_en/strings.xml`
``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<!-- mainpage -->
	<string name="mainpage_title">Hello</string>
	<string name="mainpage_content">World!</string>
<!-- footer -->
	<string name="footer_terms_of_service">Terms of Service</string>
	<string name="footer_privacy_policy">Privacy Policy</string>
<!-- dummy -->
	<string name="dummy_engineer">Engineer</string>
	<string name="dummy_software">Software</string>
	<string name="dummy_agree">Agree</string>
</resources>
```
