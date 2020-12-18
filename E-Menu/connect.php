<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 45%;
}

.center {
  margin-left: auto;
  margin-right: auto;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #4CAF50;
  color: white;
}

div #header{
  font-family: Arial, Helvetica, sans-serif;
  padding-top: 14px;
  padding-bottom: 14px;
  text-align: center;
  font-weight: bold;
  background-color: #4CAF50;
  color: white;
  width:45%;

}

#header{
  font-family: Arial, Helvetica, sans-serif;
  padding-top: 14px;
  padding-bottom: 14px;
  text-align: center;
  font-weight: bold;
	font-size: 15px;
  background-color: #ff9933;
  color: white;
  width:45%;

}

.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 18px;
  font-weight: bold;
  border-radius: 7px;
  cursor: pointer;
  margin: auto;
}
</style>

<?php
$servername = "localhost:3308";
$username = "root";
$password = "";
$dbname = "menudb";


$First_name = $_POST['First_name'];
	$Last_name = $_POST['Last_name'];
	$Phone = $_POST['Phone'];
	$Email = $_POST['Email'];
	$Street_name = $_POST['Street_name'];
	$Building_no = $_POST['Building_no'];
	$Food_type = $_POST['Food_type'];
	$Dishe_type = $_POST['Dishe_type'];
	$spice_level = $_POST['spice_level'];
	$Drink = $_POST['Drink'];
	$Extra_flavor = $_POST['Extra_flavor'];
  $Allergy = $_POST['Allergy'];
 
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// prepare and bind
$stmt = $conn->prepare("INSERT INTO orderinfo (First_name,
Last_name, Phone, Email, Street_name, Building_no, Food_type, Dishe_type,spice_level,
 Drink, Extra_flavor, Allergy) VALUES ( ?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?)");
$stmt->bind_param("ssssssssssss", $First_name,
$Last_name, $Phone, $Email, $Street_name, $Building_no, $Food_type, $Dishe_type,$spice_level,
 $Drink, $Extra_flavor, $Allergy);
// set parameters and execute

$stmt->execute();


$last_order=$conn->insert_id;

if ($result = $conn->query("SELECT * FROM orderinfo ORDER BY ID DESC LIMIT 5;")) {
	while ($row = $result->fetch_row()) {
		echo "<p class=center id=header>Your order created successfully</p>";
		echo "<div>
    <p class=center id=header>Order-ID:  ". $row[0] . "</p>

   
		</div>
    
    <table class=center id=customers>

			<tr>
				<td>Name </td>
				<td>". $row[1] . " " . $row[2] . "</td>
			</tr>

			<tr>
				<td>Phone</td>
				<td>". $row[3] . "</td>
			</tr>

			<tr>
				<td>E-mail</td>
				<td>". $row[4] . "</td>
			</tr>

			<tr>
				<td>Street name</td>
				<td>". $row[5] . "</td>
			</tr>

			<tr>
				<td>Building number</td>
				<td>". $row[6] . "</td>
			</tr>

			<tr>
				<td>Type of food</td>
				<td>". $row[7] . "</td>			
			</tr>

			<tr>
				<td>Type of dishe</td>
				<td>". $row[8] . "</td>
			</tr>

			<tr>
				<td>Spice level</td>
				<td>". $row[9] . "</td>
			</tr>
			<tr>
				<td>Drink</td>
				<td>". $row[10] . "</td>
			</tr>

			<tr>
				<td>Extra flavor</td>
				<td>". $row[11] . "</td>
			</tr>

		<tr>
		<td>Allergy</td>
		<td>". $row[12] . "</td>
	</tr>
    </table> 
    <p class=center id=header><a href=/E-menu/Home.html class=button>Home</a></p> ";
    
  break;
  }
	/* free result set */
	$result->close();
}

 


$stmt->close();
$conn->close();
?>