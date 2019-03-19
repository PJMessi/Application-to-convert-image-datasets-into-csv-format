# Convert-dataset-to-CSV

<b>Required Libraries</b>
<ol>
  <li>Scipy &nbsp; <b>$ pip install scipy</b></li>
  <li>Pandas &nbsp; <b>$ pip install pandas</b></li>
  <li>Numpy &nbsp; <b>$pip install numpy</b></li>
</ol>

<p>I'm using the datasets in test.zip and train.zip and convert them into csv.</p>

<small>Both test.zip and train.zip contain the handwritten nepali character datas. They each contain 58 folders with folder name 0 to 57. Folder 0 to 9 contains the data for nepali digit 0 to 9. Folder 10 to 45 contains the data for nepali consonant 'kaa' to 'gya'. Folder 46 to 57 contain data for nepali vowels 'aaa' to 'aah'</small>

<p>You can use your own dataset. But if you want to use mine, <b>Extract the test.zip and train.zip in the same directory and run conversion.py</b></p>

<p>I have explained every command inside the conversion.py in details using comments.</p>

<p>I have also included the <b>'test_converted_csv.ipynb'</b> file to test the converted csv file and <b> 'feed_csv_to_model.ipynb'</b>, where i feed the csv to a model. You can run this file using jupyter notebook.</p>