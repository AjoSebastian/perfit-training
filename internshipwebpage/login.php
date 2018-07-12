 <?php
$conn = mysqli_connect("localhost", "id6425033_ajo", "ajo@1998", "id6425033_perfitlogin");
  // Check connection
  if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
  } 
 $username1 = trim($_REQUEST['username']);
 $password1 = trim($_REQUEST['password']);
  $sql = "SELECT * from item where username = '".$username1."' && password ='".$password1."'";
  $result = $conn->query($sql);
  if ($result->num_rows > 0)
   {
   // output data of each row
   while($row = $result->fetch_assoc())
    {
    echo "<tr><td>" . $row["FirstName"]. "</td><td>" . $row["LastName"] . "</td><td>". $row["DoB"]. "</td><td>" . $row["BloodGroup"]. "</td><td>" . $row["ContactNo"]. "</td></tr>";
    }
echo "</table>";
} 
else { echo "0 results"; }
