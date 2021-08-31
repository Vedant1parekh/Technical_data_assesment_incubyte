# Incubyte_data_Engineer
This repository conatins implementation of Incubyte Technical assesment for data Engineer

<h3>Concepts</h3>
<ul>
  <li>Data processing</li>
  <li>ETL</li>
 </ul>
<h3>🔹Tools and Technology<h3>
  <ul>
    <li>Python</li>
    <li>My sql Database</li>
    <li> My sql Workbench</li>
    <li>My sql connector-python</li>
    <li>Datetime</li>
    <li>Pandas</li>
   </ul>
<h3>🔹Working</h3>
  <ul>
    <li> First Create Mysql database with specified Schema</li>
    <li><b>database_connector.py</b> python script, fetches database by establishing connection with MySQL server</li>
    <li> Second Step is divided into further three parts:</li>
      <ol>
        <li>Extract data from patients.txt file </li>
        <li> Trasform date into specific format</li>
        <li> For int data type convert null to 0 value</li></ol>
        <li>The data will be in panda-dataframe and inserted into database</li>
        <li> The data of each country is retrieved in pandas dataframe and generated pipe seperated data in <b>output_data.txt</b> file.</li>
  </ul>

       
  











